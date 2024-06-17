import pytest
from main import sum, rest, mult, div #es_mayor_que, login

def test_sum1():
    assert sum(2,5)== 7
    print("La funcion sum trabaja correctamente")
    
def test_sum1():
    assert sum(10,5)== 15
    print("La funcion sum trabaja correctamente")
    
def test_rest1():
    assert rest(-5,3)== -8
    print("La funcion rest trabaja correctamente")
    
def test_rest1():
    assert rest(-13,5)== -18
    print("La funcion rest trabaja correctamente")
    
def test_mult1():
    assert mult(-3,5)== -15
    print("la funcion mult trabaja correctamente")
    
def test_mult1():
    assert mult(6,8)== 48
    print("la funcion mult trabaja correctamente")
    
def test_div1():
    assert div(15,3)== 5
    print("la funcion mult trabaja correctamente")
    
def test_div1():
    assert div(100,4)== 25
    print("la funcion mult trabaja correctamente")
    
#def test_es_mayor_que():
    #assert es_mayor_que(10,2)
    #print("La funcion es mayor que trabaja correctamente")
    
#@pytest.mark.parametrize(
    #"input_x,input_y,esperado",
    #[
        #(-2,-5,-7),
        #(5,sum(2,-1),6),
        #(sum(-2,-4),-8,-14)
    #]
#)

#def test_sum_params(input_x, input_y, esperado):
    #assert sum(input_x, input_y)==esperado
    #print("las funciones parametrizadas trabajan correctamente")
    
#def test_login_pass():
    #login_passes = login("Metodologias" ,"710011C")
    #assert login_passes
    
#def test_login_fail():
    #login_fail = login("Metodologia" ,"710012C")
    #assert not login_fail