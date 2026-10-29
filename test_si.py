from si import simple_interest

def test_simple_interest():
    assert simple_interest(8000, 6, 8) == 3840

def test_simple_interest_zero():
    assert simple_interest(10000, 0, 12) == 0