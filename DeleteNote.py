################################################################################
##                      Nome do Arquivo: DeleteNote.py                        ##
##                  Criado por: Heitor Bardemaker A. Bisneto                  ##
################################################################################

import os

SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'

def App():
    import MyNotes
    MyNotes.App()

class cd:
    def __init__(Self, NewPath):
        Self.NewPath = os.path.expanduser(NewPath)

    def __enter__(Self):
        Self.SavedPath = os.getcwd()
        os.chdir(Self.NewPath)

    def __exit__(Self, Etype, Value, Traceback):
        os.chdir(Self.SavedPath)
        
def DeletarNota(MyFiles = []):
    MyFiles.clear()
    with cd(NotesFolder):
        Process = os.listdir()
        
        for Files in Process:
            MyFiles.append(Files)
            if '.DS_Store' in MyFiles:
                MyFiles.remove('.DS_Store')

        print(f'>> Notas Disponíveis:')
        print("="*80)
        Count = 0
        for Arquivo in MyFiles:
            Count += 1
            print(f'{Count}. {Arquivo}')

        if Count == 0:
            print(f'>> Não há notas disponíveis!')
            print("="*80)
        else:
            print("="*80)
            Opc = int(input(">> Digite o número da opção: "))

            print("="*80)
            print(f'>> Tem certeza que gostaria de deletar a nota "{MyFiles[Opc-1]}"?')
            print(f'>> 1. Sim')
            print(f'>> 2. NÃO')
            print("="*80)
            Confirm = int(input(">> Digite o número da opção: "))

            if Confirm == 1:
                if os.path.exists(f'{NotesFolder}{MyFiles[Opc-1]}'):
                    os.remove(f'{NotesFolder}{MyFiles[Opc-1]}')
                    print(f'>> Arquivo excluído: "{MyFiles[Opc-1]}"')
                else:
                    print("="*80)
                    print(">> Erro ao deletar arquivo! <<")
                    print(">> Verifique a existência do arquivo e tente novamente")
                    print("="*80)
            else:
                print(">> Operação cancelada!")
        print('>> Digite "App()" para executar o programa novamente')
        

        
