from tkinter import *
from tkinter import ttk, messagebox
import requests

root = Tk() # Exibindo janela
root.title("CONSULTA DE CNPJ") # Título do programa
root.geometry("300x100")

def get_cnpj():
    root.geometry("300x500")
    consult = cnpj.get()
    url = f"https://receitaws.com.br/v1/cnpj/{consult}"
    response = requests.get(url)
    data = response.json()

    show_data(data)

def copy_text(text):
    root.clipboard_clear()
    root.clipboard_append(text)

def show_data(data):
    messagebox.showinfo("Clique no texto para copiá-lo")

    NOME = Label(root, text=f"Nome: {data['nome']}", cursor="hand2")
    NOME.place(x=10, y=60)
    NOME.bind("<Button-1>", lambda event: copy_text(data['nome']))

    FANTASIA = Label(root, text=f"Fantasia: {data['fantasia']}", cursor="hand2")
    FANTASIA.place(x=10, y=80)
    FANTASIA.bind("<Button-1>", lambda event: copy_text(data['fantasia']))

    DATA_ABERTURA = Label(root, text=f"Data de Abertura: {data['abertura']}", cursor="hand2")
    DATA_ABERTURA.place(x=10, y=100)
    DATA_ABERTURA.bind("<Button-1>", lambda event: copy_text(data['abertura']))

# Adicionando texto na tela
text = Label(root, text="Digite o CNPJ: ")
text.place(x=10, y=10)

# Solicitando entrada de CNPJ
cnpj = Entry(root)
cnpj.place(x=10, y=30)

# Adicionando botão
button = Button(root, text="Adquirir Dados", command=get_cnpj, bg='black', fg='white')
button.place(x=125, y=30, height=20)

root.mainloop()