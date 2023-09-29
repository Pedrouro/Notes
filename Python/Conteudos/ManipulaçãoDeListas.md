# Manipulação de Listas

O Python possui diversos métodos para manipular objetos da classe lista (list), alguns deles são:

## [ ].append

Utilizamos o append para adicionar elementos à lista.

```python
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]
```

## [ ].clear

Utilizamos o clear para limpar uma lista.

```python
lista = [1, "Python", [40, 30, 20]]

print(lista)  # [1, "Python", [40, 30, 20]]

lista.clear()

print(lista)  # []
```

## [ ].copy

Utilizamos o copy para retornar uma copia de uma lista. O copy é muito utilizado para evitar alterações acidentais

```python
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
```

## [ ].count

Utilizamos o count para determinar quantas vezes um objeto aparece em uma determinada lista.

```python
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
```

## [ ].extend

Utilizamos o extend quando queremos juntar listas.

```python
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
```

## [ ].index

Utilizamos o index para saber qual é a posição da primeira ocorrencia de um objeto.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
```

## [ ].pop

Utilizamos o pop para remover elementos de uma lista. Por padrão o pop remove o último elemento de uma lista e para remover um elemento em específico precisamos adicionar a posição do elemento que será removido.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
```

## [ ].remove

Utilizamos o remove para remover algum elemento em específico de uma lista.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]
```

## [ ].reverse

Utilizamos o reverse para espelhar uma lista.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]
```

## [ ].sort

Utilizamos o sort para ordenar uma lista. O sort possui o parâmetro reverse que ordena a lista em ordem alfabética inversa.

```python
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
```

## len

Utilizamos o len para descobrir o tamanho de um objeto.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5
```

## sorted

Utilizamos o sorted para ordenar uma lista. O sorted possui o parâmetro reverse que ordena a lista em ordem alfabética inversa.

```python
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
```
