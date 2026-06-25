import mysql.connector

# Function de conexao
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="dbbiblioteca"
    )

# Function de limpar o console quando necessário
def limpar_tela():
     os.system("cls" if os.name == "nt" else "clear")

# Function de cadastro
def cadastrar_livro(conexao, cursor):
    print("\n" + "=" * 50)
    print("CADASTRO DE LIVRO")
    print("=" * 50)

    titulo = input("\nDigite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    try:
        ano_publicacao = int(input("Digite o ano de publicação: "))
    except ValueError:
        print("\nInsira somente números")
        
    sql = "INSERT INTO livro (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
    valores = (titulo, autor, ano_publicacao)

    cursor.execute(sql, valores)
    conexao.commit()

    print("\n" + "=" * 50)
    print("LIVRO CADASTRADO COM SUCESSO")
    print("=" * 50)

# Function de listar os livros
def listar_livros(conexao, cursor):

    print("\n" + "=" * 50)
    print("LISTA DE LIVROS")
    print("=" * 50)

    cursor.execute("SELECT * FROM livro ORDER BY titulo")
    livros = cursor.fetchall()

    if not livros:
        print("\nNenhum livro cadastrado!")
    else:
        for livro in livros:
            print("\n" + "-" * 50)
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano: {livro[3]}")
        print("-" * 50)

# Function de buscar livros
def buscar_livro(conexao, cursor):

    print("\n" + "=" * 50)
    print("BUSCAR LIVRO")
    print("=" * 50)
    print("[1] Buscar por ID")
    print("[2] Buscar por Título")
    print("[3] Buscar por Autor")
    print("[4] Voltar ao Menu Principal")
    print("=" * 50)

    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        opcao = -1

    if opcao == 1:
        try:
            id_livro = int(input("\nDigite o ID do livro: "))

            if id_livro > 0:
                cursor.execute(
                    "SELECT * FROM livro WHERE id_livro = %s",
                    (id_livro,)
                )

                livro = cursor.fetchone()

                if livro:
                    print("\n" + "=" * 50)
                    print("LIVRO ENCONTRADO")
                    print("=" * 50)
                    print(f"ID: {livro[0]}")
                    print(f"Título: {livro[1]}")
                    print(f"Autor: {livro[2]}")
                    print(f"Ano: {livro[3]}")
                    print("=" * 50)
                else:
                    print("\nLivro não encontrado!")
            else:
                print("\nInsira somente valores maiores que zero")

        except ValueError:
            print("\nInsira um número válido")

    elif opcao == 2:
        print("\nBuscar por título ainda não implementado")

    elif opcao == 3:
        print("\nBuscar por autor ainda não implementado")

    elif opcao == 4:
        print("\nRetornando ao menu...")

    else:
        print("\nOpção inválida")

# Function do menu de escolha
def menu():
    print("\n" + "=" * 50)
    print("MENU PRINCIPAL")
    print("=" * 50)
    print("[1] Cadastrar Livro")
    print("[2] Listar Livros")
    print("[3] Buscar Livro")
    print("[4] Atualizar Livro")
    print("[5] Excluir Livro")
    print("[6] Sair")
    print("=" * 50)

    try:
        return int(input("\nEscolha uma opção: "))
    except ValueError:
        return -1

# Mensagem inicial do programa
print("\n" + "=" * 50)
print("SISTEMA BIBLIOTECÁRIO v1.0")
print("=" * 50)
print("Banco de dados conectado com sucesso!")
print("=" * 50)

conexao = conectar()
cursor = conexao.cursor()

while True:
    escolha = menu()

    if escolha == 1:
        cadastrar_livro(conexao, cursor)

    elif escolha == 2:
        listar_livros(conexao, cursor)

    elif escolha == 3:
        buscar_livro(conexao, cursor)

    elif escolha == 4:
        print("\nAtualização ainda não implementada")

    elif escolha == 5:
        print("\nExclusão ainda não implementada")

    elif escolha == 6:
        conexao.close()
        print("\nBanco de dados desconectado com sucesso!")
        print("Encerrando sistema...\n")
        break

    else:
        print("\nOpção inválida! Tente novamente")