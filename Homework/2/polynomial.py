'''################################################################################
        CSCE 206 Homework - 2 , Exercise P5
                Polynomial
                        
                Author:   Sendurr Selvaraj
                Email:    sendurr@hotmail.com
################################################################################'''

roots = [-1 , 1 , 2]

prod =1
x= 15

for i in roots:
    prod = prod*(x-i)

print("For the value of x=" + str(x) + " ,p(x) = " + str(prod))



'''################################################################################
        End of Program
################################################################################'''
