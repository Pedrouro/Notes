idade = float(input("Digite a sua idade: "))

if idade < 18 and idade >=1:
    print("Voce não pode tirar a CNH por ser menor de idade")

elif idade < 0:
    print("Voce ainda não nasceu, volte novamente daqui a alguns anos")

elif idade >= 18:
    print("Voce ja pode tirar a CNH, Parabens!!!")