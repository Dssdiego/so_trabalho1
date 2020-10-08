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


# def ordena_retorno(arr):
#     if len(arr) >1: 
#         mid = len(arr)//2 # Meio do array
#         L = arr[:mid] # Dividindo os elementos do array
#         R = arr[mid:] # em 2 metades

#         ordena_retorno(L) # Ordena a primeira metade
#         ordena_retorno(R) # Ordena a segunda metade
  
#         i = j = k = 0
          
#         # Copia os dados temporários (esquerda e direita)
#         while i < len(L) and j < len(R): 
#             if L[i].tempo_retorno <= R[j].tempo_retorno: # Compara os tempos de retorno
#                 arr[k] = L[i] 
#                 i+= 1
#             else: 
#                 arr[k] = R[j] 
#                 j+= 1
#             k+= 1
          
#         # Verifica se sobrou algum elemento sem ordenar
#         while i < len(L): 
#             arr[k] = L[i] 
#             i+= 1
#             k+= 1
          
#         while j < len(R): 
#             arr[k] = R[j] 
#             j+= 1
#             k+= 1

# def compara_tempo_retorno(p1, p2):
#     if p1.tempo_retorno < p2.tempo_retorno:
#         return -1
#     elif p1.tempo_retorno > p2.tempo_retorno:
#         return 1
#     else:
#         return 0

# def ordena_retorno(arr):
#     quick_sort(arr, len(arr), len(arr), compara_tempo_retorno())

# def quick_sort(arr, minimo, maximo):
#     if len(arr) == 1:
#         return arr
#     if minimo < maximo:
#         pi = particao(arr, minimo, maximo)
 
#         quick_sort(arr, minimo, pi-1)
#         quick_sort(arr, pi+1, maximo)

# def particao(arr, minimo, maximo):
#     i = (minimo-1)         
#     pivot = arr[maximo]     
 
#     for j in range(minimo, maximo):
 
#         if arr[j] <= pivot:
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
 
#     arr[i+1], arr[maximo] = arr[maximo], arr[i+1]
#     return (i+1)