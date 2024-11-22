import tkinter as tk
from tkinter import messagebox
import threading
import time as time_module
from playsound import playsound

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")

        tk.Label(root, text="Reminder Text:").grid(row=0, column=0, padx=10, pady=5)
        self.reminder_text = tk.Entry(root, width=30)
        self.reminder_text.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Time (HH:MM 24-hour):").grid(row=1, column=0, padx=10, pady=5)
        self.reminder_time = tk.Entry(root, width=10)
        self.reminder_time.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Add Reminder", command=self.add_reminder).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Delete Selected Reminder", command=self.delete_reminder).grid(row=3, column=0, columnspan=2, pady=10)

        self.reminder_listbox = tk.Listbox(root, width=50, height=10)
        self.reminder_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.reminders = []

        # Start the reminder checker in a separate thread
        self.running = True
        threading.Thread(target=self.check_reminders, daemon=True).start()

    def add_reminder(self):
        text = self.reminder_text.get()
        time = self.reminder_time.get()

        if text and time:
            self.reminders.append({"text": text, "time": time})
            self.reminder_listbox.insert(tk.END, f"{time}: {text}")
            messagebox.showinfo("Reminder Added", f"Reminder '{text}' set for {time}")
        else:
            messagebox.showwarning("Input Error", "Please enter both reminder text and time.")

    def delete_reminder(self):
        selected_indices = self.reminder_listbox.curselection()
        if selected_indices:
            for index in selected_indices[::-1]:
                self.reminder_listbox.delete(index)
                del self.reminders[index]
            messagebox.showinfo("Reminder Deleted", "Selected reminder(s) deleted.")
        else:
            messagebox.showwarning("Selection Error", "Please select a reminder to delete.")

    def check_reminders(self):
        while self.running:
            current_time = time_module.strftime("%H:%M")
            for reminder in self.reminders:
                if reminder["time"] == current_time:
                    playsound('C:/Users/H.P/Documents/jupyter/upes python class assignment/python projects/reminder application/remind.mp3')  # Path to your notification sound file
                    messagebox.showinfo("Reminder", f"Reminder: {reminder['text']}")
                    self.show_reminder_popup(reminder)
                    self.reminders.remove(reminder)
                    self.update_reminder_listbox()
            time_module.sleep(1)  # Check every minute
    
    def show_reminder_popup(self, reminder):
        # Show the reminder popup in the main thread
        self.root.after(0, lambda: messagebox.showinfo("Reminder", f"Reminder: {reminder['text']}"))

    def update_reminder_listbox(self):
        # Update the reminder listbox in the main thread
        self.root.after(0, self._update_reminder_listbox)

    def _update_reminder_listbox(self):
        self.reminder_listbox.delete(0, tk.END)
        for rem in self.reminders:
            self.reminder_listbox.insert(tk.END, f"{rem['time']}: {rem['text']}")        

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()