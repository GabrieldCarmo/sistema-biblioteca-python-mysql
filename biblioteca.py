import mysql.connector
import os
from datetime import datetime
import time

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

def confirma_enter():
    input("\nAperte enter para voltar ao menu: ")

# Function de cadastrar os livros
def cadastrar_livro(conexao, cursor):
    limpar_tela()
    print("\n" + "=" * 50)
    print("CADASTRO DE LIVRO")
    print("=" * 50)

    titulo = input("\nDigite o título do livro: ")
    autor = input("Digite o autor do livro: ")

    try:
        ano_publicacao = int(input("Digite o ano de publicação: "))
    except ValueError:
        print("\nInsira somente números")
        return

    if not titulo.strip() or not autor.strip():
        time.sleep(2)
        print("\nPreencha todos os campos")
        return
    
    ano_atual = datetime.now().year
    if ano_publicacao > ano_atual:
        print("\nInsira um ano válido")
        time.sleep(2)
        return

    sql = "INSERT INTO livro (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
    valores = (titulo, autor, ano_publicacao)

    cursor.execute(sql, valores)
    conexao.commit()

    limpar_tela()
    print("\n" + "=" * 50)
    print("LIVRO CADASTRADO COM SUCESSO")
    print("=" * 50)

    confirma_enter()

# Function de listar os livros
def listar_livros(conexao, cursor):

    limpar_tela()

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
    
    confirma_enter()

# Function de buscar livros
def buscar_livro(conexao, cursor):
    limpar_tela()
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

    # Busca por ID
    if opcao == 1:

        try:
            id_livro = int(input("\nDigite o ID do livro: "))
        except ValueError:
            print("\nInsira um número válido!")
            return

        if id_livro > 0:
            cursor.execute(
                "SELECT * FROM livro WHERE id_livro = %s",
                (id_livro,)
            )
            livro = cursor.fetchone()
            if livro:
                limpar_tela()
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

    # Busca por titulo
    elif opcao == 2:
        titulo = input("\nDigite o título do livro: ")

        if titulo:
            cursor.execute(
                "SELECT * FROM livro where titulo LIKE %s",
                (f"%{titulo}%",)
            )

            livros = cursor.fetchall()

            if livros:
                limpar_tela()
                print("\n" + "=" * 50)
                print("LIVROS ENCONTRADOS")
                print("=" * 50)

                for livro in livros:
                    print(f"ID: {livro[0]}")
                
                    print(f"Título: {livro[1]}")
                    print(f"Autor: {livro[2]}")
                    print(f"Ano: {livro[3]}")
                    print("-" * 50)
            else:
                print("\nLivro não encontrado!")
        else:
            print("\nDigite um título válido")

    elif opcao == 3:
        autor = input("\nDigite o nome do autor do livro: ")

        if autor:
            cursor.execute(
                "SELECT * FROM livro where autor LIKE %s",
                (f"%{autor}%",)
            )

            livros = cursor.fetchall()

            if livros:
                limpar_tela()
                print("\n" + "=" * 50)
                print("LIVROS ENCONTRADOS")
                print("=" * 50)

                for livro in livros:
                    print(f"ID: {livro[0]}")
                
                    print(f"Título: {livro[1]}")
                    print(f"Autor: {livro[2]}")
                    print(f"Ano: {livro[3]}")
                    print("-" * 50)
            else:
                print("\nLivro não encontrado!")
        else:
            print("\nDigite um autor válido!")

    elif opcao == 4:
        print("\nRetornando ao menu...")

    else:
        print("\nOpção inválida")
        return
    confirma_enter()

#Function de atualização de livros
def atualizar_livro(conexao, cursor):
    limpar_tela()
    try:
        id_livro = int(input("\nDigite o ID do livro que deseja atualizar: "))
    except ValueError:
        print("\nInsira um valor válido!")
        return

    if id_livro > 0 and id_livro:
        cursor.execute(
            "SELECT * FROM livro WHERE id_livro LIKE %s",
            (id_livro,)
        )
        
        livro = cursor.fetchone()

        if livro: 
            limpar_tela()
            print("\n" + "=" * 50)
            print("LIVRO ENCONTRADO")
            print("=" * 50)
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano: {livro[3]}")
            print("=" * 50)

            time.sleep(1)

            print("\n" + "=" * 50)
            print("O QUE DESEJA ATUALIZAR? ")
            print("=" * 50)
            print("[1] Atualizar título")
            print("[2] Atualizar Autor")
            print("[3] Atualizar ano de lançamento")
            print("[4] Voltar ao Menu Principal")
            print("=" * 50)


            try:
                opcao = int(input("\nEscolha uma opção: "))
            except ValueError:
                opcao = -1
            
            limpar_tela()

            # Atualizar titulo do livro
            if opcao == 1:
                novo_titulo = input("\nDigite o novo título do livro: ")

                cursor.execute(
                    "UPDATE livro SET titulo = %s WHERE id_livro = %s",
                    (novo_titulo, id_livro,)
                )
                limpar_tela()
                print("\nTítulo do livro atualizado com sucesso! ")

            #Atualizar autor do livro
            elif opcao == 2:
                novo_autor = input("\nDigite o novo autor do livro: ")

                cursor.execute(
                    "UPDATE livro SET autor = %s WHERE id_livro = %s",
                    (novo_autor, id_livro,)
                )
                limpar_tela()
                print("\nAutor do livro atualizado com sucesso! ")
            
            #Atualizar ano de lancamento do livro
            elif opcao == 3:
                novo_ano = input("\nDigite o novo ano de lançamento: ")

                cursor.execute(
                    "UPDATE livro set ano_publicacao = %s WHERE id_livro = %s",
                    (novo_ano, id_livro,)
                )
                limpar_tela()
                print("\nAno de lançamento do livro atualizado com sucesso! ")

            #voltar ao menu
            elif opcao == 4:
                return
            
            else:
                print("\nOpção inválida! Tente novamente")

            conexao.commit()
            confirma_enter()

#Function de deletar livros
def deletar_livros(conexao, cursor):
    try:
        id_livro = int(input("\nDigite o ID do livro que deseja deletar: "))
    except ValueError:
        print("\nInsira um valor válido!")
        return

    if id_livro > 0 and id_livro:
        cursor.execute(
            "SELECT * FROM livro WHERE id_livro LIKE %s",
            (id_livro,)
        )
        
        livro = cursor.fetchone()

        if livro: 
            limpar_tela()
            print("\n" + "=" * 50)
            print("LIVROS ENCONTRADOS")
            print("=" * 50)
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Ano: {livro[3]}")
            print("=" * 50)

            time.sleep(1.5)

            try:
                escolha = str(input("\nTem certeza que deseja apagar este livro? (S/n): "))
            except ValueError:
                print("\nInsira apenas S ou N para continuar!")
                return
            
            
            if escolha.lower() == "s" :
                print("\nApagando Livro!")
                time.sleep(1.5)
                cursor.execute(
                    "DELETE FROM livro WHERE id_livro = %s",
                    (id_livro,)
                )
                time.sleep(1.5)
                limpar_tela()
                conexao.commit()
                print("\nLivro apagado com sucesso!")
            else:
                print("\nInsira apenas S ou N para continuar!")
                return
        else:
            print("\nLivro não encontrado!")
    else:
        print("\nInsira um ID válido!")
    confirma_enter()
    
# Function do menu de escolha
def menu():
    limpar_tela()
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

limpar_tela()

conexao = conectar()
cursor = conexao.cursor()

print("\n" + "=" * 50)
print("SISTEMA BIBLIOTECÁRIO v1.0")
print("=" * 50)
print("Banco de dados conectado com sucesso!")
print("=" * 50)

time.sleep(1.5)

while True:
    escolha = menu()

    if escolha == 1:
        cadastrar_livro(conexao, cursor)

    elif escolha == 2:
        listar_livros(conexao, cursor)

    elif escolha == 3:
        buscar_livro(conexao, cursor)

    elif escolha == 4:
        atualizar_livro(conexao, cursor)

    elif escolha == 5:
        deletar_livros(conexao, cursor)

    elif escolha == 6:
        conexao.close()
        print("\nBanco de dados desconectado com sucesso!")
        print("Encerrando sistema...\n")
        break

    else:
        print("\nOpção inválida! Tente novamente")