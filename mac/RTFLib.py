################################################################################
##                      Nome do Arquivo: RTFLib.py                            ##
##                  Criado por: Heitor Bardemaker A. Bisneto                  ##
################################################################################

import os
from mac import CreateNote

SystemLocation = os.getcwd()
NotesFolder = SystemLocation + '/Notas/'
NomeNota = str()
FileName = str()
DocumentStructure = "{\\rtf1\\ansi\\ansicpg1252\\cocoartf1504\\cocoasubrtf840\n{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}\n{\\colortbl;\\red255\\green255\\blue255;}\n{\\*\\expandedcolortbl;;}\n\\paperw11900\\paperh16840\\margl1440\\margr1440\\vieww10800\\viewh8400\\viewkind0\n\\pard\\tx566\\tx1133\\tx1700\\tx2267\\tx2834\\tx3401\\tx3968\\tx4535\\tx5102\\tx5669\\tx6236\\tx6803\\pardirnatural\\partightenfactor0\n\n\n\\f0\\fs24 \\cf0 "

def SaveRTF():
    NewLine = "\n"
    
    print("="*80)
    print(f'[MyNotes] - Exportar para RTF Document...')
    print("="*80)
    
    try:
        f = open(f'{FileName}', 'x')
        print(f'>> Nota salva como "{NomeNota}"')
        f.write(f'{DocumentStructure}')
        for Writer in CreateNote.NoteProcessor:
            f.write(f'{Writer}\{NewLine}')
        f = open(f'{FileName}', 'a')
        f.write("}")
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
            f = open(f'{FileName}', 'w')
            print(f'>> Nota salva como "{NomeNota}"')
            f.write(f'{DocumentStructure}')
            for Writer in CreateNote.NoteProcessor:
                f.write(f'{Writer}\{NewLine}')
            f = open(f'{FileName}', 'a')
            f.write("}")
            print('>> Digite "App()" para executar o programa novamente')
        else:
            print(">> A Nota não foi salva!")
            App()
