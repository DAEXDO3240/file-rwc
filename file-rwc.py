#---------------------------LEGGI,COPIA,SCRIVI,FILE----------------------------#
#------------------------------------------------------------------------------#
def CopiaFile(Originale, Copia): 
  f1 = open(Originale, "r") 
  f2 = open(Copia, "w") 
  while 1: 
    Testo = f1.read(50) 
    if Testo == "": 
      break 
    f2.write(Testo) 
  f1.close() 
  f2.close() 
  return
#------------------------------------------------------------------------------#
k=0
#------------------------------------------------------------------------------#
print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
print("|  LEGGI,COPIA,SCRIVI,FILE  |")
while(k==0):
  fil=True
  print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
  print("| Chiudere il programma: 0  |")
  print("| Aprire un file: 1         |")
  print("| Copiare un file: 2        |")
  print("| Creare/resettare file: 3  |")
  print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
  n=int(input("=> Cosa voui fare? "))
#-------------------------------------------------------------#
  if(n==0):
    k=1
    print("")
    print("=> Spegnimento in corso...")
#-------------------------------------------------------------#
  if(n==1):
    while(fil!=False):
      fI=str(input("=> Che file vuoi aprire? "))
      if(fI=="nessuno"):
        fil=False
        print("")
      else:
        rw=str(input("=> Il file lo vuoi, leggerlo o modificarlo? "))
        #--------------------------------#
        if(rw=="leggerlo" or rw=="l"):
          try:
            f=open(fI,"r")
          except:
            print("=> Il file",fI,"non esiste")
          print(f.read())
          f.close()
          h=str(input("=> Vuoi continuare? "))
          if(h=="no"):
            fil=False
            print("")
        #--------------------------------#
        elif(rw=="modificarlo" or rw=="m"):
          try:
            f=open(fI,"r")
            Testo=f.read()
            print("=> Quello che c'è scritto nel file:")
            print(Testo)
            f.close()
            f=open(fI,"w")
            Text=str(input("=> Cosa vuoi scrive? "))
            f.write(Testo+Text)
            f.close()
          except:
            print("=> Il file", fI,"non esiste")
          h=str(input("=> Vuoi continuare? "))
          if(h=="no"):
            fil=False
            print("")
        #--------------------------------#
        elif(rw=="niente" or rw=="n"):
          fil=False
          print("")
        else:
          print("=> ErrorStr: non puoi scrivere numeri o parole se non quelle seguenti: leggerlo,modificarlo,niente,l,m,n")
#-------------------------------------------------------------#
  if(n==2):
      Originale=str(input("=> Dammi il nome del file originale => "))
      Copia=str(input("=> Dammi il nome del file in cui devo copiare => "))
      CopiaFile(Originale,Copia)
      print("=> Sto copiando...")
      print("=> Ho finito di copiare.")
      print("")
#-------------------------------------------------------------#
  if(n==3):
    fI=str(input("=> Che file vuoi aprire? "))
    try:
      f=open(fI,"r")
      Testo=f.read()
      print("=> Quello che c'è scritto nel file:")
      print(Testo)
      f.close()
      bi=str(input("=> Ne sei sicuro di resettarlo? "))
      if(bi=="no"):
        print("=> Ah, Bufuuuu...")
      if(bi=="si"):
        f=open(fI,"w")
      Text=str(input("=> Cosa vuoi scrive? "))
      f.write(Text)
      f.close()
    except:
      f=open(fI,"w")
      Text=str(input("=> Cosa vuoi scrive? "))
      f.write(Text)
      f.close()
