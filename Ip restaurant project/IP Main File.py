import pandas as pd
import os

#file1=pd.read_csv("Restaurant_Data.csv")
while True:
    print("This is a detailed analysis of *Insert Name* restaurant")
    print("Main Menu")
    print("1. Our Carte De Jour")
    print("2. *Insert Name* in Data")
    print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
    o1=int(input("Enter your choice:"))
    if o1==1:
        while True:
            print("Do you want to-")
            print("1. Display full menu\n2. Sort menu by price\n3. Return to main menu")
            print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
            o2=int(input("Enter your choice:"))
            if o2==1:
                print("1. Drinks menu")
                print("2. Display full menu")
                print("3. Display only Italian dishes")
                print("4. Display only Indian dishes")
                print("5. Display only Continental dishes")
                print("6. Display only Chinese dishes")
                print("7. Display only Miscellaneous dishes")
                print("8. Return to Main Menu")
                print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
                o3=int(input("Enter your choice:"))
                while o3<=8:
                    if o3==1:
                        print(file1[file1["Is Drink"]=='True'])
                    elif o3==2:
                        print(file1)
                    elif o3==3:
                        print(file1(file1["Dish Type"]=="Italian"))
                    elif o3==4:
                        print(file1(file1["Dish Type"]=="Indian"))
                    elif o3==5:
                        print(file1(file1["Dish Type"]=="Continental"))
                    elif o3==6:
                        print(file1(file1["Dish Type"]=="Chinese"))
                    elif o3==7:
                        print(file1(file1["Dish Type"]=="Other"))
                    elif o3==8:
                        os.system("IP Main File.py")
                    else:
                        print("Enter Valid Input")
                        exit()
            elif o2==2:
                print("1. I wanna view by price intervals\n2. I wanna enter my own price interval")
                print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
                o4=int(input("Enter your choice:"))
                while o4<=2:
                    if o4==1:
                        print("1. Sort by price interval 0-50 Rupees")
                        print("2. Sort by price interval 50-100 Rupees")
                        print("3. Sort by price interval 100-150 Rupees")
                        print("4. Sort by price interval 150-200 Rupees")
                        print("5. Sort by price interval 200-250 Rupees")
                        print("6. Sort by price interval 250-300 Rupees")
                        print("7. Sort by price interval 300-350 Rupees")
                        print("8. Sort by price interval 350 Rupees and above")
                        print("9. Return to main menu")
                        print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
                        o5=int(input("Enter your choice:"))
                        while o5<=9:
                            if o5==1:
                                print(file1(file1["Price"]>0 and file1["Price"]<=50))
                            elif o5==2:
                                print(file1(file1["Price"]>50 and file1["Price"]<=100))
                            elif o5==3:
                                print(file1(file1["Price"]>100 and file1["Price"]<=150))
                            elif o5==4:
                                print(file1(file1["Price"]>150 and file1["Price"]<=200))
                            elif o5==5:
                                print(file1(file1["Price"]>200 and file1["Price"]<=250))
                            elif o5==6:
                                print(file1(file1["Price"]>250 and file1["Price"]<=300))
                            elif o5==7:
                                print(file1(file1["Price"]>300 and file1["Price"]<=350))
                            elif o5==8:
                                print(file1(file1["Price"]>350))
                            elif o5==9:
                                os.system("IP Main File.py")
                            else:
                                print("Enter Valid Input")
                        exit()
                    elif o4==2:
                        a=int(input("Enter the lower value:"))
                        b=int(input("Enter the upper value:"))
                        file2=file1.sort_values("Price")
                        series1=pd.Series(file2.Price)
                        alpha=series1.index(a)
                        beta=series1.index(b)
                        print(file2.loc[alpha,beta:])
            elif o2==3:
                continue
            else:
                print("Enter Valid Input")
                exit()
 #   elif o1==2:
