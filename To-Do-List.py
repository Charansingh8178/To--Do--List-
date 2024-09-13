import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("To-Do List")
img= Image.open(r'C:\Users\Charan singh\Desktop\DAILY\PERSONAL PROJECT\clock.jpg')
bg=ImageTk.PhotoImage(img)
background= tk.Label(root,image=bg)
background.image=bg
background.place(relwidth=1,relheight=1)

root.geometry('500x500')

frame = tk.Frame(root, bg='#223441')
frame.pack(pady=10)

def newTask():
    task = my_entry.get()
    if task != "":

        task_frame = tk.Frame(frame, bg='#223441')
        task_frame.pack( fill="x", pady=2)

        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            task_frame, text=task, variable=var, onvalue=True, offvalue=False,
            bg='#223441', fg='white', font=('Times', 14), anchor="w",
            padx=10, pady=5, selectcolor='#223441' 
        )
        checkbox.var = var 
        checkbox.pack(side="left", fill="x", padx=10, pady=2)

        my_entry.delete(0, 'end')

def deleteTask():
    for widget in frame.winfo_children():
        checkbox= widget.winfo_children()[0]
        if checkbox.var.get():
            widget.destroy()

# Label and Entry for user input
tk.Label(root, text='Enter your Task Below', font=('Times', 13), pady=19, bg='#223441', fg='white').pack()
my_entry = tk.Entry(root, font=('Times', 14))
my_entry.pack(pady=20)

# Frame for the buttons
button_frame = tk.Frame(root, bg='#223441')
button_frame.pack(pady=20)

# Add Task button
addTask = tk.Button(button_frame, text='Add Task', bg='#c5f776', font=('Times', 14), padx=20, pady=10, command=newTask)
addTask.pack(fill="both", expand=True, side="left")

# Delete Task button
delTask = tk.Button(button_frame, text="Delete Task", font=('Times', 14), bg='#ff8b61', padx=20, pady=10, command=deleteTask)
delTask.pack(fill="both", expand=True, side="left")

# Run the Tkinter event loop
root.mainloop()
