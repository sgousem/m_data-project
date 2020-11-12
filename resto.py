food = ["\n\t\tSTARTERS" , "\n\t\tMAIN MENU " , "\n\t\tDESSERTS"]
sm = ["\n1. Tandoori Chicken \t\t\t 280/-", "\n2. Chicken lollipop \t\t\t 200/-", "\n3. Chicken Spring Rolls \t\t 180/-"]
mm = ["\n1. Roti \t\t\t\t 20/-", "\n2. Biryani Handi \t\t\t 300/-", "\n3. Chicken Mandi \t\t\t 280/-", "\n4 . Chicken Fried Rice \t\t\t 180/-"]
dm = ["\n1. Kunafa \t\t\t\t 200/-", "\n2.Ice Cream \t\t\t\t 120/- per scoop", "\n3. Khurbani Ka Meetha \t\t\t 150/-"]
sel=[]
quant =[]

# cost = 0

def main():
    print("Welcome To Royal Pakwaan, A place where you'll find the taste like never before! ")
    menuu()
    order()
    
def menuu():
    print(food[0])
    
    for items in sm:
        print(items)

    print(food[1])
    
    for items in mm:
        print(items)

    print(food[2])
    
    for items in dm:
        print(items)

def order():
    cost=0
    print("What would you like to have in starters?")
    dish = int(input("Select your dish Sir \n >>>"))
    if(dish== 1):
        quantity= int(input("Enter the quantity of Tandoori Chicken\n >>> "))
        cost = (quantity * 200)+cost
        sel.append(sm[dish-1])
        quant.append(quantity)
    elif(dish==2):
        quantity= int(input("Enter the quantity of Chicken lollipop\n >>> "))
        cost = (quantity * 200) + cost
        sel.append(sm[dish-1])
        quant.append(quantity)
    elif(dish==3):
        quantity= int(input("Enter the quantity of Chicken spring roll\n >>> "))
        cost = (quantity * 180) + cost
        sel.append(sm[dish-1])
        quant.append(quantity)

    else:
        print("Try another item")

    print("What would you like to have in Main Menu?")
    dish = int(input("Select your dish Sir \n >>>"))
    if(dish== 1):
        quantity= int(input("Enter the quantity of Roti \n >>> "))
        cost = (quantity * 20)+cost
        sel.append(mm[dish-1])
        quant.append(quantity)

    elif(dish==2):
        quantity= int(input("Enter the quantity of Biryani Handi\n >>> "))
        cost = (quantity * 300) + cost
        sel.append(mm[dish-1])
        quant.append(quantity)

    elif(dish==3):
        quantity= int(input("Enter the quantity of Chicken Mandi\n >>> "))
        cost = (quantity * 280) + cost
        sel.append(mm[dish-1])
        quant.append(quantity)

    elif(dish==4):
        quantity= int(input("Enter the quantity of Chicken Fried Rice\n >>> "))
        cost = (quantity * 180) + cost 
        sel.append(mm[dish-1])
        quant.append(quantity)
     
    else:
        print("Try another item")
    
    print("What would you like to have in desserts?")
    dish = int(input("Select your dish Sir \n >>>"))
    if(dish== 1):
        quantity= int(input("Enter the quantity of Kunafa \n >>> "))
        cost = (quantity * 200)+cost
        sel.append(dm[dish-1])
        quant.append(quantity)

    elif(dish==2):
        quantity= int(input("Enter the quantity of n2.Ice Cream\n >>> "))
        cost = (quantity * 120) + cost
        sel.append(dm[dish-1])
        quant.append(quantity)

    elif(dish==3):
        quantity= int(input("Enter the quantity of Khurbani Ka Meetha \n >>> "))
        cost = (quantity * 150) + cost
        sel.append(dm[dish-1])
        quant.append(quantity)

        
    else:
        print("Try another item")
        print("Total bill is: ",cost) 


            
    print("""**************BILL******************""")
    print("%s \t\tX %d" %(sel[0],quant[0]))
    print("%s \t\tX %d" %(sel[1],quant[1]))
    print("%s \t\tX %d" %(sel[2],quant[2]))
    print("\n\nTotal bill is: \t\t\t\t",cost)                   
    print("*******THANK YOU VISIT AGAIN********")

main()

