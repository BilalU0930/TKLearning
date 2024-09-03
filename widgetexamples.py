from tabnanny import check
from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

#label
my_label = Label(text="my label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()

#button
def button_clicked():
    print("button clicked")
    print(my_text.get("1.0", END))
    # 1.0 -> 1 -> line , 0 -> character

my_button = Button(text="button", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

#entry
my_entry = Entry(width=20)
my_entry.focus()
my_entry.pack()

#multiline
#text
my_text = Text(width=30, height=5)
#my_text.focus()
my_text.pack()

#scale
def scale_selected(value):
    print(value)
my_scale = Scale(from_=0, to=50, command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
my_checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

#radio button
def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text="1. option", value=10, variable=radio_checked_state, command=radio_selected)
my_radiobutton_2 = Radiobutton(text="2. option", value=20, variable=radio_checked_state, command=radio_selected)

my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Bilal", "ABC", "KJF", "Popoyes", "BurgerKing"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>', listbox_selected)
my_listbox.pack()

window.mainloop()