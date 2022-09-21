from AlunoRepository import AlunoRepository
from Aluno import Aluno

#chama o gerenciador 
repo=AlunoRepository()

print("Bem vindo ao Sistema Cleto School!")
print('''[1] Incluir aluno
[2] Pesquisar aluno
[3] Alterar aluno
[4] Excluir aluno ''')
opcao = input("Escolha uma das opções: ")
print("Opção escolhida: {}".format(opcao))


if(opcao=="1"):
    print(" -------- CADASTRO DE ALUNOS ------- ")
    nome=input("Informe nome: ")
    matricula=input("Informe a matricula: ")
    cpf = input("Informe o CPF: ")
    endereco = input("Informe o endereco: ")
    aluno=Aluno(nome,matricula,cpf,endereco)
    
    repo.inserir(aluno)
    repo.listar()

    
