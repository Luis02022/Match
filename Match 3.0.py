import os 

os.system("cls || clear")

dia = int(input("Escolha um dia da semana de 1 á 7:"))

while True:
 match(dia):
   case 1:
      print("Domingo")
      break
   case 2: 
      print("Segunda-Feira") 
      break
   case 3:   
      print("Terça-Feira")
      break
   case 4:   
      print("Quarta-Feira")
      break
   case 5:   
      print("Quinta-Feira")
      break
   case 6:   
      print("Sexta-Feira")
      break
   case 7:   
      print("Sábado")
      break
   case _:
       print("Opção inválida")
       break
