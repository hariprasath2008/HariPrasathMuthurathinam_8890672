
import totalAndMean
def test_total():
    # Test adding 5 numbers
    assert totalAndMean.totalofnumbers(1,1,1,1,1) == 5

def test_mean():
    # Test mean of 5 numbers
    assert totalAndMean.mean(totalAndMean.totalofnumbers(1,1,1,1,1),5) == 2