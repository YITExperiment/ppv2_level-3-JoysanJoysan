Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================================================== RESTART: C:\Users\PC\Desktop\KALEIDO-SPIRAL.PY =========================================================
Traceback (most recent call last):
  File "C:\Users\PC\Desktop\KALEIDO-SPIRAL.PY", line 17, in <module>
    draw_circle(30,0,1)
  File "C:\Users\PC\Desktop\KALEIDO-SPIRAL.PY", line 12, in draw_circle
    draw_circle(size+5, angle-20,shift-10)
  File "C:\Users\PC\Desktop\KALEIDO-SPIRAL.PY", line 12, in draw_circle
    draw_circle(size+5, angle-20,shift-10)
  File "C:\Users\PC\Desktop\KALEIDO-SPIRAL.PY", line 12, in draw_circle
    draw_circle(size+5, angle-20,shift-10)
  [Previous line repeated 14 more times]
  File "C:\Users\PC\Desktop\KALEIDO-SPIRAL.PY", line 9, in draw_circle
    turtle.circle(size)
  File "<string>", line 8, in circle
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1994, in circle
    self._rotate(w)
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 3295, in _rotate
    self._update()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2661, in _update
    self._update_data()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 2647, in _update_data
    self.screen._incrementudc()
  File "C:\Users\PC\AppData\Local\Programs\Python\Python311\Lib\turtle.py", line 1293, in _incrementudc
    raise Terminator
turtle.Terminator
