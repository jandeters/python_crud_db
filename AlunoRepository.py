class AlunoRepository():

    def __init__(self, alunos=[]):
       self.alunos=alunos

    def inserir(self,aluno):
        self.alunos.append(aluno)


    def listar(self):
        print("------------ Lista de alunos  ------------")
        for aluno in self.alunos:
            print(" Nome: {} Matricula: {} CPF: {} Endereço:  {} ".format(aluno.nome, aluno.matricula,aluno.cpf,aluno.endereco))
        print("-------------------------------------")    
        