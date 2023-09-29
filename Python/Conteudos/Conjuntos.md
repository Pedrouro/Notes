# Conjuntos ou Sets

Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.



## Criando um set

Os sets podem ser criados utilizando chaves ( { } ) ou passando um objeto iteravel para o método set().

```python
conjunto = {1, 2, 3, 1, 3, 4}  # {1, 2, 3, 4}

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio",)) # {"gol", "celta", "palio",}
```


## Acessando dados de um set

Os sets não suportam indexação e nem fatiamento, caso queira acessar osseus valors é necessário converter o conjunto para uma lista.

```python
numeros = {1, 2, 3, 4, 1, 2}

numeros = list(numeros)

print(numeros[0])
```

## Percorrer um set

```python
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```