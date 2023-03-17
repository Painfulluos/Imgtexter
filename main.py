import logic
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Imgtexter")
root.geometry("400x400")
root.resizable(False,False)


main_menu = tk.Menu(root)
root.config(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="Exit", command=exit)

settings_menu = tk.Menu(main_menu, tearoff=0)
settings_menu.add_command(label="Language")


main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Settings", menu=settings_menu)



label_btn_convert = tk.Label(root, text="Save or copy the original to the clipboard:")
label_btn_convert.pack()

btn_convert = tk.Button(root, text="Default Convert", command=lambda:logic.imgToString(root))
btn_convert.pack()

label_btn_translate = tk.Label(root, text="Convert with translation.\nSelect the language to be translated into and click on the button:")
label_btn_translate.pack()

combo_choose_dest_lang = ttk.Combobox(root, values=logic.config.lang_list)
combo_choose_dest_lang.current(1)
combo_choose_dest_lang.pack()

btn_translate = tk.Button(root, text="Translation Convert", command=lambda:logic.imgToString(root, True, combo_choose_dest_lang.get()))
btn_translate.pack()






root.mainloop()