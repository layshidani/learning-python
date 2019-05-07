***Lays Marie Hidani - Notebook***
# Python

- Linguagem de alto nível (mais próximo da linguagem humana)
- Multiplataforma
- Open source
- Forte no mercado
- Forte suporte da comunidade
- Forte documentação
- Dinâmica
- Interage bem com outras linguagens
- Fácil de aprender
- Vasta biblioteca padrão

Documentação oficial: <https://www.python.org/doc/>

# Aprendendo PYTHON

## Algumas Convenções:

- Convenções de estilo completa. verificar PEP 8 <https://www.python.org/dev/peps/pep-0008/#code-lay-out>

    - Ex:

    -> não é legal
    import os, math


    -> o melhor é:
    import os
    import math

    mas, pode se for from-import:
    from subprocess import Popen, PIPE


    -> outro ex:

    Yes: x = 8*5 + 4*3   -> separar apenas operadores de diferentes prioridades
    Yes: i = i + 1

    NO: x = 8 * 5 + 4 * 3


    -> outro ex:

    Yes: if x == 4: print x, y; x, y = y, x
    No:  if x == 4 : print x , y ; x , y = y , x


- (#) Utiliza-se # seguido do texto, para inserir comentários no código. Esses comentários não serão vísiveis no programa, somente no código e auxiliam a organizar e informar sobre trechos do código tanto para você mesmo quanto para trabalhos em equipe.

- Há uma convenção de que não se deve usar mais do que 72 caractéres por linha no código, a fim de torná-lo mais legível e organizado.

- Indentação: utilizar 4 espaços (dá para configurar a tecla **tab** em alguns IDE p/ fazer essa identação correta de 4 espaços). Utiliza-se identação para separar blocos de código.

- Quando o texto de uma string é muito longo, usa-se '''texto''' -> 3 haspas ao invés de 1.

- A contagem de posição de um caracter ou elemento sempre começa em 0, ou seja:

    'Olá' ->
    O = posição 0

    l = posição 1

    á = posição 2


    ex:
    lista = [1, 2, 3]

    1 = posição 0

    2 = posição 1

    3 = posição 2

- Utiliza-se -1, -2, -3, n para contar inversamente. (do último para o primeiro)

- Você pode unir strings em um **print** utlizando (+):
    * Exemplo:

    first_name = 'Lays'

    middle_name = 'Marie'

    print('O nome é: ' + first_name + middle_name)

- Você pode unir diferentes tipos de dados em um **print** utlizando (,):
    * Exemplo:

    first_name = 'Lays'

    middle_name = 'Marie'

    age = 28

    print('O nome é: ', first_name, middle_name, '. ' 'Idade: ', 28, ' anos.')


- Em **print** Utiliza-se {} para preencher um texto (string) com um valor e depois utiliza-se *'.format(variavel ou expressão)'* para associar o valor.

    * exemplo:

    - nome = 'Lays'

    - print('Meu nome é {}' .format(nome))

        - resultado esperado: >>> *Meu nome é Lays*


- Utiliza-se {:.xf} -> x é o número de casas decimais

    - {:.2f} por exemplo para imprimir um float com duas casas decimais

    - print('10 divido por 3 = {:.2f}' .format(10 / 3))

        - resultado esperado:  >>>  *10 dividido por 3 = 3.33*


- Utiliza-se {:,} para separar um nº grande por ','.

    - numero = 1000000

    - print('O nº é {:,}' .format(numero))

         - resultado esperado:   >>> 1,000,000



# Variáveis

- Exemplo:

- x = 30

- y = 'Olá Mundo!'

Onde:
x e y -> São variáveis
30 e 'Olá mundo!' são os dados recebidos ('=' significa 'recebe') pela variável correspondente.

## Atribuir nome para variáveis:
- Python diferencia letras maiúsculas e minúsculas
- O nome da variável pode ter letras, números e '_'
- Sempre começar com letras
- Nunca utilizar espaço
- Em Python, existem palavras reservadas que não podem ser usadas para nomear variáveis, pois elas já estão atribuídas para definir regras e estrutura da linguagem, por isso são reservadas. São elas:

and	exec	not
assert	finally	or
break	for	pass
class	from	print
continue	global	raise
def	if	return
del	import	try
elif	in	while
else	is	with
except	lambda	yield

## Tipos de dados básicos:

- Números:
    * (int)     -> Inteiros -> ex: -3, -2, -1, 0, 1, 2, 3
    * (float)   -> Ponto flutuante/Decimal -> ex: 4.81 (em Python, usa-se '.' ao invés de ',').
    * (long)    -> Longo -> ex: 25989506564809890
    * (complex) -> Complexos -> ex: 5 + 8j


- String (texto):
    * (str)     -> Texto -> ex: 'letra', '10', 'Olá mundo!' (em python, toda string vai dentro de '')
    * (unicode) -> Unicode


- List (listas):
    * list = [ ]

        ex:

        lista_1 = [0, 1, 2, 3]
        lista_2 = [0, '1', '2', 3, 'livro']


- Tuplas:
    (A diferença das tuplas para as listas, é que as tuplas são IMUTÁVEIS)
    * Tupla = ( )

    ex:
    tupla1 = (0, 1, 2)

- Arquivo

- Booleanos:
    * (bool):

    -> True
    -> False


- Conjuntos:
    * set
    * frozenset


- None



## Operadores aritméticos

- soma           ->   (+)   ->  ex: 8 + 4
- subtração      ->   (-)   ->  ex: 8 - 4
- multiplicação  ->   (*)   ->  ex: 8 * 4
- divisão        ->   (/)   ->  ex: 8 / 4
- exponenciação  ->   (**)  ->  ex  8 ** 2  (resp = 64)
- parte inteira  ->   (//)  ->  ex: 8 // 5  (resp = 1, 1 parte inteira de divisão de 8 por 5)
- módulo         ->   (%)   ->  ex: 8 % 5   (resp = 3, é o resto da divisão de 8 por 5)


## Operadores relacionais

- Igual a	           (==)
- Diferente            (!=)
- Maior que	           (>)
- Menor que	           (<)
- Maior ou igual a	   (>=)
- Menor ou igual a	   (<=)


## Operadores lógicos

- and   ->  ex: if x > 2 **and** y > 3

- or    ->  ex: if x > 2 **or** y > 3

- not   ->  ex: if x **not** in lista


## Entrada e saída de dados

### Input
Uma forma bastante usada para entrada de dados é o *input*, que leva para 'dentro' do programa uma informação dada pelo usuário.

### Print
Uma forma para saída de dados é o comando *print* que imprime na tela o que é determinado pelo programa.


ex:


```python
#coding: utf-8


login = input("Informe seu Login: ") #entrada de dado: o login
senha = input("Informe sua Senha: ") #entrada de dado: a senha do usuário

print('O usuário informado foi {}, e a senha é {}.' .format(login, senha)) #saída de dados: o login e a senha
```


```python
# coding: UTF-8
print('----' * 25)
print('Glossário de programação'.center(25, ':'))
print('----' * 25)

glossario = {
    'string': 'Sequência linear de caracteres. Itens são acessados via índice'
              '\n>>> Ex: \'Isso é uma string\'\n',
    'lista': 'Sequência linear de valores (elementos) que podem ser de qualquer e de diferentes tipos '
             '\n(listas, strings, inteiros, etc). Itens são acessados via índice'
             '\n>>>Ex: lista = [elemento1, elemento2, elemento3]\n',
    'tupla': 'Sequência linear de valores (elementos) que podem ser de qualquer e de diferentes tipos '
             '\nPorém, diferentemente das listas, são imutáveis!'
             '\n>>>Ex: tupla = (elemento1, elemento2, elemento3)\n',
    'range': 'Intervalo sequenciado de números inteiros. O índice começa em 0, por isso o último nº \nnão entra na '
             'sequência \n>>>Ex: range(0,11) irá criar um intervalo de 0 a 10\n',
    'dicionario': 'Coleção associativa desordenada. O valor é acessado por uma **chave** imutável '
                  'e não por indice\n>>>Ex: dicionário = {chave1: valor1, chave2: valor2}'
    }

for word, significado in glossario.items():
    print('\n' + ':::' + word.title() + ':::' + '\nSignificado -> ' + significado)

print('----' * 30)
```

    ----------------------------------------------------------------------------------------------------
    :Glossário de programação
    ----------------------------------------------------------------------------------------------------

    :::String:::
    Significado -> Sequência linear de caracteres. Itens são acessados via índice
    >>> Ex: 'Isso é uma string'


    :::Lista:::
    Significado -> Sequência linear de valores (elementos) que podem ser de qualquer e de diferentes tipos
    (listas, strings, inteiros, etc). Itens são acessados via índice
    >>>Ex: lista = [elemento1, elemento2, elemento3]


    :::Tupla:::
    Significado -> Sequência linear de valores (elementos) que podem ser de qualquer e de diferentes tipos
    Porém, diferentemente das listas, são imutáveis!
    >>>Ex: tupla = (elemento1, elemento2, elemento3)


    :::Range:::
    Significado -> Intervalo sequenciado de números inteiros. O índice começa em 0, por isso o último nº
    não entra na sequência
    >>>Ex: range(0,11) irá criar um intervalo de 0 a 10


    :::Dicionario:::
    Significado -> Coleção associativa desordenada. O valor é acessado por uma **chave** imutável e não por indice
    >>>Ex: dicionário = {chave1: valor1, chave2: valor2}
    ------------------------------------------------------------------------------------------------------------------------


## Métodos vs Funções

- Função:           função(objeto)

- Método:           objeto.metodo()

# Strings

## Operadores com strings

  - (+)
  - (*)


  ex:


```python
string1 = 'oi, '
string2 = 'tudo bem?'

print(string1 + string2) #este operador soma o texto
print(string1 * 5) #este operador multiplica o texto um determinado número de vezes

#Cuidado quando estiver trabalhando com strings e números. Os números podem ser strings, dependendo do caso...
#Quando utilizamos números como string, os operadores vão funcionar do mesmo jeito, pois é um texto. Mais exemplos:
string3 = '2'
string4 = '5'

print(string3 + string4)
print(string3 * 5)

#Se tratarmos números como números e não como strings, teremos um resultado diferente.

string5 = 2
string6 = 5

print(string5 + string6)
print(string5 * 5)
```

    oi, tudo bem?
    oi, oi, oi, oi, oi,
    25
    22222
    7
    10


## Métodos com Strings

- .strip() : apaga espaços em branco no texto
    * rstrip(): apaga espaços em branco à **direita** (right) do texto
    * lstrip(): apaga espaços em branco à **esquerda** (left) do texto

- .lower() : deixa todo o texto em caixa baixa

- .upper() : deixa todo o texto em caixa alta

- .title() : deixa a primeira letra de cada palavra em maiúscula

- .swapcase() : primeira letra da frase minúscula

- .capitalize() : primeira letra da frase maiúscula

- .count(argumento) : conta o número de vezes em que o argumento especificado aparece no texto

- .replace(old, new) : substitui palavra ou caractere ->.replace('substitui esse', 'por esse')

- .find(argumento) : encontra a primeira incidência do argumento, retorna a posição dele na string

- .split(sequência) : separar uma sequência

- str.join(sequencia) : juntar uma sequência utlizando um caracter, ou espaço especificado (ver exemplo mais abaixo)

- .center(tamanho, 'caracter de preenchimento') : centraliza o texto, preenche com caracter (o padrão é espaço)

- .rjust(tamanho, 'caracter de preenchimento') : justifica o texto à **direita** (right)

- .ljust(tamanho, 'caracter de preenchimento')  : justifica o texto à **esquerda** (left)


ex:



```python
#Exemplos do uso de .strip()

texto = '   Olá mundo!   '

print('Texto antes: ' + texto)
print('Texto sem espaços em branco: ' + texto.strip())
print('Texto sem espaços em branco à direita: ' + texto.rstrip())
print('Texto sem espaços em branco à esquerda: ' + texto.lstrip())

#Exemplo do uso de .lower()
print('Texto convertido para letras minúsculas: ' + texto.lower())

#Exemplo do uso de .upper()
print('Texto convertido para letras maiúsculas: ' + texto.upper())

#Exemplo do uso de .title()
print('Texto convertido para primeira letra de cada palavra em maiúscula: ' + texto.title())

```

    Texto antes:    Olá mundo!
    Texto sem espaços em branco: Olá mundo!
    Texto sem espaços em branco à direita:    Olá mundo!
    Texto sem espaços em branco à esquerda: Olá mundo!
    Texto convertido para letras minúsculas:    olá mundo!
    Texto convertido para letras maiúsculas:    OLÁ MUNDO!
    Texto convertido para primeira letra de cada palavra em maiúscula:    Olá Mundo!



```python
#Exemplos do uso de .count()

texto_2 = 'A verdadeira coragem é ser honesto consigo mesmo. (Mr Robot)'

#conta quantas vezes a letra 'a' aparece na frase (obs: diferencia-se maiúsculas de minúsculas)
#portanto o programa não irá contar a incidência de maiúsculas, neste caso.
print(texto_2.count('a'))

#Agora verificando 'A' maiúscula
print(texto_2.count('A'))
```

    3
    1



```python
#Exemplo do uso de .replace(old, new)

texto_3 = 'Maria gosta de televisão.'

print('Antes a frase era assim: ' + texto_3)
print('Agora a frase ficou assim: ' + texto_3.replace('televisão', 'videogame'))


#Exemplo do uso de .find()
#irá informar em que posição da string começa a palavra 'gosta'
print('\nPosição da palavra na frase: {}' .format(texto_3.find('gosta')))


#ao invés de uma palavra, pode encontrar uma letra (a 1ª vez que ela aparecer na string)
print('\nPosição do caracter na frase: {}' .format(texto_3.find('i')))
```

    Antes a frase era assim: Maria gosta de televisão.
    Agora a frase ficou assim: Maria gosta de videogame.

    Posição da palavra na frase: 6

    Posição do caracter na frase: 3



```python
#Exemplo de uso de .split()

#Com uma frase
texto_4 = '''Este é o mundo em que vivemos. Pessoas se dando bem em cima dos erros alheios
para manipularem e usarem uns aos outros. (Mr Robot)'''

print(texto_4.split())


```

    ['Este', 'é', 'o', 'mundo', 'em', 'que', 'vivemos.', 'Pessoas', 'se', 'dando', 'bem', 'em', 'cima', 'dos', 'erros', 'alheios', 'para', 'manipularem', 'e', 'usarem', 'uns', 'aos', 'outros.', '(Mr', 'Robot)']



```python
#Exemplo de .join(sequencia)

s = ', ' #vai unir os elementos da sequencia entre ', '
sequencia = ('a', 'b', 'c')

print(s.join(sequencia))

#outro exemplo
x = ' - ' #vai unir os elementos da sequencia entre ', '
sequencia_2 = ('a', 'b', 'c')
print(x.join(sequencia_2))

#outro exemplo
y = ' ' #vai unir os elementos da sequencia entre ' '
sequencia_3= ('Olá', 'mundo', '!')
print(y.join(sequencia_3))
```

    a, b, c
    a - b - c
    Olá mundo !



```python
#Exemplo de aplicação .rjust(tamanho, 'caracter de preenchimento')
palavra = 'olá'
print('Justificado à direita:    ' + palavra.rjust(20, '*'))

#Exemplo de aplicação .ljust(tamanho, 'caracter de preenchimento')
palavra = 'olá'
print('Justificado à esquerda:    ' + palavra.ljust(20, '*'))

#Exemplo de aplicação .center(tamanho, 'caracter de preenchimento')
palavra = 'olá'
print('Justificado centralizado:    ' + palavra.center(20, '*'))

#Outro exemplo:
print('Somador de número inteiro'.center(40, '-'))
```

    Justificado à direita:    *****************olá
    Justificado à esquerda:    olá*****************
    Justificado centralizado:    ********olá*********
    -------Somador de número inteiro--------


## Funções: strings

- len() : mostra o tamanho do texto (nº de caracteres)


```python
texto_4 ='''
Mudamos o mundo todos os dias.
Mas para mudar o mundo de um jeito significativo,
leva muito mais tempo do que as pessoas têm.
Nunca acontece ao mesmo tempo.
É devagar. É metódico. É exaustivo.
Nem todos temos o estômago para isso.
'''

print('O texto tem {} caracteres.' .format(len(texto2)))

```

    O texto tem 237 caracteres.


# Fatiar uma string, Listas

Começa a contar de 0
e soma +1 ao último nº, pois o python não exibe a última posição.

Utiliza-se -1, -2, -3, n para contar inversamente.

**[de posição : até posição]**


Se deixar em branco a posição 'de', o Python considera que começa em 0 por padrão.

**[:até posição]**


Se deixar em branco a posição 'até ', o Python considera que termina na última posição por padrão.

**[de posição:]**



```python
string = 'paralelepipedo'

print('Da posição 4 até posição 8: ' + string[4:8])
print('Da posição inicial até posição 4: ' + string[:4])
print('Da posição 8 até posição final: ' + string[8:])

#com listas
lista = [0, 1, 2, 3, 4, 5]
print('\n', lista)

print('Da posição 2 até posição 4: {}' .format(lista[2:4]))
print('Da posição inicial até posição 4: {}' .format(lista[:4]))
print('Da posição -1: {}' .format(lista[-1:]))

```

    Da posição 4 até posição 8: lele
    Da posição inicial até posição 4: para
    Da posição 8 até posição final: pipedo

     [0, 1, 2, 3, 4, 5]
    Da posição 2 até posição 4: [2, 3]
    Da posição inicial até posição 4: [0, 1, 2, 3]
    Da posição -1: [5]


# Função sum() max() min() para números

- sum(): retorna a soma

- max(): retorna o maior nº

- min(): retorna o menor nº



```python
#exemplo de sum()
print('A soma da sequência é {}' .format(sum([1, 2, 3, 4, 5])))

#exemplo de max()
print('O maior nº da sequência é {}' .format(max(5, 6, 2, 8)))

#exemplo de min()
print('O menor número da sequência é {}' .format(min(5, 6, 2, 8)))
```

    A soma da sequência é 15
    O maior nº da sequência é 8
    O menor número da sequência é 2


# Definindo funções


def nome_da_função(parâmetro):      -> Tanto pode conter um parâmetro quanto não. Depende do caso </br>
    '''Comentário sobre o que a função faz (Docstring)'''
    </br>  Ações da função indentadas



*Sempre usar 2 linhas em branco antes e depois de cada função*
EX:


```python
# aqui a variável 'nome' é o parâmetro da função
def ola(nome):
    '''Saúda uma pessoa pelo nome'''
    print('\nOlá, ' + nome + '. É um prazer te conhecer!')

# Aqui recebemos do usuário um input que informará a variável 'nome'
nome = str(input('\nQual é o seu nome? ').strip().title())

# aqui chamamos a função e informamos qual é o argumento da variável 'nome'
ola(nome)

# agora o programa age sozinho e executa a função
```


    Olá, Lays. É um prazer te conhecer!



```python
# Um exemplo que não precisa passar um parâmetro
def ola():
    '''exibe uma mensagem padrão'''
    print('\nOlá à todos! É um grande prazer recebê-los aqui!!!\n')

# Chamamos a função
ola()

print('---' * 15)
print('\nOutro exemplo:')

# Outro exemplo
import random
def sorteia():
    '''Exibe um nº sorteado de uma lista de 0 a 10'''
    lista = random.randrange(0, 10)
    print(lista)

# Chamamos a função
sorteia()

```


    Olá à todos! É um grande prazer recebê-los aqui!!!

    ---------------------------------------------

    Outro exemplo:
    4

---

# Anexos

# Como escrever um programa em Python
> A maneira mais simples para escrever um programa em Python é utilizando um editor de texto. Assim, usando qualquer editor, você pode criar um programa e salvá-lo em um arquivo (com extesão .py).
Para executar o programa basta digitar "python nome_do_programa.py" em um terminal, a partir do mesmo diretório onde o programa foi salvo.
Os editores de texto comuns, no entanto, não oferecem muitos recursos para edição de programas em Python.
    > Retirado de: <https://panda.ime.usp.br/panda/static/data/python/ide.html>

## IDEs
*(Ambiente integrado de desevolvimento de programas (ou IDE do inglês Integrated Development Environment)*

- __[PyCharm](http://www.jetbrains.com/pycharm)__ Meu IDE preferido. É bastante customizável. Facilita a programação com 'autocompletar' e dá dicas para que seu código esteja nas normas do PEP 8.


## REPLs alternativos
(implementação interativa)

* *Gosto dos notebooks para criar cadernos de aprendizado como este próprio, pois possibilitam entrada de texto (markdown) e código.. é ótimo para criar exemplos..*
* *Pelo fato de ser interativo, é ótimo para testar códigos mais rapidamente durante a aprendizagem, pois basta teclar* **ctrl + ENTER** *para executar um código rapidamente após escrevê-lo, e o output já sai na linha de baixo..*

- __[Pacote Anaconda](https://www.anaconda.com/download/)__ vem com as famosas aplicações:
    - Jupyter Notebook
    - Jupyterlab
    - Spyder
    - Outras


## Editores de texto

<!-- - __[Sublime Text](http://www.sublimetext.com)__ Por ser um editor de texto, é muito mais leve e abre muito mais rapidamente do que o PyCharm. Pode ser amplamente 'configurado'/'estilizado' para ficar ao gosto do programador.
    Complementos para deixar o Sublime text ainda melhor:
    - __[Install Package Control](https://packagecontrol.io/installation#st3)__ Antes de tudo, instale o Install Package Control, com ele vai ficar muito mais fácil instalar outros package. (no Sublime 3, tecle CTRL + ', vai abrir um console na parte inferior, nele você vai colar o código que está no link do Install Package Control e teclar ENTER. Depois de instalado, basta teclar CTRL + p, e digitar no console que abrirá na parte superior:

        - Install package (para instalar um novo plugin), ENTER, Nome do plugin, ENTER

        - Remove package (para desinstalar um plugin), ENTER, Nome do plugin, ENTER

        - Disable package (para desativar um plugin) // // //

        - Enable package (para ativar um plugin) // // //



    - Anaconda

    - Python PEP8 Autoformat

    - Jedi -->

# Livros recomendados
__[Clique p/ acessar Minha Pasta no GDrive](https://drive.google.com/open?id=1RnAIlg5iiw20kD0zcg6S56vYIQu_k2VN)__

- **Curso Intensivo de Python Uma** - Eric Matthes

- **Automatize tarefas macantes com PYTHON **- Al Sweigart

- **Python Fluente **- Luciano Ramalho *(ainda não tenho)**

- **Python CookBook - Receitas para dominar Python 3** - Alex Martelli, David Ascher, Anna Martelli Ravenscroft

- **Dive Into Python 3** - Mark Pilgrim

- **Python_para_desenvolvedores_2ed**

- **Invent Your Own Computer Games** - Al Sweigart

- **Making Games** - Al Sweigart



# Links úteis:

### Para tirar dúvidas:

- __[StackOverflow BR ](https://pt.stackoverflow.com/)__ Fórum - em português

- __[StackOverflow](https://stackoverflow.com)__ Fórum - em inglês


### Para consultar

- __[Python.org](https://www.python.org/)__ (inglês) Página oficial do Python, dá para baixar o Python e tem acesso a toda a documentação.

- __[The Python Guru:](https://thepythonguru.com/)__ (inglês) Um ótimo tutorial em texto sobre Python

- __[W3Schools:](https://www.w3schools.com/python/default.asp)__ (inglês) Vários exemplos e materiais

- __[CookBook da Wiki Python BR:](https://wiki.python.org.br/CookBook)__ Trechos de código como referência

- __[Wiki Python BR - geral:](https://wiki.python.org.br/PythonBrasil)__ Vários informações sobre Python


### Para exercitar:

- __[Lista de exercícios do Wiki Python BR](https://wiki.python.org.br/ListaDeExercicios)__ Recomendada lista de exercícios para treinar durante a aprendizagem

- __[Codingbat](https://codingbat.com/python)__ (inglês) exercícios feitos na própria plataforma

- __[Coderbat](https://www.coderbyte.com/)__ (inglês) exercícios feitos na própria plataforma

### Exemplos:

- __[Scripts Python](https://www.scriptbrasil.com.br/codigos/python/)__ Vários códigos em Python


### Outros:

- __[Markdown CheatSheet JupyterNotebook - IBM:](https://www.ibm.com/support/knowledgecenter/en/SSQNUZ_1.1.0/dsx/markd-jupyter.html)__ Formatar textos com Markdown no JupyterNotebook

- __[PEP 8 - Guia de estilo](https://www.python.org/dev/peps/pep-0008/)__ Guia oficial de estilo. "O jeito correto de escrever o código".

- __[Guia comparativo de código do antigo para o novo](https://pyformat.info/)__

### Para aprender:

- __[Introdução à Computação com Python - PandaUSP](https://panda.ime.usp.br/cc110/static/cc110/index.html#introducao-a-computacao-com-python)__

- __[Princípios de Desenvolvimento de Algoritmos em Python - PandaUSP](https://panda.ime.usp.br/algoritmos/static/algoritmos/index.html)__

- __[Aulas em Python: Edição interativa - PandaUSP](https://panda.ime.usp.br/aulasPython/static/aulasPython/index.html)__

- __[Livro: Python Practice Book](https://anandology.com/python-practice-book/index.html)__

- __[DevFuria - Artigos e curso Python:](http://www.devfuria.com.br/python/)__ Várias informações importantes

- __[Livro: Como Pensar como um cientista da computação](http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/apresentacao.html)__ livro traduzido para o português (leitura online)

- __[Green Tea Press - Free books by Allen B. Downey](https://greenteapress.com/wp/)__ (inglês) Ler ou baixar gratuitamente livros do Allen Downey, como o Think Python.

- __[Livro: Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html)__


### Livros p/ Download:

- __[Python Books](https://pythonbooks.revolunet.com/)__ (inglês)

- __[Al Sweigart (Automatize tarefas maçantes com Python)](http://inventwithpython.com/invent4thed/)__ (inglês) livros, recursos de livros do próprio autor.


### Referências: Programadores

- **Luciano Ramalho**
    - __[Github](https://github.com/ramalho)__

- **Fernando Massanori**
    - __[Github](https://github.com/fmasanori)__
    - __[Twitter](https://twitter.com/fmasanori)__

- **Kenneth Reitz**
    - __[Site Pessoal](https://www.kennethreitz.org/)__
    - __[Github](https://github.com/kennethreitz)__
    - __[Requests](http://docs.python-requests.org/pt_BR/latest/)__

- **Raymond Hettinger**
    - __[Site Pessoal](https://rhettinger.wordpress.com/)__
    - __[Github](https://github.com/rhettinger)__


# Plataformas de Cursos gratuitos recomendados:

- **CursoEmVideo** <https://www.cursoemvideo.com/>
    * Tem certificado
    * Português
    * Ótimo para aprender o básico


- **Python para Zumbis** <https://www.pycursos.com/python-para-zumbis/>
    * Ótimo curso, porém desatualizado (Python 2)
    * Dá para aprender bastante


- **DataCamp** <https://www.datacamp.com/>
    * Tem certificado
    * Inglês
    * Bom para praticar, serve mais como um complemento
    * Tem cursos pagos também


- **Udacity** <https://br.udacity.com>
    * Não tem certificado para cursos gratuitos
    * Inglês
    * Recomendado já ter algum conhecimento básico
    * Tem cursos pagos também

- **PyCubator** <http://df.python.org.br/pycubator/>
    * Em forma de texto
    * Em inglês

## Youtube

Alguns canais legais sobre Python

- __[Clever Programmer ](https://www.youtube.com/channel/UCqrILQNl5Ed9Dz6CGMyvMTQ)__

- __[Coding is for girls](https://www.youtube.com/channel/UC0hNd2uW8jTR5K3KBzRuG2A)__

- __[Al Sweigart](https://www.youtube.com/channel/UCRjTEkDLPREZNlREZMlotMQ)__

- __[Curso em Vídeo](https://www.youtube.com/channel/UCrWvhVmt0Qac3HgsjQK62FQ)__

## PodCasts

- __[Curto Circuito - Henrique Bastos](https://henriquebastos.net/tags/curto-circuito/)__

- __[Castálio](https://itunes.apple.com/br/podcast/castalio-podcast/id446259197)__

- __[Sudocast](https://www.sudocast.com.br/)__
