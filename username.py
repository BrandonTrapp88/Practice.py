#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:25:15 2021

@author: brandontrapp
"""

# simple string processing program to generate username 

def main():
    print("This program generates computer username. \n")
    
    #Getting the user first name 
    firstName = input("PLEASE enter your first name in all lowercase letters: ")
    
    #Getting the user last name 
    lastName = input("PlEASE enter your last name in all lowercase letters: ")
    
    # concatenate (also mean combine) first inital with 7 chars of the last name 
    
    userName = firstName[0] +  lastName[:7]
    
    #Output the username
    
    print("Your username is: ", userName)
    
main()
