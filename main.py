import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Tech Solutions - Gestor de Tareas")
        self.root.geometry("400x450")

        # --- Interfaz Gráfica ---

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # Instrucción para el usuario
        self.label_info = tk.Label(root, text="Presiona Enter o haz clic en Añadir", font=("Arial", 8))
        self.label_info.pack()

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=5)

        # Lista de tareas (Listbox)
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Frame para botones de acción
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.mark_completed,
                                         bg="#2196F3", fg="white")
        self.complete_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336",
                                       fg="white")
        self.delete_button.grid(row=0, column=1, padx=5)

        # --- Manejo de Eventos ---

        # Evento: Presionar Enter en el Entry
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Evento Opcional: Doble clic para completar tarea
        self.tasks_listbox.bind('<Double-Button-1>', lambda event: self.mark_completed())

    def add_task(self):
        """Añade una nueva tarea desde el Entry al Listbox."""
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar entrada
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def mark_completed(self):
        """Modifica visualmente la tarea seleccionada para marcarla como completada."""
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)

            # Si ya está marcada, no hacer nada o quitar la marca (opcional)
            if "✔ " not in task:
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, f"✔ {task}")
                self.tasks_listbox.itemconfig(index, fg="gray")  # Cambia color a gris
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona una tarea de la lista.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Atención", "Selecciona la tarea que deseas eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()