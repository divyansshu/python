import tkinter as tk #GUI

root = tk.Tk()
root.title("File Organize")
root.geometry("400x250")

def show_input():
    user_input = entry.get() # get text from the entry box
    print("user input:", user_input) # laber for entry
    
label = tk.Label(root, text="Enter Address")
label.pack(pady=10) #add padding around the labelEntry (input block) where user can't

entry = tk.Entry(root, width=100)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10) #start the GUI event loop

root.mainloop()

#design a file organizer GUI app 