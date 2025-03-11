from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

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
canvas.create_rectangle(
    430.9999999999999,
    0.0,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")

# Botão gerar
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=556.9999999999999,
    y=401.0,
    width=180.0,
    height=55.0
)

# Titulo
canvas.create_text(
    39.999999999999886,
    127.0,
    anchor="nw",
    text="Projeto sentinelas",
    fill="#FCFCFC",
    font=("Roboto Bold", 24 * -1)
)

# Texto 01
canvas.create_text(
    481.9999999999999,
    74.0,
    anchor="nw",
    text="Selecione o arquivo",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

#  Retangulo sublinhado
canvas.create_rectangle(
    39.999999999999886,
    160.0,
    99.99999999999989,
    165.0,
    fill="#FCFCFC",
    outline="")

# Entrada de texto 01
text_area_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    185.5,
    image=text_area_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=489.9999999999999,
    y=155.0,
    width=321.0,
    height=59.0
)

# Entrada de texto 02
text_area_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    329.5,
    image=text_area_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=489.9999999999999,
    y=299.0,
    width=321.0,
    height=59.0
)

# Botão carregar arquivo
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=782.9999999999999,
    y=319.0,
    width=24.0,
    height=22.0
)

# Logo
logo = PhotoImage(
    file=relative_to_assets("logo1.png"))

canvas.create_image(
    268,
    260.0,
    image=logo,
    anchor="center"
)

window.resizable(False, False)
window.mainloop()
