import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
liste_states = states_data["state"].to_list()
game_is_on = True

guessed_states = []

while game_is_on:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = [i for i in liste_states if i not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            game_is_on = False
        elif answer_state in liste_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.speed("fastest")
            new_states_data = states_data[states_data.state == answer_state]
            t.goto(int(new_states_data.x), int(new_states_data.y))
            t.write(answer_state, font=("normal", 9, "normal"))


