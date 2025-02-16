import random
class Train:
  def __init__(self, trainNo, start, to):
    self.trainNo = trainNo
    self.start = start
    self.to = to

  def bookSeat(self):
    print(f"seat is booked in train no {self.trainNo} for {self.start} - {self.to}")

  def status(self):
    print('Traing is running is very fine.')

  def getFare(self):
    print(f"seat is booked in train no {self.trainNo} for {self.start} - {self.to} and fair is {random.randint(222,777)}")


ticket = Train(1234, 'Uti', 'Masoori')
ticket.bookSeat()
ticket.status()
ticket.getFare()