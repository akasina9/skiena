from utilities import process_input

def insertion_sort(input_list): # {{{
    '''
    Given an input list, sorts the array and returns it.
    '''

    if not isinstance(input_list, list):
	raise Exception("Input is not a valid list")

    for i in range(len(input_list)): # {{{
	j = i
	while (j > 0 and input_list[j] < input_list[j-1]):
	    input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
	    j = j - 1
    # }}}

    return input_list
# }}}


if __name__ == "__main__":
    input_list = process_input.get_numeric_list()
    if input_list:
        print insertion_sort(input_list)
