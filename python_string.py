Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "io"
>>> 5+9
14
>>> print (5+7)
12
>>> print(6*8)
48
>>> 4/3
1.3333333333333333
>>> 6^2
4
>>> 
======================= RESTART: D:/software/ex python.py ======================
>>> 
======================= RESTART: D:/software/ex python.py ======================
28
marco
enea
>>> print(name)
marco
>>> children
['asia', 'enea', 'giugno']
>>> age
28
>>> len (name)
5
>>> len (children)
3
>>> str.find("marco", "mb")
-1
>>> str.find("marco","r")
2
>>> str.replace(name, "marco", "squalo")
'squalo'
>>> name
'marco'
>>> name= str.replace (name, "marco", "squalo")
>>> name
'squalo'
>>> name= str.replace (name, "squalo", "marcolino")
>>> name
'marcolino'
>>> children
['asia', 'enea', 'giugno']
>>> newname= "Marco Baldo"
>>> newname
'Marco Baldo'
>>> namelist= str.split(newname, ',')
>>> namelist
['Marco Baldo']
>>> newname= "marco", "giada", "lollo", "francescp"
>>> namelist=str.split(newname, ",")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    namelist=str.split(newname, ",")
TypeError: descriptor 'split' for 'str' objects doesn't apply to a 'tuple' object
>>> namelist=str.split(newname, ",")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    namelist=str.split(newname, ",")
TypeError: descriptor 'split' for 'str' objects doesn't apply to a 'tuple' object
>>>  names= "marco", "giada", "lollo", "francesco"
 
SyntaxError: unexpected indent
>>> names = "marco", "giada", "lollo", "francesco"
>>> nameslist = str.split(names, ',')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    nameslist = str.split(names, ',')
TypeError: descriptor 'split' for 'str' objects doesn't apply to a 'tuple' object
>>> newname= "Marco Baldo"
>>> newname
'Marco Baldo'
>>> namelist= str.split(newname, ',')
>>> namelist
SyntaxError: multiple statements found while compiling a single statement
>>> names
('marco', 'giada', 'lollo', 'francesco')
>>> names = "marco, giada, lollo, francesco"
>>> nameslist = str.split(names, ',')
>>> nameslist
['marco', ' giada', ' lollo', ' francesco']
>>> namelist[0]
'Marco Baldo'
>>> nameslist[0]
'marco'
>>> nameslist[2]
' lollo'
>>> name[0:4]
'marc'
>>> name[-3:]
'ino'
>>> name[-6:3]
''
>>> 
