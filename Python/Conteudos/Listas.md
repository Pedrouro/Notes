# Listas ou vetores

As listas é quando um conjunto de variáveis é armazenado em um objeto.

## Criando uma lista

```python
lista = ["Camaro", "Mustang", "Tesla", "Fusca", "Abacate"]

A = []

x = ["Arnaldo", 100, false , 0.5]
```

## Fatiamento de lista

```python
lista = ["p", "y", "t", "h", "o","n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
```

Explicação: Utilizamos o fatiamento quando queremos selecionar apenas alguns elementos de uma lista.

## Percorrer uma lista

A forma mais comum para percorrer os dados de umalista pe utilizando o comando for.

```python
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

## Compreensão de listas

Uilizamos a compreensão de lista quando precisamos criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova losta aplicando alguma modificação nos elementos de uma lista existente.

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print(pares)
```

ou

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)
```