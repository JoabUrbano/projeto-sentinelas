# Tratamento de dados projeto sentinelas
<h1 id="usage" > 💻 Descrição </h1>

Projeto feito em python 3 que visa pegar os dados csv do projeto sentinelas, tratar os dados e inseri-los em um banco MySQl.

<h1 id="usage" > 📚 Bibliotecas </h1>
- Matplotlib<br>
- Numpy<br>
- Pandas<br>
- PyMySQL<br>
- python-dotenv<br>

<h2>Como rodar o projeto?</h2>

1. É necessario ter o <a href="https://www.python.org/">python 3</a> instalado e o pip.

2. Com o pip instalado é necessario instalar as bibliotecas.
```sh
    pip install numpy
```
```sh
    pip install matplotlib
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

3. Na pasta ```Dados``` coloque as tabelas que deseja tratar, instancie as classes especificas para tratar cada tipo de arquivo csv.

4. No arquivo main crie os objetos com o nome do arquivo ee passe um objeto repository especifico para aquele arquivo csv.

5. Crie um arquivo ```.env``` na raiz do projeto e defina as variaveis de ambiente no arquivo como está no ```.env.example```.

<h3>Autor</h3>
<a href="https://github.com/JoabUrbano">Joab Urbano</a><br>
