#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:26:22 2021

@author: brandontrapp
"""

#coffee.py
#This program will give the user the price for the amount of coffee per pound
#also calculates the shipping
def main():
    print("Welcome to the coffee shop")
    print()

    coffee = int(input("How many pounds of coffee do you want? "))
    totalPrice = coffee * 10.50 + 0.86 * coffee + 1.50
    print("The total price for your coffee is $",totalPrice)

main()