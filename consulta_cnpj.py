from tkinter import *
from tkinter import ttk
import requests
import webbrowser

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

def get_ie():
    webbrowser.open("https://www.google.com/search?q=consulta+inscri%C3%A7%C3%A3o+estadual")

def copy_text(text):
    root.clipboard_clear()
    root.clipboard_append(text)

def show_data(data):
    NOME = Label(root, text=f"Nome: {data['nome']}", cursor="hand2")
    NOME.place(x=10, y=60)
    NOME.bind("<Button-1>", lambda event: copy_text(data['nome']))

    FANTASIA = Label(root, text=f"Fantasia: {data['fantasia']}", cursor="hand2")
    FANTASIA.place(x=10, y=80)
    FANTASIA.bind("<Button-1>", lambda event: copy_text(data['fantasia']))

    DATA_ABERTURA = Label(root, text=f"Data de Abertura: {data['abertura']}", cursor="hand2")
    DATA_ABERTURA.place(x=10, y=100)
    DATA_ABERTURA.bind("<Button-1>", lambda event: copy_text(data['abertura']))

    TIPO = Label(root, text=f"Tipo: {data['tipo']}", cursor="hand2")
    TIPO.place(x=10, y=120)
    TIPO.bind("<Button-1>", lambda event: copy_text(data['tipo']))

    SITUACAO = Label(root, text=f"Situação: {data['situacao']}", cursor="hand2")
    SITUACAO.place(x=10, y=140)
    SITUACAO.bind("<Button-1>", lambda event: copy_text(data['situacao']))

    LOGRADOURO = Label(root, text=f"Logradouro: {data['logradouro']}", cursor="hand2")
    LOGRADOURO.place(x=10, y=160)
    LOGRADOURO.bind("<Button-1>", lambda event: copy_text(data['logradouro']))

    NUMERO = Label(root, text=f"Número: {data['numero']}", cursor="hand2")
    NUMERO.place(x=10, y=180)
    NUMERO.bind("<Button-1>", lambda event: copy_text(data['numero']))

    BAIRRO = Label(root, text=f"Bairro: {data['bairro']}", cursor="hand2")
    BAIRRO.place(x=10, y=200)
    BAIRRO.bind("<Button-1>", lambda event: copy_text(data['bairro']))

    CEP = Label(root, text=f"CEP: {data['cep']}", cursor="hand2")
    CEP.place(x=10, y=220)
    CEP.bind("<Button-1>", lambda event: copy_text(data['cep']))

    EMAIL = Label(root, text=f"E-mail: {data['email']}", cursor="hand2")
    EMAIL.place(x=10, y=240)
    EMAIL.bind("<Button-1>", lambda event: copy_text(data['email']))

    TELEFONE = Label(root, text=f"Telefone: {data['telefone']}", cursor="hand2")
    TELEFONE.place(x=10, y=260)
    TELEFONE.bind("<Button-1>", lambda event: copy_text(data['telefone']))

    button = Button(root, text="Inscrição Estadual", command=get_ie, bg='black', fg='white')
    button.place(x=125, y=280, height=20)

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