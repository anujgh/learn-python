import random
def game():
  score = random.randint(1, 62)
  print('your score is : ',score)
  # fetct the highscore
  f =  open(r"chapter9 ps\highscore.txt")
  highscore = f.read()
  if(highscore != ""):
    highscore = int(highscore)
  else:
    highscore = 0
  print('Highscore is : ',highscore)
  f.close()

  # set the highscore in file
  if(highscore < score or highscore == "" ):
    with open(r"chapter9 ps\highscore.txt", "w") as f:
      f.write(str(score))


game()