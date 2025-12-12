import sys
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mult, div, log, square, sin, sqrt, percentage

def test_add1():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add3():
    assert add(6,5) == 11



def test_sub1():
    assert sub(5, 6) == -1

def test_sub2():
    assert sub(5,6) != 0

def test_sub3():
    assert sub(5, 5) == 0

def test_sub4():
    assert sub(6,5) == 1



def test_mult1():
    assert mult(5,6) == 30

def test_mult2():
    assert mult(5,6) != 35

def test_mult3():
    assert mult(6,5) == 30

def test_mult4():
    assert mult(1,5) == 5

def test_mult5():
    assert mult(5,1) == 5

def test_mult6():
    assert mult(0,5) == 0

def test_mult7():
    assert mult(5,0) == 0



def test_div1():
    assert div(30, 5) == 6 

def test_div2():
    assert div(5, 30) != 6

def test_div3():
    assert div(5, 2) == 2.5

def test_div4():
    assert div(5, 1) == 5

def test_div5():
    assert div(5, 0) == "undef"

def test_div6():
    assert div(0, 5) == 0



def test_log1():
    assert log(0, 10) == "undef"

def test_log2():
    assert log(-2, 10) == "undef"

def test_log3():
    assert log(10, 0) == "undef"

def test_log4():
    assert log(10, -2) == "undef"

def test_log5():
    assert log(1, 19) == "undef"

def test_log6():
    assert log(10, 1) == 0

def test_log7():
    assert log(2, 8) == 3

def test_log8():
    assert log(2, 8) != 9



def test_square1():
    assert square(0) == 0

def test_square2():
    assert square(1) == 1

def test_square3():
    assert square(2) == 4

def test_square4():
    assert square(-2) == 4

def test_square5():
    assert square(0.5) == 0.25



def test_sin1():
    assert sin(0) == 0

def test_sin2():
    result = sin(2 * math.pi) 
    assert result < 0.0001 and result > -0.0001

def test_sin3():
    result = sin(math.pi)
    assert result < 0.0001 and result > -0.0001  

def test_sin4():
    result = sin(math.pi/2)
    assert result < 1.0001 and result > 0.9999

def test_sin5():
    result = sin(-2 * math.pi) 
    assert result < 0.0001 and result > -0.0001

def test_sin6():
    result = sin(-1 * math.pi)
    assert result < 0.0001 and result > -0.0001

def test_sin7():
    result = sin(-1 *math.pi/2)
    assert result > -1.0001 and result < -0.9999



def test_sqrt1():
    assert sqrt(0) == 0

def test_sqrt2():
    assert sqrt(1) == 1

def test_sqrt3():
    assert sqrt(-2) == "undef"

def test_sqrt4():
    assert sqrt(4) == 2



def test_percentage1():
    assert percentage(0.5) == 50

def test_percentage2():
    assert percentage(0) == 0

def test_percentage3():
    assert percentage(1) == 100

def test_percentage4():
    assert percentage(-1) == -100
