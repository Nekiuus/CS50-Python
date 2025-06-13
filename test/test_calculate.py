import pytest
from test.calculate import square
'''
def main():
    test_square()
    '''

def test_positive():
    assert square(2) == 4, "Test failed!"
    assert square(3) == 9, "Test failed!"

def test_negative():
    assert square(-2) == 4, "Test failed!"
    assert square(-3) == 9, "Test failed!"

def test_zero():
    assert square(0) == 0, "Test failed!"

def test_string():
    with pytest.raises(TypeError):
        square("cat")



    '''
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed! 2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed! 3 squared is not 9")

    '''

    '''
    if square(2) != 4:
        print("Test failed!")
    if square(3) != 9: 
        print("Test failed!")
    '''
'''
if __name__ == "__main__":
    main()
    '''