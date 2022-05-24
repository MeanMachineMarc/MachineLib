import MachineLib as L

def test_positive():
    assert L.sign(3)==1

def test_negative():
    assert L.sign(-3)==-1

def test_zero():
    assert L.sign(0)==0