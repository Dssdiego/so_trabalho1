# Autor: Diego Santos Seabra 

import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
from processo import Processo

# Algoritmos
from round_robin import round_robin, round_robin_tempo_espera
from menor_primeiro import menor_primeiro

opcoes = ['1. Apresentação', 
          '2. Definições e Conceitos', 
          '3. Round Robin - Vantagens e Desvantagens', 
          '4. Round Robin - Demonstração', 
          '5. Menor Primeiro - Vantagens e Desvantagens', 
          '6. Menor Primeiro - Demonstração', 
          '7. Obrigado!'
          ]
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
    visualizacao = st.selectbox(label='Escolha o que deseja visualizar',options=opcoes)
    st.write("---------------")

    if visualizacao == '1. Apresentação':
        apresentacao()

    if visualizacao == '2. Definições e Conceitos':
        definicoes_conceitos()

    if visualizacao == '3. Round Robin - Vantagens e Desvantagens':
        vd_round_robin()

    if visualizacao == '4. Round Robin - Demonstração':
        algo_round_robin()

    if visualizacao == '5. Menor Primeiro - Vantagens e Desvantagens':
        vd_menor_primeiro()

    if visualizacao == '6. Menor Primeiro - Demonstração':
        algo_menor_primeiro()

    if visualizacao == '7. Obrigado!':
        obrigado()

def apresentacao():
    st.header('Apresentação')
    st.write('Este sistema foi feito para a apresentação do Trabalho Prático 1 da disciplina de Sistemas Operacionais')
    st.write('O intuito foi apresentar os algoritmos de escalonamento com uma interface gráfica que permitisse a visualização dinâmica da alocação de processos')
    st.write('Obs.: Estamos partindo do pressuposto que os processos são todos **CPU-Bound**')
    st.write('-----------')
    st.write('**Como Usar o Sistema**')
    st.write('Na parte superior existe um *combobox* no qual é possível selecionar o que você gostaria de acessar')
    st.write('Tenta lá! Mude para uma outra seção! :wink:')
    st.write('-----------')
    st.write('**Código Fonte**')
    st.write('O código fonte deste projeto é Open Source e se encontra [aqui](https://github.com/Dssdiego/so_trabalho1/tree/master).')
    st.write('PR\'s são bem vindos :slightly_smiling_face:')
    pass

def definicoes_conceitos():
    st.header('Definições e Conceitos')
    st.write('**Duração**')
    st.write('Cada processo em um sistema de computador requer algum tempo para sua execução. Este tempo é o tempo da CPU e o tempo de E/S. O tempo da CPU é o tempo que a CPU leva para executar o processo. Já o tempo de E/S é o tempo gasto pelo processo para realizar alguma operação de E/S. Em geral, ignoramos o tempo de E/S e consideramos apenas o tempo de CPU para um processo (que é o que foi feito neste trabalho). Logo, o **Tempo de Duração é o tempo total gasto pelo processo para sua execução na CPU.**')
    st.write('**Duração é o tempo total gasto pelo processo para sua execução na CPU**')
    st.write('-----------')
    st.write('**Ingresso**')
    st.write('O ingresso é o momento em que um processo entra no estado pronto e está pronto para sua execução.')
    st.write('-----------')
    st.write('**Tempo de Resposta**')
    st.write('O tempo de resposta é o tempo gasto quando o processo está no estado pronto e "obtém" a CPU pela primeira vez.')
    st.write('**Tempo de Resposta = Tempo em que o processo obtém a CPU pela primeira vez - Ingresso**')
    st.write('-----------')
    st.write('**Tempo de Retorno (Turnaround)**')
    st.write('O tempo de retorno é a quantidade total de tempo gasto pelo processo desde o estado de pronto pela primeira vez até sua conclusão.')
    st.write('**Tempo de Retorno = Duração + Tempo de Espera**')
    st.write('-----------')
    st.write('**Tempo de Espera**')
    st.write('O tempo de espera é o tempo total gasto pelo processo no estado pronto aguardando a CPU.')
    st.write('**Tempo de Espera = Tempo de Retorno - Duração**')
    st.write('-----------')
    st.write('**Taxa de Transferência**')
    st.write('A taxa de transferência é uma forma de encontrar a eficiência de uma CPU. Pode ser definido como o número de processos executados pela CPU em um determinado período de tempo. Por exemplo, digamos que o processo P1 leva 3 segundos para ser executado, P2 leva 5 segundos e P3 leva 10 segundos. Portanto, taxa de transferência, neste caso, a taxa de transferência será (3 + 5 + 10) / 3 = 18/3 = 6 segundos.')
    st.write('**Taxa de Transferência = Número de processos executados pela CPU em um período de tempo**')

def vd_round_robin():
    st.header('Round Robin - Vantagens e Desvantagens')
    st.write('**Vantagens**')
    st.write('→ Cada processo é servido pela CPU por um quantum de tempo fixo, portanto, todos os processos recebem a mesma prioridade. É um algoritmo "justo".')
    st.write('→ Melhora drasticamente os tempos médios de resposta.')
    st.write('→ Um quantum pequeno permite que o sistema percorra os processos rapidamente, porém aumenta a troca de contextos (veja abaixo).')
    st.write('**Desvantagens**')
    st.write('→ A taxa de transferência do Round Robin depende muito da escolha da duração do quantum de tempo. Se o quantum de tempo for maior do que o necessário, ele tende a exibir o mesmo comportamento do FCFS (First Come, First Served).')
    st.write('→ Se o quantum de tempo for menor do que o necessário, o número de vezes que a CPU muda de um processo para outro aumenta (troca de contexto). Isso leva à diminuição da eficiência da CPU, pois a CPU fica ocupada com a mudança de contexto e "deixa de lado" o trabalho real de executar o processo.')
    st.write('→ Seu tempo médio de espera costuma ser longo.')

def vd_menor_primeiro():
    st.header('Menor Primeiro (SJF) - Vantagens e Desvantagens')
    st.write('**Vantagens**')
    st.write('→ Processos mais curtos são favorecidos.')
    st.write('→ Mais processos podem ser executados em menos tempo. Isso aumenta o rendimento do processador.')
    st.write('**Desvantagens**')
    st.write('→ Pode causar inanição, se processos mais curtos continuarem ocorrendo. Ou seja, processos longos podem nunca ocorrer e "morrer de fome". Porém este problema pode ser resolvido com envelhecimento (aging).')

def inicia_processos(processos):
    for proc in processos:
        proc.tempo_espera = 0
        proc.tempo_retorno = 0
        proc.tempo_resposta = 0
        proc.finalizado = False

def algo_round_robin():
    st.header('Round Robin - Demonstração')
    # st.write('Para mudar os processos, basta alterar [essa planilha](https://docs.google.com/spreadsheets/d/1vTeJ80BnAhXqQjpO9ml0bRAjikwSyBhkKS9iH1vPRe8/edit?usp=sharing) e atualizar a página :wink:')

    escolhe_proc = st.selectbox(label='Escolha o csv para ser carregado',options=['Demonstração 1', 'Demonstração 2', 'Demonstração 3'])
    if (escolhe_proc == 'Demonstração 1'):
        df = pd.read_csv('round_robin.csv')

    if (escolhe_proc == 'Demonstração 2'):
        df = pd.read_csv('round_robin2.csv')

    if (escolhe_proc == 'Demonstração 3'):
        df = pd.read_csv('round_robin3.csv')

    # Busca os processos de uma planilha do Google
    # df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRqjZdPyFphn5nD9vwbv94obvpuY4vlPTRz31wLe_SaRCYSKGBZzvlIQkNd51rcow2Npua4RTLyf4PL/pub?output=csv')
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

def algo_menor_primeiro():
    st.header('Menor Primeiro (SJF) - Demonstração')

    escolhe_proc = st.selectbox(label='Escolha o csv para ser carregado',options=['Demonstração 1', 'Demonstração 2', 'Demonstração 3'])
    if (escolhe_proc == 'Demonstração 1'):
        df = pd.read_csv('menor_primeiro.csv')

    if (escolhe_proc == 'Demonstração 2'):
        df = pd.read_csv('menor_primeiro2.csv')

    if (escolhe_proc == 'Demonstração 3'):
        df = pd.read_csv('menor_primeiro3.csv')

    # Busca os processos de uma planilha do Google
    # df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRqjZdPyFphn5nD9vwbv94obvpuY4vlPTRz31wLe_SaRCYSKGBZzvlIQkNd51rcow2Npua4RTLyf4PL/pub?output=csv')
    # df = pd.read_csv('processos.csv')

    st.write('**Processos**')
    st.write(df)

    # Lista de Processos
    processos = []

    # Cria lista de processos
    for index, proc in df.iterrows():
        processos.append(Processo(proc['id'], proc['ingresso'], proc['duracao']))
    inicia_processos(processos)

    menor_primeiro(processos)

def obrigado():
    st.title('Obrigado!')

    pass

if __name__ == '__main__':
    main()