## IMPORTING ALL THE REQUIRED LIBRARIES

from datetime import datetime 
from datetime import date 
from time import sleep 
import os,socket,sys
from dhooks import Webhook 
import pyfiglet

#############  Functions   ################
result = pyfiglet.figlet_format("FOOD  ON  PHONE", font = "big" )

nointernet = pyfiglet.figlet_format("No Internet", font = "banner" )

hook = Webhook('Enter Your API here')

today = date.today()

now = datetime.now()

lines  = ("-" * 40)

print(str(lines))

ip = socket.gethostbyname(socket.gethostname())
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
clear()

if ip=="127.0.0.1":
    print(nointernet)
    print("Please Connect to Internet")
    exit()
else:
    print("Connected, with the IP address: "+ ip )

#############  Functions   ################

print(now)
print(result)
print("""
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
        \n\n
        You can order your favourite food!
        """)
        
        # sleep(0.5)

        # sleep(0.7)
def validation():
        while True:
                name = input("Please enter your name\n")
                
                print("Hello "+ name.upper() +"!\n"+"Welcome to Food on Phone!\n\n ")
                print("What would you like from our menu today? \nHere is what we are serving.\n", end="\r")
                menuTYPE= input("  1 --for--SHAKES\n\n  2--for-- JUICES\n\n  3--for-- COFFEE\n\n  4--for-- OTHER \n\n".upper())
                if menuTYPE.upper() in ('SHAKES','JUICES','COFFEE','OTHER','1','2','3','4'):
                        
                        
                        
                        if menuTYPE.upper().endswith('1'):
                                
                                
                                print("Here is what we are serving in Shakes.\n", end="\r")
                                menu= input("  1 --for--BANANA SHAKE\n\n  2--for-- MANGO SHAKE\n\n  3--for-- OREO SHAKE\n\n  4--for-- PAPAYA SHAKE \n\n 5--for-- STRAWBERRY SHAKE \n\n".upper())
                                if menu.upper().endswith('1'):
                                        menu1=('BANANA SHAKE')
                                elif menu.upper().endswith('2'):
                                        menu1=('MANGO SHAKE')
                                elif menu.upper().endswith('3'):
                                        menu1=('OREO SHAKE')       
                                elif menu.upper().endswith('4'):
                                        menu1=('PAPAYA SHAKE')
                                elif menu.upper().endswith('5'):
                                        menu1=('STRAWBERRY SHAKE')
                                        
                                        
                        elif menuTYPE.upper().endswith('2'):
                                
                                
                                print("Here is what we are serving in Juices.\n", end="\r")
                                menu= input("  1 --for--MIXED FRUIT\n\n  2--for-- ORANGE\n\n  3--for-- POMEGRANATE\n\n  4--for-- CARROT \n\n 5--for-- SUGARCANE \n\n".upper())
                                if menu.upper().endswith('1'):
                                        menu1=('MIXED FRUIT')
                                elif menu.upper().endswith('2'):
                                        menu1=('ORANGE')
                                elif menu.upper().endswith('3'):
                                        menu1=('POMEGRANATE')       
                                elif menu.upper().endswith('4'):
                                        menu1=('CARROT')
                                elif menu.upper().endswith('5'):
                                        menu1=('SUGARCANE')
                                        
                                        
                                        
                        
                                
                                
                        elif menuTYPE.upper().endswith('3'):
                                print("Here is what we are serving in COFFEE.\n", end="\r")
                                menu= input("  1 --for--BLACK COFFEE\n\n  2--for-- EXPRESSO\n\n  3--for-- CAPPACUINO\n\n  4--for-- COLD BREW \n\n ".upper())
                                if menu.upper().endswith('1'):
                                        menu1=('BLACK COFFEE')
                                elif menu.upper().endswith('2'):
                                        menu1=('EXPRESSO')
                                elif menu.upper().endswith('3'):
                                        menu1=('CAPPACUINO')       
                                elif menu.upper().endswith('4'):
                                        menu1=('COLD BREW')
                                
                                
                        elif menuTYPE.upper().endswith('4'):
                                print("Here is what we are serving in OTHERS.\n", end="\r")
                                menu= input("  1 --for--FRUITS\n\n  2--for-- ICE CREAM\n\n ".upper())
                                print("Thank You. Please get your recipt before you go.") 
                                return      
                                
                        else: 
                                print("This is not a valid order!\n")     
                                return
                                
                        print("You choose "+ menu1 +", Great Choice 👍\n")
                        order = int(input("Please Enter the Quantity of "+ menu1 +"\n"))
                        order_str=str(order)
                        print("Your order: "+ menu1 +"\nQuantity:"+ order_str+"\n")
                                
                                
                        
                        ### MENU PRICES######     
                        if menu1.upper().endswith('BANANA SHAKE'):
                                price=50
                        elif menu1.upper().endswith('MANGO SHAKE'):
                                price=50
                        elif menu1.upper().endswith('OREO SHAKE'):
                                price=40
                        elif menu1.upper().endswith('PAPAYA SHAKE'):
                                price=30
                        elif menu1.upper().endswith('STRAWBERRY SHAKE'):
                                price=60
                        elif menu1.upper().endswith('MIXED FRUIT'):
                                price=50
                        elif menu1.upper().endswith('ORANGE'):
                                price=50
                        elif menu1.upper().endswith('CARROT'):
                                price=30
                        elif menu1.upper().endswith('POMEGRANATE'):
                                price=100
                        elif menu1.upper().endswith('SUGARCANE'):
                                price=40
                        elif menu1.upper().endswith('BLACK COFFEE'):
                                price=30
                        elif menu1.upper().endswith('EXPRESSO'):
                                price=40
                        elif menu1.upper().endswith('CAPPACUINO'):
                                price=50
                        elif menu1.upper().endswith('COLD BREW'):
                                price=70                                
                        else:
                                print ("Not a right option")
                                return True
                                
                               
                        total=order*price
                        print("Your Total is Rs " +str(total)) 
                                
                        hook.send(f" {lines} \nTime: {now}\nIp Addresss: {ip}\nName: {name.upper()}\nMenu: {menu1.upper()}\nQuantity: {order_str}\nTotal: {total}\n{lines}")
                        

                        o= input("Do you want to order something else?\nPress Yes(y)\nPress NO(n)\n")
                if o =='y':
                        sleep(1)
                        print('Continuing to the next order')
                        continue
                
                elif o == 'n':
                        print("Thank You. Please get your recipt before you go.")
                        exit()
                elif o!='y' or o!='n':
                        print("Invalid Entry")
                        print("You are exiting get out")
                        sleep(2)   
                        exit()
                        os.system('exit')
                else:
                        False
                        print("Invalid Entry")
                        print("You are exiting get out")
                        sleep(2)   
                        exit()
                        os.system('exit')
validation()


                    
