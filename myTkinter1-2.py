import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('470x580')
root.resizable(width=False, height=False)

colour1 = '#020f12'
colour2 = 'chocolate4'
colour3 = 'coral4'
colour4 = 'black'

main_frame = tk.Frame(root, bg=colour1, pady=40)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

button1 = tk.Button(
    main_frame,
    background=colour2,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness=2,
    highlightbackground=colour2,
    highlightcolor='white',
    width=13,
    height=2,
    border=-1,
    cursor='hand1',
    text='Get Started',
    font=('white', 16, 'bold'),
)

button1.place(x=150, y=300)
root.mainloop()













