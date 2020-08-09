#!/usr/bin/env python3

def stroke(x):
    x = x + " "
    return x[140:150]+x[130:140]+x[120:130]+x[110:120]+x[100:110]+x[90:100]+x[80:90]+x[70:80]+x[60:70]+x[50:60]+x[40:50]+x[30:40]+x[20:30]+x[10:20]+x[0:10]

phrase = ""

while(phrase != "exit"):
    phrase = input("strokeify: ")
    print(">> "+stroke(phrase))
