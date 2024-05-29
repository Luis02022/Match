import os 

os.system("cls || clear")
resultado = False 
#resultado = 0

while True :
 os.system("cls || clear")
 a = int(input("Digite o primeiro número:"))
 operador = input("Digite o operador + - * /:")
 b = int(input("Digite o segundo número:"))


 
 match(operador):
    case '+':
        resultado = a + b
        break
    case '-':
        resultado = a - b    
        break
    case '*':
        resultado = a * b    
        break
    case '/':
        resultado = a / b
        break
    case _:
     #print("||Operador não digitado||") 
     input("||Operador não digitado||")        
 

print(f"{a} {operador} {b} = {resultado}")        