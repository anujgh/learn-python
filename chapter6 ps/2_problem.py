maths = int(input('Maths marks: '))
hindi = int(input('Hindi marks: '))
science = int(input('Science marks: '))

maths_per = (maths / 100) * 100
hindi_per = (hindi / 100) * 100
science_per = (science / 100) * 100
sum = maths + hindi + science
total_per = (sum / 300)*100


if((maths_per >= 33 and hindi_per >= 33 and science_per >= 33) or total_per > 40):
  print('Pass', total_per)
else:
  print('Fail', total_per)