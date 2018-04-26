#!/bin/python3.6
## two types of objects - 1. instance objects 2. class objects e.g company is also object

class company:
  c_code=123
## Instance Method
  def set_comp_name(self,n):  # instance for creating namespace c1 c2
    self.c_name=n
  def get_comp_name(self):
    return self.c_name
## Class methods
  def gov_rules(): ## rule will be common for all
    s='rule_xyz'
    return s
c1=company()   ## creat object c1
c2=company()   # create object c2
c1.set_comp_name('Synechron')
c2.set_comp_name('IBM')
r1=c1.get_comp_name()
r2=c2.get_comp_name()
print('r1=',r1,'r2=',r2)

## priting class method - use classname.method
print(company.c_code)
r=company.gov_rules()
print(r)

## Sub class of company class, will inherit all properties of company class
## useful if new requirment comes like pending adhar field in exiting account 
## here creating new team in existing comp class
class Team(company):
  def create_team(self):
    self.team=[]
  def add_emp(self,n):
    self.team.append(n)
    return self.team
t1=Team()
t1.set_comp_name('Redhat') #set_comp_name inherited from class company 
r=t1.get_comp_name() # get_comp_name inherited from class company
print('comp=',r)
t1.create_team()
t1.add_emp('mhn')

## Subclass 2

class Team2(company):
  def __init__(self):
    self.team=[]
  def add_emp(self,n):
    self.team.append(n)
    return self.team
t2=Team2() ## __init__ method will be called here 
t2.set_comp_name('DELL') #set_comp_name inherited from class company
r=t2.get_comp_name() # get_comp_name inherited from class company
print('comp=',r)
t2.add_emp('emp1')


## Multilevel inheritance 
## Subclass 3

class new_team(Team2):
  def add_emp(self,n):
    self.team.append(n)
    return self.team
  def __init__(self):
    super().__init__()  ## calling class Team2 because team is not difined in this class and need to call from Team2 class
n1=new_team()
r=n1.add_emp('emp2')
print('emp_list=',r)

## Below is separate class using methods available in Team2 class and company class

class location:
  def add_location(self,n):
    self.l=n
    return self.l
class MyTeam(new_team,location):
  def msg(self):
    return 'hello'
M1=MyTeam()
M1.set_comp_name('Oracle')  ## set_comp name is in company class, 
#so it will search in new_team, then location, so new_team will point to company class which is super class
r=M1.add_location('Pune')
print('Location =',r)

## Composite Object : object is linked to another object
class SomeTeam():
  def __init__(self):
    l1=location()
    self.l2=location()
  def somemesg(self):
    pass
s1=SomeTeam()


