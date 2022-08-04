## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from exception import Exceptions
from windows import FileSystem

def Main():
   ################################################################################
   ##                      Biblioteca usada: MyNotes.py                          ##
   ##                  Criado por: Heitor Bardemaker A. Bisneto                  ##
   ################################################################################

   from windows import BackupLib
   from windows import CreateNote
   from windows import DeleteNote
   from windows import OpenNote
   from datetime import date
   import os

   SystemLocation = os.getcwd()
   NotesFolder = SystemLocation + '/Notas/'
   BackupFolder = SystemLocation + '/Backup/'

   AnoAtual = date.today().year
   SoftwareName = "MyNotes"
   Version = "2.0"
   CopyrightName = "Heitor Bisneto."

   print("="*80)
   print(f'[{SoftwareName} for Windows] - Em Execução...')
   print("="*80)
   print("Nome:", SoftwareName)
   print("Versão:", Version)
   print("Criado por:", CopyrightName)

   if AnoAtual == 2021:
       print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
   else:
       print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
   print()

   class cd:
       def __init__(Self, NewPath):
           Self.NewPath = os.path.expanduser(NewPath)

       def __enter__(Self):
           Self.SavedPath = os.getcwd()
           os.chdir(Self.NewPath)

       def __exit__(Self, Etype, Value, Traceback):
           os.chdir(Self.SavedPath)

   def PrepararSistema():
       try:
           print("="*80)
           print(f'>> Verificação de arquivos do sistema {SoftwareName} <<')
           print("="*80)
           print(f'>> Verificando pasta: "{NotesFolder}"...')
           os.mkdir(NotesFolder)
           print(f'>> Pasta "{NotesFolder}" criada')
           os.mkdir(BackupFolder)
           print(f'>> Pasta "{BackupFolder}" criada')
           print()
       except OSError:
           print(f'>> Status: Pasta "{NotesFolder}" configurada!')
           print(f'>> Status: Pasta "{BackupFolder}" configurada!')
           print()

   def ListarNotas(MyFiles = []):
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
       print('>> [MyNotes]: O programa foi finalizado') ## Create Library for System Messages (MyNotes #21)

   def App():
       PrepararSistema()
       CreateNote.NoteProcessor.clear()
       print("="*80)
       print(f'>> [{SoftwareName}] - Menu <<')
       print("="*80)
       print(f'>> 1. Criar Nota')
       print(f'>> 2. Abrir Nota')
       print(f'>> 3. Deletar Nota')
       print(f'>> 4. Listar Notas')
       print(f'>> 5. Backup')
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
       elif Opc == 4:
           print("="*80)
           print(f'>> Listar Notas: <<')
           print("="*80)
           ListarNotas()
       elif Opc == 5:
           print("="*80)
           print(f'>> Backup: <<')
           print("="*80)
           BackupLib.PrepareBackup() 
   App()

Main()
