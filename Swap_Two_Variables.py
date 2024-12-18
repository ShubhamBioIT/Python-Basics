#soln1 : Using temporary variable (3rd variable)

'''
LOGIC 
let,
X = 13
Y = 12

temp = X (13)   .......(#Used to store X value in diff variable)
X = Y (12)
Y = temp (13)

congrats your X & Y Values got swapped 
'''

#CODE 

X = int(input("X: "))
Y = int(input("Y: "))

Temp = X 
#print("The value of temp is", X)

X = Y 
print("The value of X is", X)

Y = Temp
print("The value of Y is", Y)


#Soln2 : Without using 3rd variable 

P = int(input("P: "))
Q = int(input("Q: "))

P,Q = Q,P      #MAIN SOLUTION

print("The value of P is", P)
print("The value of Q is", Q)