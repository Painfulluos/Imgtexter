import logic
import tkinter as tk

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


label_btn_convert = tk.Label(root, text="Choose image:")
btn_convert = tk.Button(root, text="Open", command=lambda:logic.imgToString(root))

label_btn_convert.pack()
btn_convert.pack()

root.mainloop()