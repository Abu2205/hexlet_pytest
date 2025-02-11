def reverse(string):
	"""Reverse string
	
	>>> reverse('This is the course about test on Hexlet sxhool!')
	'!loohxs telxeH no tset tuoba esruoc eht si sihT'

	>>> reverse('I do not understand the task but I will add these results to example.py file!')
	'!elif yp.elpmaxe ot stluser eseht dda lliw I tub ksat eht dnatsrednu ton od I'
	"""	


	return string[::-1]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
