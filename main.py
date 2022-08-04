import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.A STATE GAME")

image = "blank_states_img.gif"


screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")

data_list = data["state"].to_list()

guessed_list = []


while len(guessed_list) < 50:



    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Count", prompt="What's another state name? ").title()

    if answer_state == "Exit":
        # missed_states = []
        # for state in data_list:
        #     if state not in guessed_list:
        #         missed_states.append(state)
        missed_states = [word for word in data_list if word not in guessed_list]
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break





    if answer_state in data_list:
        guessed_list.append(answer_state)

        new_human = turtle.Turtle()
        new_human.hideturtle()
        new_human.penup()
        answer_row = data[data["state"] == answer_state]
        answer_value = answer_row["state"]
        x_val = answer_row['x']
        y_val = answer_row['y']
        new_human.goto(int(x_val), int(y_val))
        new_human.write(answer_row["state"].item())














screen.exitonclick()



