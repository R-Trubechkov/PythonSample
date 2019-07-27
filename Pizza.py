 
pizza={'peperony': 13}
drinks={'pepsi': 2}
adds={'nuggets': 8}
menu=[pizza,drinks,adds]
def admin():
    print('Youre admin now!')
    while True:
        add=input('what you want to add? pizza/drinks/adds/nothing\n')
        if add == 'pizza': edit(pizza)
        elif add == 'drinks': edit(drinks)
        elif add == 'adds': edit(adds)
        elif add == 'nothing': break
        else:
            print('Fuck off you leatherman!!!')
            raise ProcessLookupError
        

def edit(field):
    dish = input("new dish: ")
    cost = input ("input cost: ")
    field[dish] = int(cost)
    
def user():
    count=0
    print('Hello,my friend, please, order smthng,here our menu: ')
    print(menu)
    while True:
        order=input('What is your choise? ')
        if order in pizza:count+=pizza[order]
        if order in adds:count+=adds[order]
        if order in drinks:count+=drinks[order]
        order=input('Do you want order more? yes/no ')
        if order == 'yes': continue
        elif order == 'no': break
        else:
            print('Fuck off you leatherman!!!')
            raise ProcessLookupError
    print('Your lunch cost: %d rubles' %count)
    return count

print('Welcome to my Pizzeria!!!')
while True:
    choice = input('Who you are? admin/user\n')
    if choice == 'admin':
        password=input('Enter password:\n')
        if len(password) == 4: admin()
        else:
            print('Fuck off you leatherman!!!')
            raise ProcessLookupError
    elif choice == 'user':
        name=input('Enter your name:\n')
        billfile=open(name + '.txt','w')
        billfile.write("your order:"+"\n")
        billfile.write(str(user()))
        billfile.close()
        exit=input('Do you wonna go?? yes/no')
        if exit == 'yes': break
        elif exit == 'no': continue
        else:
            print('Fuck off you leatherman!!!')
            raise ProcessLookupError

    else:
        print('Fuck off you leatherman!!!')
        raise ProcessLookupError

print('До новых встреч!')