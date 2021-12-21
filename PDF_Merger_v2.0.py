import tkinter as tk
from tkinter import messagebox, filedialog
from ttkthemes import ThemedTk
import os
from PyPDF2 import PdfFileMerger
from pathlib import Path


root = ThemedTk(theme="breeze")
root.title('PDF Merger v2.0')
root.geometry('600x230')

listb = tk.Listbox(root, selectmode=tk.MULTIPLE, background="light grey")
listb.pack(fill=tk.X)

downloads_path = str(Path.home() / "Downloads")
downloads_path = downloads_path.replace('\\\\', '\\')

def browse_cmd():
    """Opens file explorer browse dialogue box for user to search for files in GUI."""
    root.filename = filedialog.askopenfilename(filetypes=[('pdf file', '*.pdf')])
    listb.insert(listb.size(), root.filename)
    return None

def clearall():
    listb.delete(0,'end')
    submit_button["state"] = "active"

def main_func():
    submit_button["state"] = "disable"

    merger = PdfFileMerger()
    if listb.size() != 0 and len(listb.curselection()) != 0:
        files = [listb.get(x) for x in listb.curselection()]
        for file in files:
            merger.append(file)
        merger.write(downloads_path +"\Merged_PDF.pdf")
        merger.close()
        clearall()
    elif listb.size() != 0 and len(listb.curselection()) == 0:
        tk.messagebox.showerror('No File Selected','Please select/highlight the files in the entry box before pressing the merge button.')
        submit_button["state"] = "active"
    else:
        tk.messagebox.showerror('No File Added','Please add files before selected the merge button.')
        submit_button["state"] = "active"
        clearall()
        return


add_button = tk.Button(root, text='Add File', command= browse_cmd, width=20)
add_button.pack()
submit_button = tk.Button(root, text='Merge', command= main_func, width=25)
submit_button.pack()


root.mainloop()