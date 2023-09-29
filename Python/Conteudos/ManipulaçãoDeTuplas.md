## Manilulação de tuplas

O Python possui diversos métodos para manipular objetos da classe tupla (tuple), alguns deles são:

## [ ].count

Utilizamos o count para determinar quantas vezes um objeto aparece em uma determinada tupla.

```python
cores = ("vermelho", "azul", "verde", "azul",)

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1
```

## [ ].index

Utilizamos o index para saber qual é a posição da primeira ocorrencia de um objeto.

```python
linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0
```

## len

Utilizamos o len para descobrir o tamanho de um objeto.

```python
linguagens = ("python", "js", "c", "java", "csharp",)

print(len(linguagens))  # 5
```