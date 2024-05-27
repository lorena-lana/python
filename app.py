# print('fala seus porras')

import os

restaurantes =['pythonBurge','madalousso','notubo']

def exibir_nome_do_programa():
    print('s̷a̷b̷o̷r̷ e̷x̷p̷r̷e̷s̷s̷')
    
    
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')
    
    
def voltar_menu_principal():
    input('digite uma tecla para voltar ao menu pricipal') 
    main()
    
    
    
def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu_principal()
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')
    nome_do_restaurante=input('digite o nome do restaurante que voce quer cadastar: ')
    restaurantes.append(nome_do_restaurante)    
    
    
def listar_restaurantes():
    exibir_subtitulo('LISTANDO RESTAURANTES')
    
    for restaurante in restaurantes:
        print(restaurante)
    voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo('finalizar app')
    
    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def escolher_opcao():
    try:
        opcao_escolhida=int(input("esclha uma opção: "))
        
        if opcao_escolhida==1:
            #    print('voce escolheu cadastar um restaurante') 
             cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            #    print('voce escolheu listar restaurantes') 
            listar_restaurantes()
        elif opcao_escolhida==3:
            print('ativar restaurante') 
        else:
            opcao_invalida()   
    except:    
        opcao_invalida()
    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__=='__main__':
    main()