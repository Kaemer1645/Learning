#const
import random as rd
min_value = 0
max_value = 100

NUMBER = rd.randint(min_value,max_value)

class Guesser_game:
    def correct(self, win):
        return print('Thanks you for the game, your number is: ' + str(win))

    def guesser(self, number = NUMBER):
        while True:
            print('Your number is %s ?' % str(number))
            Ans = input()
            if Ans == 'yes':
                self.correct(number)
                break
            else:
                print('Is your number is higher or lower?')
                Ans = input()
                if Ans == 'higher':
                    number += rd.randint(1,4)
                else:
                    number -= rd.randint(1,4)





def run():
    instance = Guesser_game()
    instance.guesser()
if __name__ == '__main__':
    run()




'''#binary search

my_list = [-10, 1, 2, 6, 7, 12, 21]
target = 20
guess = 0
while not (len(my_list) == 1 or guess == target):
  center_index = int(len(my_list) / 2)
  guess = my_list[center_index]
  if guess > target:
    my_list = my_list[:center_index]
  elif guess < target:
    my_list = my_list[center_index:]
    print(my_list)
if guess == target:
  print("Found target! Guess = " + str(guess))
else:
  print("Target not found. Last guess = " + str(guess))'''