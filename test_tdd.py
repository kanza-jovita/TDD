from tdd import multiply

# def test_multiply_1_by_1():
#     product = multiply(1,1)
#     assert product == 1

def test_multiply_2_by_2():
    product = multiply(2,2)
    assert product == 4

def test_multiply_3_by_3():
    product = multiply(3,3)
    assert product == 9

def test_multiply_4_by_4():
    product = multiply(4,4)
    assert product == 16

def test_multiply_23_by_45():
    product = multiply(23,45)
    assert product == 1035
