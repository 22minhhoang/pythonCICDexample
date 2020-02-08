from src import addfunc

def test_3and5():
    ans = addfunc.addfunc(3,5)

    assert ans == 8
