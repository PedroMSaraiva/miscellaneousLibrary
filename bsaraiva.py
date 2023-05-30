#bsaraiva - Biblioteca com funções uteis desenvolvidas ao longo das aulas

import numpy as np

def prime_finder(num): #Verify is the number given is a prime number
  if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               return False
       else:
           return True

def prime_list(num): #Return a list with prime numbers
  lista = []
  for i in range(num+1):
    if prime_finder(i):
      lista.append(i)
    else:
      pass
  return lista

def make_matrix(x,y): #Creates a bidimensional matrix that receveis the values from the user
  matriz = np.ones((x,y))
  for i in range(x):
    for j in range(y):
      matriz[i][j] = input(f"Type the value of the element in position({i+1},{j+1}): ")
  return matriz
            
def is_pangram(s): #Verify if the string is a pangram
    i = 0
    pangram = list(s)
    for letra in pangram:
        if pangram.count(letra) == 1:
            i += 1
    if len(pangram) == i:
        return False
    else:
        return True

def loading_bar():
	n = 0
    	while n <= 20: #creates a loading bar
          print("_"*22)
          print("|"+'▇'*n+' '*(20-n)+'|')
          print("‾"*22)
          time.sleep(2)
          n += 1
          clear_output()
