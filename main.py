import tkinter as tk

def add_tarefa():
    tarefa = entry.get()
    if tarefa:
        listbox.insert(tk.END, tarefa)
        entry.delete(0, tk.END)

def deletar_tarefa():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("Lista de Afazeres")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

add_botao = tk.Button(root, text="Adicionar", command=add_tarefa, width=15, height=1)
add_botao.pack(pady=5)

botao_deletar = tk.Button(root, text="Deletar", command=deletar_tarefa, width=15, height=1)
botao_deletar.pack(pady=3)

frame = tk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

listbox = tk.Listbox(frame)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.geometry("500x400")
root.minsize(300, 200)

root.mainloop()