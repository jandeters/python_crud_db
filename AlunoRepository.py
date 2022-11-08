# primeiro nome do arquivo e depois a classe
from Aluno import Aluno
class AlunoRepository():
    

    def __init__(self, alunos=[]):
       self.alunos=alunos

    def inserir(self,aluno:Aluno): 
        self.alunos.append(aluno)

    def pesquisar(self,nome:str): 
        lista=[]
        for aluno in self.alunos:
            if nome in aluno.nome:
                lista.append(aluno)         
        return lista

    def remover(self,cpf:str): 
        excluido = False
        for aluno in self.alunos:
            if cpf in aluno.cpf:
                self.alunos.remove(aluno) 
                excluido = True       
        return excluido
        
    def listar(self):
        print("------------------   Lista de alunos  ---------------------")
        for aluno in self.alunos:
            print(" Nome: {} Matricula: {} CPF: {} Endereço:  {} ".format(aluno.nome, aluno.matricula,aluno.cpf,aluno.endereco))
        print("------------------=----------------------------------------")    
        