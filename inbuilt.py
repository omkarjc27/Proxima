from collections import OrderedDict

def add(a,b,env):
	return a[0]+b[0]

def sub(a,b,env):
	return a[0]-b[0]

def mul(a,b,env):
	return a[0]*b[0]

def div(a,b,env):
	return a[0]/b[0]

def mod(a,b,env):
	return a[0]%b[0]

def gr(a,b,env):
	return a[0]>b[0]

def ls(a,b,env):
	return a[0]<b[0]

def ge(a,b,env):
	return a[0]>=b[0]

def le(a,b,env):
	return a[0]<=b[0]

def eq(a,b,env):
	return a[0]==b[0]

def noteq(a,b,env):
	return a[0]!=b[0]

def logor(a,b,env):
	return a[0] or b[0]

def logand(a,b,env):
	return a[0] and b[0]

def lognot(a,b,env):
	return not b[0]

def assign(a,b,env):
	if a[0] in env.variables:
		env.variables[a[0]] = b[0]
		return b
	else:
		raise Exception()
def to(a,b,env):
	return range(a[0],b[0]+1)

def printing(a,b,env):
	print(b[0])

def search(a,b,env):
	return a[0] in b[0]

def power(a,b,env):
	return a[0]**b[0]

def colon(a,b,env):
	return None

def retfn(a,b,env):
	env.variables["__return__"]=b[0]

def comma(a,b,env):
	return a+b

def fact(a,b,env):
	def factorial(n):
		if n <=1:return 1
		else:return n*factorial(n-1)
	#print(a)
	return factorial(a[0])

operators = OrderedDict()
operators[None]=None
operators[":"]=colon

operators["="]=assign
operators["print"]=printing
operators["in"]=search
operators["to"]=to

operators["return"]=retfn

operators[","]=comma
operators["or"]=logor
operators["and"]=logand
operators["not"]=lognot

operators[">="]=ge
operators[">"]=gr
operators["<="]=le
operators["<"]=ls
operators["=="]=eq
operators["!="]=noteq


operators["+"]=add
operators["-"]=sub
operators["/"]=div
operators["*"]=mul
operators["%"]=mod
operators["!"]=fact
operators["**"]=power
operators["to_power"]=power

