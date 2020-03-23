# Proxima
Intentional Programming Language (Where u just specify the intention of the program)

[![Under Construction](https://img.shields.io/badge/Status-UnderConstruction-yellow.svg)]()

### Example

##### Hello World
```
Code :- 
print "Hello World"

Output:-
	> Hello World
```

##### To numbers 1 to 10
```
Code :- 

print 1 to 10

Output:-
	> [1,2,3,4,5,6,7,8,9,10]
```


##### Defining A new operator C to find nCr
```
Code :- 

# Operator Definition

operator C: # Defining an operator named "C"
	n = left # Assign value of left Operand to n
	r = right # Assign value of right Operand to r
	return n!/((n-r)!*r!) # Return Calculated Value

# Operator Call

print 5 C 2 

Output:-
	> 10
```

##### [See a small tutorial code](examples/tutorial.pox)


### Installation & Usage

```
git clone This Repository
cd Proxima
python proxima.py /path/to/file/filename.pox 
```
