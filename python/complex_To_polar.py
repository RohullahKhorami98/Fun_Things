'''
cmath module is used to perform complex number operations

'''
import cmath
expression = complex(input())
r = abs(expression)
theta = cmath.phase(expression)
print(r)
print(theta)