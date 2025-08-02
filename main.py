import json
import random

pokemon = ("Eevee","Leafeon","Vaporeon", "Flareon", "Sylveon", "Pikachu", "Raichu", "Shaymin", "Metagross", "Groudon", "Gardevoir") # list of pokemon I've got working now and are allowed to be used

class Pkmn:
  '''pokemon object'''
  def __init__(self, name, lvl, moves):
    '''set a bunch of initial stuff'''
    self.name = name
    self.lvl = lvl
    self.moves = moves
    pkmn_data = get_pkmn_data(name)
    type = [pkmn_data.get("type1")]
    if pkmn_data.get("type2") != "None":
      type.append(pkmn_data.get("type2"))
    self.types = type
    stats = pkmn_data.get("stats")
    hpbase = stats.get("hp")
    atkbase = stats.get("attack")
    defbase = stats.get("defence")
    spatkbase = stats.get("sp-attack")
    spdefbase = stats.get("sp-defence")
    spdbase = stats.get("speed")
    self.maxhp = int(0.01*(2*hpbase+31)*lvl)+lvl+10
    self.maxatk = int(0.01*(2*hpbase+31)*lvl)+5
    self.maxdef = int(0.01*(2*hpbase+31)*lvl)+5
    self.maxspatk = int(0.01*(2*hpbase+31)*lvl)+5
    self.maxspdef = int(0.01*(2*hpbase+31)*lvl)+5
    self.maxspd = int(0.01*(2*hpbase+31)*lvl)+5
    self.chp = self.maxhp
    self.catk = self.maxatk
    self.cdef = self.maxdef
    self.cspatk = self.maxspatk
    self.cspdef = self.maxspdef
    self.cspd = self.maxspd
    self.cacc = 100
    self.atk_m = 0
    self.def_m = 0
    self.spatk_m = 0
    self.spdef_m = 0
    self.spd_m = 0
    self.acc_m = 0
  def __str__(self):
    '''get summary of pokemon'''
    moves = ""
    for move in self.moves:
      moves += move + ", "
    moves = moves[0:len(moves)-2]
    types = ""
    for type in self.types:
      types += type + " "
    return " - " + self.name + "\nType: " + types + "\n   lvl " + str(self.lvl) + "\n   Moves: " + moves + "\n   Stats:\n     HP: " + str(self.chp) + "/" + str(self.maxhp) + "\n     Attack: " + str(self.maxatk) + "\n     Defence: " + str(self.maxdef) + "\n     Special Attack: " + str(self.maxspatk) + "\n     Special Defence: " + str(self.maxspdef) + "\n     Speed: " + str(self.maxspd)
  def get_moves(self):
    '''returns move list'''
    return self.moves
  def get_name(self):
    '''returns name string'''
    return self.name
  def get_lvl(self):
    '''returns level int'''
    return self.lvl
  def get_type(self):
    '''returns type list'''
    return self.types
  def get_max_stats(self):
    '''returns max stats as list'''
    return [self.maxhp, self.maxatk, self.maxdef, self.maxspatk, self.maxspdef, self.maxspd]
  def get_current_stats(self):
    '''returns current stats as list'''
    return [self.chp, self.catk, self.cdef, self.cspatk, self.cspdef, self.cspd, self.cacc]
  def mod_hp(self,amount):
    self.chp += amount
  def calc_stats_m(self):
    '''calculates stat modifiers'''
    self.catk = calc_m_stat(self.maxatk,self.atk_m)
    self.cdef = calc_m_stat(self.maxdef,self.def_m)
    self.cspatk = calc_m_stat(self.maxspatk,self.spatk_m)
    self.cspdef = calc_m_stat(self.maxspdef,self.spdef_m)
    self.cspd = calc_m_stat(self.maxspd,self.spd_m)
    if self.acc_m < 0:
      self.cacc = int(100 * (3/(0 - self.acc_m + 3)))
    elif self.acc_m > 0:
      self.cacc = int(100 * ((self.acc_m + 3)/3))
  def mod_stat(self,type,amount):
    '''modify stat ifs'''
    if type == "atk":
      self.atk_m += amount
      if self.atk_m > 6:
        self.atk_m = 6
      elif self.atk_m < -6:
        self.atk_m = -6
    if type == "def":
      self.def_m += amount
      if self.def_m > 6:
        self.def_m = 6
      elif self.def_m < -6:
        self.def_m = -6
    if type == "spatk":
      self.spatk_m += amount
      if self.spatk_m > 6:
        self.spatk_m = 6
      elif self.spatk_m < -6:
        self.spatk_m = -6
    if type == "spdef":
      self.spdef_m += amount
      if self.spdef_m > 6:
        self.spdef_m = 6
      elif self.spdef_m < -6:
        self.spdef_m = -6
    if type == "spd":
      self.spd_m += amount
      if self.spd_m > 6:
        self.spd_m = 6
      elif self.spd_m < -6:
        self.spd_m = -6
    if type == "acc":
      self.acc_m += amount
      if self.acc_m > 6:
        self.acc_m = 6
      elif self.acc_m < -6:
        self.acc_m = -6
  def faint(self):
    '''fainted: hp set to 0 because its nicer'''
    self.chp = 0


def get_pkmn_data(name):
  '''collects info from the json files'''
  if name == "Eevee":
    f = open('pokemon/eevee.json')
  elif name == "Leafeon":
    f = open('pokemon/leafeon.json')
  elif name == "Vaporeon":
    f = open('pokemon/vaporeon.json')
  elif name == "Flareon":
    f = open('pokemon/flareon.json')
  elif name == "Sylveon":
    f = open('pokemon/sylveon.json')
  elif name == "Pikachu":
    f = open('pokemon/pikachu.json')
  elif name == "Raichu":
    f = open('pokemon/raichu.json')
  elif name == "Shaymin":
    f = open('pokemon/shaymin.json')
  elif name == "Metagross":
    f = open('pokemon/metagross.json')
  elif name == "Groudon":
    f = open('pokemon/groudon.json')
  elif name == "Gardevoir":
    f = open('pokemon/gardevoir.json')
  pkmn_data = json.load(f)
  f.close()
  return pkmn_data

def calc_m_stat(max, mod):
  '''calculate a modified stat'''
  new = 0
  if mod < 0:
    new = max * (2/(0 - mod + 2))
  elif mod > 0:
    new = max * ((mod + 2)/2)
  else:
    new = max
  return int(new)

def change_m_stat(move_info, pkmn, pkmn_name):
  '''modify stat of pokemon - move'''
  if "attack" in move_info:
    chance = move_info.get("attack").get("chance")
    amount = move_info.get("attack").get("amount")
    if chance >= random.randrange(100) + 1:
      pkmn.mod_stat("atk",amount)
      if amount == 1:
        print(pkmn_name + "'s Attack Rose!")
      elif amount == -1:
        print(pkmn_name + "'s Attack Fell!")
      if amount > 1:
        print(pkmn_name + "'s Attack Sharply Rose!")
      elif amount < -1:
        print(pkmn_name + "'s Attack Sharply Fell!")
  if "defence" in move_info:
    chance = move_info.get("defence").get("chance")
    amount = move_info.get("defence").get("amount")
    if chance >= random.randrange(100) + 1:
      pkmn.mod_stat("def",amount)
      if amount == 1:
        print(pkmn_name + "'s Defence Rose!")
      elif amount == -1:
        print(pkmn_name + "'s Defence Fell!")
      if amount > 1:
        print(pkmn_name + "'s Defence Sharply Rose!")
      elif amount < -1:
        print(pkmn_name + "'s Defence Sharply Fell!")
  if "sp-attack" in move_info:
    chance = move_info.get("sp-attack").get("chance")
    amount = move_info.get("sp-attack").get("amount")
    if chance >= random.randrange(100) + 1:
      pkmn.mod_stat("spatk",amount)
      if amount == 1:
        print(pkmn_name + "'s Special Attack Rose!")
      elif amount == -1:
        print(pkmn_name + "'s Special Attack Fell!")
      if amount > 1:
        print(pkmn_name + "'s Special Attack Sharply Rose!")
      elif amount < -1:
        print(pkmn_name + "'s Special Attack Sharply Fell!")
  if "sp-defence" in move_info:
    chance = move_info.get("sp-defence").get("chance")
    amount = move_info.get("sp-defence").get("amount")
    if chance >= random.randrange(100) + 1:
      pkmn.mod_stat("spdef",amount)
      if amount == 1:
        print(pkmn_name + "'s Special Defence Rose!")
      elif amount == -1:
        print(pkmn_name + "'s Special Defence Fell!")
      if amount > 1:
        print(pkmn_name + "'s Special Defence Sharply Rose!")
      elif amount < -1:
        print(pkmn_name + "'s Special Defence Sharply Fell!")
  if "speed" in move_info:
    chance = move_info.get("speed").get("chance")
    amount = move_info.get("speed").get("amount")
    if chance >= random.randrange(100) + 1:
      pkmn.mod_stat("spd",amount)
      if amount == 1:
        print(pkmn_name + "'s Speed Rose!")
      elif amount == -1:
        print(pkmn_name + "'s Speed Fell!")
      if amount > 1:
        print(pkmn_name + "'s Speed Sharply Rose!")
      elif amount < -1:
        print(pkmn_name + "'s Speed Sharply Fell!")
  if "accuracy" in move_info:
    chance = move_info.get("accuracy").get("chance")
    amount = move_info.get("accuracy").get("amount")
    if chance >= random.randrange(100) + 1:
      pkmn.mod_stat("acc",amount)
      if amount == 1:
        print(pkmn_name + "'s Accuracy Rose!")
      elif amount == -1:
        print(pkmn_name + "'s Accuracy Fell!")
      if amount > 1:
        print(pkmn_name + "'s Accuracy Sharply Rose!")
      elif amount < -1:
        print(pkmn_name + "'s Accuracy Sharply Fell!")
  pkmn.calc_stats_m()

def select_team():
  '''selecting a pokemon team of 1-6'''
  team = []
  loop = 0
  while loop < 6:
    name_loop = True
    while name_loop:
      name = input("Enter a pokemon (blank to stop): ").title()
      if not name in pokemon and name != "":
        print("Please choose one of the following pokemon:", pkmnstr)
      else:
        if loop == 0 and name == "":
          print("Please choose at least one Pokemon.")
        else:
          name_loop = False
    if name != "":
      lvl_loop = True
      while lvl_loop:
        int_loop = True
        while int_loop:
          lvl = input("Enter the level: ")
          if lvl != "":
            int_loop = False
          else:
            print("Please enter a Level")
        lvl = int(lvl)
        if lvl <= 100 and lvl > 0:
          lvl_loop = False
        else:
          print("Level must be between 1 and 100.")
      if name in pokemon:
        move_list = get_pkmn_data(name).get("moves")
        for i in range(len(move_list)):
          print(str(i+1) + ":", move_list[i])
        moves = []
        move_nums = []
        move_loop = 0
        while move_loop < 4:
          move = input("Enter a move number (blank to stop): ")
          if move != "":
            move = int(move)
            move_tst = False
            for move_test in move_nums:
              if move == move_test:
                move_tst = True
            if move > 0 and move <= len(move_list) and not move_tst:
              move_nums.append(move)
              moves.append(move_list[move-1])
            else:
              print("Chose a move on the list and has not been chosen already.")
              move_loop -= 1
          else:
            if move_loop == 0:
              print("Please select at least one move.")
              move_loop -= 1
            else:
              move_loop = 100
          move_loop += 1
        team.append(Pkmn(name, lvl, moves))
    else:
      loop = 100
    loop += 1
  return team

def attack(team,o_team,pkmn_out,o_pkmn_out,move_list,move_choice,move_data):
  '''attacking stuff'''
  print(team[pkmn_out].get_name(), "used", move_list[move_choice] + "!")
  crit = 1
  type_eff = 1
  damage = 0
  immune = False
  if len(o_team[o_pkmn_out].get_type()) == 1:
    if move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[0]).get("immune"):
      immune = True
  else:
    if move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[0]).get("immune") or move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[1]).get("immune"):
      immune = True
  if immune:
    print(move_list[move_choice], "Does Not Affect", o_team[o_pkmn_out].get_name() + ".")
  else:
    if move_data.get(move_list[move_choice]).get("accuracy") >= random.randrange(100) + 1 or move_data.get(move_list[move_choice]).get("accuracy") == -1:
      if move_data.get(move_list[move_choice]).get("power") > 0:
        if random.randrange(24) == 0:
          crit = 1.5
        random_num = random.randint(85,100)/100
        if move_data.get(move_list[move_choice]).get("type") in team[pkmn_out].get_type():
          stab = 1.5
        else:
          stab = 1
        if move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[0]).get("weak"):
          type_eff *= 2
        if len(o_team[o_pkmn_out].get_type()) == 2:
          if move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[1]).get("weak"):
            type_eff *= 2
        if move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[0]).get("resist"):
          type_eff *= 0.5
        if len(o_team[o_pkmn_out].get_type()) == 2:
          if move_data.get(move_list[move_choice]).get("type") in type_data.get(o_team[o_pkmn_out].get_type()[1]).get("resist"):
            type_eff *= 0.5
        if type_data.get(move_data.get(move_list[move_choice]).get("type")).get("type") == 0:
          damage = int((((((2*team[pkmn_out].get_lvl())/5)+2)*move_data.get(move_list[move_choice]).get("power")*(team[pkmn_out].get_current_stats()[1]/o_team[o_pkmn_out].get_current_stats()[2])/50)+2)*crit*stab*type_eff*random_num)
        else:
          damage = int((((((2*team[pkmn_out].get_lvl())/5)+2)*move_data.get(move_list[move_choice]).get("power")*(team[pkmn_out].get_current_stats()[3]/o_team[o_pkmn_out].get_current_stats()[4])/50)+2)*crit*stab*type_eff*random_num)
      move_effects = move_data.get(move_list[move_choice]).get("effects")
      if "target" in move_effects:
        move_effects_target = move_effects.  get("target")
        # print("d- target effect")
        change_m_stat(move_effects_target,o_team[o_pkmn_out],o_team[o_pkmn_out].get_name())
      if "user" in move_effects:
        move_effects_user = move_effects.get("user")
        # print("d- user effect")
        change_m_stat(move_effects_user,team[pkmn_out],team[pkmn_out].get_name())
    else:
      print(o_team[o_pkmn_out].get_name(), "avoided the attack!")
  if type_eff > 1:
    print("It's Super Effective!")
  if type_eff < 1:
    print("It's Not Very Effective.")
  if crit == 1.5:
    print("Critical Hit!")
  # print("d- damage",damage)
  o_team[o_pkmn_out].mod_hp(0 - damage)
  # print("d- opp stats",o_team[o_pkmn_out].get_current_stats())
  # print("d- user stats",team[pkmn_out].get_current_stats())

def print_hp(o_pkmn,u_pkmn):
  '''displays hp of both pokemon'''
  print("Opposing", o_pkmn.get_name() + "'s hp:", o_pkmn.get_current_stats()[0])
  print("Player's", u_pkmn.get_name() + "'s hp:", u_pkmn.get_current_stats()[0])


# displays all the pokemon available
pkmnstr = ""
for i in pokemon:
  pkmnstr += i + ", "
pkmnstr = pkmnstr[0:len(pkmnstr)-2]

print("All Pokemon in this:", pkmnstr)
#--

print("Chose your team:")
team = select_team()

print("\nChose opposing team:")
o_team = select_team()

print("Your Team:")
for i in team:
  print(i)

print("\nOpposing Team:")
for i in o_team:
  print(i)

# get move and type info
f = open('moves.json')
move_data = json.load(f)
f.close()
f = open('types.json')
type_data = json.load(f)
f.close()
# --
pkmn_out = 0
o_pkmn_out = 0
turn = 1
loop = True
finish_turn = False
while loop:
  # main loop
  fainted = False
  o_fainted = False
  print("\nTurn", turn, "\n")
  print_hp(o_team[o_pkmn_out],team[pkmn_out])
  choice_loop = True
  while choice_loop:
    print("\n1. Attack\n2. Pokemon\n3. Run")
    int_loop = True
    while int_loop:
      choice = input("What will " + team[pkmn_out].get_name() + " do? ")
      if choice != "":
        int_loop = False
      else:
        print("Please choose a number.")
    choice = int(choice)
    if choice < 1 or choice > 3:
      print("You can only choose these options.")
    else:
      choice_loop = False
  switched = False
  o_switch = False
  if_opp_atk = False
  if random.randrange(25) == 0 and len(o_team) != 1: #opponent move stuff
    o_switch = True
    o_switch_loop = True
    while o_switch_loop:
      new_o_pkmn = random.randrange(len(o_team))
      if o_team[new_o_pkmn].get_current_stats()[0] > 0 and new_o_pkmn != o_pkmn_out:
        o_switch_loop = False
  else:
    move_num = len(o_team[o_pkmn_out].get_moves())
    o_choice = random.randrange(move_num)
    if_opp_atk = True
    # print("d-", o_team[o_pkmn_out].get_moves()[o_choice])
  if choice == 1:
    # if attacking
    list_moves = "0. Back\n"
    move_list = team[pkmn_out].get_moves()
    o_move_list = o_team[o_pkmn_out].get_moves()
    for i in range(len(move_list)):
      list_moves += str(i+1) + ". " + move_list[i] + "\n"
    list_moves = list_moves[0:len(list_moves)-1]
    print(list_moves)
    move_loop = True
    while move_loop:
      int_loop = True
      while int_loop:
        move_choice = input("Which move will " + team[pkmn_out].get_name() + " use? ")
        if move_choice != "":
          int_loop = False
        else:
          print("Please choose a number.")
      move_choice = int(move_choice) - 1
      if move_choice < -1 or move_choice > len(move_list) - 1:
        print("You can only choose these options.")
      else:
        move_loop = False
    if move_choice != -1:
      if o_switch:
        print("The Opposing", o_team[o_pkmn_out].get_name(), "Switched Out With", o_team[new_o_pkmn].get_name())
        o_pkmn_out = new_o_pkmn
      finish_turn = True
      priority = False
      if team[pkmn_out].get_current_stats()[5] < o_team[o_pkmn_out].get_current_stats()[5]: #SPEED (move order logic)
        if not o_switch:
          if move_data.get(move_list[move_choice]).get("priority") > move_data.get(o_move_list[o_choice]).get("priority"):
            # print("d- fast")
            switched = True
            priority = True
        if not priority:
          # print("d- slow")
          if_opp_atk = False
          attack(o_team,team,o_pkmn_out,pkmn_out,o_move_list,o_choice,move_data)
        # else:
          # print("d- fast")
      else:
        if not o_switch:
          if move_data.get(move_list[move_choice]).get("priority") < move_data.get(o_move_list[o_choice]).get("priority"):
            # print("d- slow")
            if_opp_atk = False
            attack(o_team,team,o_pkmn_out,pkmn_out,o_move_list,o_choice,move_data)
        # else:
          # print("d- fast")
      if team[pkmn_out].get_current_stats()[0] > 0:
        attack(team,o_team,pkmn_out,o_pkmn_out,move_list,move_choice,move_data) #yay we attack now
        if o_team[o_pkmn_out].get_current_stats()[0] < 1:
          o_fainted = True
      else:
        print(team[pkmn_out].get_name(), "Fainted.")
        fainted = True
  elif choice == 2:
    # swap information stuff
    menu_loop = True
    while menu_loop:
      choice_loop = True
      while choice_loop:
        print("0. Back\n1. Check Summary\n2. Swap")
        int_loop = True
        while int_loop:
          pkmn_choice = input("What will you do? ")
          if pkmn_choice != "":
            int_loop = False
          else:
            print("Please choose a number.")
        pkmn_choice = int(pkmn_choice)
        if pkmn_choice < 0 or pkmn_choice > 2:
          print("You can only choose these options.")
        else:
          choice_loop = False
        if pkmn_choice == 1:
          # summary
          pkmn_names = ""
          for i in range(len(team)):
            pkmn_names += str(i+1) + ". " + team[i].get_name() + "\n"
          pkmn_names = pkmn_names[0:len(pkmn_names)-1]
          print(pkmn_names)
          choice_loop = True
          while choice_loop:
            choose_pkmn = int(input("Choose a pokemon: "))
            if choose_pkmn < 1 or choose_pkmn > len(team):
              print("Please choose a pokemon on the list.")
            else:
              choice_loop = False
          print(team[choose_pkmn-1])
        elif pkmn_choice == 2:
          # swap
          pkmn_names = ""
          for i in range(len(team)):
            pkmn_names += str(i+1) + ". " + team[i].get_name() + "\n"
          pkmn_names = pkmn_names[0:len(pkmn_names)-1]
          print(pkmn_names)
          choice_loop = True
          while choice_loop:
            choose_pkmn = int(input("Choose a pokemon: "))
            if choose_pkmn < 1 or choose_pkmn > len(team):
              print("Please choose a pokemon on the list.")
            else:
              if team[choose_pkmn-1].get_current_stats()[0] > 0:
                choice_loop = False
              else:
                print("Please choose a pokemon that has not fainted.")
          pkmn_out = choose_pkmn - 1
          finish_turn = True
          menu_loop = False
          switched = True
        else:
          #exit
          menu_loop = False
  if choice != 3:
    # move order logic (extra)
    # print("d-", if_opp_atk, switched, o_switch)
    if if_opp_atk or switched:
      if not o_switch:
        if not fainted and not o_fainted:
          attack(o_team,team,o_pkmn_out,pkmn_out,o_move_list,o_choice,move_data) # attack stuff if player switched/faster
          if team[pkmn_out].get_current_stats()[0] < 0:
            print(team[pkmn_out].get_name(), "Fainted.")
            fainted = True
  else:
    # run away (end program - way 1)
    print("You ran away and ended the battle!")
    loop = False
  if finish_turn == True:
    #completing a turn (as to have loop proper without exiting menu and opponent attacking)
    finish_turn = False
    turn += 1
  if fainted:
    #user pokemon faints
    team[pkmn_out].faint()
    menu_loop = True
    all_fainted = 0
    for i in team:
      if i.get_current_stats()[0] < 1:
        all_fainted += 1
    if all_fainted == len(team):
      #end program - way 2
      menu_loop = False
      print("You lost :(")
      loop = False
    while menu_loop: #swapping after faint
      choice_loop = True
      while choice_loop:
        print("Choose a Pokemon to switch to:\n1. Check Summary\n2. Swap")
        int_loop = True
        while int_loop:
          pkmn_choice = input("What will you do? ")
          if pkmn_choice != "":
            int_loop = False
          else:
            print("Please choose a number.")
        pkmn_choice = int(pkmn_choice)
        if pkmn_choice < 1 or pkmn_choice > 2:
          print("You can only choose these options.")
        else:
          choice_loop = False
        if pkmn_choice == 1:
          pkmn_names = ""
          for i in range(len(team)):
            pkmn_names += str(i+1) + ". " + team[i].get_name() + "\n"
          pkmn_names = pkmn_names[0:len(pkmn_names)-1]
          print(pkmn_names)
          choice_loop = True
          while choice_loop:
            choose_pkmn = int(input("Choose a pokemon: "))
            if choose_pkmn < 1 or choose_pkmn > len(team):
              print("Please choose a pokemon on the list.")
            else:
              choice_loop = False
          print(team[choose_pkmn-1])
        elif pkmn_choice == 2:
          pkmn_names = ""
          for i in range(len(team)):
            pkmn_names += str(i+1) + ". " + team[i].get_name() + "\n"
          pkmn_names = pkmn_names[0:len(pkmn_names)-1]
          print(pkmn_names)
          choice_loop = True
          while choice_loop:
            choose_pkmn = int(input("Choose a pokemon: "))
            if choose_pkmn < 1 or choose_pkmn > len(team):
              print("Please choose a pokemon on the list.")
            else:
              if team[choose_pkmn-1].get_current_stats()[0] > 0:
                choice_loop = False
              else: #make sure swap is valid and not into a fainted 'mon
                print("Please choose a pokemon that has not fainted.")
          pkmn_out = choose_pkmn - 1
          finish_turn = True
          menu_loop = False
          switched = True
  if o_fainted:
    #opponent fainting logic
    print("The Opposing", o_team[o_pkmn_out].get_name(), "Fainted.")
    o_switch_loop = True
    all_o_fainted = 0
    for i in o_team:
      if i.get_current_stats()[0] < 1:
        all_o_fainted += 1
    if all_o_fainted == len(o_team):
      o_switch_loop = False
    while o_switch_loop:
      new_o_pkmn = random.randrange(len(o_team))
      if o_team[new_o_pkmn].get_current_stats()[0] > 0 and new_o_pkmn != o_pkmn_out: # check selected if not fainted
        o_switch_loop = False
    if all_o_fainted != len(o_team):
      print("The Opposing", o_team[o_pkmn_out].get_name(), "Switched Out With", o_team[new_o_pkmn].get_name())
      o_pkmn_out = new_o_pkmn
    else:
      #end program - way 3
      print("You win :)")
      loop = False