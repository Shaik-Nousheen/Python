
n = int(input("enter the row no:" ))

for i in range(n):
	print(' '*(n-i), end='')
	print(' '.join(map(str, str(11**i))))
	
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# map(fun, iter)
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

