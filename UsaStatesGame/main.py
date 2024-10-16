import turtle
import pandas
from text import Text

screen = turtle.Screen()
screen.screensize(800, 600)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
states_done = []

game_is_on = True
while game_is_on:
    answer = screen.textinput(f"States Game {len(states_done)}/50",
                              "Write the name of a state:\n Write 'exit' to give up.").title()
    if answer == "Exit":
        break
    if answer in all_states:
        state = data[data["state"] == answer]
        x_cor = state.x.item()
        y_cor = state.y.item()
        text = Text(x_cor, y_cor, answer, "black")
        if answer not in states_done:
            states_done.append(answer)
    if len(states_done) == 50:
        text.game_over()
        game_is_on = False

for state_name in all_states:
    if state_name not in states_done:
        state = data[data["state"] == state_name]
        x_cor = state.x.item()
        y_cor = state.y.item()
        text = Text(x_cor, y_cor, state.state.item(), "red")

states_missed = [name for name in all_states if name not in states_done]
csv_data = pandas.DataFrame(states_missed)
csv_data.to_csv("States_missed.csv")

screen.exitonclick()
