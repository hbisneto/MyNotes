################################################################################
##                      Nome do Arquivo: BackupLib.py                         ##
##                  Criado por: Heitor Bardemaker A. Bisneto                  ##
################################################################################

import os
import shutil
import datetime

def PrepareBackup():
    Count = 0
    while Count < 15:
        Count += 1

    if Count >= 15:
        DateFunc()
        Backup()

def DateFunc():
    DateFunc.Day = datetime.date.today().day
    DateFunc.Month = datetime.date.today().month
    DateFunc.Year = datetime.date.today().year

    DateFunc.Hour = datetime.datetime.now().hour
    DateFunc.Minute = datetime.datetime.now().minute
    DateFunc.Second = datetime.datetime.now().second

    DateFunc.DayStr = str(DateFunc.Day)
    DateFunc.MonthStr = str(DateFunc.Month)
    DateFunc.YearStr = str(DateFunc.Year)

    if DateFunc.Day < 10:
        DateFunc.DayStr = "0" + str(DateFunc.Day)
    else:
        DateFunc.DayStr = DateFunc.Day

    if DateFunc.Month < 10:
        DateFunc.MonthStr = "0" + str(DateFunc.Month)
    else:
        DateFunc.MonthStr = DateFunc.Month

    DateFunc.DateFormat = f'{DateFunc.DayStr}-{DateFunc.MonthStr}-{DateFunc.YearStr}_{DateFunc.Hour}_{DateFunc.Minute}_{DateFunc.Second}'

def Backup():
    source = f'{os.getcwd()}/Notas/'
    target = f'{os.getcwd()}/Backup/{DateFunc.DateFormat}/'
    try:
        print(f'[MyNotes] - Processando Backup...')
        print("="*80)
        shutil.copytree(source, target)
        print(">> Backup Concluído!")
        print('>> [MyNotes]: O programa foi finalizado') ## Create Library for System Messages (MyNotes #21)
    except shutil.Error as e:
        print('>> Diretório não copiado. Código do Erro: %s' % e)
        print('>> [MyNotes]: O programa foi finalizado') ## Create Library for System Messages (MyNotes #21)
    except OSError as e:
        print('>> Diretório não copiado. Código do Erro: %s' % e)
        print('>> [MyNotes]: O programa foi finalizado') ## Create Library for System Messages (MyNotes #21)
