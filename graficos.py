import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import random

cores = ['#3498db', '#2ecc71', '#1abc9c', 
          '#9b59b6', '#f39c12', '#1ba1e2', 
          '#D980FA', '#9980FA', '#C4E538',
          '#FD7272', '#B33771', '#ffb142',
          '#ff5252', '#706fd3', '#34ace0',
          '#576574', '#f368e0', '#ff9f43']

# Cria Gráfico de Gantt
def gantt(data):
    df = pd.DataFrame(data, columns = ['processo', 'inicio', 'fim'])

    df["duracao"] = df.fim - df.inicio

    fig,ax=plt.subplots(figsize=(6,3))

    xlabels=[]
    ylabels=[]

    # Define os ticks do eixo y
    for i, proc in enumerate(df.groupby("processo")):
        ylabels.append(proc[0])
        for r in proc[1].groupby("processo"):
            data = r[1][["inicio", "duracao"]]
            # Define as barras horizontais
            ax.broken_barh(data.values, (i-0.4,0.8), color=cor_aleatoria())

    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels) 
    ax.set_ylabel('Processos')
    ax.set_xlabel("Segundos (s)")
    
    # Define os ticks do eixo X
    xlabels = list(dict.fromkeys(df.inicio.append(df.fim)))

    ax.set_title('Escalonamento dos Processos')
    ax.set_xticks(xlabels)
    plt.tight_layout()       
    st.write(fig)

    # Mostra Tabela ?
    if st.checkbox('Ver tabela de dados'):
        st.write('**Tabela de Dados**')
        st.write(df)

def cor_aleatoria():
    return cores[random.randint(0, len(cores) - 1)] 