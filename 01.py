# Zadanie 1
# Napisz funkcję tail pobierającą N elementów z końca listy. 
# Lista jest podana do funkcji jako argument. 
# Skorzystaj z zaproponowanego kodu
# def tail(N, lista):
#    pass
# Przetestuj kod dla następujących przypadków:
# Lista ma więcej elementów niż chcemy wyświetlić
# Lista ma mniej elementów niż chcemy wyświetlić
# Lista jest pusta
# Próba wyświetlania ujemnej ilości
# Próba wyświetlenia zerowej ilości elementów listy

list = [1,2,3,4,5,6,7]
list2 = []

def tail(N,lista):
    if len(lista) > 0:
      x = len(lista)
      return lista[x-N:x]
    else:
      pass

print(tail(2,list))    
print(tail(12,list))    
print(tail(2,list2))    
print(tail(-2,list))
print(tail(0,list))    

