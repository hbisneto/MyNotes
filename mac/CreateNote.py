################################################################################
##                      Nome do Arquivo: CreateNote.py                        ##
##                  Criado por: Heitor Bardemaker A. Bisneto                  ##
################################################################################

import os
from mac import RTFLib

SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'
NoteProcessor = []
Extension = ['.html', '.md', '.py', '.rtf', '.txt']

def App():
    import MyNotes
    MyNotes.App()
    
def SalvarNota():
    Count = 0
    NewLine = "\n"
    
    print("="*80)
    print(f'>> Salvar Nota: <<')
    print("="*80)
    NomeNota = str(input(">> Nome da Nota: "))
    print("="*80)
    print(f'>> Extensão do arquivo: <<')
    print("="*80)

    for Format in Extension:
        Count += 1
        print(f'{Count} {Format}')
    print("="*80)
    Opc = int(input(">> Escolha a extensão da Nota: "))

    if Extension[Opc - 1] == ".rtf":
        NotaExport = f'{NotesFolder}{NomeNota}{Extension[Opc-1]}'
        NomeNota = f'{NomeNota}{Extension[Opc-1]}'
        
        RTFLib.FileName = NotaExport
        RTFLib.NomeNota = NomeNota
        RTFLib.SaveRTF()
    else:
        try:
            f = open(f'{NotesFolder}{NomeNota}{Extension[Opc-1]}', 'x')
            print(f'>> Nota salva como "{NomeNota}{Extension[Opc-1]}"')
            for Writer in NoteProcessor:
                f.write(Writer + NewLine)
            print('>> Digite "App()" para executar o programa novamente')

        except:
            print("="*80)
            print(f'>> Arquivo já existente: <<')
            print('>> Gostaria de sobreescrever?')
            print("="*80)
            print('1. Sim')
            print('2. Não')
            print("="*80)
            Confirm = int(input(f'>> Digite o número da opção: '))

            if Confirm == 1:
                f = open(f'{NotesFolder}{NomeNota}{Extension[Opc-1]}', 'w')
                print(f'>> Nota salva como "{NomeNota}{Extension[Opc-1]}"')
                for Writer in NoteProcessor:
                    f.write(Writer + NewLine)
                print('>> Digite "App()" para executar o programa novamente')
            else:
                print(">> A Nota não foi salva!")
                App()
    
def CriarNota():
    print(f'>> Dica: Aperte "Enter" no teclado para opções da nota')
    print("="*80)
    Content = str(input(">> "))
    NoteProcessor.append(Content)
    
    Loop = True
    while Loop == True:
        print("="*80)
        print(f'>> 1. Nova Linha')
        print(f'>> 2. Ler Nota')
        print(f'>> 3. Salvar Nota')
        print("="*80)
        Opc = int(input(">> Digite o número da opção: "))

        if Opc == 1:
            Content = str(input(">> "))
            NoteProcessor.append(Content)
        elif Opc == 2:
            print()
            print("="*40)
            print(f'>> Ler Nota: <<')
            print("="*40)
            for Writer in NoteProcessor:
                print(Writer)
            print("="*40)
            print()
        elif Opc == 3:
            Loop = False
            SalvarNota()
        else:
            print("="*80)
            print(f'>> Nota finalizada')
            print("="*80)
            Loop = False

