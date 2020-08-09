======================= RESTART: D:/software/ex_pyt.2.py =======================
Traceback (most recent call last):
  File "D:/software/ex_pyt.2.py", line 3, in <module>
    a + b
NameError: name 'b' is not defined
>>> a= 5
B= 2
a + b
c = a+b
c
a * b
a / b
b / a
b // a
SyntaxError: multiple statements found while compiling a single statement
>>> a=5
>>> b=12
>>> a+b
17
>>> c= a+b
>>> c
17
>>> a*b
60
>>> a/b
0.4166666666666667
>>> b/a
2.4
>>> b//a
2
>>> 5**2
25
>>> a**2
25
>>> a/b
0.4166666666666667
>>> b/a
2.4
>>> b//a
2
>>> b%a
2
>>> a
5
>>> b
12
>>> b%a
2
>>> b/a
2.4
>>> b-a*2
2
>>> a*2
10
>>> 5**2
25
>>> 9**.5
3.0
>>> a=5
>>> b=7ù
SyntaxError: invalid syntax
>>> b=7
>>> c= (a**2+b**2)**.5
>>> c
8.602325267042627
>>> mylist= ["art", "bob", "joe"]
>>> mylist
['art', 'bob', 'joe']
>>> mylist[0]
'art'
>>> mylist = [["art",52], ["bob", 19], ["sue" ,44]]
>>> mylist
[['art', 52], ['bob', 19], ['sue', 44]]
>>> mylist = [["art",54], ["bob", 19], ["sue" ,42]]
>>> mylist[0]
['art', 54]
>>> mylist[1]
['bob', 19]
>>> mylist[0][0]
'art'
>>> mylist[1][0]
'bob'
>>> mylist[2][1]
42
>>> year= [2015,2014,2016]
>>> year
[2015, 2014, 2016]
>>> year.append(2017)
>>> year
[2015, 2014, 2016, 2017]
>>> year.append([2018,2019])
>>> year
[2015, 2014, 2016, 2017, [2018, 2019]]
>>> year.append(2018)
>>> year.append(2019)
>>> year.remove([2018, 2019])
>>> year
[2015, 2014, 2016, 2017, 2018, 2019]
>>> year.reverse()
>>> year
[2019, 2018, 2017, 2016, 2014, 2015]
>>> year.reverse()
>>> year
[2015, 2014, 2016, 2017, 2018, 2019]
>>> del year[0]
>>> del year[-1]
>>> del year(2016)
SyntaxError: cannot delete function call
>>> del year[2016]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del year[2016]
IndexError: list assignment index out of range
>>> year.remove)
SyntaxError: unmatched ')'
>>> year.remove(2016)
>>> year
[2014, 2017, 2018]
>>> mylist = [7,6,9,11,5,8]
>>> mylist.reverse()
>>> mylist
[8, 5, 11, 9, 6, 7]
>>> mylist.reverse()
>>> mylist
[7, 6, 9, 11, 5, 8]
>>> mylist.sort()
>>> mylist
[5, 6, 7, 8, 9, 11]
>>> max(mylist)
11
>>> min(mylist)
5
>>> lent(mylist)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    lent(mylist)
NameError: name 'lent' is not defined
>>> len(mylist)
6
>>> print(mylist[len(mylist)-1])
11
>>> print(mylist[len(mylist)-2])
9
>>> print(mylist[len(mylist)-3])
8
>>> 
