import pytest
@pytest.mark.xfail
def test_skip():
    print("Hai")
    x=5
    y=6
    assert x==y
@pytest.mark.regression
def test_sample():
    print("Hello")
    assert 1+1==2
@pytest.mark.skipif()
def test_sample2():
    print("python")
    x="aa"
    y="aa"
    assert x==y #or x.__eq__(y)
    #assert x in y
   #assert x<y or assert x>y 
@pytest.mark.xfail
def test_sample3():
    print("Hiii")

#parameterization
@pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
def test_parameter(test_input,expected):
    assert test_input+2==expected