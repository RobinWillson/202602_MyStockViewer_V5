import os
import re
import json


def parse_grid_table(lines):
    rows = []
    current_row = []

    for line in lines:
        if line.startswith("+-") or line.startswith("+=") or line.startswith("+:"):
            if current_row:
                num_cols = max(len(r) for r in current_row)
                cols = [""] * num_cols
                for r in current_row:
                    for i, c in enumerate(r):
                        clean_c = c.strip().replace("**", "")
                        if clean_c.endswith("\\"):
                            # This slash typically means newline in the cell
                            clean_c = clean_c[:-1] + "\n"
                        else:
                            clean_c += " "
                        cols[i] = cols[i] + clean_c
                rows.append([c.strip() for c in cols])
                current_row = []
        elif line.startswith("|"):
            parts = line.split("|")[1:-1]
            current_row.append([p.strip() for p in parts])

    return rows


def format_memo(memo_text):
    if not memo_text:
        return ""
    lines = memo_text.split("\n")
    formatted = []
    # Try to extract keys if they look like "0: XXX", "1: YYY"
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Handle multiple key-value pairs separated by space
        parts = re.split(r"\s+(?=[A-Za-z0-9\-\+]+[:：])", line)
        for p in parts:
            p = p.strip()
            im = re.match(r"^([A-Za-z0-9\-\+]+)\s*[:：]\s*(.*)$", p)
            if im:
                formatted.append(f"    - `{im.group(1)}`: {im.group(2)}")
            else:
                # It might just be a note
                formatted.append(f"    - *說明*: {p}")
    return "\n".join(formatted)


def build_json_preview(fields, name_suffix):
    parent_obj = {}
    child_obj = {}

    current_context = parent_obj
    has_child = False

    for f in fields:
        fname = f["name"]
        if "ParentStruct" in fname:
            current_context = parent_obj
            continue
        elif "ChildStruct" in fname:
            current_context = child_obj
            has_child = True
            continue

        ftype = f["type"].lower()

        if "byte" in ftype or "string" in ftype:
            val = "example"
        elif "int" in ftype or "short" in ftype or "long" in ftype:
            val = 0
        else:
            val = ""

        if fname == "uintCount" or fname == "uintCount_In" or fname == "uintCount_Out":
            val = 1

        current_context[fname] = val

    result = {}
    if parent_obj:
        result[f"ParentStruct_{name_suffix}"] = parent_obj
    else:
        result["ParentStruct"] = {"uintCount": 1} if has_child else {}

    if has_child:
        child_arr = [child_obj] if child_obj else [{}]
        result[f"ChildStruct_{name_suffix}"] = child_arr

    return json.dumps(result, indent=2, ensure_ascii=False)


def convert_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    tables = []
    current_table_lines = []
    in_table = False

    for line in lines:
        if line.startswith("+-") or line.startswith("+=") or line.startswith("+:"):
            if not in_table:
                in_table = True
            current_table_lines.append(line)
        elif line.startswith("|") and in_table:
            current_table_lines.append(line)
        else:
            if in_table:
                tables.append(current_table_lines)
                current_table_lines = []
                in_table = False

    if in_table and current_table_lines:
        tables.append(current_table_lines)

    metadata = {
        "Service ID": "",
        "COM Name": "",
        "Service Desc": "",
        "Communication Mode": "",
        "Date": "",
    }

    in_fields = []
    out_fields = []
    current_field_list = None

    for t_lines in tables:
        rows = parse_grid_table(t_lines)
        if not rows:
            continue

        for row in rows:
            # check for metadata
            for i, cell in enumerate(row):
                if "Service ID" in cell and i + 1 < len(row):
                    metadata["Service ID"] = row[i + 1]
                if "COM Name" in cell and i + 1 < len(row):
                    metadata["COM Name"] = row[i + 1]
                if "Service Desc" in cell and i + 1 < len(row):
                    metadata["Service Desc"] = row[i + 1]
                if "Communicatio" in cell and i + 1 < len(row):
                    metadata["Communication Mode"] = row[i + 1]
                if "製作日期" in cell and i + 1 < len(row):
                    metadata["Date"] = row[i + 1]

                if "Input Spec Table" in cell:
                    current_field_list = in_fields
                if "Output Spec Table" in cell:
                    current_field_list = out_fields

            # check for fields
            if len(row) >= 5 and current_field_list is not None:
                joined_head = "".join(
                    [c.replace("**", "").replace(" ", "").lower() for c in row]
                )
                if "fileldname" in joined_head or "fieldname" in joined_head:
                    continue
                fname = row[0]
                if not fname:
                    continue
                # To prevent garbage rows
                if len(fname) > 50:
                    continue

                desc = row[1]
                typ = row[2]
                size = row[3]
                memo = row[4]

                current_field_list.append(
                    {
                        "name": fname,
                        "desc": desc,
                        "type": typ,
                        "size": size,
                        "memo": memo,
                    }
                )

    if not in_fields and not out_fields:
        return None

    md = []
    service_id = (
        metadata["Service ID"].split(" ")[0] if metadata["Service ID"] else "Unknown"
    )
    com_name = metadata["COM Name"] or "Unknown"

    md.append(f"# {service_id} - {com_name} ({metadata['Service Desc']})")
    md.append("")
    md.append("## 1. 基本資訊 (Metadata)")
    md.append(f"- **Service ID**: `{metadata['Service ID']}`")
    md.append(f"- **COM Name**: `{metadata['COM Name']}`")
    md.append(f"- **設計描述**: {metadata['Service Desc']}")
    md.append(f"- **通訊模式**: `{metadata['Communication Mode']}`")
    md.append(f"- **更新日期**: {metadata['Date']}")
    md.append("")
    md.append("---")
    md.append("")

    def generate_spec_section(title, fields, suffix):
        if not fields:
            return
        md.append(f"## {title}")
        md.append("")
        md.append(f"### JSON 結構範例")
        md.append("```json")
        md.append(build_json_preview(fields, suffix))
        md.append("```")
        md.append("")
        md.append(f"### 參數說明 (Parameter Details)")
        md.append("")

        for f in fields:
            fname = f["name"]
            if "ParentStruct" in fname:
                md.append(f"- `{fname}` : {f['desc']} (Object)")
                continue
            elif "ChildStruct" in fname:
                md.append("")
                md.append(f"- `{fname}` : {f['desc']} (Array of Objects)")
                continue

            prefix = "  - "
            size_str = ""
            if f["size"]:
                size_str = f", Size: {f['size'].replace('#','').strip()}"
            type_size = f"({f['type']}{size_str})" if f["type"] else ""

            md.append(f"{prefix}`{fname}` : {f['desc']} {type_size}")
            memo_str = format_memo(f["memo"])
            if memo_str:
                md.append(memo_str)

        md.append("")
        md.append("---")
        md.append("")

    generate_spec_section("2. 請求結構 (Request Specification)", in_fields, "In")
    generate_spec_section("3. 回傳結構 (Response Specification)", out_fields, "Out")

    safe_service = re.sub(r'[<>:"/\\|?*]', "", service_id)
    safe_com = re.sub(r'[<>:"/\\|?*]', "", com_name)
    new_filename = f"{safe_service}-{safe_com}.md"

    # Avoid overwriting the ones we carefully crafted by hand
    if new_filename in ["0A000010-RP_RealReportMerge.md", "0A000014-RP_Realport.md"]:
        return None

    new_filepath = os.path.join(os.path.dirname(file_path), new_filename)

    with open(new_filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    return new_filepath


if __name__ == "__main__":
    folder_path = r"C:\Node_Space\202602_MyStockViewer_V5\YuantaOneAPI_Python\IO_Doc"
    processed = 0
    for fname in os.listdir(folder_path):
        if fname.endswith(".md") and "_IO_Spec.md" in fname:
            fpath = os.path.join(folder_path, fname)
            new_fpath = convert_file(fpath)
            if new_fpath:
                print(
                    f"[{processed+1}] Processed {fname} -> {os.path.basename(new_fpath)}"
                )
                processed += 1
                os.remove(fpath)  # remove the original .md generated by pandoc
    print(f"Total processed: {processed}")
