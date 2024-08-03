import tkinter as tk


def add_num(p_num):
    l_val = calc.get()
    l_val +=str(p_num)
    calc.delete(0, tk.END)
    calc.insert(0, l_val)

win = tk.Tk()
win.geometry(f"240x280+100+100")
win['bg'] = '#33ffe6'
win.title("Калькулятор")

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',15), width= 15)

calc.grid(row=0, column=0, columnspan=3, stick="wens")

tk.Button(text="1", bd=5, font=('Arial',13),  command=lambda : add_num(1)).grid(row=1, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="2", bd=5, font=('Arial',13), command=lambda : add_num(2)).grid(row=1, column=1, stick="wens", padx=5, pady=5)
tk.Button(text="3", bd=5, font=('Arial',13), command=lambda : add_num(3)).grid(row=1, column=2, stick="wens", padx=5, pady=5)
tk.Button(text="4", bd=5, font=('Arial',13), command=lambda : add_num(4)).grid(row=2, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="5", bd=5, font=('Arial',13), command=lambda : add_num(5)).grid(row=2, column=1, stick="wens", padx=5, pady=5)
tk.Button(text="6", bd=5, font=('Arial',13), command=lambda : add_num(6)).grid(row=2, column=2, stick="wens", padx=5, pady=5)
tk.Button(text="7", bd=5, font=('Arial',13), command=lambda : add_num(7)).grid(row=3, column=0, stick="wens", padx=5, pady=5)
tk.Button(text="8", bd=5, font=('Arial',13), command=lambda : add_num(8)).grid(row=3, column=1, stick="wens", padx=5, pady=5)
tk.Button(text="9", bd=5, font=('Arial',13), command=lambda : add_num(9)).grid(row=3, column=2, stick="wens", padx=5, pady=5)
tk.Button(text="0", bd=5, font=('Arial',13), command=lambda : add_num(0)).grid(row=4, column=0, stick="wens", padx=5, pady=5)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)


win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)


win.mainloop()