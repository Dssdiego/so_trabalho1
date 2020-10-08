# Autor: Diego Santos Seabra
# Algoritmo: Menor Processo Primeiro (SJF)

import pandas as pd
import streamlit as st

from graficos import gantt
from ordenacao import ordena_ingresso, ordena_retorno
from tabelas import tabela_geral, tabela_medias

def menor_primeiro(processos):
    tempo_espera_total = 0
    tempo_duracao_total = 0
    # tempo_turnaround_total = 0
    # tempo_resposta_total = 0

    # st.write('Antes de ordenar')
    # for i in range(len(processos)):
    #     st.write(processos[i].pid)

    # ordena_retorno(processos)
    # st.write('Depois de ordenar')
    # st.write(processos.sort())
    # for i in range(len(processos)):
    #     st.write(processos[i].pid)

    menor_primeiro_calcula_tempo(processos)
    menor_primeiro_turn_around(processos)

    for proc in processos:
        proc.tempo_retorno = proc.turnaround + proc.ingresso
        proc.tempo_resposta = proc.tempo_espera

        tempo_espera_total += proc.tempo_espera
        tempo_duracao_total += proc.duracao
        # tempo_resposta_total += proc.tempo_resposta

    processos = ordena_retorno(processos)

    menor_primeiro_grafico(processos)
    tabela_geral(processos)
    tabela_medias(tempo_duracao_total, tempo_espera_total, len(processos))

def menor_primeiro_calcula_tempo(processos):
    tempo_atual = 0
    menor = 0

    processos[0].finalizado = True
    processos[0].tempo_retorno = processos[0].duracao
    processos[0].turnaround = processos[0].duracao - processos[0].ingresso
    processos[0].tempo_espera = 0

    tempo_atual = processos[0].duracao

    for i in range(1, len(processos)):
        for j in range(1, len(processos)):
            if processos[j].finalizado == True:
                continue
            else:
                menor = j
                break

        for j in range(1, len(processos)):
            if processos[j].finalizado == False and processos[j].ingresso <= tempo_atual and processos[j].duracao < processos[menor].duracao:
                menor = j
        
        processos[menor].tempo_espera = tempo_atual - processos[menor].ingresso
        processos[menor].finalizado = True

        tempo_atual += processos[menor].duracao

        processos[menor].tempo_retorno = tempo_atual
        processos[menor].turnaround = processos[menor].tempo_retorno - processos[menor].ingresso

def menor_primeiro_turn_around(processos):
    for proc in processos:
        proc.turnaround = proc.duracao + proc.tempo_espera - proc.ingresso

def menor_primeiro_grafico(processos):
    gantt_data = []
    tempo_atual = 0
    menor = 0

    processos[0].finalizado = True
    processos[0].tempo_retorno = processos[0].duracao
    processos[0].turnaround = processos[0].duracao - processos[0].ingresso
    processos[0].tempo_espera = 0

    tempo_atual = processos[0].duracao
    gantt_data.append([processos[0].pid, processos[0].tempo_espera, processos[0].turnaround])

    for i in range(1, len(processos)):
        for j in range(1, len(processos)):
            if processos[j].finalizado == True:
                continue
            else:
                menor = j
                break

        for j in range(1, len(processos)):
            if processos[j].finalizado == False and processos[j].ingresso <= tempo_atual and processos[j].duracao < processos[menor].duracao:
                menor = j
        
        processos[menor].tempo_espera = tempo_atual - processos[menor].ingresso
        processos[menor].finalizado = True

        gantt_data.append([processos[i].pid, processos[i].tempo_espera, processos[i].turnaround])
        tempo_atual += processos[menor].duracao

    trocas_contexto_total = 0
    for i in range(len(gantt_data)):
        if i != 1:
            if gantt_data[i][0] != gantt_data[i-1][0]:
                trocas_contexto_total += 1

    gantt(gantt_data)

    processos[0].tempo_espera = 0

    st.write('**Trocas de Contexto:** ' + str(trocas_contexto_total))

    pass