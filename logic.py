from tkinter import filedialog
from tkinter import messagebox

from datetime import datetime

from PIL import Image
import pytesseract


######
pytesseract.pytesseract.tesseract_cmd = r'C:\\Python_Scripts\\img_to_text\\venv\\tesseract.exe' #Путь к Движку Tesseract
tessdata_dir_config = r'--tessdata-dir "C:\\Python_Scripts\\img_to_text\\venv\\tessdata"' # Путь к языкам
######

def imgToString():
		img_path = filedialog.askopenfile().name
		img = Image.open(img_path)
		text = pytesseract.image_to_string(img, lang="rus+eng", config=tessdata_dir_config)
		isSaveToFile = messagebox.askquestion("Save to file", "Do you want to save the received text to a .txt file?")
		if isSaveToFile == "yes":
			textToFile(text)
		print("\n", text, "\n")

def textToFile(text):
	current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	with open(f"Result_{current_time}.txt", "w+", encoding="utf-8") as f:
		f.write(text)
