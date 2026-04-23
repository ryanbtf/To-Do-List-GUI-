import tkinter as tk
import os

ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                listbox.insert(tk.END, linha.strip())

def salvar_tarefas():
    tarefas = listbox.get(0, tk.END)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for tarefa in tarefas:
            f.write(tarefa + "\n")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        salvar_tarefas()

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        salvar_tarefas()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")

entry = tk.Entry(root)
entry.pack(pady=10)

add_button = tk.Button(root, text="Adicionar", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Remover", command=delete_task)
delete_button.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

listbox = tk.Listbox(frame)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

carregar_tarefas()

root.mainloop()