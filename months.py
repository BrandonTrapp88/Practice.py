#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:42:29 2021

@author: brandontrapp
"""

# a simple program that seperates the month's in a really long string 

def main():
    # months is used as a lookup table 
    
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    #asking user to enter birthday month 
    birthMonth = int(input("please enter the month you was born (1-12): "))
    
    # compute starting postion of month birthMonth in months 
    
    pos = (birthMonth - 1) * 3
    
    # Grab the appropriate slice from months 
    
    monthAbbrev = months[pos:pos+3]
    
    #printing the result 
    
    print("The month abbrreviation is ", monthAbbrev + ".")
    
main()