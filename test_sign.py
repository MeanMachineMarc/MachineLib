import MachineLib

def test_positive():
    assert MachineLib.sign(3)==1

def test_negative():
    assert MachineLib.sign(-3)==-1

def test_zero():
    assert MachineLib.sign(0)==0