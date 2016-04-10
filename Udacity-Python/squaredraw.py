import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    jim = turtle.Turtle()
    jim.hideturtle()
    jim.color("blue")
    jim.speed(100)
    for i in range (1,50):
        draw_square(jim)
        jim.right(1)
    window.exitonclick()


draw_art() 
    
                
