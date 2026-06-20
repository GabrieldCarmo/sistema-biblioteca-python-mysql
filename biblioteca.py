import mysql.connector

#Function de conexao
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="dbbiblioteca"
    )

#Function de cadastro
def cadastrar_livro():
    conexao = conectar()
    cursor = conexao.cursor()

    titulo = input("Digite o nome do livro que deseja cadastrar: ")
    autor = input("Digite o autor do livro: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))

    sql = "INSERT INTO livro (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
    valores = (titulo, autor, ano_publicacao)

    cursor.execute(sql, valores)
    conexao.commit()

    conexao.close()

    print("\nLivro cadastrado com sucesso!\n")

#Function de listar os livros
def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM livro ORDER BY titulo")
    livros = cursor.fetchall()

    print("\n" + "=" * 50)

    if not livros:
        print("Nenhum livro cadastrado!")
    else:
        print("LISTA DE LIVROS")
        print("=" * 50)

        for livro in livros:
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano: {livro[3]}")
            print("-" * 50)

    conexao.close()

#Function de buscar livros
def buscar_livro():
    conexao = conectar
    cursor = conexao.cursor()

    input()

#Mensagem inicial do programa
print("\n" + "=-=-" * 10)
print("SISTEMA BIBLIOTECÁRIO v1.0")
print("=-=-" * 10)

#Function do menu de escolha
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
        return int(input("Escolha uma opção: "))
    except Value:
        return -1


while True:
    escolha = menu()

    if escolha == 1:
        cadastrar_livro()

    elif escolha == 2:
        listar_livros()

    elif escolha == 3:
        print("Buscando Livro...\n")

    elif escolha == 4:
        print("Atualizando Livro...\n")

    elif escolha == 5:
        print("Excluindo Livro...\n")

    elif escolha == 6:
        print("Saindo...\n")
        break

    else:
        print("Opção inválida! Tente novamente\n")