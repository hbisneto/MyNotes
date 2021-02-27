# Criar Nota
import os
SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'
NoteProcessor = []
Extension = ['.html', '.md', '.py', '.txt']

def App():
    import MyNotes
    MyNotes.App()

def WordProcessor():
    print("="*80)
    print(f'>> Processando Arquivo do Microsoft Word...')
    print("="*80)
    
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
    try:
        f = open(f'{NotesFolder}{NomeNota}{Extension[Opc-1]}', 'x')
        print(f'>> Nota salva como "{NomeNota}{Extension[Opc-1]}"')
        for Writer in NoteProcessor:
            f.write(Writer + NewLine)
        App()
##        NoteProcessor.clear()
##        print(NoteProcessor)
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
##            NoteProcessor.clear()
##            print(NoteProcessor)
            App()
        else:
            print(">> A Nota não foi salva!")
##    NoteProcessor.clear()
##    print(NoteProcessor)
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
        print(f'>> 4. Finalizar Nota (Somente Leitura)')
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
        elif Opc == 4:
            print("="*40)
            print(f'>> Ler Nota: <<')
            print("="*40)
            for Writer in NoteProcessor:
                print(Writer)
            print("="*40)
            print()
            NoteProcessor.clear()
        else:
            print("="*80)
            print(f'>> Nota finalizada')
            print("="*80)
            Loop = False

