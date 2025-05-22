# Tratamento de dados projeto sentinelas
<h1 id="usage" > 💻 Descrição </h1>

Projeto feito em python 3 que visa pegar os dados csv do projeto sentinelas, tratar os dados e inseri-los em um banco MySQl.

<h1 id="usage" > 📚 Bibliotecas </h1>
- Numpy<br>
- Pandas<br>
- PyMySQL<br>
- python-dotenv<br>
- Tkinter<br>

<h2>👨‍💻 Como rodar o projeto</h2>

1. É necessario ter o <a href="https://www.python.org/">python 3</a> instalado e o pip.

2. Com o pip instalado é necessario instalar as bibliotecas.
```sh
    pip install numpy
```
```sh
    pip install pandas
```
```sh
    pip install PyMySQL
```
```sh
    pip install python-dotenv
```

3. Crie um arquivo ```.env``` na raiz do projeto e defina as variaveis de ambiente no arquivo como está no ```.env.example```.

4. O arquivo ```gui.py```  é a interfacie gráfica do projeto, baasta executana na pasta raiz do projeco com:
```sh
    python gui.py
```
e poderá utilizar o programa.

5. Alternativamente, se quiser gerar um executavel basta rodar na raiz:
```sh
    pip install pyinstaller

    pyinstaller --onefile --windowed --add-data ".env;." --add-data "assets/frame0;assets/frame0" gui.py
```
que irá gerar o executável dentro de uma pasta ```dist```. Basta arrastar o executavel para a raiz do projeto e pode apagar a pasta ```dist```, a ```build``` e o arquivo ```gui.spec```. Há também a possibilidade de criar um atalho do arquivo e movelo para onde você desejar.

<h3>Autor</h3>
<a href="https://github.com/JoabUrbano">Joab Urbano</a><br>
