# python 3.8.5 module index # default py modules that you can use as library to make analysis and functions needed
# -> json:  Encode and decode the JSON format. json — JSON encoder and decoder: https://docs.python.org/3.8/library/json.html#module-json
# -> math: additional possible Mathematical functions!! https://docs.python.org/3.8/library/math.html#module-math. to make python lighter some maths operation are into this module. is your choice to lanch it.
# Power and logarithmic functions. math.exp(x) = Return e raised to the power x, where e = 2.718281= e^x
# 'math.log10(x)' Return the base-10 logarithm of x.     'math.sqrt(x)' Return the square root of x.   ' math.pow(x,y)'= Unlike the built-in ** operator, math.pow() converts both its arguments to type float. Use ** or the built-in pow() function for computing exact integer powers.
# 'math.cos(x)' Return the cosine of x radians. 
#'math.dist(p, q)' Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates. The two points must have the same dimension. Roughly equivalent to: sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
# 'math.hypot(*coordinates)' : Return the Euclidean norm, sqrt(sum(x**2 for x in coordinates)). This is the length of the vector from the origin to the point given by the coordinates.
# 'math.sin(x)' Return the sine of x radians. math.tan(x) Return the tangent of x radians.
# 'math.erf(x)': Return the error function at x.The erf() function can be used to compute traditional statistical functions such as the cumulative standard normal distribution:  #  def phi(x):
                                                                                                                                                                                       # 'Cumulative distribution function for the standard normal distribution'
                                                                                                                                                                                       # return (1.0 + erf(x / sqrt(2.0))) / 2.0

# multiprocessing — Process-based parallelism


name = "marco"
age = 28
girl= "viky"
children= ["asia","enea", "giugno"]
print(age)
print(name)
print(children[1])


##importation of modules..

import time, math
print(math.factorial(5))
print(math.pow(25,2))
print(25**2)

print(math.pi)
print (math.cos(43))

print (time.time())
starttime= time.time()
endtime= time.time() - starttime
print (endtime)

# bring in html page library directly
import urllib.request
html = urllib.request.urlopen('http://gisadvisor.com').read()
print(html)
# copy the java script in a blocknotes file and save with name. later you can open it thanks the browser directory: file:///D:/software/test.html. or clicking on the file saved.



