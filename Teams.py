class team:
    def __init__(self, name):
        self.team_name = name 
        
    def manager(self, manager_name, manager_salary):
        self.manager = manager_name
        self.manager_salary = manager_salary
        self.cost_list= []      # Keeps all expenses of a team
        self.cost_list.append(manager_salary)
        # print(self.cost_list)
        
    def captain(self, captain_name, captain_salary):
        self.captain = captain_name
        self.captain_salary = captain_salary
        self.cost_list.append(captain_salary)  # Added to team's salary
        # print(self.cost_list)
        
    def budget(self, budget):
        self.budget = budget
        
    def budget_after_costs(self):
        self.bac = self.budget
        temp = self.budget
        for x in self.cost_list:
            temp -= x 
        self.bac = temp 
        return self.bac 
        
    def budget_suggestion(self):
        if self.bac <= self.budget * .1 and self.bac>=  0:
            print("Your remaning budget is ", round((self.bac * 100)/self.budget, 2) , "% of the season's budget, try cutting expenses! ") 
        elif self.bac < 0: 
            print("You are losing money! Cut expenses ASAP!!! ")
        elif self.bac >= self.budget *.1 and self.bac < self.budget*.35:
            print("Budget is looking okay..Your remaning budget is ", round( (self.bac * 100)/self.budget, 2), "% of the season's budget. Be smart with it.")
        else:
            print("Nice job! Looks like we are in good shape financially after the expenses. Keep it up! ")
        
    def info(self):
        print("****", self.team_name.upper(), "**** ")
        print("Manager: ", self.manager, " Salary: ", self.manager_salary)
        print("Captain: ", self.captain, " Salary: ", self.captain_salary)
        print("Season's Total Budget: " , self.budget)
        print("Remaining Budget for the Season: ", self.budget_after_costs())
        self.budget_suggestion()
        

while True:
    num = input("How many teams will you like to create? ")
    if not num.isdecimal() or int(num) <= 0:  # takes care of anything except nums, doubles or <0
        print("Number of teams can only be a Positive Integer! ")
    else: 
        num = int(num)
        break

team_list = []
for i in range(num):
    while True:
        name = input("Enter Team #{} name: ".format(i+1))
        if name.isalpha():
            team_list.append(team(name))
            break
        else:
            print("Team's name can only have alphabets! Try again...")

# first_team = team("Bucks") # Test using only 1 team 
for t in team_list:
    while True:
        a = input("{}'s manager: ".format(t.team_name))
        if not a.isalpha():
            print("Manage's name can only have alphabets! Try again...")
            continue
        break
    while True:
        b = (input("{}'s salary: ".format(a)))
        if b.isdecimal():
            b = float(b)
            break
        else:
            print("Salary can only have numbers! Try again...")
            
    while True:
        c = input("{}'s captain: ".format(t.team_name))
        if not c.isalpha():
            print("Captain's name can only have alphabets! Try again...")
            continue
        break
    
    
    while True:
        d = input("{}'s salary: ".format(c))
        if d.isdecimal():
            d = float(d)
            break
        else:
            print("Salary can only have numbers! Try again...")
            
    
    
    while True:
        e = input("{}'s budget: ".format(t.team_name))
        if e.isdecimal():
            e = float(e)
            break
        else:
            print("Budget can only have numbers! Try again...")
    
    t.manager(a, b)
    t.captain(c, d)
    t.budget(e)

print("\n\n***** There are total {} teams *****\n".format(len(team_list)))


j = 1
for team in team_list:
    print("\n#", j, ": ")
    team.info()
    j+=1

# first_team.info()









