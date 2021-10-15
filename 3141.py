from datetime import date
from datetime import datetime

def calc_idade(nome, nasc, hoje):
    nasc = datetime.strptime(nasc, "%d/%m/%Y")
    hoje = datetime.strptime(hoje, "%d/%m/%Y")
    idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
    if(nasc.day == hoje.day and nasc.month == hoje.month): print("Feliz aniversario!")
    print("Voce tem",idade,"anos",nome+".")

nome = input()
hoje = input()
nasc = input()

calc_idade(nome, nasc, hoje)