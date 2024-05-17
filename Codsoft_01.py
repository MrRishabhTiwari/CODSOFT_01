import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.configure(bg="orange")

        self.tasks = []
        self.completed_tasks = []

        self.task_entry = tk.Entry(master, width=90)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="lightblue", fg="black")
        self.add_button.grid(row=1, column=0, padx=15, pady=15)

        self.listbox = tk.Listbox(master, width=90, selectmode=tk.SINGLE, bg="white", fg="black")
        self.listbox.grid(row=2, column=0, padx=10, pady=10)

        self.complete_button = tk.Button(master, text="Completed", command=self.complete_task, bg="yellow", fg="black")
        self.complete_button.grid(row=3, column=0, padx=(10, 5), pady=10)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_task, bg="red", fg="white")
        self.delete_button.grid(row=4, column=0, padx=(5, 10), pady=10)

        self.show_completed_button = tk.Button(master, text="Show Completed", command=self.show_completed_tasks, bg="green", fg="white")
        self.show_completed_button.grid(row=5, column=0, padx=10, pady=(0, 10))

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def complete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            completed_task = self.tasks.pop(index)
            self.completed_tasks.append(completed_task)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def show_completed_tasks(self):
        if self.completed_tasks:
            messagebox.showinfo("Completed Tasks", "\n".join(self.completed_tasks))
        else:
            messagebox.showinfo("Completed Tasks", "No completed tasks.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
