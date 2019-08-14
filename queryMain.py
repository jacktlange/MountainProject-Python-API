# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:56:15 2019

@author: Jack
"""

from mpQuery import * 

def main():

    privateKey = '112446503-8924701af82f2e439e9312357672ca8d'
    user = getUser(privateKey, "jacktlange@gmail.com")
    print(user)
main()