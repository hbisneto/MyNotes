# BackupLib

import os
import shutil
import datetime

Day = datetime.date.today().day
DayStr = str(Day)
Month = datetime.date.today().month
MonthStr = str(Month)
Year = datetime.date.today().year
YearStr = str(Year)

Hour = datetime.datetime.now().hour
Minute = datetime.datetime.now().minute
Second = datetime.datetime.now().second

if Day < 10:
    DayStr = "0" + str(Day)
else:
    DayStr = Day

if Month < 10:
    MonthStr = "0" + str(Month)
else:
    MonthStr = Month

DateFormat = f'{DayStr}-{MonthStr}-{YearStr}_{Hour}_{Minute}_{Second}'

def App():
    import MyNotes
    MyNotes.App()

def Backup(source = f'{os.getcwd()}/Notas/', target = f'{os.getcwd()}/Backup/{DateFormat}/'):
    try:
        print("="*80)
        print(f'[MyNotes] - Processando Backup...')
        print("="*80)
        shutil.copytree(source, target)
        print(">> Backup Concluído!")
        print('>> Digite "App()" para executar o programa novamente')
    # Diretórios iguais
    except shutil.Error as e:
        print('>> Diretório não copiado. Código do Erro: %s' % e)
        print('>> Digite "App()" para executar o programa novamente')
    # Erro de sistema: Provavelmente o diretório não existe
    except OSError as e:
        print('>> Diretório não copiado. Código do Erro: %s' % e)
        print('>> Digite "App()" para executar o programa novamente')
