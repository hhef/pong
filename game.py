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

window.mainloop()