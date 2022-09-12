# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:54:02 2022

@author: Dhawal
"""

import pandas as pd
import numpy as np
import os
import sys
print("This is a detailed analysis of *Insert Name* restaurant")
print("Main Menu")
print("1. Our Carte De Jour")
print("2. *Insert Name* in Data")
print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
o1=int(input("Enter your choice:"))
if o1==1:
    print("Do you want to-")
    print("1. Display full menu\n2. Sort menu by price\n3. Return to main menu")
    print("Enter serial number of your choice as shown in the following example-\nEnter your choice:2")
    o2=int(input("Enter your choice:"))
    if o2==3:
        os.execv(sys.argv[0], sys.argv)
    elif o2==1:
        print("1. Drinks menu")
        print("2. Display alphabetically sorted menu")
        print("3. Display only Italian dishes [Randomly sorted]")
        print("4. Display only Indian dishes [Randomly sorted]")
        print("5. Display only Continental dishes [Randomly sorted]")
        print("6. Display only Chinese dishes dishes [Randomly sorted]")
        print("7. Display only Miscellaneous dishes")