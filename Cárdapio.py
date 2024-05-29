import os 

os.system("cls || clear")


os.system("cls || clear")
while True:
 print("1 - Picanha  vale R$: 25,00")
 print("2 - Lasanha vale R$: 20,00")
 print("3 - Strogonoff vale R$: 18,00")
 print("4 - Bife acebolado vael R$: 15,00")
 print("5 - Pão com ovo vale R$: 5,00\n")
 opcao = int(input("Escolha uma das opções:"))

 match(opcao):
   case 1:
      print("Picanha || R$; 25,00")
      break 
   case 2:
      print("Lasanha || R$: 20,00")
      break
   case 3:
      print("Strogonoff || R$: 18,00 ")   
      break
   case 4:
      print("Bife Acebolado || R$: 15,00")
      break
   case  5:  
      print("Pão com ovo || R$: 5,00")
      break
   case _:
     # print("||Opção escolhida inválida, tente novamente||")  
     input("||Opção escolhida inválida, tente novamente||")
