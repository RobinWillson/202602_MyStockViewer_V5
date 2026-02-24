import os
import glob
import re


def parse_grid_table(lines):
    rows = []
    current_row = []

    for line in lines:
        if line.startswith("+-") or line.startswith("+=") or line.startswith("+:"):
            # End of a row
            if current_row:
                num_cols = max(len(r) for r in current_row)
                cols = [""] * num_cols
                # merge multi-line row content
                for r in current_row:
                    for i, c in enumerate(r):
                        clean_c = c.strip().replace("**", "")
                        if clean_c.endswith("\\"):
                            clean_c = clean_c[:-1] + "\n"
                        else:
                            clean_c += " "
                        cols[i] = cols[i] + clean_c

                rows.append([c.strip() for c in cols])
                current_row = []
        elif line.startswith("|"):
            # It's a row content line
            parts = line.split("|")[1:-1]
            current_row.append([p.strip() for p in parts])

    return rows


def format_memo(memo_text):
    if not memo_text:
        return "  - (無)"

    lines = memo_text.split("\n")
    formatted = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Split merged patterns "0: SelectAll 1: 不列取消單"
        items = re.split(r"\s+(?=\w+[:：])", line)
        for item in items:
            im = re.match(r"^(\w+)\s*[:：]\s*(.*)$", item)
            if im:
                formatted.append(f"  - {im.group(1)} : {im.group(2)}")
            else:
                formatted.append(f"  - {item}")

    return "\n".join(formatted)


def convert_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    create_date = ""
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

    output_lines = []

    for t_lines in tables:
        rows = parse_grid_table(t_lines)
        if not rows:
            continue

        # Check "製作日期" in table
        for row in rows:
            for i, cell in enumerate(row):
                if "製作日期" in cell and i + 1 < len(row):
                    create_date = row[i + 1]
                    break

        # Check if it's a field table
        if len(rows) > 0 and len(rows[0]) >= 5:
            is_field_table = False
            start_idx = 0

            for idx, r in enumerate(rows):
                # Search for 'Fileld Name' / 'Field Name'
                joined_head = "".join(
                    [c.replace("**", "").replace(" ", "").lower() for c in r]
                )
                if "fileldname" in joined_head or "fieldname" in joined_head:
                    is_field_table = True
                    start_idx = idx + 1
                    break

            if is_field_table:
                for row in rows[start_idx:]:
                    if len(row) < 5:
                        continue
                    field_name = row[0]
                    desc = row[1]
                    typ = row[2]
                    size = row[3]
                    memo = row[4]

                    if (
                        field_name
                        and "ParentStruct" not in field_name
                        and "ChildStruct" not in field_name
                    ):
                        output_lines.append(f"# {field_name}")
                        if create_date:
                            output_lines.append(f"* createDate : {create_date}")
                        output_lines.append(f"* description : {desc}")
                        output_lines.append(f"* type : {typ}")
                        output_lines.append(f"* Size : {size}")
                        output_lines.append(f"* Memo :")
                        output_lines.append(format_memo(memo))
                        output_lines.append("")

    if output_lines:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))
        return True
    return False


if __name__ == "__main__":
    folder_path = r"C:\Node_Space\202602_MyStockViewer_V5\YuantaOneAPI_Python\IO_Doc"
    count = 0
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".md"):
            if convert_file(os.path.join(folder_path, file_name)):
                count += 1

    print(f"成功轉換了 {count} 個 Markdown 檔案的格式。")
