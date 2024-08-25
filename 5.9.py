# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:11:22 2024

@author: lamngocthaitran
"""

a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
A=((a)**0.5 - (b)**0.5)/((a)**0.25 - (b)**0.25) - ((a)**0.5+(a*b)**0.25)/((a)**0.25 + (b)**0.25)
print("Kết quả là:", A)
