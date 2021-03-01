# MyNotes

import os
from datetime import date
import CreateNote
import OpenNote
import DeleteNote

SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'

AnoAtual = date.today().year
SoftwareName = "MyNotes"
Version = "1.2.2"
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
    CreateNote.NoteProcessor.clear()
    print("="*80)
    print(f'>> Menu <<')
    print("="*80)
    print(f'>> 1. Criar Nota')
    print(f'>> 2. Abrir Nota')
    print(f'>> 3. Deletar Nota')
    print("="*80)
    Opc = int(input(">> Digite o número da opção: "))

    if Opc == 1:
        print("="*80)
        print(f'>> Criar Nota: <<')
        print("="*80)
        CreateNote.CriarNota()
    elif Opc == 2:
        print("="*80)
        print(f'>> Abrir Nota: <<')
        print("="*80)
        OpenNote.AbrirNota()
    elif Opc == 3:
        print("="*80)
        print(f'>> Deletar Nota: <<')
        print("="*80)
        DeleteNote.DeletarNota()

App()
