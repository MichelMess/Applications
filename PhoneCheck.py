#!/usr/bin/python
import sys

Contactos_list = []
contact_list = "/var/tmp/lab/assignement2/ContactosIII_Fase2.csv"

# Open a file
try:
   fn  = open(contact_list,"r")
except Exception, e:
    print"I can't  read your file: Issue:" ,e
    sys.exit()
            
#File read
lines = fn.readline()
while lines:
    a = lines.split("|")
    Contactos_list.append(a[3])
    lines = fn.readline()
    if not lines:
       break

#Lists
mcel_list = []
voda_list = []
movi_list = []
invalidumbers_list = []
validnumbers_list = []

# Costs
Mcelcost = 0.9
Vodacost = 0.8
Movicost = 0.7

# total costs calculations
McelTotal  = len(mcel_list) * Mcelcost * 2 #(2 messages spent per each message sent)
VodaTotal  = len(voda_list) * Vodacost * 2
MoviTotal = len(movi_list) * Movicost * 2
 
# conctactos Lenght
print 'Total numbers: ',len(Contactos_list)

# Mcel,Vodacom and Movitel array
for i in Contactos_list:
 b = i.replace(",", "")
 if b[0:2] == '82' and len(b) == 9:
    mcel_list.append(b)
    validnumbers_list.append(b)
    
 elif b[0:2] == '84' and len(b) == 9:
     voda_list.append(b)
     validnumbers_list.append(b)
    
 elif b[0:2] == '86' and len(b) == 9:
     movi_list.append(b)
     validnumbers_list.append(b)
 else: 
    len(b) != 9 
    invalidumbers_list.append(b)     
     
 #results from the three plataforms
print'\nMcel Numbers:', mcel_list,'\nVodacom Numbers:',voda_list,'\nMovitel Numbers:',movi_list

#invalid numbers
print'Invalid Numbers:', invalidumbers_list

#lenght results from the three Plataforms
print'\nForam encontrados', len(mcel_list),'numeros na Rede Mcel'
print'\nForam encontrados', len(voda_list),'numeros na Rede VM.'
print 'Foram encontrados', len(movi_list),'numeros na Rede Movitel.'

# total costs for each Plataform
print'\nCusto total de envio de SMS para a rede Mcel sao',len(mcel_list) * Mcelcost * 2,'Mt'
print'Custo total de envio de SMS para a rede Mcel sao',len(voda_list) * Vodacost * 2,'Mt'
print'Custo total de envio de SMS para a rede Mcel sao',len(movi_list) * Movicost * 2,'Mt'

#invalid Numbers lenght
print'\nForam encontrados', len(invalidumbers_list),'numeros invalidos.'
 
 #Valid Numbers lenght
print'Foram encontrados',len(validnumbers_list),'numeros validos'





