HOTEL = "Marina Bay Hotel"
config = {"member": False, "Living": False, "where_eating": None}

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FOOD = pd.read_csv("FOOD.csv")
PEOPLE = pd.read_csv("PEOPLE.csv")

def int_inp(inp_str = "\nSelect option: "):
    while True:
        try:
            inp = int(input(inp_str))
            break
        except ValueError:
            print("Invalid option, try again.")
    return inp

def get_option(options):
    print("\nOptions:")
    for i, option in enumerate(options):
        print(f"{i+1} - {option}")
    while True:
        inp = int_inp()
        if inp > 0 and inp <= len(options):
            break
        print("Invalid option, try again.")
    return options[inp-1]

def member():
    res = input(f"\nIf you are living in this hotel press y, if not press n? (y/n): ")
    if res.lower() in ("y", "yes"):
        config["living"] = True
        

    res = input(f"\nAre you a member? (y/n): ")
    if res.lower() in ("y", "yes"):
        config["member"] = True

    return "where_eat"

def where_eat():
    print("\nWhere would you like to eat?")
    op = get_option(["Palm Springs", "Moka Pot", "Shimmer", "Room Service", "Conference Hall"] if config.get("living") else ["Palm Springs", "Moka Pot", "Shimmer"])
    #user is prompted all dining options

    if op == "Palm Springs":
        #user chose Palm Springs
        print("\nPlease proceed to the green door on the left")
        config["where_eating"] = "PS"
        return "PS1"

    elif op == "Moka Pot":
        #user chose Moka Pot
        print("\nTurn right and then take the first staircase to find Moka Pot")
        config["where_eating"] = "MP"
        return "MP1"

    elif op == "Shimmer":
        #user chose Shimmer
        print("Please take the elevator on the left and proceed to the rooftop")
        config["where_eating"] = "SH"
        return "SH1"

    elif op == "Room Service":
        config["where_eating"] = "RS"
        return "RS1"

    elif op == "Conference Hall":
        #user chose Conference Hall
        return "CH1"

def PS1():
    print("\nwelcome to Palm Springs!")
    inp = int_inp("How many people would you like a table for?: ")
    return "food_menu"

def MP1():
    print("\nWelcome to Moka Pot")
    inp = int_inp("How many people would you like a table for?: ")
    return "food_menu"

def SH1():
    print("\nWelcome to Shimmer")
    inp = int_inp("How many people would you like a table for?: ")
    return "food_menu"

def RS1():
    print("\nRoom Service")

    return "food_menu"

def CH1():
    res = int_inp("\nEnter your room number: ")
    room = PEOPLE.loc[PEOPLE["Room Number"] == res]
    if room.empty:
        print("Invalid room number")
    else:
        if room["Conference Booking"] == "T":
            print("\nBooking found under:")
            print("Name:", room["Name"])
            print("Name of Hall:", room["Name of Hall"])
            print("\nProceeding to Conference hall. Have a good day!")
        else:
            print("No booking found for that room.")


def food_menu():
    print("What type of cuisines would you like to try?")
    res = get_option(["indian", "italian", "continental", "japanese"])

    checks = {"PS": "Availability in Palm Springs", "MP": "Availability in Moka Pot", "SH": "Availability in Shimmer", "RS": "Availability in Room Service"}

    print(f"\nDisplaying {res} category menu:")
    _food = FOOD[FOOD[checks.get(config.get("where_eating"))] == "T"]
    menu = _food.loc[FOOD["Type of Cuisine"] == res].loc[:,["Name of Dish", "Category", "Price"]].loc[FOOD["Category"].isin(["soup", "starter", "snack", "meal"])]
    menu = pd.concat([menu, _food.loc[:,["Name of Dish", "Category", "Price"]].loc[FOOD["Category"].isin(["drinks", "dessert"])]])
    print(menu)

    orders = []
    while True:
        print("\nWhat would you like to order?")
        print("<dish id> - ID of Dish\nstop - Stop ordering")
        res = input("--> ")
        if res.lower() == "stop":
            if orders:
                break
            else:
                print("\nAb aa gaye ho toh kuch kha ke jao.")
                continue
        try:
            res = int(res)
            if res in menu.index:
                orders.append(res)
                continue
        except ValueError:
            pass
        print("Enter valid id and try again.")

    print("\nYour order:")
    for order in orders:
        print(menu.loc[order, "Name of Dish"].ljust(30, "_"), menu.loc[order, "Price"])
    total = menu.loc[orders, "Price"].sum()
    print("Total:", total)

    if config.get("member"):
        total = (total * 0.9).round(2)
        print("Member discount: 10%")
        print("Total price:", total)
    
    print("\nYour order will arrive shortly. Bon Apetit!")

menus = {
    "member": member,
    "where_eat": where_eat,
    "PS1": PS1, "MP1": MP1, "SH1": SH1, "RS1": RS1, "CH1": CH1,
    "food_menu": food_menu
}

current = "member"

def beta():
    n=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
    m=[1015,1894,2049,2234,2683,2991,3245,4677,104,1042,4998]
    plt.xlabel('Year')
    plt.ylabel("No. of Customers")
    plt.title("No. of customers per year from opening till 2022")
    plt.plot(n,m,marker='d',markersize=10,markeredgecolor='red')
    plt.show()

def gamma():
    a=["January","February","March",'April','May','June','July','August','September','October','November','December']
    b=[204,343,452,499,773,844,643,494,321,500,792,623]
    plt.xlabel('Month')
    plt.ylabel("Rough Average number of customers")
    plt.title("Rough average number of customers by month")
    plt.plot(a,b,marker='d',markersize=10,markeredgecolor='red')
    plt.show()
    
def delta():
    c=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
    d=[100,150,225,250,350,350,475,470,80,310,450]
    plt.xlabel("Year")
    plt.ylabel("No. of Employees")
    plt.title("No. of employees per year")
    plt.plot(c,d,marker='d',markersize=10,markeredgecolor='red')
    plt.show()
    
def epsilon():
    seasons=["Winter","Spring","Summer",'Autumn']
    guests=[467,376,883,642]
    plt.xlabel('Season')
    plt.ylabel("No. of customers")
    plt.title("No. of customers per season")
    plt.bar(seasons,guests)
    plt.show()

def zeta():
    dishes=['Indian','Italian','Continental','Japanese']
    pop=[23.4,46.3,22.9,7.4]
    plt.xlabel("Dishes")
    plt.ylabel("Popularity percentage")
    plt.title("Popularity of types of dishes served")
    plt.ylim(0,100)
    plt.bar(dishes,pop)
    plt.show()
    
def eta():
    rest=['Palm Springs', 'Moka Pot', 'Shimmer', 'Room Service']
    popu=[32.1,56.2,10,2.7]
    plt.xlabel("Restaurant")
    plt.ylabel("Popularity percentage")
    plt.title("Popularity of Restaurants")
    plt.ylim(0,100)
    plt.bar(rest,popu)
    plt.show()

def theta():
    l=np.array([12,34,23,44,56,23,55,47,97,36,75])
    plt.hist(l,bins=[0,10,20,30,40,50,60,70,80,90,100])
    plt.title("Earning over the years")
    plt.show()
    
print(f"Welcome to {HOTEL}!")
alpha=str(input("If you want to view our HOTEL SERVICES, type in 'h', else if you want to view our VISUALIZED DATA then enter 'd':"))
if alpha=='h':
    while current:
        current = menus.get(current)()
elif alpha=='d':
    print("Enter the Number of the following data you want to view")
    print("1.No. of customers per year from opening till 2022")
    print('2.Rough average number of customers by month')
    print("3.No. of employees per year")
    print("4.No. of customers per season")
    print("5.Popularity of types of dishes served")
    print("6.Popularity of Restaurants")
    print("7.Earning over the years")
    bil=int(input("Enter a number:"))
    if bil==1:
        beta()
    elif bil==2:
        gamma()
    elif bil==3:
        delta()
    elif bil==4:
        epsilon()
    elif bil==5:
        zeta()
    elif bil==6:
        eta()
    elif bil==7:
        print("This is classified information, only personell with security clearance can access")
        trip=str(input("Enter password"))
        if trip=='sigma':
            theta()
else:
    print("Enter valid inputs henceforth")
