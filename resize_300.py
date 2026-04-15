from PIL import Image
import os
from pathlib import Path

# 設定圖片資料夾路徑
image_folder = r'C:\CTL\AI\02-2_pdf2svg\outputs_generater_character_list'  # 請將此處替換為您的資料夾路徑

# 取得所有 PNG 檔案
png_files = list(Path(image_folder).glob('*.png'))

for file_path in png_files:
    try:
        with Image.open(file_path) as img:
            # 調整圖片大小為 300x300
            img_resized = img.resize((300, 300), Image.LANCZOS)
            # 儲存並覆蓋原始檔案
            img_resized.save(file_path)
            print(f"已處理：{file_path.name}")
    except Exception as e:
        print(f"處理 {file_path.name} 時發生錯誤：{e}")