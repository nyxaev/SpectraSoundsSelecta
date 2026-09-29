
import re
from pymongo import MongoClient


# spectra sounds (reaproveitei memo) pra treinar mangas db
#⡴⠒⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠉⠳⡆⠀
#⣇⠰⠉⢙⡄⠀⠀⣴⠖⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠁⠙⡆
#⠘⡇⢠⠞⠉⠙⣾⠃⢀⡼⠀⠀⠀⠀⠀⠀⠀⢀⣼⡀⠄⢷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠰⠒⠲⡄⠀⣏⣆⣀⡍
#⢠⡏⠀⡤⠒⠃⠀⡜⠀⠀⠀⠀⠀⢀⣴⠾⠛⡁⠀⠀⢀⣈⡉⠙⠳⣤⡀⠀⠀⠀⠘⣆⠀⣇⡼⢋⠀⠀⢱
#⠀⠘⣇⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡴⢋⡣⠊⡩⠋⠀⠀⠀⠣⡉⠲⣄⠀⠙⢆⠀⠀⠀⣸⠀⢉⠀⢀⠿⠀⢸
#⠀⠀⠸⡄⠀⠈⢳⣄⡇⠀⠀⢀⡞⠀⠈⠀⢀⣴⣾⣿⣿⣿⣿⣦⡀⠀⠀⠀⠈⢧⠀⠀⢳⣰⠁⠀⠀⠀⣠⠃
#⠀⠀⠀⠘⢄⣀⣸⠃⠀⠀⠀⡸⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠈⣇⠀⠀⠙⢄⣀⠤⠚⠁⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢰⣿⣿⣿⡿⠛⠁⠀⠉⠛⢿⣿⣿⣿⣧⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⣸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠹⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⣀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣀⣀⠀⢀⣀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


cliente = MongoClient("mongodb://localhost:roda no padrao (27017) mas pode usar outro/", serverSelectionTimeoutMS=3000)

# "banco"
banco = cliente["catalogo"]

# "musicas"
musicas = banco["musicas"]

def ler_numero(texto, permitir_vazio=False):
    """Pede um número inteiro ao usuário até ele digitar certo."""
    while True:
        valor = input(texto).strip()
        if permitir_vazio and valor == "":
            return None
        if valor.isdigit():
            return int(valor)
        print("  Digite apenas números.")
def mostrar(lista):
    if not lista:
        print("\n  Nenhuma música encontrada.")
        return
    print()
    for i, m in enumerate(lista, start=1):
        print(f"  {i}. {m['titulo']} - {m['artista']} "
              f"| {m['bpm']} BPM | {m['ano']} | {m['subgenero']}")
def escolher(lista):
    mostrar(lista)
    if not lista:
        return None
    n = ler_numero("\nNúmero da música (0 para cancelar): ")
    if n == 0 or n > len(lista):
        print("  Cancelado.")
        return None
    return lista[n - 1]

# CRUD
def adicionar():

    print("\n--- Adicionar música ---")
    musica = {
        "titulo": input("Título: ").strip(),
        "artista": input("Artista: ").strip(),
        "bpm": ler_numero("BPM: "),
        "ano": ler_numero("Ano: "),
        "subgenero": input("Subgênero: ").strip(),
    }
    musicas.insert_one(musica) 
    print("  Música adicionada!")
def listar():
    print("\n--- Todas as músicas ---")
    mostrar(list(musicas.find().sort("artista", 1)))

def buscar():
    print("\n--- Buscar por artista ---")
    nome = input("Nome do artista: ").strip()
    
    filtro = {"artista": {"$regex": re.escape(nome), "$options": "i"}}
    mostrar(list(musicas.find(filtro)))

def atualizar():
    print("\n--- Atualizar música ---")
    musica = escolher(list(musicas.find().sort("artista", 1)))
    if not musica:
        return

    print("\nEnter em branco = manter o valor atual.")
    novos = {}

    for campo in ["titulo", "artista", "subgenero"]:
        valor = input(f"{campo} [{musica[campo]}]: ").strip()
        if valor:
            novos[campo] = valor

    for campo in ["bpm", "ano"]:
        valor = ler_numero(f"{campo} [{musica[campo]}]: ", permitir_vazio=True)
        if valor is not None:
            novos[campo] = valor

    if novos:
        musicas.update_one({"_id": musica["_id"]}, {"$set": novos})
        print("  Música atualizada!")
    else:
        print("  Nada foi alterado.")


def remover():
    print("\n--- Remover música ---")
    musica = escolher(list(musicas.find().sort("artista", 1)))
    if not musica:
        return
    confirmar = input(f"Apagar '{musica['titulo']}'? (s/n): ").strip().lower()
    if confirmar == "s":
        musicas.delete_one({"_id": musica["_id"]})  
        print("  Música removida!")
    else:
        print("  Cancelado.")




2

def menu():

    try:
        cliente.admin.command("ping")
    except Exception:
        print("Não consegui conectar no MongoDB. Ele está ligado?")
        return

    opcoes = {
        "1": adicionar,
        "2": listar,
        "3": buscar,
        "4": atualizar,
        "5": remover,
    }

    while True:
        print("\n=== CATÁLOGO===")
        print("1 - Adicionar música")
        print("2 - Listar músicas")
        print("3 - Buscar por artista")
        print("4 - Atualizar música")
        print("5 - Remover música")
        print("0 - Sair")

        escolha = input("Escolha: ").strip()
        if escolha == "0":
            print("Até mais! 🎧")
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("  Opção inválida.")


if __name__ == "__main__":
    menu()
