import tkinter as tk


def add_num(p_num):
    l_val = calc.get()

    # 1208
    if l_val[0]=='0':
        l_val = l_val[1:]

    l_val += str(p_num)
    calc.delete(0, tk.END)
    calc.insert(0, l_val)


# 1208
def add_operation(p_oper):
    l_val = calc.get()


    if l_val[-1] in '-+/*':
        l_val = l_val[:-1]

    calc.delete(0, tk.END)
    calc.insert(0, l_val+p_oper)


def calculate():
    l_val = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, eval(l_val))


# 1208
def make_digit_button(p_num):
    return tk.Button(text=p_num, bd=5, font=('Arial', 13), command=lambda: add_num(p_num))

# 1208
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg= 'Red', command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg= 'Red', command=calculate)



win = tk.Tk()
win.geometry(f"240x280+100+100")
win['bg'] = '#33ffe6'
win.title("Калькулятор")

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')

calc.grid(row=0, column=0, columnspan=4, stick="wens")

# 1208
make_digit_button(1).grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, stick="wens", padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick="wens", padx=5, pady=5)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
