import logic
import tkinter as tk

root = tk.Tk()
root.title("Imgtexter")
root.geometry("400x400")
root.resizable(False,False)


label_btn_convert = tk.Label(root, text="Choose image:")
btn_convert = tk.Button(root, text="Open", command=lambda:logic.imgToString(root))

label_btn_convert.pack()
btn_convert.pack()

root.mainloop()