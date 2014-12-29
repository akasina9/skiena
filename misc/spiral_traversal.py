

def traverse_right(input_array, indices): # {{{
    traversed 	= False
    for i in xrange(indices[3] + 1, indices[1]):
	print input_array [indices[0] + 1] [i]
	traversed = True

    # Increment top_index
    indices[0] 	= indices[0] + 1
    return indices, traversed
# }}}


def traverse_down(input_array, indices): # {{{
    traversed 	= False
    for i in xrange(indices[0] + 1, indices[2]):
	print input_array [i] [indices[1] - 1]
	traversed = True
    
    # Decrement right_index
    indices[1]	= indices[1] - 1
    return indices, traversed
# }}}


def traverse_left(input_array, indices): # {{{
    traversed 	= False
    for i in xrange(indices[1] - 1, indices[3], -1):
	print input_array [indices[2] - 1] [i]
	traversed = True

    # Decrement bottom_index
    indices[2] = indices[2] - 1
    return indices, traversed
# }}}


def traverse_up(input_array, indices): # {{{
    traversed 	= False
    for i in xrange(indices[2] - 1, indices[0], -1):
	print input_array [i] [indices[3] + 1]
	traversed = True

    # Increment left_index
    indices[3] 	= indices[3] + 1
    return indices, traversed
# }}}


def spiral_traversal(input_array): # {{{
    '''
    Given a 2D array traverse in an inward spiral starting from index [0][0]
    '''

    top_index  		= left_index  		= -1
    bottom_index	= len(input_array)
    right_index		= len(input_array[0])
    
    indices = [top_index, right_index, bottom_index, left_index]
    
    traversal_count 	= 0
    traversed = True

    while(traversed): # {{{
	if traversal_count%4 == 0:
	    indices, traversed	= traverse_right(input_array, indices)
	    traversal_count 	= traversal_count + 1
	elif traversal_count % 4 == 1:
	    indices, traversed 	= traverse_down(input_array, indices)
	    traversal_count 	= traversal_count + 1
	elif traversal_count % 4 == 2:
	    indices, traversed 	= traverse_left(input_array, indices)
	    traversal_count 	= traversal_count + 1
	else:
	    indices, traversed 	= traverse_up(input_array, indices)
	    traversal_count 	= traversal_count + 1
    # }}}

    print '-------------------------------------------------------'
# }}}

if __name__ == '__main__':
    input_array 	= [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    spiral_traversal(input_array)

    input_array         = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
    spiral_traversal(input_array)


