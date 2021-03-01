# OpenNote

import os
SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'

def App():
    import MyNotes
    MyNotes.App()

class cd:
    # Gerenciador de contexto para mudar o diretório atual
    def __init__(Self, NewPath):
        Self.NewPath = os.path.expanduser(NewPath)

    def __enter__(Self):
        Self.SavedPath = os.getcwd()
        os.chdir(Self.NewPath)

    def __exit__(Self, Etype, Value, Traceback):
        os.chdir(Self.SavedPath)
        
def AbrirNota(MyFiles = []):
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
            print(f'>> Conteúdos da nota <<')
            print("="*80)
            f = open(f'{NotesFolder}{MyFiles[Opc-1]}', "r")
            print(f.read())
            print('>> Digite "App()" para executar o programa novamente')
