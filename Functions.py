"""
# Fonseca e Fleming
varmin = [-4, -4,-4]
varmax = [4,4,4]
nvar = 3

def function1(x):
    return 1-np.exp(-(x[0]-1/np.sqrt(3))**2-(x[1]-1/np.sqrt(3))**2-(x[2]-1/np.sqrt(3))**2)

def function2(x):
    return 1 - np.exp(-(x[0] + 1 / np.sqrt(3)) ** 2 - (x[1] + 1 / np.sqrt(3)) ** 2 - (x[2] + 1 / np.sqrt(3)) ** 2)
"""

"""
# Poloni's two objective function

varmin = [-np.pi,-np.pi]
varmax = [np.pi,np.pi]
nvar = 2

def function1(x):
    A1 = 0.5*np.sin(1)-2*np.cos(1)+np.sin(2)-1.5*np.cos(2)
    A2 = 1.5*np.sin(1) - np.cos(1)+2*np.sin(2)-0.5*np.cos(2)
    B1 = 0.5*np.sin(x[0])-2*np.cos(x[0])+np.sin(x[1])-1.5*np.cos(x[1])
    B2 = 1.5*np.sin(x[0])-np.cos(x[0])+2*np.sin(x[1])-0.5*np.cos(x[1])
    return 1+(A1-B1)**2+(A2-B2)**2

def function2(x):
    return (x[0]+3)**2+(x[1]+1)**2
"""

"""
varmin = [0.1,0]
varmax = [1,5]
nvar = 2

def function1(x):
    return x[0]

def function2(x):
    return (1+x[1])/x[0]
"""

"""
# Zitzler–Deb–Thiele's function N. 3
varmin = [0,0]
varmax = [1,1]
nvar = 2

def function1(x):
    return x[0]
    
def function2(x):
    return 1-np.sqrt(x[0]/(1+(9/29)*x[1]))-(x[0]/(1+(9/29)*x[1]))*np.sin(10*np.pi*x[0])

"""
"""
#Karsawe function
varmin = [-5,-5,-5]
varmax = [5,5,5]
nvar = 3

def function1(x):
    return -10*np.exp(-0.2*np.sqrt(x[0]**2+x[1]**2))-10*np.exp(-0.2*np.sqrt(x[1]**2+x[2]**2))

def function2(x):
    return abs(x[0])**0.8+5*np.sin(x[0]**3)+abs(x[1])**0.8+5*np.sin(x[1]**3)+abs(x[2])**0.8+5*np.sin(x[2]**3)
"""


"""
#Schaffer function N1
varmin = [-10]
varmax = [10]
nvar = 1

def function1(x):
    return x[0]**2

def function2(x):
    return (x[0]-2)**2
"""

"""
#Schaffer function N1
varmin = [-5]
varmax = [10]
nvar = 1

def function1(x):
    if x<=1:
        return -x
    if 1<x<=3:
        return x-2
    if 3<x<=4:
        return 4-x
    if x>4:
        return x-4

def function2(x):
    return (x-5)**2
"""
