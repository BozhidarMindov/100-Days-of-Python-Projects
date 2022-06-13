from tkinter import *

FONT = ("Arial", 12, "bold")

#function that does the conversion
def calc():
    value = float(input.get())
    result = round(value * 1.6093, 3)
    result_label.config(text=str(result))

#creating the window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx = 50, pady = 50)

#Is_equal_to label
is_eq_to_label = Label(text = "is equal to", font = FONT)
is_eq_to_label.grid(column = 0, row = 1)
is_eq_to_label.config(padx = 20)

#Miles label
miles_label = Label(text="Miles", font = FONT)
miles_label.grid(column=2, row = 0)
miles_label.config(padx=20)

#Km label
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=20)

#Result label
result_label = Label(text = "0", font=FONT)
result_label.grid(column=1, row=1)

#Calculate button
calc_button = Button(text="Calculate", command = calc)
calc_button.grid(column=1,row=2)

#Entry
input = Entry(width=15, font=FONT)
input.grid(column=1, row=0)


window.mainloop()