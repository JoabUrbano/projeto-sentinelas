from pathlib import Path

import tkinter
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, filedialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

from Core.DadosController import DadosController
controller = DadosController()

def onClick():
    """
    Verifica se os campos estão preenchidos para poder chamar a classe controller
    """
    path = entry.get()
    opcao = combobox.get()
    if path == "":
        tkinter.messagebox.showwarning(
            title="Campo Vazio", message="Caminho vazio!"
        )
    elif opcao == "Selecione o tipo da planilha":
        tkinter.messagebox.showwarning(
            title="Opção não selecionada", message="Nenhuma opção selecionada!"
        )
    else:
        response = controller.tratarRequisicao(path, opcao)
        if response == "Dados inseridos com sucesso!":
            tkinter.messagebox.showinfo(title="Sucesso", message=response)
        else:
             tkinter.messagebox.showerror(title="Erro", message=response)

def relative_to_assets(path: str) -> Path:
    """
    Pega o caminho para os assets
    """
    return ASSETS_PATH / Path(path)

def selecionar_arquivo():
    """
    Abrir seleção do arquivo
    """
    caminho_arquivo = filedialog.askopenfilename()
    if caminho_arquivo:
        entry.delete(0, tkinter.END)  # Limpa o Entry antes de inserir o novo caminho
        entry.insert(0, caminho_arquivo)  # Insere o caminho do arquivo

window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")

canvas = Canvas(
    window, bg = "#3A7FF6", height = 519, width = 862, bd = 0,
    highlightthickness = 0, relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(431, 0, 862, 519, fill="#FCFCFC", outline="")

# Botão gerar
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1, borderwidth=0, highlightthickness=0,
    command=onClick, relief="flat"
)
button_1.place(x=557, y=401, width=180, height=55)

# Titulo
canvas.create_text(
    40, 127, anchor="nw", text="Projeto sentinelas",
    fill="#FCFCFC", font=("Roboto Bold", 24 * -1)
)

# Texto 01
canvas.create_text(
    482, 74, anchor="nw", text="Selecione o arquivo", 
    fill="#505485", font=("Roboto Bold", 24 * -1)
)

#  Retangulo sublinhado
canvas.create_rectangle(40, 160, 100, 165, fill="#FCFCFC", outline="")

# Entrada de texto 01
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.TCombobox",
    fieldbackground="#F1F5FF", background="#F1F5FF",
    foreground="#000716", borderwidth=0, relief="flat", padding=5,
)

listaOpcoes = ["Avistagem e detecção", "tipo 2"]
combobox = ttk.Combobox(window, values=listaOpcoes, state="readonly", style="Custom.TCombobox")  # O state="readonly" impede entrada manual
combobox.place(x=490, y=155, width=321, height=30)
combobox.set("Selecione o tipo da planilha")

# Entrada de texto 02
text_area = PhotoImage(file=relative_to_assets("entry.png"))

entry_bg = canvas.create_image(650.5, 329.5, image=text_area)

entry = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry.place(x=490, y=299, width=321, height=59)

# Botão carregar arquivo
button_file = PhotoImage(file=relative_to_assets("button_2.png"))

button_generate = Button(
    image=button_file,
    borderwidth=0,
    highlightthickness=0,
    command=selecionar_arquivo,
    relief="flat"
)
button_generate.place(x=783, y=319, width=24, height=22)

# Logo
logo = PhotoImage(file=relative_to_assets("logo1.png"))
canvas.create_image(268, 260, image=logo, anchor="center")

window.resizable(False, False)
window.title("Projeto Sentinelas")
window.mainloop()
