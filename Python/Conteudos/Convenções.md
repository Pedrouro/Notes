# Convenções
A linguagem de programação Python possui algumas regras estabelecidas pela propria comunidade de desenvolvimento, com o objetivo de padronizar os códigos. Um dos exemplos é a nomeação de variaveis, que seguem alguns padroes para melhor compreensão dos códigos.

## Nomeação de constantes

O Python não possui um comando para a declaração de constantes, por isso a comunidade criou um acordo de que as variáveis que possuem um valor imutável devem ser escritas com todas as letras maiúsculas.

```python
PI = 3,1415

ENDERECO = "Rua 123"
```

## Identação

O Python não possui um caracter especifico para o fechamento de um bloco, para isso ele utiliza a identação do código para saber onde começa e termina um bloco de comando.

```python
def sacar(self, valor: float) -> None:

    if self.saldo >= valor:

        self.saldo -= valor

    # fim do bloco do if

# fim do bloco do método
```