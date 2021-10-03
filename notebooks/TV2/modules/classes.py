class TestUser():
    def __init__(self,id,username,password,age,zipcode,gender,focus,pr1,pr2,pr3,pr4,pr5,pr6):
        self.username=username
        self.password=password
        self.id=id
        self.testData={
            "age":age,
            "zipcode":zipcode,
            "gender":gender,
            "focus":focus,
            "pr1":pr1,
            "pr2": pr2,
            "pr3":pr3,
            "pr4":pr4,
            "pr5":pr5,
            "pr6":pr6
        }
    
    
class User():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.id=None
        self.cars=[]

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n < len(self.cars):
            self.n+=1
            return self.cars[self.n-1]
        else:
            raise StopIteration  # signals "the end"

    def __repr__(self):
        return 'User(%r,%r)' % (self.username,self.password)
        return 'Car(%r,%r,%r,%r,%r,%r,%r,%r)' % ( self.model,self.fuel,self.year,self.km,self.capacity,self.estimated_price,self.sale_price,self.car_id)

    def __str__(self):
        c_str=""
        for c in self.cars:
            c_str+=', '
            c_str+=c.__str__()
        return ' {}. {} has:  {}.'.format(self.id,self.username, c_str)





class Car():
    def __init__(self,model,fuel,year,km,capacity,estimated_price,sale_price,car_id):
        self.car_id=car_id
        self.model=model
        self.fuel=fuel
        self.year=year
        self.km=km
        self.capacity=capacity
        self.estimated_price=estimated_price
        self.sale_price=sale_price

    def __repr__(self):
        return 'Car(%r,%r,%r,%r,%r,%r,%r,%r,)' % ( self.model,self.fuel,self.year,self.km,self.capacity,self.estimated_price,self.sale_price,self.car_id)

    def __str__(self):
        return 'Audi {} from {}, {} {}.'.format(self.model,self.year, self.capacity, self.fuel)


class DataBaseException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


# car = Car("A1",'Diesel',  2018, 75000, 2.5, 200000,210000,1)
# print(car.__repr__())
# print(car.__str__())

# user = User("Magda", 'passsssss')
# user.cars.append(car)
# user.cars.append(car)
# user.cars.append(car)
# print()
# print(user.__repr__())
# print(user.__str__())

# print('\ncars:')
# for c in user:
#     print(c)