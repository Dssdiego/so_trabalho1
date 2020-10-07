import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

from graficos import gantt
from ordenacao import ordena_ingresso

def round_robin(processos, quantum):
    tempo_espera_total = 0
    tempo_turnaround_total = 0
    calc_tempo_resposta_total = 0

    # st.write('Sem ordenação')
    # for i in range(len(processos)):
    #     st.write(processos[i].pid)

    ordena_ingresso(processos)
    # st.write('Ordenado')
    # for i in range(len(processos)):
    #     st.write(processos[i].pid)

    round_robin_tempo_espera(processos, quantum)
    round_robin_turn_around(processos)

    for proc in processos:
        proc.tempo_espera = proc.turnaround - proc.duracao
        proc.tempo_retorno = proc.ingresso + proc.duracao + proc.tempo_espera

        tempo_espera_total += proc.tempo_espera
        tempo_turnaround_total += proc.turnaround
        calc_tempo_resposta_total += proc.tempo_resposta

    round_robin_grafico(processos, quantum)

    st.write("Tempo de Espera Médio: " + str(tempo_espera_total / len(processos)))
    st.write("Tempo de Turn Around Médio: " + str(tempo_turnaround_total / len(processos)))
    st.write("Tempo de Resposta Médio: " + str(calc_tempo_resposta_total / len(processos)))

    round_robin_tabela(processos)

def round_robin_tempo_espera(processos, quantum):
    tempo_atual = 0

    duracao_restante = [] # Tempo de duracao (execução) restante para cada processo
    tempo_resposta = []    # Tempo de resposta para cada processo 

    # Salva os tempos no array
    for i in range(len(processos)):
        duracao_restante.append(processos[i].duracao)
        tempo_resposta.append(False)

    # Permanece rodando até que todos os processos sejam concluídos
    while True:
        check = True

        for i in range(len(processos)):
            if duracao_restante[i] > 0:
                check = False
                
                if tempo_resposta[i] == False:
                    processos[i].tempo_resposta = tempo_atual - processos[i].ingresso
                    tempo_resposta[i] = True

                if duracao_restante[i] > quantum:
                    tempo_atual += quantum
                    duracao_restante[i] -= quantum
                else:
                    tempo_atual += duracao_restante[i]
                    processos[i].tempo_espera = tempo_atual - processos[i].duracao
                    duracao_restante[i] = 0

        if check == True:
            break

def round_robin_turn_around(processos):
    for proc in processos:
        proc.turnaround = proc.duracao + proc.tempo_espera - proc.ingresso

def round_robin_grafico(processos, quantum):
    tempo_atual = 0
    duracao_total = 0

    duracao_restante = [] 
    gantt_data = [] 

    # Salva os tempos no array
    for i in range(len(processos)):
        duracao_restante.append(processos[i].duracao)
        duracao_total += processos[i].duracao

    # Permanece rodando até que todos os processos sejam concluídos
    while True:
        check = True

        for i in range(len(processos)):
            if duracao_restante[i] > 0:
                check = False

                gantt_data.append([processos[i].pid, tempo_atual, 0])
			
                if duracao_restante[i] > quantum:
                    tempo_atual += quantum
                    duracao_restante[i] -= quantum
                else:
                    tempo_atual += duracao_restante[i]
                    processos[i].tempo_espera = tempo_atual - processos[i].duracao
                    duracao_restante[i] = 0

        if check == True:
            break

    # Corrige início e fim dos processos
    for i in range(len(gantt_data)):
        if i == 0:
            gantt_data[i][2] = gantt_data[i+1][1]
        else:
            if i != len(gantt_data) - 1:
                gantt_data[i][2] = gantt_data[i+1][1]
            else:
                gantt_data[i][2] = duracao_total

    gantt(gantt_data)

    pass

def round_robin_tabela(processos):
    data = []

    for proc in processos:
        data.append([proc.pid, proc.ingresso, proc.duracao, proc.tempo_retorno, proc.tempo_resposta, proc.tempo_espera, proc.turnaround])
    
    df = pd.DataFrame(data, columns=['PID', 'Ingresso', 'Duração', 'Tempo de Retorno', 'Tempo de Resposta', 'Tempo de Espera', 'Tempo de Turn Around'])
    st.write(df)
    # for i in range(len(processos)):
    #     data.append([])
    #     st.write(processos[i].pid)
    #     st.write(processos[i].duracao)
    #     st.write(processos[i].tempo_espera)
    #     st.write(processos[i].turnaround)
    #     st.write(processos[i].tempo_resposta)
    #     st.write(processos[i].tempo_retorno)