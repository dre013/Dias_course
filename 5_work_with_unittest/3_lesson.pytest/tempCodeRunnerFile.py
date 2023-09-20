@pytest.mark.one
def test_equal():
    assert 1 == 1, 'Good'


@pytest.mark.two
def test_notEqual():
    assert 1 == 2, 'Good'


def square():
    n = 2
    assert n*n == 4