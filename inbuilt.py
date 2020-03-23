from collections import OrderedDict

def add(a,b,env):
	return a[0]+b[0]

def sub(a,b,env):
	if a[0]!=None:
		return a[0]-b[0]
	else:
		return -b[0]
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

def output(a,b,env):
	print(b[0])

def rinput(a,b,env):
	return raw_input(b[0])

def search(a,b,env):
	return a[0] in b[0]

def power(a,b,env):
	return a[0]**b[0]

def colon(a,b,env):
	return None

def retfn(a,b,env):
	env.variables["__return__"]=b[0]

def comma(a,b,env):
	if type(b[0]) == list:
		return a+b[0]
	else:
		return a+b
def fact(a,b,env):
	def factorial(n):
		if n <=1:return 1
		else:return n*factorial(n-1)
	#print(a)
	return factorial(a[0])

def num(a,b,env):
    try:
        return int(b[0])
    except ValueError:
        return float(b[0])

def string(a,b,env):
	return str(b[0])

def boolean(a,b,env):
	return bool(b[0])

def th(a,b,env):
	#print(a,b)
	return b[0][a[0]]

def leng(a,b,env):
	#print(a,b)
	return len(b[0])

operators = OrderedDict()
operators[None]=None
operators[":"]=colon

operators["="]=assign
operators["print"]=output
operators["input"]=rinput
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

operators["st"]=th
operators["nd"]=th
operators["rd"]=th
operators["th"]=th
operators["len"]=leng


operators["+"]=add
operators["-"]=sub
operators["/"]=div
operators["*"]=mul
operators["%"]=mod
operators["!"]=fact
operators["**"]=power

operators["num"]=num
operators["str"]=string
operators["bool"]=boolean
