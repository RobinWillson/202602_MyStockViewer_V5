import os
import win32com.client
import pypandoc

def convert_doc_to_md(folder_path):
    print("正在啟動 Word 應用程式...")
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    try:
        files = [f for f in os.listdir(folder_path) if f.endswith(".doc")]
        
        if not files:
            print("找不到任何 .doc 檔案！")
            return

        for file_name in files:
            print(f"處理中: {file_name} ...", end=" ")
            doc_path = os.path.join(folder_path, file_name)
            docx_path = doc_path + "x"
            md_path = doc_path.replace(".doc", ".md")
            
            try:
                doc = word.Documents.Open(doc_path)
                doc.SaveAs(docx_path, FileFormat=16)
                doc.Close()
            except Exception as e:
                print(f"[失敗] Word 轉檔 .docx 錯誤: {e}")
                continue
                
            try:
                pypandoc.convert_file(docx_path, 'md', outputfile=md_path)
                print("[成功]")
            except Exception as e:
                print(f"[失敗] Pandoc 轉檔 .md 錯誤: {e}")
            finally:
                if os.path.exists(docx_path):
                    try:
                        os.remove(docx_path)
                    except:
                        pass

    finally:
        word.Quit()
        print("轉換作業結束。")

if __name__ == "__main__":
    target_folder = r"C:\Node_Space\202602_MyStockViewer_V5\YuantaOneAPI_Python\IO_Doc"
    convert_doc_to_md(target_folder)
