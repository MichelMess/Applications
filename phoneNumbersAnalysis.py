#!/usr/bin/python
#The Primary goal of this Program is to analyze Mcel,Vodacom,Movitel,Invalid Phone Numbers,and 
# create a file with their respective List Phone numbers*
#This program is free software.
#Written by Michel Muchanga
#Attention: In order to work properly create this indicated directorys first: /var/lab/assignment4/McelVodacomMovitel.dir
#--------------------------------------------------------------------------------------------------------------------- 
import sys 
import time 
import os
from os.path import join as pjoin
  
def file(ContactsFile):  
    McelVodaMovi_list = []
    ValidMcelNumbers_list = [] 
    ValidVodaNumbers_list = []
    ValidMoviNumbers_list = []
    InvalidNumbers_list = []
    
    FinalDirectory = "/var/lab/assignment4/McelVodacomMovitel.dir"
 
    McelVodacomFile = "Mcel and Vodacom.txt" 
    MovitelFile = "Movitel.txt"
    InvalidFile = "Invalid Numbers.txt"

    McelVoda_Path = pjoin(FinalDirectory, McelVodacomFile)
    McelVodacomFile = open(McelVoda_Path, "w")

    Movitel_Path = pjoin(FinalDirectory,MovitelFile)
    MovitelFile = open(Movitel_Path, "w")

    Invalid_Path = pjoin(FinalDirectory,InvalidFile)
    InvalidFile = open(Invalid_Path, "w")
    
    # Opening the file
    try:
        PhoneNumbers  = open(ContactsFile,"r")
    except Exception, e:
        print"I can't read your file: Issue:" ,e
        sys.exit()
    
    # Reading File
    lines = PhoneNumbers.readline()
    while lines:
        a = lines.strip()
        b = a.split(",") 
        McelVodaMovi_list.append(b[1])
        lines = PhoneNumbers.readline()
        if not lines:
            break

    for i in McelVodaMovi_list:
        if i[5:7] == '82' and len(i) == 14:
            ValidMcelNumbers_list.append(i)   
            ValidMcelNumbers_list = list(set(ValidMcelNumbers_list))
        
        elif i[5:7] == '84' and len(i) == 14: 
            ValidVodaNumbers_list.append(i)
            ValidVodaNumbers_list = list(set(ValidVodaNumbers_list))

        elif i[5:7] == '86' and len(i) == 14:
            ValidMoviNumbers_list.append(i)
            ValidMoviNumbers_list = list(set(ValidMoviNumbers_list))
     
        else: 
            len(i) != 14
            InvalidNumbers_list.append(i)    
            InvalidNumbers_list = list(set(InvalidNumbers_list))
 

    #Writes Mcel,Vodacom,Movitel and Invalid Numbers analysis into a file
    #Mcel and Vodacom Phone Numbers File
    McelVodacomFile.write('Mcel and Vodacom Phone Numbers\n') 
    McelVodacomFile.write('\nMcel Numbers')
    McelVodacomFile.write(' '.join(('\nTotal Mcel Numbers:',str(len(ValidMcelNumbers_list)))))
 
    for i in range(len(ValidMcelNumbers_list)):  
        McelVodacomFile.writelines(' '.join(('\nNumber:',str(i),'Mcel:',str(ValidMcelNumbers_list[i]),'\n------------------------------------------')))
    McelVodacomFile.write('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    McelVodacomFile.write('\nVodacom Numbers')
    McelVodacomFile.write(' '.join(('Total Vodacom Numbers:',str(len(ValidVodaNumbers_list)))))
    for i in range(len(ValidVodaNumbers_list)):
        McelVodacomFile.writelines(' '.join(('\nNumber:',str(i),'Vodacom',str(ValidVodaNumbers_list[i]),'\n------------------------------------------')))

    #Movitel Phone Numbers file
    MovitelFile.write('Movitel Phone Numbers')
    MovitelFile.write(' '.join(('\nTotal Movitel Numbers:',str(len(ValidMoviNumbers_list)))))
    for i in range(len(ValidMoviNumbers_list)):
        MovitelFile.writelines(' '.join(('\nNumber:',str(i),'Movitel:',str(ValidMoviNumbers_list[i]),'\n-----------------------------------------------')))
 
    #Invalid Phone Numbers File 
    InvalidFile.write('Invalid Phone Numbers')
    InvalidFile.write(' '.join(('\nTotal Invalid Numbers:',str(len(InvalidNumbers_list)))))
    for i in range(len(InvalidNumbers_list)): 
        InvalidFile.writelines(' '.join(('\nNumber:',str(i),'Invalid:',str(InvalidNumbers_list[i]),'\n-------------------------------------------------')))
 
    McelVodacomFile.close()
    MovitelFile.close()
    InvalidFile.close()
    

file("/var/lab/assignment4/Lista de Contactos.csv")  
 

   