import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")

if answer in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer]
    t.goto(state_data.x, state_data.y)
    t.write(state_data.state)


screen.exitonclick()