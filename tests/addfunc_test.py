from src import addfunc

def test_3and5():
    ans = addfunc.addfunc(3,5)

    assert ans == 8


def test_1and2():
    ans = addfunc.addfunc(1,2)

    assert ans == 3
