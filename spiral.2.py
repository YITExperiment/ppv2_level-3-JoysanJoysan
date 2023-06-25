Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: C:\Users\PC\Downloads\KALEIDO-SPIRAL.PY ===============
Traceback (most recent call last):
  File "C:\Users\PC\Downloads\KALEIDO-SPIRAL.PY", line 15, in <module>
    draw_circle(30)
  File "C:\Users\PC\Downloads\KALEIDO-SPIRAL.PY", line 10, in draw_circle
    draw_circle(size+5)
  File "C:\Users\PC\Downloads\KALEIDO-SPIRAL.PY", line 10, in draw_circle
    draw_circle(size+5)
  File "C:\Users\PC\Downloads\KALEIDO-SPIRAL.PY", line 10, in draw_circle
    draw_circle(size+5)
  File "C:\Users\PC\Downloads\KALEIDO-SPIRAL.PY", line 9, in draw_circle
    turtle.circle(size)
  File "<string>", line 8, in circle
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1991, in circle
    self.speed(speed)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2460, in pen
    self._update()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
