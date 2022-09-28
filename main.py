from AlunoRepository import AlunoRepository
from Aluno import Aluno

#chama o gerenciador 
repo=AlunoRepository()
opcao=0
print("Bem vindo ao Sistema Cleto School!")

while(opcao!=6):
    print(''' 
    ------  MENU ------- 
    [1] Incluir aluno
    [2] Pesquisar aluno
    [3] Alterar aluno
    [4] Excluir aluno 
    [5] Listar
    [6] Sair ''')
    opcao = int(input("Escolha uma das opções: "))
    print("Opção escolhida: {}".format(opcao))


    if(opcao==1):
        print(" -------- CADASTRO DE ALUNOS ------- ")
        nome=input("Informe nome: ")
        matricula=input("Informe a matricula: ")
        cpf = input("Informe o CPF: ")
        endereco = input("Informe o endereco: ")
        aluno=Aluno(nome,matricula,cpf,endereco)
        
        repo.inserir(aluno)
        repo.listar()

    if(opcao==2):
       
        nome2=input("Pesquisar pelo o nome: ")
        saida=repo.pesquisar(nome2)
        if not saida: 
             print("Nenhum aluno encontrado com o nome:",nome2)
        else: 
            for aluno in saida:
                print(" Nome: {} Matricula: {} CPF: {} Endereço:  {} ".format(aluno.nome, aluno.matricula,aluno.cpf,aluno.endereco))
                print("------------------=----------------------------------------")    
        