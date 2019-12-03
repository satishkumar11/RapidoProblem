import math

class PlanetArmy:
  attackList=[]
  def assign_army(self,attackList):
    self.attackList=attackList
  def display_armies(self,name_of_army,attackList):
    self.assign_army(attackList)
    print(name_of_army)
    print("==============================")   
    print("No. of Horses         :"+str(self.attackList[0]))
    print("No. of Elephants      :"+str(self.attackList[1]))
    print("No. of Armoured Tanks :"+str(self.attackList[2]))
    print("No. of Sling Guns     :"+str(self.attackList[3]))
    print("==============================")
    print("                                ")
    
class Defender:
  defender_attack=[]
  attacker_attack=[]
  
  def __init__(self,Shan):
    self.Shan=Shan
    self.defender_attack=self.Shan.attackList

  def defend(self,attacker_attack):
    winCount=0
    self.attacker_attack=attacker_attack
    local_defender_attack=[]
    local_defender_attack.extend(math.ceil(army/2) for army in self.attacker_attack)
    for index,army in enumerate(local_defender_attack):
      if army>self.defender_attack[index]:
        if(index==0):
          local_index=1  
          if(self.substitute(self.defender_attack,local_defender_attack,index,local_index)):
            winCount+=1
        else:
          local_index=index-1
          if(self.substitute(self.defender_attack,local_defender_attack,index,local_index)):
            winCount+=1
          else:
            if(index!=len(attacker_attack)-1):
              local_index=index+1
              if(self.substitute(self.defender_attack,local_defender_attack,index,local_index)):
                winCount+=1
              else:
                local_defender_attack[index]=self.defender_attack[index]
            else:
                local_defender_attack[index]=self.defender_attack[index]
      else:
        winCount+=1

    print("                                ")
    print("++++++++++++++++++++++++++++++++")
    if(winCount==len(attacker_attack)):
      print("Defender army wins")
      self.Shan.display_armies("Winning Defender's army:",local_defender_attack)
    else:
      print("Defender army loses")
      self.Shan.display_armies("Lost Defender's army:",local_defender_attack)
    print("++++++++++++++++++++++++++++++++")
    print("                                ")
      
  def substitute(self,actual_army,local_army,index,local_index) :
    local_var=(actual_army[local_index]-(local_army[local_index]))
    if(local_var>0):
      for army in range(1,local_var+1):
        if(index<local_index):
          if((local_army[index]-(2*army))<=math.ceil(actual_army[index])):
            local_army[index]-=2*army 
            local_army[local_index]+=army
            return True
          elif(army==local_var):
            local_army[index]-=2*army 
            local_army[local_index]+=army
            return
        elif(index>local_index):
          if(local_army[index]-army//2==math.ceil(actual_army[index])):
            local_army[index]-=math.ceil(army//2)
            local_army[local_index]+=army
            return True
          elif(army==local_var):
            local_army[index]-=math.ceil(army//2)
            local_army[local_index]+=army
            return 

    return False
  
def checkValidAttacks(attacker_attack,actual_army):
  for i in range(len(attacker_attack)):
    if(attacker_attack[i]>actual_army[i]):
      return False
  return True
  
if __name__=="__main__":
  Falcon=PlanetArmy()
  Falcon.display_armies("Total Strength of Falcon's PlanetArmy",[300,200,40,20])
  Shan=PlanetArmy()
  Shan.display_armies("Total Strength of King Shan's PlanetArmy",[100,50,10,5])
  print("Enter attacking Falcon army")
  print("input format 1 1 1 1")
  attacker_attack=list(map(int, input().split()))
  if(checkValidAttacks(attacker_attack,Falcon.attackList)):
    d=Defender(Shan)
    d.defend(attacker_attack)
  else:
    print("Attacking army should not be greater than actual army")