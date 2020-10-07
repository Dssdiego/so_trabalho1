# import sys
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

# # Merge Sort
# def ordena_ingresso(array, esquerda, direita):
#     sys.setrecursionlimit(1500)

#     if esquerda < direita:
#         meio = (esquerda + direita) / 2

#         # Divide em 2
#         ordena_ingresso(array, esquerda, meio)
#         ordena_ingresso(array, meio + 1, direita)

#         mescla(array, esquerda, meio, direita)

# # Merge
# def mescla(array, esquerda, meio, direita):
#     fIdx = esquerda # Indice Matriz Esquerda
#     rIdx = meio + 1
#     sIdx = esquerda

#     ordenado = []

#     while fIdx <= meio and rIdx <= direita:
#         if array[fIdx].tempo_chegada <= array[rIdx].tempo_chegada:
#             ordenado[sIdx] = array[fIdx++]
#         else:
#             ordenado[sIdx] = array[rIdx++]

#         sIdx++
    
#     if fIdx > meio:
#         pass
#     else:
#         pass

#     for i in range(len(esquerda)):


#     pass