from utilities import process_input

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
	
	if not min_index == index:
	    input_list[index], input_list[min_index] = input_list[min_index], input_list[index]
    
    return input_list
# }}}


if __name__ == "__main__":
    input_list = process_input.get_numeric_list()
    if input_list:
        print selection_sort(input_list)
