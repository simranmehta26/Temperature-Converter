from tkinter import Tk, ttk
from tkinter import *

win = Tk()
win.title("Temperature Converter")
win.geometry("300x320")
win.configure(bg="WHITE")
win.resizable(height=False, width=False)


# function for conversion
def conversion():
    if select1.get() == '\N{DEGREE CELSIUS}' and select2.get() == 'Kelvin':
        label = value.get()
        k = float(label) + 273.15
        result['text'] = f'{round(k, 3)}'

    if select1.get() == 'Kelvin' and select2.get() == '\N{DEGREE CELSIUS}':
        label = value.get()
        c = float(label) - 273.15
        result['text'] = f'{round(c, 3)}'

    if select1.get() == '\N{DEGREE FAHRENHEIT}' and select2.get() == '\N{DEGREE CELSIUS}':
        label = value.get()
        c = (5 / 9) * (float(label) - 32)
        result['text'] = f'{round(c, 3)}'

    if select1.get() == '\N{DEGREE CELSIUS}' and select2.get() == '\N{DEGREE FAHRENHEIT}':
        label = value.get()
        f = ((9 / 5) * float(label)) + 32
        result['text'] = f'{round(f, 3)}'

    if select1.get() == 'Kelvin' and select2.get() == '\N{DEGREE FAHRENHEIT}':
        label = value.get()
        f = (1.8 * (float(label) - 273.15)) + 32
        result['text'] = f'{round(f, 3)}'

    if select1.get() == '\N{DEGREE FAHRENHEIT}' and select2.get() == 'Kelvin':
        label = value.get()
        k = ((float(label) - 32) * (5 / 9)) + 273.15
        result['text'] = f'{round(k, 3)}'

    if (select1.get() == '\N{DEGREE CELSIUS}' and select2.get() == '\N{DEGREE CELSIUS}') or \
            (select1.get() == '\N{DEGREE FAHRENHEIT}' and select2.get() == '\N{DEGREE FAHRENHEIT}') or \
            (select1.get() == 'Kelvin' and select2.get() == 'Kelvin'):
        result['text'] = f'Invalid !'

    if (select1.get() == '' and (select2.get() == '\N{DEGREE CELSIUS}' or '\N{DEGREE FAHRENHEIT}' or 'Kelvin')) or \
            (select2.get() == '' and (select1.get() == '\N{DEGREE CELSIUS}' or '\N{DEGREE FAHRENHEIT}' or 'Kelvin')):
        result['text'] = f'Enter both units'


# frames
top = Frame(win, width=300, height=60)
top.grid(row=0, column=0)

main = Frame(win, width=300, height=260, bg="dark slate grey")
main.grid(row=1, column=0)

# top frame
app_name = Label(top, text=" Temperature Converter ", height=2, padx=25, pady=5, anchor=CENTER,
                 font='Arial 16 bold ', bg="dark slate grey", fg="white")
app_name.place(x=0, y=0)

# main frame
result = Label(main, text=" ", height=2, width=16, pady=7, anchor=CENTER, font='Ivy 15 bold', bg="WHITE",
               fg="black", relief="solid")
result.place(x=50, y=10)

units = ['\N{DEGREE CELSIUS}', '\N{DEGREE FAHRENHEIT}', 'Kelvin']

from_label = Label(main, text="From", height=1, width=6, padx=0, pady=0, anchor=NW, font='Ivy 10 bold', bg="WHITE",
                   fg="black", relief="flat")
from_label.place(x=48, y=90)

select1 = StringVar()
combo1 = ttk.Combobox(main, width=7, justify=CENTER, font='Ivy 12 bold', textvariable=select1)
combo1['values'] = units
combo1['state'] = 'readonly'
combo1.place(x=48, y=115)

to_label = Label(main, text="To", height=1, width=6, padx=0, pady=0, anchor=NW, font='Ivy 10 bold', bg="WHITE",
                 fg="black", relief="flat")
to_label.place(x=160, y=90)

select2 = StringVar()
combo2 = ttk.Combobox(main, width=7, justify=CENTER, font='Ivy 12 bold', textvariable=select2)
combo2['values'] = units
combo2['state'] = 'readonly'
combo2.place(x=160, y=115)

value = Entry(main, width=22, justify=CENTER, font='Ivy 12 bold', relief="solid")
value.place(x=50, y=155)

button = Button(main, text="Converter", width=19, height=1, padx=5, bg="green", fg="white", font='Ivy 12 bold',
                relief="solid", command=conversion)
button.place(x=50, y=200)

win.mainloop()
