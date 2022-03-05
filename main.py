from CzyInwestowac import *
from inwestyjce import *
from plnusd import *

a = float(input('podaj ilosc PLN:    '))
b = float(input('podaj kurs USD:    '))

print(f"USD: ", przeliczenie(a,b))

print(investments(przeliczenie(a,b)))
