#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:29:56 2021

@author: brandontrapp
"""

def main():
    print("This program computes the average of three exam scores. ")
    
    score1,score2,score3 = eval(input("Enter three scores seperated by a comma:"))
    average = ((score1 + score2 + score3) / 3)
    print("Your grade for the semsester is ", average)

main()
    