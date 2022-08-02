class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def full_spec(self):
        print(f"The full spec of this phone in {self.brand} {self.model} and the price is {self.price}")


class SmartPhone(Phone):
    def __init__(self,brand,model,price,ram,memory,camera):
        super().__init__(brand,model,price)
        self.ram=ram
        self.memory=memory
        self.camera=camera

    def full_spec(self):
        print(f"The full spec of this phone in {self.brand} {self.model} and the price is {self.price} ") 

class FlagshipPhone(SmartPhone):
    def __init__(self,brand,model,price,ram,memory,camera,security):
        super().__init__(brand,model,price,ram,memory,camera)
        self.security=security
    def full_spec(self):
        print(f"The full spec of this phone in {self.brand} {self.model} and the price is {self.price} with full security {self.security} ") 


phone1= Phone("Maharsi","Landline",4500)
sp= SmartPhone("mi","note 5",45000,"3GB","64 GB","20MP")
fp=FlagshipPhone("Samsung","S10+0",45000,"8GB","256 GB","100MP","nothing")

print(fp.brand)
print(fp.security)
print(sp.model)
print(fp.full_spec())
# print(help(FlagshipPhone))
# print(FlagshipPhone.mro())


print(isinstance(sp,SmartPhone))
print(isinstance(sp,Phone))
print(isinstance(sp,FlagshipPhone))


print(issubclass(SmartPhone,Phone))
print(issubclass(FlagshipPhone,Phone))
print(issubclass(Phone,FlagshipPhone))
print(issubclass(FlagshipPhone,FlagshipPhone))