def silnia(liczba):
    silnia = 1
    for i in range(1, liczba + 1):
        silnia = silnia * i
    return silnia

def test_answer():
    assert silnia(5) == 120
