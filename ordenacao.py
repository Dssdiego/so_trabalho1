# Autor: Diego Santos Seabra

import streamlit as st

def ordena_ingresso(arr):
    if len(arr) >1: 
        mid = len(arr)//2 # Meio do array
        L = arr[:mid] # Dividindo os elementos do array
        R = arr[mid:] # em 2 metades

        ordena_ingresso(L) # Ordena a primeira metade
        ordena_ingresso(R) # Ordena a segunda metade
  
        i = j = k = 0
          
        # Copia os dados temporários (esquerda e direita)
        while i < len(L) and j < len(R): 
            if L[i].ingresso <= R[j].ingresso: # Compara os tempos de chegada
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Verifica se sobrou algum elemento sem ordenar
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def ordena_retorno(arr):
    return quicksort(arr)

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0].duracao
        i = 0
        for j in range(len(x)-1):
            if x[j+1].duracao < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part