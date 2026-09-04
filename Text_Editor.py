# sab say pehly hum tkinter module ko improt kary gay jo k GUI (user interface) app hota hai
import tkinter as tk
from tkinter import filedialog,messagebox

# ya hai basic text editor ka structure 
root=tk.Tk()
root.title("Majid Ali Text Editor")
root.geometry("800x600")

#for create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helventica",12)

)
text.pack(expand=True,fill=tk.BOTH)

#main logic is start now 

# function 1=> to create a new file
def new_file():
    text.delete(1.0,tk.END)

# function 2 -> to open a new file
def open_file():
    #agar new file ko kholna ho
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text FIles","*.txt")]
    )

    if file_path:
        # open file
        with open(file_path,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

# function 3 -> save the file
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text FIles","*.txt")]
    )

    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo("info","Congratulation Majid Ali your file is save Successfully") 

#Menu bar
menu = tk.Menu(root) 
root.config(menu=menu) 
file_menu= tk.Menu(menu)

#new , open file , save and exit

#add file menu to manu bar
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.command)

# it start and keeps the window open
root.mainloop()