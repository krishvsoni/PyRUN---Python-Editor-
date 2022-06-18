from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import os
window = Tk()
window.title('PyRUN - Python Editor')
window.geometry("644x500")
window.wm_maxsize(744,600)
window.wm_iconbitmap("pyrun.ico")

gpath = ''

def runMyCode():
    global gpath
    if gpath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="Please save the file first...")
        msg.pack()
        return
    command = f'python {gpath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    output.insert('1.0',outputResult)
    output.insert('1.0',error)
     

def openMyFile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        textEditor.insert('1.0', code)
        global gpath
        gpath = path

def saveMyFileAs():
    global gpath
    if gpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = gpath    
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        file.write(code)
def quitApp():
    window.destroy()


def about():
    showinfo("PyRUN - Python Editor","PyRUN is an open source editor python. Edit and run your python code with PyRUN. For queries contact us on  mail.pyrun@gmail.com")


textEditor = Text()
textEditor.config(bg='#362f2e', fg='#d2ded1', insertbackground='black')
textEditor.pack()

output = Text(height=7)
output.config(bg='#362f2e', fg='#1dd604')
output.pack()

menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Open', command = openMyFile)
fileBar.add_command(label='Save', command = saveMyFileAs)
fileBar.add_command(label='Save As', command = saveMyFileAs)
fileBar.add_command(label='Exit', command = quitApp)
menuBar.add_cascade(label='File', menu = fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command = runMyCode)
menuBar.add_cascade(label='Run', menu = runBar)

pyBar = Menu(menuBar, tearoff=0)
pyBar.add_command(label='About',command=about)
menuBar.add_cascade(label='Help',menu=pyBar)


window.config(menu=menuBar)
window.mainloop()