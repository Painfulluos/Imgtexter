from tkinter import filedialog
from tkinter import messagebox

from datetime import datetime

from PIL import Image

from googletrans import Translator, constants

import config


def translateText(text, dest):
	translator = Translator()
	return translator.translate(text, dest=dest).text

def copyToClipboard(text, root):
	root.clipboard_clear()
	root.clipboard_append(text)

def imgToString(root, isTranslate=False, dest="en"):
		try:
			img_path = filedialog.askopenfile().name
		except AttributeError:
			raise "The file was not selected" 

		img = Image.open(img_path)
		text = config.pytesseract.image_to_string(img, lang="rus+eng", config=config.tessdata_dir_config)
		if isTranslate == True:
			text = translateText(text, dest)
		isSaveToFile = messagebox.askyesnocancel("Save to file", "Do you want to save the received text to a .txt file?\nYes - Save the result to a file\nNo - Copy to Clipboard\nCancel - Cancel - Cancel the convert")
		print(isSaveToFile)
		print(f"******************\n******************\n{text}\n******************\n******************")
		if isSaveToFile == True:
			save_path = filedialog.asksaveasfilename(filetypes=config.file_types, defaultextension=".txt")
			textToFile(text, save_path)
		elif isSaveToFile == False:
			copyToClipboard(text, root)
		else:
			return
		return text


def textToFile(text, save_path):
	current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	with open(save_path, "w+", encoding="utf-8") as f:
		f.write(text)