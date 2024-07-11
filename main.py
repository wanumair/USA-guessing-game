import turtle
from typing import List, Any

import pandas
import pandas as pd



screen = turtle.Screen()
screen.title("Guess the states")
image = "blank_states_img.gif"
screen.addshape(image)
score = 0

turtle.shape(image)


#check answer
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{score}/{len(all_states)} States Correct:",
                                    prompt="What's another state name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_state = all_states
        for state in all_states:
            missing_state.remove(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        score += 1
        screen.update()

