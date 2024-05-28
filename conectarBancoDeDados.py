
from pymongo.mongo_client import MongoClient
from pprint import pprint
from colorama import init, Fore

connectURL = 'mongodb+srv://<user>:<pass>@cluster-db.blzhilc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-DB' 

client = MongoClient(connectURL)

meubanco = client['db_teste']
colecao = meubanco['collection-teste']


def buscar_todos_trabalhos():
    trabalhos = colecao.find()
    return list(trabalhos)

def inserir_trabalho(trabalho):
    insert_document = colecao.insert_one(trabalho)
    print(f"Documento inserido com sucesso e seu ID é: {insert_document.inserted_id}")

def buscar_trabalho(status):
    trabalho = colecao.find_one({'status': status})
    print(trabalho)

def atualizar_trabalho(tipo, novos_dados):
    colecao.update_one({'type': tipo}, {'$set': novos_dados})

def deletar_trabalho(tipo):
    colecao.delete_one({'type': tipo})

def menu():
    print(Fore.YELLOW + "Escolha uma ação:\n")
    print(Fore. RESET + "1. Buscar todos os trabalhos")
    print("2. Inserir Trabalho")
    print("3. Buscar trabalho pelo status")
    print("4. Atualizar trabalho")
    print("5. Deletar trabalho")

    print(Fore.RED + "0. SAIR\n")
    try:
        escolha = int(input(Fore.GREEN + "Digite o número correspondente à ação: "))
        return escolha
    except ValueError:
        print(Fore.RED + "Desculpe, você não inseriu um número inteiro válido.")

def main():
    escolha = ...

    while(escolha!=0):

        escolha = menu()

        if escolha == 1:
            todos_trabalhos = buscar_todos_trabalhos()
            print(Fore.YELLOW + "\nTodos trabalhos\n")

            for trabalho in todos_trabalhos:
                print(trabalho)

        elif escolha == 2:
            tipo = input("Digite o tipo de trabalho: ")
            status = input("Digite o status de trabalho: ")

            inserir_trabalho({'type': tipo, 'status': status})
        
        elif escolha == 3:
            status = input("Digite o status de trabalho: ")

            buscar_trabalho(status)
        
        elif escolha == 4:
            tipo = input("Digite o tipo de trabalho a ser atualizado: ")
            novo_tipo = input("Digite o novo tipo de trabalho: ")
            novo_status = input("Digite o novo status de trabalho: ")

            novos_dados = {"type": novo_tipo, "status": novo_status}

            atualizar_trabalho(tipo, novos_dados)

        elif escolha == 5:
            tipo = input("Digite o tipo de trabalho: ")

            deletar_trabalho(tipo)

        
        elif escolha == 0:
            print(Fore.RED + "\nBye bye!\n")
            Fore.RESET
            break

        else:
            print(Fore.RED + "\nOpção inválida!\n")

        continuar = input(Fore.RESET + "\nPressione qualquer tecla para continuar ou 'q' para sair: \n")
        if continuar.lower() == 'q':
            print("\nBye bye!\n")
            Fore.RESET
            break

if __name__ == "__main__":
    main()

client.close()






