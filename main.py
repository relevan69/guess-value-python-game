import os
import random

MIN_VALUE = 0
MAX_VALUE = 20

def game_process():
  while True:
    random_value = random.randint(MIN_VALUE, MAX_VALUE)
    try:
      user_input = input(f"Угадай число от {MIN_VALUE} до {MAX_VALUE}: ")
      os.system("cls || clear")
      if len(user_input) == 0:
        print("Ты ничего не написал! :с")
        continue
      user_value = int(user_input);
      if user_value < MIN_VALUE or user_value > MAX_VALUE:
        print(f"Число загадано в диапазоне от {MIN_VALUE} до {MAX_VALUE}! Будь внимательнее.")
        continue
      if user_value == random_value:
        print("Ты угадал число! Да ты везунчик!! :3")
      else:
        print("А вот и не угадал! Повезет в следующий раз :^")
    except ValueError:
      print("Ты ввел что-то помимо числа!! Так нельзя! >:c")

def main():
  game_process()


main()
