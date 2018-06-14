# Künstliche Intelligenz - Gruppe 1 [![Build Status](https://travis-ci.com/deep-green/ki1.svg?branch=master)](https://travis-ci.com/deep-green/ki1)

## Benennung der Input-Knoten

| **Figur**| **Weiß**|   **Schwarz**   |
|:-----|:----------:|:-------------------
| Leeres Feld  | 0 | 0 |
| Bauer  | 0,083 | 0,166 |
| Turm | 0,249 | 0,332 |
| Springer | 0,415 | 0,498 |
| Läufer | 0,581 | 0,664 |
| Dame | 0,747 | 0,83 |
| König | 0,913 | 1 |

## Python Unittests & Travis CI
> Wichtig: Dateien mit Tests müssen im Ordner tests/ liegen und mit "test" in Minuskeln beginnen (z.B.: testExample.py oder test_MyTests.py).

### Beispiel Unittest in Python
```python
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
```
> Funktionen in Testklassen müssen mit "test_" beginnen um als Tests erkannt zu werden.
