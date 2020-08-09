>>> f = open('d:/software/specie_invasive.txt')
>>> f
<_io.TextIOWrapper name='d:/software/specie_invasive.txt' mode='r' encoding='cp1252'>
>>> for line if f:
	
SyntaxError: invalid syntax
>>> for line if f: print(line)
SyntaxError: invalid syntax
>>> for line if f:
	
SyntaxError: invalid syntax
>>> for line in f:
	print(line)

	
Callosciurus, erythraeus, Scoiattolo di Pallas, Localizzata

Herpestes ,javanicus, Mangusta indiana, Assente

Muntiacus ,reevesii, Muntjak della Cina, Assente

Myocastor ,coypus ,Nutria ,Diffusa

Nasua ,nasua, Nasua o coati rosso, Assente

Nyctereutes ,procyonoides ,Cane procione, Localizzata

Ondatra ,zibethicus Topo muschiato, Presenza da confermare

Procyon ,lotor ,Procione o orsetto lavatore, Localizzata

Sciurus ,carolinensis, Scoiattolo grigio,nordamericano,Localizzata

Sciurus ,niger ,Scoiattolo volpe ,Assente

Tamias ,sibiricus ,Tamia siberiano o borunduk ,Diffusa

Alopochen, aegyptiacus, Oca egiziana ,Presente

Corvus ,splendens ,Corvo indiano delle case, Assente

Oxyura ,jamaicensis, Gobbo della Giamaica, Occasionale

Threskiornis, aethiopicus ,Ibis sacro, Localizzata

Trachemys ,scripta ,Tartaruga palustre americana, Diffusa

Lithobates (Rana), catesbeianus, Rana toro americana, Localizzata

Perccottus ,glenii , ns, Assente

Pseudorasbora ,parva, Pseudorasbora, Diffusa

Eriocheir, sinensis ,Granchio cinese, Presenza da confermare

Orconectes, limosus, Gambero americano, Diffusa

Orconectes, virilis, Gambero virile, Assente

Pacifastacus, leniusculus, Gambero della California, Diffusa

Procambarus, clarkii ,Gambero rosso della Louisiana ,Diffusa

Procambarus, fallax f. virginalis, Gambero marmorato ,Diffusa

Vespa, velutina nigrithorax, Calabrone ,asiatico
>>> o = open('d:/software/classe.txt', 'w')
>>> for line if o:
	
SyntaxError: invalid syntax
>>> for line in o:
	o.write(line)

	
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    for line in o:
io.UnsupportedOperation: not readable
>>> for line in f:
	o.write(colunm)

	
>>> for line in f:
	o.write(line)

	
>>> 
>>> o.close
<built-in method close of _io.TextIOWrapper object at 0x00000244AF2E02B0>
>>> o.close()
>>> o = open('d:/software/classe.txt', 'w')
>>> for line in f:
	o.write(colunm)

	
>>> o = open('d:/software/classe2.txt', 'w')
>>> o = open('d:/software/classe.txt', 'w')                #scrivi nel file originale e copia dati sull'altro
>>> oo = open('d:/software/classe2.txt', 'w')
>>> for line in o:
	o.write(line)

	
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    for line in o:
io.UnsupportedOperation: not readable
>>> for line in f:
	o.write(line)

	
>>> 
>>> o.close()
>>> oo.close()

import math
array = [12,9,17,16]
sumtotal = 0
for i in array:
    print (i)
    sumtotal = i +sumtotal
print  ( 'the sum of the values is'  + str(sumtotal))   # la somma dei numeri della mia lista

import math
array = [12,9,17,16]
sumtotal = 0
for i in array:
    print (i**2)
    sumtotal = i**2 +sumtotal
print  ( 'the sum of the squares of the values is'  + str(sumtotal))   #somma i valori e fai i quadrati di ogni variabile


array = [12,9,17,16]
largest = 0

for i in array:
    if i > largest:
        largest= i                      ## the algoritm to gave a new largest value when it is fond at  y list
        
print(largest)




# open file and select variables in my file list

f = open('d:/software/specie_invasive.txt')

for line in f:
    addr = line.split(',')
    print(line)
    if addr[3] == 'NY':
        print('this is a NY addres ' + line)
    elif addr[3] == 'NJ':
        print('this is a NJ address' + line)
    else:
        print(line + ' this address isnt in NY or NJ')



        ## to remove white space on py
	
f = open('d:/software/specie_invasive.txt')

for line in f:
    addr = line.split(',')
    if addr[3].strip() == 'NY':
        print('this is a NY addres ' + line)
    elif addr[3].strip() == 'NJ':
        print('this is a NJ address' + line)
    else:
        print(line + ' this address isnt in NY or NJ')
	
	
