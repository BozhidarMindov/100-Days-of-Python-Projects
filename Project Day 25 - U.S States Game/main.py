from turtle import Turtle, Screen
import turtle
import pandas

#creating a screen
screen = Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")

#setting background image
turtle.shape("blank_states_img.gif")

#opening file
data = pandas.read_csv("50_states.csv")
guessed_states = []

#prompting the user to guess a state
while len(guessed_states) < 50:
    answer = screen.textinput(title = f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    data = pandas.read_csv("50_states.csv")
    states = data.state.to_list()

    #if the user types "exit" the loop stops and the remaining states are shown on screen
    if answer == "Exit":
        screen.tracer(0)
        states_left = []
        for state in states:
            if state not in guessed_states:
                states_left.append(state)
                t = turtle.Turtle()
                t.hideturtle()
                t.color("red")
                t.penup()

                state_data = data[data.state == state]
                t.goto(int(state_data.x), int(state_data.y))
                t.write(state_data.state.item())
        
        #the states that weren't guessed are placed into a separate csv file
        new_data = pandas.DataFrame(states_left)
        new_data.to_csv("states_to_learn.csv")

        break
    
    #populating our guessed_states list
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
    

screen.exitonclick()