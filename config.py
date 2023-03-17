import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Python_Scripts\\Imgtexter\\venv\\tesseract.exe' #Path to The Tesseract Engine
tessdata_dir_config = r'--tessdata-dir "C:\\Python_Scripts\\Imgtexter\\venv\\tessdata"' # Path to langs

# File types for save the file 
file_types = [
            ('Text Document', '*.txt'),
            ]

lang_list = ["ru", "en",]