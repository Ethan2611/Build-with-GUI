from tkinter import*
from tkinter.ttk import*
from time import strftime
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("Project")
window.config(background="gray")
menubar=Menu(window)
window.config(menu=menubar)


file= Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)

file.add_command(label='New File', command=None)
file.add_command(label='New Window', command=None)
file.add_command(label='Open File', command=None)
file.add_separator()
file.add_command(label='Open Folder', command=None)
file.add_command(label='Open Recent', command=None)
file.add_separator()
file.add_command(label='Add Folder to Workspace', command=None)
file.add_command(label='Save Workspace as...', command=None)

edit= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit)

edit.add_command(label='New File', command=None)
edit.add_command(label='New Window', command=None)
edit.add_command(label='Open File', command=None)
edit.add_separator()
edit.add_command(label='Open Folder', command=None)
edit.add_command(label='Open Recent', command=None)
edit.add_separator()
edit.add_command(label='Add Folder to Workspace', command=None)
edit.add_command(label='Save Workspace as...', command=None)
window.config(menu=menubar)



selec= Menu(menubar,tearoff=0)
menubar.add_cascade(label='Selection',menu=edit)

selec.add_command(label='New File', command=None)
selec.add_command(label='New Window', command=None)
selec.add_command(label='Open File', command=None)
selec.add_separator()
selec.add_command(label='Open Folder', command=None)
selec.add_command(label='Open Recent', command=None)
selec.add_separator()
selec.add_command(label='Add Folder to Workspace', command=None)
selec.add_command(label='Save Workspace as...', command=None)
window.config(menu=menubar)




window.mainloop()#To make the output window stay on the screen