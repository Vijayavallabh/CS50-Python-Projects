import numpy as np
import pandas as pd
import random
import warnings
warnings.filterwarnings('ignore')
last_1 = 0
last_2 = 0

scores = [0, 0]
def main():
  reset()
  valid_entries = ['0', '1']
  while True:
    predicted = prediction()
    player_input = input("\nEnter either 1 or 0: ")

    while player_input not in valid_entries:
      print("\nInvalid Input!")
      player_input = input("Please enter either 1 or 0: ")

    player_input = int(player_input)
    update_inputs(player_input)
    update_scores(predicted, player_input)

    if scores[0] == 10:
      print("\nBad Luck, Computer Wins!\n")
      break

    elif scores[1] == 10:
      print("\nCongrats, You Won!\n")
      break

inputs = np.zeros(shape=(2, 2, 2), dtype=int)

def update_inputs(current):
  global last_1, last_2
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0
    inputs[last_2][last_1][0] = current

  last_2 = last_1
  last_1 = current

def prediction():
  if inputs[last_2][last_1][1] == 1:
    predict = inputs[last_2][last_1][0]
  else:
    predict = random.randint(0, 1)
  return predict

def update_scores(predicted, player_input):
  if predicted == player_input:
    scores[0] = scores[0] + 1
    print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1])

  else:
    scores[1] = scores[1] + 1
    print("\nComputer Score:", scores[0], "\nPlayer Score:", scores[1])

def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k] = 0

  for i in range(2):
    scores[i] = 0


if __name__ == "__main__":
    main()
