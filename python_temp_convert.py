# first we give values at the diff. tempersature unit

fahrenheit= 32
celsius= 0
celsius = (fahrenheit- 32)* 5.0/9.0
print(celsius)

fahrenheit = (celsius * 9.0/5.0) + 32
print(fahrenheit)


# second we put an imput to give the temp 

fahrenheit= input('enter fahrenheit temperature: ')
celsius= input ('enter celsisus temperature: ')
celsius = (float (fahrenheit)- 32)* 5.0/9.0
print(celsius)

fahrenheit = (celsius * 9.0/5.0) + 32
print(fahrenheit)


choice = input ('Enter 1 if you want to convert f -> c or 2 for c -> f')
if choice == '1':
   fahrenheit = input('enter fahrenheit temperature: ')
   celsius = (float (fahrenheit)- 32)* 5.0/9.0
   print(celsius)
elif choice == '2':
   celsius= input ('enter celsisus temperature: ')
   fahrenheit = (float(celsius) * 9.0/5.0) + 32
   print(fahrenheit)
else:
    print('nothing selected')
