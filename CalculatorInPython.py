## Variáveis (interface)
wlc = "Welcome to my calculator"

## "Interface"
print("=-=-="*14)
print(f"{wlc: >47}")
print("=-=-="*14)
print("-Essa calculadora funciona somente com números inteiros até o momento-")
print(''*15)
print(''*15)
print("---> Você deseja fazer um calculo?")
print(''*15)
print(''*15)

## Variáveis (Do programa)
resposta = input("[Sim] ou [Não]: ").upper().startswith('S')

#contadores
contador1 = 0
contador2 = 0

if resposta is True:
    while contador1 == 0:
        print(''*15)
        print("--->         ótimo! Vamos começar pelas primeiras opções          <---")
        print("=-=-="*14)
        
        falsenumber1 = input("Digite um número: ")
        falsenumber2 = input("Digite o segundo número: ")
        falseoperador = input("Digite o operador desejado [/, +, -, *]: ")

        if falsenumber1.isdigit() and int and falsenumber2.isdigit() and int:
            number1 = float(falsenumber1)
            number2 = float(falsenumber2)

            if falseoperador == '/':
                print(''*15)
                print(f"O resultado da divisão entre {number1} e {number2} é: ")    
                divisao = (number1/number2)
                print(f'{divisao}')
                print(''*15)
                print("---> Você quer testar outra vez? ")  
                resposta2 = input("[Sim] ou [Não]: ").upper().startswith('S')
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                contador1 = 0
                if resposta2 is True:  
                    contador1 = 0
                else:
                    print("Você saiu do programa! até a próxima!") 
                    contador1 = 1 
            elif falseoperador == '*':
                print(''*15)
                print(f"O resultado da multiplicação entre {number1} e {number2} é: ")    
                multiplicacao = (number1*number2)
                print(f'{multiplicacao}')
                print(''*15)
                print("---> Você quer testar outra vez?")    
                resposta2 = input("[Sim] ou [Não]: ").upper().startswith('S')
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                contador1 = 0
                if resposta2 is True:  
                    contador1 = 0
                else:
                    print("Você saiu do programa! até a próxima!")               
                    contador1 = 1 
            elif falseoperador == '+':
                print(''*15)
                print(f"O resultado da adição entre {number1} e {number2} é: ")    
                soma = (number1+number2)
                print(f'{soma}')
                print(''*15)
                print("---> Você quer testar outra vez?")    
                resposta2 = input("[Sim] ou [Não]: ").upper().startswith('S')
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                contador1 = 0
                if resposta2 is True:  
                    contador1 = 0
                else:
                    print("Você saiu do programa! até a próxima!")
                    contador1 = 1 
            elif falseoperador == '-':
                print(''*15)
                print("O resultado da sua divisão é: ")    
                divisao = (number1-number2)
                print(f'{divisao}')
                print(''*15)     
                print("---> Você quer testar outra vez? ")           
                resposta2 = input("[Sim] ou [Não]: ").upper().startswith('S')
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15)   
                print(''*15) 
                if resposta2 is True:  
                    contador1 = 0
                else:
                    print("Você saiu do programa! até a próxima!")
                    contador1 = 1 
        else:
            print(''*15)
            print(''*15)
            print("---> VOCÊ NÃO DIGITOU ALGO VÁLIDO! (sugestão: digite somente números inteiros!) <---")
            print(''*15)
            print(''*15)
            contador1 = 0
else:
    print("Você saiu do programa :/")