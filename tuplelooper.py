def tuple_looper(current_position, shift, our_tuple):
    """

    :param current_position:
    :param shift:
    :param our_tuple:
    :return:
    >>> tuple_looper(5, 4, (4, 3, 4, 9))
    4
    >>> tuple_looper(1, 2, (1, 2, 3, 4, 5))
    3
    >>> tuple_looper(7, 1, ("bob", "michelle", "jim", "sam", "ali", "rais", "husam"))
    'bob'
    """
    result = 0
    newfound_position = 0
    if current_position >= len(our_tuple):
        result = ((current_position + shift) - len(our_tuple)) % len(our_tuple)
    else:
        result = current_position + shift
    return our_tuple[result - 1]  # TODO Check again with Chris