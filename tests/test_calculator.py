from app.calculator import add,subtract

...
 from app -> folder
calculator -> FileName
import add,subtract (functions)
...

def test_add():
  assert add(2,3) ==5

def test_subtract():
  assert subtract(5,3) ==2
