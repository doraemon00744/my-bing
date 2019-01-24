# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import getpass
import bing
import tkFileDialog



root = Tk()
root.title("Pretty Wallpaper")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe['borderwidth'] = 2
mainframe['relief'] = 'solid'
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
# mainframe.columnconfigure(0, weight=3)
# mainframe.columnconfigure(1, weight=3)
# mainframe.columnconfigure(2, weight=3)
# mainframe.columnconfigure(3, weight=1)
# mainframe.columnconfigure(4, weight=1)
# mainframe.rowconfigure(1, weight=1)

# image = PhotoImage(file="C://Users//wuyh35//PycharmProjects//my_bing_wallpaper//bing.jpg")

main_label = ttk.Label(mainframe, text="Just Click the Button ^_^")
main_label.grid(column=1, row=1, columnspan=2, sticky=N)
main_label.bind('<Enter>', lambda e: main_label.configure(text='Hurry Up!!'))
main_label.bind('<Leave>', lambda e: main_label.configure(text='Just Click the Button ^_^'))
# main_label['image'] = image


# def create_bing_selections():
#     phone = StringVar()
#     home = ttk.Radiobutton(mainframe, text='Home', variable=phone, value='home')
#     office = ttk.Radiobutton(mainframe, text='Office', variable=phone, value='office')
#     cell = ttk.Radiobutton(mainframe, text='Mobile', variable=phone, value='cell')
#     root.update()

def wallpaper_from_bing():
    main_label.configure(text='lo')
    bing.change_wallpaper_from_bing()

ttk.Button(mainframe, text="Local", command=bing.select_file_from_local).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Bing", command=wallpaper_from_bing).grid(column=2, row=3, sticky=(W, E))



# measureSystem = StringVar()
# ttk.Checkbutton(mainframe, text='Use Metric',
# 	    variable=measureSystem,
# 	    onvalue='metric', offvalue='imperial').grid(column=1, row=4)


for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)
    child.columnconfigure(0, weight=1, minsize=10)



root.mainloop()