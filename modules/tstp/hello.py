def say_my_name(name):
  print("Hello, {}".format(name))
  ask_something(name)

def ask_something(name):
  answer = input("{}, Would you like to drink coffee?\n".format(name))
  take_answer(answer)

def take_answer(answer):
  if int(answer) >= 1:
    print("Very well, here is your coffee.")
  else:
    print("Then go fuck off!")
