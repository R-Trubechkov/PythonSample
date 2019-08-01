
menu={'pizza':{'peperony': 13},'drinks':{'pepsi': 2},'adds':{'nuggets': 8}}
def exeptions():
    print('Fuck off you leatherman!!!')
    raise ProcessLookupError

def isAdmin(login,password):
    if login and password == 'admin':
        return True
    else: return False
def writeMenu():
    with open("menu.txt",'w' ) as menufile:
       menufile.write(str(menu))
       menufile.close()
      
def admin():
    print('Youre admin now!')
    print('Here our menu:\n')
    print(menu) 
    while True:
        add=input('what you want to add? menu/nothing\n')
        if add == 'menu': 
            edit()
            print('new menu:\n')
            print(menu) 
        elif add == 'nothing':
            writeMenu()
            break
        else:
            exeptions()
def creatingPaycheck(name,count,bill):
    with open(name + '.txt','w') as billfile:
        billfile.write("your order:"+"\n")
        billfile.write(bill)
        billfile.write(count)
        billfile.close()            
            
            
def edit():
    field = input("What type of food you want to add? ")
    dish = input("new dish: ")
    cost = input ("input cost: ")
    menu.setdefault(field)[dish]=int(cost)
    
def user():
    count=0
    bill=[]
    name=input('Enter your name:\n')
    print('Hello user, please, order smthng,here our menu: ')
    print(menu) 
    while True:
        order=input('What is your choise? ')
        for i in menu.keys():
            if order in menu[i]:
                count =count + menu[i][order]
        bill.append(order)
        order=input('Do you want order more? yes/no ')
        if order == 'yes': continue
        elif order == 'no': break
        else:
           exeptions()
    print('Your lunch cost: %d rubles' %count)
    return count and bill


if __name__ == "__main__":
    print('Welcome to my Pizzeria!!!')
    while True:
        choice = input('Who you are? admin/user\n')
        if choice == 'admin':
            login = input('login: ')
            password = input('password: ')
            if isAdmin(login,password): admin()
            else: user()
        else: user()
        exit=input('Do you wonna go?? yes/no ')
        if exit == 'yes': break
        elif exit == 'no': continue
        else:
            exeptions()
print('Good bye!')