################################
#  Simple test of the reactive #
#          R Library           #
#           By Phc             #
################################
from r import *
class Test:
	def __init__(self):
		self.run()

	def run(self):
		a = R(1) #Declare reactive variable a
		b = R(2) # Declare reactive variable b
		c = R()  #Initialize empty reactive variable c
		c <= (a, b) #Combine and bind the values of a and b to c
		print "c = %s" % str(c.value) #Show the value of c
		b.set(40) #Update variable b, this affects variable c
		print "c = %s" % str(c.value) #Show updated variable c
		d = R("Hello") #Declare reactive variable d
		e = R(" SIR!") #Declare reactive variable e
		f = R() #Initialize empty reactive variable f
		f <= (d, e) #Combine and bind variables d and e to f
		print "f = %s" % f.value #Show value of f
		e.set(" MAAM!") #Update variable e, this affects f
		print "f = %s" % f.value #Show value of f
		print "c + c = %s" % str(c+c) #Add two reactive variables together
Test()