from sys import maxsize #since we cannot take a infinity in a computer so we take max size of an interger  .

# now we are going to make a tree for min-max algorithm

class Node(object):
    def __init__(self,i_depth,i_player,i_sticksRemaining,i_value =0):
        self.i_depth = i_depth # how deep we are into the tree
        self.i_player = i_player#player number 1 or -1
        self.i_sticksRemaining  = i_sticksRemaining # sticks remaning
        self.i_value = i_value# game state negative infinity  0 or positive infinity
        self.children =[]
        self.CreateChildern() # here we are creating childen
                                  #self is the  always the first argument of any method of class 
    def CreateChildern(self):
        if self.i_depth >= 0 : # this checks the depths of tree if depth becomes negative it stops means we are at the top of the tree
            for i in range(1,3):# for how man ysticks we are choosing here we are chosing i or 2 sticks 
                v = self.i_sticksRemaining - i # v stors the value of how many sticks remain for each choice
                self.children.append(Node(self.i_depth -1,-self.i_player,v,self.RealVal(v)))
 #every time a new child is created        ^depth is dicreased   ^player is fliped

    def RealVal(self,value): # this function tells about what is the state of the game is
        if(value == 0 ):
            return maxsize*self.i_player #he wins
        elif(value < 0):
            return maxsize*-self.i_player# he looses
        return 0


#####################################################################################
def MinMax(node,i_depth,i_player):# first we check if we are at top of the node of if we have reached the win or the loose situation that is in our case is infinity
    if(i_depth == 0) or (abs(node.i_value) == maxsize ):
        return node.i_value # passin up the best possible move to parent node 


    i_bestValue = maxsize*-i_player # we are assing the value oppsite to the player eg: if we are positive player we will start from the negative infinioty to reach positive in finity

    for i in range(len(node.children)): # we itrate one by one all the possible moves
        child = node.children[i] 
        i_val = MinMax(child,i_depth - 1,-i_player)
        if(abs(maxsize*i_player - i_val) < abs(maxsize*i_player - i_bestValue)):# this checks the our current possition from were we want to be
            
            i_bestValue = i_val# if we are close to + or - infinity we just store the value 

    return i_bestValue
#####################################################################
def winChecker(i_sticks,i_player):
    if i_sticks <= 0:
        print("#"*30)
        if i_player > 0:
            if i_sticks == 0:
               print("\tyou win")
            else:
                print("\t you lose")
        else :
            if i_sticks == 0:
                print("\tComp wins")
            else :
                print ("\tcompt error")
        print("#"*30)
        return 0
    return 1
##############################################################################


if __name__ == '__main__':
    i_sticksTotal = 13
    i_depth =4
    i_curplayer =1
    print("Be the player to pic up the last stick \t you can pick up  1 or 2 sticks at a time")
    while(i_sticksTotal >0):
        print("\n %d sticks remain.how many would you like to choose ?"%i_sticksTotal)
        i_choice = input("\n 1 or 2 :")
        i_sticksTotal = int(float(i_choice))
        if winChecker(i_sticksTotal,i_curplayer):
            i_curplayer*=-1
            node = Node(i_depth,i_curplayer,i_sticksTotal)
            bestChoise = -100
            i_bestValue = -i_curplayer*maxsize
            for  i in range(len(node.children)):
                n_child = node.children[i]
                i_val =MinMax(n_child,i_depth,i_curplayer)
                if(abs(i_curplayer*maxsize -i_val) <=abs(i_curplayer*maxsize - i_bestValue)):
                    i_bestValue = i_val
                    bestChoice = i


            bestChoice +=1
            print("comp chooses :" +  str(bestChoice) + " Base om value" + str(i_bestValue))
            i_sticksTotal -= bestChoice
            winChecker(i_sticksTotal,i_curplayer)
            i_curplayer *= -1
            
        
        
        
    
        
