# Name: Lucke Oliveira Luz			Assignment: Homework 2       Exercise: 2

v0 = 1.0
g = 9.81
n = 11
t = 0
step = (2.0*v0/g)/(n-1)

while t < 2.0*v0/g + step:  
	y = v0*t - 0.5*g*t**2
	print "%.5f"%(t),"%.5f"%(y)
	t += step

print "LAST Y VALUE =", y #THE VALUE IS EXTREMELY CLOSE TO THE EXPECTED VALUE OF ZERO. I TRIED TO EXPLAIN THE REASONS FOR THIS RESULT BELOW.

#PYTHON WAS NOT PRINTING THE LAST VALUE WHEN SETTING THE WHILE LOOP LIMIT TO "t <= 2*v0/g". AFTER TESTING, I REALIZED THAT PYTHON CALCULATIONS WERE NOT GIVING A LAST VALUE EXACTLY EQUAL TO 2*v0/g EVEN THOUGH THE FORMULA I USED SHOULD LEAD TO EQUAL VALUES. IN ORDER TO GET THE LAST POINT, I SET THE LIMIT TO ONE MORE STEP.