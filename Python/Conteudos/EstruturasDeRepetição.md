# Estruturas de repetição

São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido préviamente ou determinado através de uma expressão lógica.

## For

O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

```python
texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, sep=" ")
```

Explicação: O código separa as vogais de uma palavra e passa elas para a sua forma maiúscula. 

## Função **range**

Range é uma função buit-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio(intrusivo) para um fim (exclusivo). Ela é comumente utilizade junto de laços do repetição FOR.

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step(opcional).

```python
for numero in range(0, 11):
    print(numero)
```
Explicação: Exibe uma sequência dos números de 0  a 10.

```python
for numero in range(5, 51, 5):
    print(numero)
```
Explicação: Exibe a tabuada do 5.

## While

O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar o while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

```python
opcao = -1

while opcao != 0:
    opcao = input("[1] Sacar\n[2] Extrato\n[0] Sair\n: ")

    if opcao == 1:
        print("Sacando... ")

    elif opcao == 2:
        print("Exibindo extrato... ")
```

## Break e Continue

As funções break e continue são utilizadas para parar um laço de repetição e para pular uma repetição de um laço respectivamente.