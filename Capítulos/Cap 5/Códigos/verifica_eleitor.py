voted = {}

def verifica_eleitor(nome):
    if voted.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar!")

verifica_eleitor("mike")

verifica_eleitor("mike")

verifica_eleitor("mike")
