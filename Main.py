'''
Created on 2019-03-17
@author: rishika1444
'''
from ParkingLot import ParkingLot

parkingLot = ParkingLot()

carsCount = int(raw_input("input the count of the cars waiting to park:"))
usedCards = []
while parkingLot.allowToPark() and carsCount > 0:
    card = parkingLot.parkTheCar()
    usedCards.append(card)
    carsCount -= 1
else:
    print "the parking lot is full, the cars after NO." + parkingLot.getTotalSpaceCount() + " shall be waiting for empty space."

parkingLot.showParkingStatus()
print str(parkingLot.getTotalEmptySpaceCount()) + " empty spaces left"

for card in usedCards:
    parkingLot.leaveTheCar(card)
print str(parkingLot.getTotalEmptySpaceCount()) + " empty spaces left after all the cards returned"
