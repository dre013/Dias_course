import json 

class Tourmenent:
    def __init__(self,name,year):
        self.name = name 
        self.year = year

tour = {
    "Lionel Messi":2021,
    "Cristiano Ronaldo":2020,
    "Luka Modric":2019
}
json_data = json.dumps(tour, indent=2)
print(json_data)

# loaded = json.loads(json_data)
# print(loaded)
# print(type(loaded))

t1 = Tourmenent("Lionel Messi", 2021)
# json_data = json.dumps(t1)
json_data = json.dumps(t1.__dict__)
print(json_data)

t = Tourmenent(**json.loads(json_data))
print(f'name = {t.name} and year = {t.year}')

class Players :
    def __init__(self,tour):
        self.tour = tour

t1 = Tourmenent("Lionel Messi", 2021)
t2 = Tourmenent("Cristiano Ronaldo", 2022)
t3 = Tourmenent("Luka Modric", 2019)

p1 = Players([t1,t2,t3])

#json_data = json.dumps(p1.__dict__)
#print(json_data)

json_data = json.dumps(p1,default = lambda obj: obj.__dict__)
print(json_data)

decod = Players(**json.loads(json_data))
print(decod)

prout = decod.tour[0]
print(type(prout))
print(tour)


class Tourmenent:
    def __init__(self,name,year):
        self.name = name 
        self.year = year

    @classmethod
    def from_json(cls,json_data):
        return cls(**json_data)

class Players :
    def __init__(self,tour):
        self.tour = tour

    @classmethod
    def from_json(cls,json_data):
        tour = list(map(Tourmenent.from_json,json_data['tour']))
        return cls(tour)

    
json_data = json.dumps(p1,default= lambda obj:obj.__dict__, indent = 4)
print(json_data)
print(type(json_    ))



with open ('player.json','r') as file_read:
    data = json.load(file_read)
print(data)

with open ('data.json','w') as write_file:
    data = json.dump(data,write_file)
print(data)