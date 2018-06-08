
Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966. You can find more information [here](https://docs.python.org/3/library/turtle.html). With the following lines, you can create this star from the example. 

<center><img src="https://raw.githubusercontent.com/qingkaikong/blog/master/2018_27_Turle_graphics/figures/figure_0.jpg" height="400" /> </center>

```python
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
```

With some changes, we could make this nice figure, it is really cool to see how it draws this beautiful pattern. 

<center><img src="https://raw.githubusercontent.com/qingkaikong/blog/master/2018_27_Turle_graphics/figures/figure_1.jpg" height="400" /> </center>


```python
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue']
p = Pen()
p.speed(0)
bgcolor('black')
begin_fill()
for i in range(360):
    p.pencolor(colors[i%6])
    p.width(i/100+1)
    p.forward(i)
    p.left(59)
end_fill()
done()
```
