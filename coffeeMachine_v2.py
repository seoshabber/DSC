
cup={}
menu={'Americano':1800, 'Cafe latte':2200, 'Cafe Mocha': 2800}
money=0
sum=0

def print_menu():
    print(' '+'='*5+'Sookmyung Cafe'+'='*5)
    print("""1. Select coffee menu
2. Check your order
3. Pay total price
4. Get change""")

def print_coffeeMenu():
    print('[Cafe Menu]')
    for coffee,won in menu.items():
        print(' '+coffee+' '+str(won)+'won')

def select_menu():
    while True:
        coffee=input('Select Menu : ')
        if coffee not in menu.keys():
            print('You selected wrong menu..')
            continue
        many=int(input('How many cups ? '))
        if coffee in cup.keys():
            cup[coffee] += many
        else:
            cup[coffee] = many
        break

def check_order():
    for coffee, many in cup.items():
        print(coffee, '\t', many,'cups')

def calculate_price():
    global sum
    global money
    sum=0
    for coffee in cup.keys():
        sum += cup[coffee]*menu[coffee]
    print('TotalPrice :',sum)
    while True:
            
            money=int(input('Pay money : '))
            if sum > money:
                print('Too small..\n')
            else:
                break
        
   

def get_change():
    
    change= money - sum
    print('Your change is',change,'won')
    print('='*30)
    change_5000=change//5000
    change=change%5000
    change_1000=change//1000
    change=change%1000
    change_500=change//500
    change=change%500
    change_100=change//100
    
    print('5000 won :',change_5000)
    print('1000 won :',change_1000)
    print('500 won :',change_500)
    print('100 won :',change_100)
    

while True:
    print_menu()
    print()
    choose=int(input('Choose : '))

    if choose == 1:
        print()
        print_coffeeMenu()
        print('\n')
        select_menu()



    elif choose == 2:
        check_order()



    elif choose == 3:
        calculate_price()
    

    elif choose == 4:
        get_change()
       
        print('\nThank you for using our machine')
        break

        
