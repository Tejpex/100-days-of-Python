import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
entry = tk.Entry()
entry.config(width=7)
entry.focus()
entry.grid(row=0, column=1)

# Text
miles_text = tk.Label(text="Miles")
miles_text.config(padx=5)
miles_text.grid(row=0, column=2)

equal_to_text = tk.Label(text="is equal to")
equal_to_text.config(padx=5)
equal_to_text.grid(row=1, column=0)

km_text = tk.Label(text="Km")
km_text.config(padx=5)
km_text.grid(row=1, column=2)

km_number = tk.Label(text="0")
km_number.grid(row=1, column=1)


# Button
def convert():
    miles = float(entry.get())
    km = round(miles * 1.609, 1)
    km_number.config(text=km)


button = tk.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
