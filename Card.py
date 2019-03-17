'''
Created on 2019-03-17
@author: rishika1444
'''

class Card:
    '''
    This class is the parking card
    '''
    __cardId = 0
    __levelId = 0
    __spaceId = 0

    def __init__(self, cardId, levelId, spaceId):
        '''
        Constructor
        '''
        self.__cardId = cardId
        self.__levelId = levelId
        self.__spaceId = spaceId

    def getCardId(self):
        '''
        The method to get the card id
        '''
        return self.__cardId
    def getLevelId(self):
        '''
        The method to get the level id
        '''
        return self.__levelId
    def getSpaceId(self):
        '''
        The method to get the space id
        '''
        return self.__spaceId
