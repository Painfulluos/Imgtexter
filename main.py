import logic
import tkinter as tk

root = tk.Tk()
root.title("Imgtexter")
root.geometry("400x400")
root.resizable(False,False)


label_btn_convert = tk.Label(root, text="Choose image:")
btn_convert = tk.Button(root, text="Open", command=logic.imgToString)

# label_converted_text = tk.Label(root, text="aaaa", background="#bdbdbd", width=50, height=50 )
converted_text = tk.Text(root, width=30, height=20)

label_btn_convert.pack()
btn_convert.pack()
converted_text.pack()


# label_converted_text.grid(row=2, column=0, pady=20)
root.mainloop()