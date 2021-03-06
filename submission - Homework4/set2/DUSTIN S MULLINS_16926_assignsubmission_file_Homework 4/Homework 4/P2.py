from matplotlib.pylab import *
import sys

def F(x):
	return exp(x**2)*sin(x)

t=linspace(-3.14,3.14,51)
y=zeros(len(t), 'd') 
for i in xrange(len(t)):
	y[i]=F(t[i])
print t
print y

plot(t, y)

xlabel('x') #adds label to x coordinate
ylabel('y')
legend('exp(x^2)*sin(x)')
title('Homework 4 - P2')
show()