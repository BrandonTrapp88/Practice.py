#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 01:27:20 2021

@author: brandontrapp
"""

#text2numbers
# A program to covert a textual message into a sequence 
# of number, utilizing the underlying Unicode Encoding 

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message")
    
    #Get the message to encode
    
    message = input("Please enter the message to encode: ")
    
    print("\nHere are the Unicode codes:")
    
    #Looping through the message and print out the Unicode values
    
    for ch in message:
        print(ord(ch), end = " ")
        
        
    print() # blank line before prompts
    
main()