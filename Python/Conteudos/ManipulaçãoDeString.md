# Manipulação de Strings

O Python possui diversos métodos para manipular objetos da classe string (str), alguns deles são:

## Upper()

```python
string = "pYtHon"

print(string.upper())

# RESULTADO: PYTHON
```
Explicação: Transforma todos os caracteres do objeto para a sua forma maiúscula.

## Lower()

```python
string = "pYtHon"

print(string.lower())

#RESULTADO: python
```
Explicação: Transforma todos os caracteres do objeto para a sua forma minúscula.

## Title()

```python
string = "pYtHon"

print(string.title())

#RESULTADO: Python
```
Explicação: Transforma o primeiro caractere em sua forma maiúscula e o resto em suas formas minúsculas.

## Strip()

```python
string = "    Python "

print(string.strip())

#RESULTADO: "Python"
```
Explicação: Remove os espaços em branco no começo e no fim de um objeto.

## Lstrip()

```python
string = "    Python  "

print(string.lstrip())

#RESULTADO: "Python  "
```
Explicação: Remove os espaços em branco no começo de um objeto.

## Rstrip()

```python
string = "    Python  "

print(string.rstrip())

#RESULTADO: "    Python"
```
Explicação: Remove os espaços em branco no fim de um objeto.

## Center()

```python
string = "Python"

print(string.center(10, "#"))

#RESULTADO: "##Python##"
```
Explicação: Aumenta o tamanho o objeto, adicionando os caracteres especificados. Se não especificar nenhum caractere, o método utilizara espaços em branco para aumentar o tamanho do objeto.

## Join()

```python
string = "Python"

print(".".join(string))

#RESULTADO: "P.y.t.h.o.n"
```
Explicação: Separa os caracteres de um objeto com o caractere especificado.

## Interpolação de variáveis

```python
nome = "Pedro"
idade = 30
profissao = "Programador"

print(f"Olá, me chamo {nome}, tenho {idade} anos e sou {profissao}.")

#RESULTADO: "Olá, me chamo Pedro, tenho 30 anos e sou programador."
```
Explicação: A utilização de variáveis dentro de uma string é feita utilizando o nome da variável dentro de chaves e a inserção do caracter "f" antes da string que será formatada.

## String de múltiplas linhas

```python
nome = "Pedro"

mensagem = f"""
        Olá, meu nome é {nome},
    estou aprendendo Pyhon.

"""

#RESULTADO: "Olá, meu nome é Pedro,
#    estou aprendendo Pyhon".
```

Explicação: Para criar uma string que ocupe mais de uma linha, utilizamos 3 aspas simples(''') ou 3 aspas duplas (""") no inicio e no final da string.