import os

def obvod_ctverce(a):
    return 4*a
def obvod_obdélníku(a,b):
    return 2*(a+b)
def obsah_ctverce(a):
    return a*a
def obsah_obdelniku(a,b):
    return a*b


strana_ctverec = input("Zadejte délku strany čtverce")

strana_obdelnik_a = input("Zadejte délku první strany obdélníku: ")

strana_obdelnik_b = input("Zadejte délku druhé strany obdélníku: ")

print("Obvod čtverce je: "+obvod_ctverce(strana_ctverec))

print("Obsah čtverce je: "+obsah_ctverce(strana_ctverec))

print("Obvod obdélniku je: "+obvod_obdélníku(strana_obdelnik_a,strana_obdelnik_b))

print("Obsah obdélniku je: "+obsah_obdelniku(strana_obdelnik_a,strana_obdelnik_b))