import os
from datetime import date
import CreateNote

SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'
CreateNote.NotesFolder = NotesFolder

AnoAtual = date.today().year
SoftwareName = "MyNotes"
Version = "1.0"
CopyrightName = "Heitor Bisneto."
print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("")

def PrepararSistema():
    try:
        print("="*80)
        print(f'>> Verificação de arquivos do sistema {SoftwareName} <<')
        print("="*80)
        print(f'>> Verificando pasta: "{NotesFolder}"...')
        os.mkdir(NotesFolder)
        print(f'>> Pasta "{NotesFolder}" criada')
        print()
    except OSError:
        print(f'>> Status: Pasta "{NotesFolder}" configurada!')
        print()

def App():
    PrepararSistema()
    print("="*80)
    print(f'>> Menu <<')
    print("="*80)
    print(f'>> 1. Criar Nota')
    print("="*80)
    Opc = int(input(">> Digite o número da opção: "))

    if Opc == 1:
        print("="*80)
        print(f'>> Criar Nota: <<')
        print("="*80)
        CreateNote.CriarNota()
App()
