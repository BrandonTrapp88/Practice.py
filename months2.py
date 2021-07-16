#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:52:36 2021

@author: brandontrapp
"""

# a program to print the month abbreviation, giving its number:
    
    

def main():
    
    #months is a list used as a lookup table 
    
    months = ["Jan", "Feb", "Mar", "Apr", "May","Jun","Jul","Aug","Sep"
              ,"Oct","Nov","Dec"]
    
    n = int(input("Enter a month number (1-12): "))
    
    print("The month abbreviation is", months[n-1] + ". ")


main()