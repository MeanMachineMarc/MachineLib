import sign

def test_positive():
    assert sign.sign(3)==1

def test_negative():
    assert sign.sign(-3)==-1

def test_zero():
    assert sign.sign(0)==0