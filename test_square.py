from square import square_num

# All the test functions will run despite if one function fails

def test_square_num():
    a = 4
    result = square_num(a)
    assert result == 16

# will not collect this function
# Also can be used as helper function for test function
# def random_fn():
#     return None

# will collect this function and raise an error
# def test_fail():
#     assert 2 == 3

