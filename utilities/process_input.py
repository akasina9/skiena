def get_numeric_list(): # {{{
    '''
    Get a list of numbers from command line
    '''
    import sys, ast    
    input_list = []

    for i in range(1, len(sys.argv)):
	try:
	    num_value = ast.literal_eval(sys.argv[i])
	    input_list.append(num_value)
	except:
	    print "EXCEPTION:", sys.argv[i], "is not a number."
	    return

    return input_list
# }}}
