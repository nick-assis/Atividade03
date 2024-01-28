def calculadora(num1, num2, tipo):
    if(tipo == 1):
     return num1 + num2
    elif(tipo == 2):
       return num1 - num2
    elif(tipo == 3):
       return num1 * num2
    elif(tipo == 4):
       return num1 / num2
    else:
       return 0
       
iniciar = True

while(iniciar == True):
   print("Selecione uma opção")
   print("1. Adição 2. Subtração 3.Multiplicação 4.Divisão")
   tipo = int(input())
   if(tipo < 0) or (tipo > 4):
      print("Opção inválida. Selecione de 1 a 4")
   elif(tipo == 0):
      iniciar = False
   else:
      print("Insira o primeiro número: ")
      num1 = int(input())
      print("Insira o segundo número: ")
      num2 = int(input())
      resultado = calculadora(num1, num2, tipo)
      print("O resultado da operação é: ", resultado)
       
                    