# Estruturas condicionais

A estrutura condicional permite o desvio do fluxo de controle, quando determinadas expressões lógicas são atendidas.

## if else

```python
saldo = 200
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("realizando saque")

else:
    print("saldo insuficiente")
```

## elif

O elif é a contração do else if no python, que utilizamos para testar uma condição apenas se a anterior for false.

## if ternário

o if ternário é uma estrutura de repetição que é feita em apenas uma linha de código.

```python
saldo = 1000
saque = 300

status = "Sucesso" if saldo >= saque else "Falha"

# se saldo for maior ou igual á saque, status será "Sucesso", se não, status será "Falha"
```