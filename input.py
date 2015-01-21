import turtle
t=turtle.Turtle()
t.speed(1)
t.shape('turtle')
for i0 in range(0
,2
,1
) :
		for i1 in range(0
,2
,1
) :
		t.pencolor("BLUE")
		size=i1
		t.forward(size)
		t.right(90)
		t.forward(size)
		t.right(90)
		t.forward(size)
		t.right(90)
		t.forward(size)
		t.right(90)
		t.right(size)
		size=90


wn = turtle.Screen()
wn.exitonclick()