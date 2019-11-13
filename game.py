import turtle

# Screen
window = turtle.Screen()
window.title("Pong")
window.bgcolor("orange")
window.setup(width=1000, height=800)
window.tracer(0)

while True:
    window.update()