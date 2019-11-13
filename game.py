import turtle

# Screen
window = turtle.Screen()
window.title("Pong")
window.bgcolor("orange")
window.setup(width=1000, height=800)

# Playing field
boarder_x = 420
boarder_y = 250

playing_field = turtle.Turtle()
playing_field.hideturtle()
playing_field.color("black")
playing_field.speed(5)
playing_field.penup()
playing_field.goto(boarder_x, boarder_y)
playing_field.pendown()
playing_field.goto(boarder_x, -boarder_y)
playing_field.goto(-boarder_x, -boarder_y)
playing_field.goto(-boarder_x, boarder_y)
playing_field.goto(boarder_x, boarder_y)

# Left Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-boarder_x + 15, 0)

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(boarder_x + -15, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0, 0)

window.mainloop()
