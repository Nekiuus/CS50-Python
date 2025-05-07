from test.sayhello import hello

def test_deafult():
    assert hello() == "Hello, World"

def test_string():
    for name in ["Sebas", "Sebastian", "Sebasito"]:
        assert hello(name) == f"Hello, {name}"


    '''
    assert hello("Sebas") == "Hello, Sebas"
    '''
