from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk

from Core.main import Main
main = Main()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("862x519")
window.configure(bg = "#3A7FF6")

canvas = Canvas(
    window,
    bg = "#3A7FF6",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(431, 0, 862, 519, fill="#FCFCFC", outline="")

# Botão gerar
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=main.carregarAvistagemDeteccao,
    relief="flat"
)
button_1.place(x=557, y=401, width=180, height=55)

# Titulo
canvas.create_text(
    40,
    127,
    anchor="nw",
    text="Projeto sentinelas",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

# Texto 01
canvas.create_text(
    482,
    74,
    anchor="nw",
    text="Selecione o arquivo",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

#  Retangulo sublinhado
canvas.create_rectangle(40, 160, 100, 165, fill="#FCFCFC", outline="")

# Entrada de texto 01
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.TCombobox",
    fieldbackground="#F1F5FF",  # Fundo da área de texto
    background="#F1F5FF",  # Fundo da lista suspensa
    foreground="#000716",  # Cor do texto
    borderwidth=0,  # Remove borda
    relief="flat",  # Deixa o design mais "clean"
    padding=5,  # Adiciona um espaçamento interno
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_generate.place(x=783, y=319, width=24, height=22)

# Logo
logo = PhotoImage(file=relative_to_assets("logo1.png"))
canvas.create_image(268, 260, image=logo, anchor="center")

window.resizable(False, False)
window.title("Tratar dados Sentinelas")
window.mainloop()
