# Manipulação de Conjuntos

O Python possui diversos métodos para manipular sets, alguns deles são:

## { }.union( )
```python
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
print(resultado)
```
Explicação: O método union junta os valores de ambos os sets.

## { }.intersection( )
```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b) # {2, 3}
print(resultado) 
```
Explicação: O método intersection retorna os valores que estão presentes em ambos os sets.

## { }.difference( )

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b) # {1}
print(resultado)

resultado = conjunto_b.difference(conjunto_a) # {4}
print(resultado)
```
Explicação: O método difference retorna os valores do conjunto_a que não estão presentes no conjunto_b.

## {}.symmetric_difference( )

```python
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)  # {1, 4}
print(resultado)
```

Explicação: O  método symmetric_difference retorna os valores que estão presentes na interseção dos conjuntos.

## {}.issubset( )

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
```
Explicação: O método issubset retorna o valor booleano **true** caso todos os elementos do conjunto_a estão no conjunto_b, o que faz o conjunto_a ser um **sub-conjunto** do conjunto_b.

## {}.issuperset( )

```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
```
Explicação: O método issuperset retorna o valor booleano **true** caso algum elemento do conjunto_a não estiver no conjunto_b, o que faz o conjunto_a ser um **super-conjunto** do conjunto_b.

## {}.isdisjoint( )

```python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
```

Explicação: Retorna true caso todos os elementos do conjunto_a forem diferentes dos elementos do conjunto_b.

## {}.add( )

```python
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)
```

Explicação: O método add adiciona um elemento à um set caso esse elemento ainda não esteja presente.

## {}.clear( )

```python
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}
```

Explicação: O método clear limpa todos os valores de um set.

## {}.copy( )

```python
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}
```

Explicação: Poh, serio q vc ta olhando a explicação? ELE COPIA CARA '-', bgl é autoexplicativo.

## {}.discard( )

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
```
Explicação: O método discord elimina valores de u set. Caso o set não possua o valor, nada acontecerá.

## {}.pop( )

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}
```
Explicação: O método pop remove o primeiro valor do set.

## {}.remove( )

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
```
Explicação: O método remove retira elementos de um set. Caso o set não possua o elemento, o método retornará um erro.

## len( )

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10
```
Explicação: O método len retorna o tamanho do set.

## in

```python
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
```
Explicação: O operador in retorna true se o elemento indicado estiver dentro do set.