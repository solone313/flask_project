def test_hello():
    assert hello('JOKER') == 'Hello, JOKER!'


def hello(name):
    return 'Hello, {}!'.format(name)