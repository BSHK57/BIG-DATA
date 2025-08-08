import sys
def h1(x):
    return (2*x+10)%300
def h2(x):
    return (10*(5*x+30))%300
def h3(x):
    return (x+4)%300

## Bloom Filter Algorithm

def bloom_filter(x,n,hash_functions):
    bit_array = [0] * (n)
    collisions = 0
    for val in x:
        for func in hash_functions:
            v = func(val)
            if not bit_array[v]:
                bit_array[v] = 1
            else :
                collisions += 1
    return bit_array,collisions

## Calculating Error Rate for all Cases
import math
def Cal_error(k,x,y):
	"""	k is the number of hash functions.
		x is the number of elements added to the filter.
		y is the number of bits in the bit array."""
	x = x + 0.0
	return (1 - math.exp(-k*y/x))**k


hash_functions = [h1,h2,h3]
elements = []
for i in sys.stdin:
	elements.append(int(i))
n = 300
bit_array,collisions = bloom_filter(elements,n,hash_functions)
print("********* Bloom Filter Results *********")
print("Bit Array  :"+" ".join(list(map(str,bit_array))))
print("No. of ones :" + str(bit_array.count(1)))
print("No. of Collisions :"+str(collisions))


x = len(elements)
y = n
print("********* Error Rate Results for all Cases *********")
for i in range(1,len(hash_functions)+1):
    print("The Error Rate for h = "+str(i)+" : " + str(Cal_error(i,x,y)))



