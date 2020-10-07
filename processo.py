class Processo:
    # TODO: Implementar prioridade?
    def __init__(self, pid, ingresso, duracao):
        self.pid = pid
        self.ingresso = ingresso
        self.duracao = duracao
        # self.tempo_espera = tempo_espera
    # self.tempo_retorno = tempo_retorno
    # self.tempo_turnaround = tempo_turnaround
    # self.tempo_resposta = tempo_resposta
    # self.finalizado = finalizado