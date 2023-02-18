class Funcionario():
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        self._horas = horas
        print('Horas registradas...')

    def mostra_tarefas(self, tarefas):
        for tarefa in tarefas:
            print(tarefa)

class Alura(Funcionario):
    pass

class Caelum(Funcionario):
    pass

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Senior(Alura, Caelum, Hipster):
    pass

