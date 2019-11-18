import turtle

boarder_x = 420
boarder_y = 250

score_a = 0
score_b = 0

paddle_move = 4

ball_move_x = 0.2
ball_move_y = 0.2

paddle_height = 10
paddle_width = 10

# Screen
window = turtle.Screen()
window.title("Pong")
window.bgcolor("orange")
window.setup(width=1000, height=800)
window.tracer(0)

# Playing field
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

# Score
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("black")
score.hideturtle()


def write_score():
    score.clear()
    score.goto(-boarder_x + 100, boarder_y + 20)
    score.write(f"{score_a}", align="center", font=("Arial", 50, "bold"))
    score.goto(boarder_x - 100, boarder_y + 20)
    score.write(f"{score_b}", align="center", font=("Arial", 50, "bold"))


# Paddles move up and down
def left_paddle_move_up():
    move = left_paddle.ycor()
    move += paddle_move
    left_paddle.sety(move)


def left_paddle_move_down():
    move = left_paddle.ycor()
    move -= paddle_move
    left_paddle.sety(move)


def right_paddle_move_up():
    move = right_paddle.ycor()
    move += paddle_move
    right_paddle.sety(move)


def right_paddle_move_down():
    move = right_paddle.ycor()
    move -= paddle_move
    right_paddle.sety(move)


window.listen()
window.onkeyrelease(left_paddle_move_up, "w")
window.onkeyrelease(left_paddle_move_down, "s")
window.onkeyrelease(right_paddle_move_up, "Up")
window.onkeyrelease(right_paddle_move_down, "Down")

write_score()
while True:
    window.update()
    ball.setx(ball.xcor() + ball_move_x)
    ball.sety(ball.ycor() + ball_move_y)

    # Ball hits top and bot boarders + misses paddles
    if ball.ycor() > boarder_y - 10:
        ball_move_y *= -1
    elif ball.ycor() < -boarder_y + 10:
        ball_move_y *= -1
    elif ball.xcor() > boarder_x - 10:
        ball.goto(0, 0)
        ball_move_x *= -1
        score_a += 1
        write_score()
    elif ball.xcor() < - boarder_x + 10:
        ball.goto(0, 0)
        ball_move_x *= -1
        score_b += 1
        write_score()

    # Ball hits paddles
    if ball.xcor() < -385 and left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50:
        ball.setx(-385)
        ball_move_x *= -1
    elif ball.xcor() > 385 and right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50:
        ball.setx(385)
        ball_move_x *= -1

    # Paddles hit boarder
    if left_paddle.ycor() + 50 > boarder_y:
        left_paddle.sety(boarder_y - 50)
    elif right_paddle.ycor() + 50 > boarder_y:
        right_paddle.sety(boarder_y - 50)
    elif left_paddle.ycor() - 50 < - boarder_y:
        left_paddle.sety(-boarder_y + 50)
    elif right_paddle.ycor() - 50 < - boarder_y:
        right_paddle.sety(-boarder_y + 50)
