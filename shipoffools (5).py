import random

class Die:
    """ 
    The class Die generates a random value.
    The roll() method assigns a random value between 1 to 6.
    """

    def __init__(self) -> None :
        self.roll()
    
    def  roll(self) -> None :
        """ The class method roll() generates a random value."""
        
        self._value = random.randint(1,6)
    
    def get_value(self) -> int :
        """ The class method get_value() returns the value of the 
        Die of type int."""
        
        return self._value


class DiceCup:
    """
    Handles five objects (dice) of class Die. 
    Has the ability to bank and release dice individually.  
    Can also roll dice that are not banked.
    """

    def __init__(self,v: int) -> None :
        self._dices = []  # type: List[int]
        self._bankeddice = [False,False,False,False,False]
        
        for i in range(v):
            self._dices.append(Die())
    
    
    def roll(self) -> None :
        """ This method rolls the dices that are unbanked. """
        
        for i in range(0,5):
            if self._bankeddice[i] == False:
                self._dices[i].roll()
    
    
    def value(self,index: int) -> int :
        """ This method returns the value for the given 
        dice index of type int. """
        
        return self._dices[index].get_value()
    
    
    def bank(self,index: int) -> None :
        """ The method bank() banks the die for the given index."""  
        self._bankeddice[index] = True
    
    
    def is_banked(self,index: int) -> bool:
        """ This method checks for the given index whether the die 
        is banked or not.It returns a boolean value."""
        
        if self._bankeddice[index] == True :
            return True
        else:
            return False
    
    
    def release(self,index: int) -> None:
        """ This method checks for the given index and releases the 
        die which are not banked. """
        self._bankeddice[index] == False
    
    
    def release_all(self) -> None :
        """ This method releases all the dice. """
        self._bankeddice = [False,False,False,False,False]


class ShipOfFoolsGame:
    """
    Responsible for the game logic and has the ability to play 
    a round of the game resulting in a score. Also has a property 
    that tells what accumulated score results in a winning state, 
    for example 21.
    """
    
    def __init__(self) -> None :
        self.winningscore = 21
        self._cup = DiceCup(5)
    
    
    def round(self) -> int:
        """
        The method round() has the ability to play a round for 
        each player in the game.
        It returns a value of type int.
        """

        self._cup.release_all()
        has_ship = False
        has_captain = False
        has_crew = False
        
        # This will be the sum of the remaining dice, i.e., the score.
        crew = 0  
        self._cup.roll()
        
        # Repeat three times
        for chance in range(3):
            dievalues = []  # Dummy list which stores die values.
            
            for p in range(5):
                dievalues.append(self._cup._dices[p].get_value())
            print(dievalues)
            
            if not (has_ship) and (6 in dievalues):
                x=dievalues.index(6)
                self._cup.bank(x)
                has_ship = True
            
            else:
                
                if has_ship:
                    pass
                else:
                    self._cup.roll()
            
            if (has_ship) and not (has_captain) and (5 in dievalues):
            # A ship but not a captain is banked
                y = dievalues.index(5)
                self._cup.bank(y)
                has_captain = True
            
            else:
                if has_captain:
                    pass
                else:
                    self._cup.roll()
            
            if has_captain and not has_crew and (4 in dievalues):
            # A ship and captain but not a crew is banked
                z = dievalues.index(4)
                self._cup.bank(z)
                has_crew = True
            
            else:
                if has_crew:
                    pass
                else:
                    self._cup.roll()
            
            if has_ship and has_captain and has_crew:
            # Now we got all needed dice, and can bank the ones we like to save.
                
                if chance < 2:
                        for i in range(5):
                            if self._cup._dices[i].get_value()>3:
                                self._cup.bank(i)
                            else:
                                self._cup.roll()
                
                elif chance == 2:
                    
                    for i in range(5):
                        if self._cup.is_banked(i):
                            pass
                        else:
                            self._cup.bank(i)
            # If we have a ship, captain and crew (sum 15)
            # calculate the sum of the two remaining.
        
        if has_ship and has_captain and has_crew:
            crew = sum(dievalues) - 15
            print("crew value:",crew)
            return crew
        
        else:
            print("crew value:",crew)
            return crew


class Player:
    """
    Responsible for the score of the individual player. 
    Has the ability, given a game logic, play a round of a game. 
    The gained score is accumulated in the attribute score.
    """

    def __init__(self,playername: str) -> None :
        self._name = self.set_name(playername)
        self._score = 0
    
    
    def set_name(self,namestring: str) -> str :
        """ This methods returns a string which is players name."""
        return namestring
    
    
    def current_score(self) -> int :
        """ This method  returns the current score of type int of 
        a player."""
        return self._score
    
    
    def reset_score(self) -> None :
        """ This method resets the player score to zero."""
        self._score=0
    
    
    def play_round(self, gameround: int) ->None:
        """ This method is responsible for updating score of 
        each player after every round."""
        self._score=self._score + gameround.round()


class PlayerRoom:
    """
    Responsible for the score of the individual player. 
    Has the ability, given a game logic, play a round of a game. 
    The gained score is accumulated in the attribute score.
    """

    def __init__(self) -> None:
        self._players = []
    
    def set_game(self,x: ShipOfFoolsGame) -> None :
        """ Starts a game."""
        self._game = x
    
    def add_player(self,y: Player) -> None :
        """ Adds a player in the game."""
        self._players.append(y)
    
    def reset_scores(self) -> None :
        """ Resets the scores of all the players to zero."""
        for i in range(len(self._players)):
            self._players[i].reset_score()
    
    def play_round(self) -> None :
        """ It plays a round untill there is a winner."""
        for i in self._players:
            i.play_round(self._game)
            if self.game_finished():
                break
            else:
                pass
    
    def game_finished(self) -> bool :
        """ 
        It checks whether the game is finished or not.
        It returns a boolean value.
        """
        empty = []  # type : List[bool]
        
        for i in range(len(self._players)):
            
            if self._players[i].current_score()>=21:
                empty.append(True)
            else:
                empty.append(False)
        
        return any(empty)
    
    
    def print_scores(self) -> None :
        """ Prints the current score of each player."""
        
        for i in range(len(self._players)):
            print(self._players[i]._name ,"=", self._players[i].current_score())
    
    
    def print_winner(self) -> None :
        """ Prints the winner."""
        
        for i in range(len(self._players)):
            
            if self._players[i].current_score()>=21:
                print("winner is:",self._players[i]._name)


if __name__ == "__main__":
    room = PlayerRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player('PLAYER_1'))
    room.add_player(Player('PLAYER_2'))
    room.reset_scores()
    print("In this game we roll 5 dices and each player gets 3 cahnces in a round.")
    print("The player should get a ship which is 6, cabin is 5 and the crew is 4.")
    print ("Bank the remaining dice if it has value greater than 3")
    print("The player whose crewvalue is 21 will be the winner of the game")

    rounds = 1
    
    while not room.game_finished():
        print("round:",rounds)
        rounds+=1
        room.play_round()
        room.print_scores()
    room.print_winner()      





                


