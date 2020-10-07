# Autor: Diego Santos Seabra 

import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
from processo import Processo

from round_robin import round_robin, round_robin_tempo_espera

processos = []

def main():

    # Define as configurações da página
    st.beta_set_page_config(
        page_title="Trabalho 1 - Sistemas Operacionais",
    )

    st.title("Trabalho 1 - Escalonamento de Processos")
    st.write("---------------")
    st.write("**Disciplina:** Sistemas Operacionais")
    st.write("**Aluno:** Diego Santos Seabra")
    st.write("**Matrícula:** 0040251")
    st.write("---------------")
    visualizacao = st.selectbox(label='Escolha o que deseja visualizar',options=['Round Robin', 'Comparação de Resultados'])
    st.write("---------------")

    if visualizacao == 'Round Robin':
        algo_round_robin()

    if visualizacao == 'Comparação de Resultados':
        comparacao()

def inicia_processos(processos):
    for proc in processos:
        proc.tempo_espera = 0
        proc.tempo_retorno = 0
        proc.tempo_resposta = 0
        proc.finalizado = False

def algo_round_robin():
    st.write('Para mudar os processos, basta alterar [essa planilha](https://docs.google.com/spreadsheets/d/1vTeJ80BnAhXqQjpO9ml0bRAjikwSyBhkKS9iH1vPRe8/edit?usp=sharing) e atualizar a página :wink:')

    # Busca os processos de uma planilha do Google
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRqjZdPyFphn5nD9vwbv94obvpuY4vlPTRz31wLe_SaRCYSKGBZzvlIQkNd51rcow2Npua4RTLyf4PL/pub?output=csv')
    # df = pd.read_csv('processos.csv')

    st.write('**Processos**')
    st.write(df)

    quantum = st.number_input(label='Escolha o quantum (em segundos)', step=1, value=2, min_value=0, max_value=99999)

    # Lista de Processos
    processos = []

    # Cria lista de processos
    for index, proc in df.iterrows():
        processos.append(Processo(proc['id'], proc['ingresso'], proc['duracao']))

    inicia_processos(processos)

    round_robin(processos, quantum)

def comparacao():
    st.write('TODO: Comparação')

    pass

if __name__ == '__main__':
    main()