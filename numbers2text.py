#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:07:45 2021

@author: brandontrapp
"""
def main():
    print("This program converts a sequence of Unicode numbers into a string of text. ")
    print("the string of text that it represents. \n")
    
    #Get the message to encode 
    
    inString = input("Please enter the Unicode-encoded message: ")
    
    #Loop through each substring and build Unicdoe message
    
    message = " "
    for numStr in inString.split():
        codeNum = int(numStr)
        message = message + chr(codeNum)
    print("\nThe decoded message is: ",  message)

main()
