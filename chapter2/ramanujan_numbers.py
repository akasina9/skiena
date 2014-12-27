# from utilities import process_input


def get_number(): # {{{
    '''
    Get a number as input from command line
    '''

    import sys, ast

    try:
	num_value = ast.literal_eval(sys.argv[1])
	return num_value
    except Exception, e:
	print "EXCEPTION:", e
	return
# }}}


def get_ramanujan_numbers(max_value): # {{{
    '''
    Given a number this will return all 5-tuples (a, b, c, d, e) 
    such that a^3 + b^3 = c^3 + d^3 = e
    '''

    ramanujan_numbers 	= []
    cube_dict 		= {}

    for i in range(input_number**3):
	cube_dict[i] 	= False

    for i in range(input_number):
	cube_dict[i**3] = i

    for a in range(input_number):
	for b in range(a, input_number):
	    for c in range(a, input_number):
		if a != b and a != c and b != c:
		    d = a**3 + b**3 - c**3

		    if a != d and b != d and c != d and d < input_number**3 and d >= c**3:
			if cube_dict[d] != False:
			    ramanujan_numbers.append((a, b, c, cube_dict[d], a**3 + b**3))
    
    return ramanujan_numbers
# }}}


if  __name__ == "__main__":
    input_number 	= get_number()
    ramanujan_numbers 	= get_ramanujan_numbers(input_number)

    print "************************RAMANUJAN NUMBERS******************************"
    for number in ramanujan_numbers:
	print number
