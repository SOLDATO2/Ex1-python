"""
Como o exercicio requer um jogo da velha com tamanho fixo, a logica é relativamente simples. é possivel estabelecer uma matriz 4x4 onde cada casa representa uma lista de 1 elemento
dentro da lista mãe, possibilitando um manuseio simples. 
"""

jogo_da_velha =[ #Matriz para o jogo da velha
    ["0"],["1"],["2"],["3"],
    ["4"],["5"],["6"],["7"],
    ["8"],["9"],["10"],["11"],
    ["12"],["13"],["14"],["15"],
]


def mostrar_jogo_da_velha():
    """
    Função responsavel por mostrar o tabuleiro
    
    """
    count = 0
    print("-----------------------------")
    for x in jogo_da_velha:
        if count != 4:
            print(x, end = " ")
            count += 1
        else:
            count = 1
            print("\n")
            print(x, end = " ")
    print("\n-----------------------------")

def vitoria(X_ou_O): # Função que verifica todos os angulos possiveis para informar qual jogador ganhou
    #Porção para verificar vitoria diagonal p.
    if all((jogo_da_velha[i][0] == X_ou_O) for i in range(0, 16, 5)):
        return True
    #Porção para verificar vitoria diagonal s.
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(12, 2, -3)):
        return True
    #Porção para verificar Horizontal
    
    
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(0, 4)):
        return True
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(4, 8)):
        return True
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(8, 12)):
        return True
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(12, 16)):
        return True
    #Porção para verificar a vitoria da vertical
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(0, 13, 4)):
        return True
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(1, 14, 4)):
        return True
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(2, 15, 4)):
        return True
    elif all((jogo_da_velha[i][0] == X_ou_O) for i in range(3, 16, 4)):
        return True
    #Porção para verificar se deu velha
    elif all(item[0] == "X" or item[0] == "O" for item in jogo_da_velha):
        return False

while(True):

    mostrar_jogo_da_velha()

    while(True):
        escolha = int(input("Você é o 'X', escolha uma casa para inserir o 'X': "))  # Aguarda a resposta do jogador, e se caso a casa ja esteja ocupada, o programa ira pedir
        if jogo_da_velha[escolha][0] == "X" or jogo_da_velha[escolha][0] == "O": #      para que outra casa seja escolhida
            print("Essa posição já está ocupada.")
        else:
            jogo_da_velha[escolha][0] = "X"
            break
        
    
    if vitoria("X") == True: # se o jogador O conseguiu formar uma linha em um dos sentidos, a função retorna true e o programa informa que o 'O' ganhou
        mostrar_jogo_da_velha()
        print("Jogador X ganhou.")
        break
    elif vitoria("X") == False: # Informa que o jogo empatou se "O" não retornar true
        print("Deu velha.")
        break

    mostrar_jogo_da_velha()

    while(True):
        escolha = int(input("Você é o 'O', escolha uma casa para inserir o 'O': ")) # Aguarda a resposta do jogador, e se caso a casa ja esteja ocupada, o programa ira pedir
        if jogo_da_velha[escolha][0] == "X" or jogo_da_velha[escolha][0] == "O":#      para que outra casa seja escolhida
            print("Essa posição já está ocupada.")
        else:
            jogo_da_velha[escolha][0] = "O"
            break

    if vitoria("O") == True: # se o jogador O conseguiu formar uma linha em um dos sentidos, a função retorna true e o programa informa que o 'O' ganhou
        mostrar_jogo_da_velha()
        print("Jogador O ganhou.")
        break
    elif vitoria("O") == False: # Informa que o jogo empatou se "O" não retornar true
        mostrar_jogo_da_velha()
        print("Deu velha.")
        break






    

