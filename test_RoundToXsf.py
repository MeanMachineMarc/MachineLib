import pytest
import MachineLib

def test_negative_frac1():
    assert MachineLib.round_xsf('-3254,12.2345',1) == -270

def test_negative_frac2():
    assert MachineLib.round_xsf('0.034,-12',2) == -0.0028

def test_positive_frac1():
    assert MachineLib.round_xsf('-3254,-12.2345',3) == 266

def test_positive_frac2():
    assert MachineLib.round_xsf('0.034,12',4) == 0.002833

def test_positive_integer1():
    assert MachineLib.round_xsf(3,1) == 3

def test_positive_integer2():
    assert MachineLib.round_xsf(3336,3) == 3340

def test_negative_integer1():
    assert MachineLib.round_xsf(-3,1) == -3

def test_negative_integer2():
    assert MachineLib.round_xsf(-3336,2) == -3300

def test_negative_float():
    assert MachineLib.round_xsf(-3.3356,4) == -3.336

def test_positive_float():
    assert MachineLib.round_xsf(3.3356,1) == 3

def test_zero():
    assert MachineLib.round_xsf(0,1) == 0

def test_positive_many_dp():
    assert MachineLib.round_xsf(0.006356,3) == 0.00636

def test_negative_many_dp():
    assert MachineLib.round_xsf(-0.006356,1) == -0.006

def test_negative_float2():
    assert MachineLib.round_xsf(-33.36,1) == -30

def test_positive_float2():
    assert MachineLib.round_xsf(33.36,2) == 33

def test_string_input_fail():
    with pytest.raises(Exception) as e_info:
         MachineLib.round_xsf('egged') == -33.4

def test_empty_string_fail():
    with pytest.raises(Exception) as e_info:
         MachineLib.round_xsf('') == -33.4

def test_no_input_fail():
    with pytest.raises(Exception) as e_info:
         MachineLib.round_xsf() == -33.4