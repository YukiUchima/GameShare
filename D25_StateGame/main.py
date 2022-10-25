import turtle
import pandas as pd

# ------------------------Setup Screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("50 States Game")
img_file = "blank_states_img.gif"
screen.addshape(img_file)
turtle.shape(img_file)
state_tag = turtle.Turtle()
state_tag.penup()
state_tag.hideturtle()


# Function that defines coordinate of click (not necessary, data is available)
# def reveal_coordinates(x,y):
# 	print(f"Coordinate: ({x},{y})")

# turtle.onscreenclick(reveal_coordinates)

# Pull csv into data file using PANDAS
data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()

# Quiz user with input window
guess_states = []
while len(guess_states) < 50:
	userPrompt = "Take a guess for another state: "
	guess = screen.textinput(f"{len(guess_states)}/50 States Correct", userPrompt).title()
	if guess == "Exit":
		missing_states = []
		for state in states_list:
			if state not in guess_states:
				missing_states.append(state)
		practice_list = pd.DataFrame(missing_states)
		practice_list.to_csv("states_to_learn.csv")
		break
	if guess in states_list:
		guess_states.append(guess)
		states_list.remove(guess)
		state_data = data[data.state == guess]
		state_tag.goto(int(state_data.x), int(state_data.y))
		state_tag.write(guess, align="left", font=('Arial', 6, 'bold'))
		# Alternative way of writing the STATE from the state_data -----------------------------------
		# state_tag.write(state_data.state.item())

# states_to_learn.csv
# practice_list = pd.DataFrame(states_list)
# practice_list.to_csv("states_to_learn.csv")




# -------------------------Keep Screen On
# Keep screen ON
screen.mainloop()
# screen.exitonclick()
