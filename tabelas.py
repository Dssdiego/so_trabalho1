# Autor: Diego Santos Seabra

import streamlit as st
import pandas as pd

def tabela_medias(tempo_duracao_total, tempo_espera_total, qtde_processos):
    st.write('**Médias (em segundos)**')
    data = []
    data.append([round(tempo_duracao_total/qtde_processos, 2), round(tempo_espera_total/qtde_processos, 2)])
    df = pd.DataFrame(data, columns=['Duração', 'Espera'])
    st.write(df)

def tabela_geral(processos):
    data = []

    for proc in processos:
        data.append([proc.pid, proc.ingresso, proc.duracao, proc.tempo_resposta, proc.tempo_espera, proc.tempo_retorno])
    
    df = pd.DataFrame(data, columns=['PID', 'Ingresso', 'Duração', 'Tempo de Resposta', 'Tempo de Espera', 'Tempo de Retorno'])
    st.write(df)