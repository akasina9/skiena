def swap_in_array(list_name, pos1, pos2):
    '''
    Swaps the two given variables
    '''
    list_name[pos1], list_name[pos2] = list_name[pos2], list_name[pos1]


def insertion_sort(input_list):
    '''
    Given an input list, sorts the array and returns it.
    '''

    if not isinstance(input_list, list):
	raise Exception("Input is not a valid list")

    for i in range(len(input_list)):
	j = i
	while (j > 0 and input_list[j] < input_list[j-1]):
	    swap_in_array(input_list, j, j-1)
	    j = j - 1
    
    return input_list


if __name__ == "__main__":
    def get_input_list():
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
    
    
    input_list = get_input_list()
    if input_list:
        print insertion_sort(input_list)
