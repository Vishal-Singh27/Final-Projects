# Importing library and packages stuff
from runner import invertimages
from functioning import pdftoimage, convert2pdf
from tkinter import Tk, Button, Label, filedialog, Entry, END, messagebox

root = Tk()
root.title("Invert PDF by Vishal Singh")

# Initializing filepath and savepath
filepath = None
savepath = None

def getfilename():
    global filepath
    global textbox
    filepath = filedialog.askopenfilename(initialdir="/", title="Browse PDF", filetypes=(("PDF Files", "*.pdf"),))
    textbox.delete(0, END)
    textbox.insert(0, filepath)


def getsavedir():
    global savepath
    global textbox1
    savepath = filedialog.asksaveasfilename()
    textbox1.delete(0, END)
    textbox1.insert(0, savepath)
    

def convert():
    global filepath
    global savepath
    if not filepath:
        if not textbox.get():
            messagebox.showerror("Error!", "Please Enter Filepath")
            return
        else:
            filepath = textbox.get()
    if not savepath:
        if not textbox1.get():
            messagebox.showerror("Error!", "Please Enter Savepath")
            return
        else:
            savepath = textbox1.get()
    
    try:
        images = pdftoimage(filepath)
    except:
        messagebox.showerror("Error!", "File Not Found!")
        return
    
    if not images:
        messagebox.showerror("Error!", "File Not Found!")
        return
    invertedimages = invertimages(images)
    
    convert2pdf(invertedimages, path=savepath)
    filepath = None
    savepath = None


Label(root, text="Invert PDF By Vishal Singh").grid(row=0, column=0, columnspan=10)
Label(root, text="Browse File: ").grid(row=1,column=0, columnspan=2)
textbox = Entry(root, width=30, border=5)
textbox.grid(row=1,column=3, columnspan=8)
Button(root, text="Browse", command=getfilename).grid(row=2, column=3)

Label(root, text="Save Directory: ").grid(row=3, column=0, columnspan=2)
textbox1 = Entry(root, width=30, border=5)
textbox1.grid(row=3,column=3, columnspan=8)
Button(root, text="Browse", command=getsavedir).grid(row=4, column=3)

Button(root, text="Convert", padx=10, pady=5, command=convert).grid(row=5, column=3)
Button(root, text="Exit", padx=10, pady=6, command=root.destroy).grid(row=6, column=3)


root.mainloop()