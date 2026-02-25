"""
使用說明 (Usage):

這個程式用來將 .doc 檔案轉換為 .md 檔案。
請在命令列中傳入參數來指定要轉換的目標：

1. 轉換單一檔案：
   python convert_docs.py <檔案路徑>
   範例: python convert_docs.py 1E64280C_30.100.40.12_IO_Spec.doc

2. 轉換特定資料夾下的所有 .doc 檔案：
   python convert_docs.py /folder/all
   這將會自動轉換預設目錄下的所有 .doc 檔案。
"""

import os
import sys
import win32com.client
import pypandoc

DEFAULT_FOLDER = r"C:\Node_Space\202602_MyStockViewer_V5\YuantaOneAPI_Python\IO_Doc"


def process_file(word_app, doc_path):
    print(f"處理中: {os.path.basename(doc_path)} ...", end=" ")
    docx_path = doc_path + "x"
    md_path = doc_path.replace(".doc", ".md")

    try:
        doc = word_app.Documents.Open(doc_path)
        doc.SaveAs(docx_path, FileFormat=16)
        doc.Close()
    except Exception as e:
        print(f"[失敗] Word 轉檔 .docx 錯誤: {e}")
        return

    try:
        pypandoc.convert_file(docx_path, "md", outputfile=md_path)
        print("[成功]")
    except Exception as e:
        print(f"[失敗] Pandoc 轉檔 .md 錯誤: {e}")
    finally:
        if os.path.exists(docx_path):
            try:
                os.remove(docx_path)
            except:
                pass


def convert_doc_to_md(target):
    print("正在啟動 Word 應用程式...")
    try:
        word = win32com.client.Dispatch("Word.Application")
    except Exception as e:
        print(f"無法啟動 Word 應用程式，請確認已安裝 Microsoft Word: {e}")
        return

    word.Visible = False

    try:
        if target == "/folder/all":
            print(f"準備轉換目錄下的所有檔案: {DEFAULT_FOLDER}")
            files = [
                f
                for f in os.listdir(DEFAULT_FOLDER)
                if f.endswith(".doc") and not f.startswith("~$")
            ]

            if not files:
                print("找不到任何 .doc 檔案！")
                return

            for file_name in files:
                doc_path = os.path.join(DEFAULT_FOLDER, file_name)
                process_file(word, doc_path)
        else:
            # 單一檔案轉換
            doc_path = target
            # 如果只給檔名，嘗試在預設目錄下尋找
            if not os.path.isabs(doc_path) and not os.path.exists(doc_path):
                potential_path = os.path.join(DEFAULT_FOLDER, doc_path)
                if os.path.exists(potential_path):
                    doc_path = potential_path

            if not os.path.exists(doc_path) or not doc_path.endswith(".doc"):
                print(f"錯誤: 找不到檔案 '{doc_path}' 或這不是一個 .doc 檔案。")
                return

            process_file(word, doc_path)

    finally:
        word.Quit()
        print("轉換作業結束。")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target_arg = sys.argv[1]
    convert_doc_to_md(target_arg)
