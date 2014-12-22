def selection_sort(input_list): # {{{
    '''
    Given a list of numbers, returns them in sorted order
    '''
    
    if not isinstance(input_list, list):
	raise Exception('Input is not a valid list')

    for index in range(len(input_list)):
	min_index = index
	for current_index in range(index, len(input_list)):
	    if input_list[current_index] < input_list[min_index]:
		min_index = current_index
	
	print index, min_index
	
	if not min_index == index:
	    input_list[index], input_list[min_index] = input_list[min_index], input_list[index]
    
    return input_list
# }}}


if __name__ == "__main__":
    def get_input_list(): # {{{
	'''
	Get the list of numbers as a list
	'''
	import sys, ast
	input_list = []
	for i in range(1, len(sys.argv)):
	    try:
		num_val = ast.literal_eval(sys.argv[i])
		input_list.append(ast.literal_eval(sys.argv[i]))
	    except Exception as e:
		print 'EXCEPTION:', sys.argv[i], ' is not a number.'
		return
	return input_list
    # }}}
    
    input_list = get_input_list()
    if input_list:
        print selection_sort(input_list)
