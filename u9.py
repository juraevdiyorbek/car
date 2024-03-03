class Car:
    def __init__(self,name,type,year,price = 4000) -> None:
        self.name = name
        self.type = type
        self.price = price
        self.year = year

    # Bu get_info() metodi mashina haqida hamma malumotlarni chiqar beradi
    def get_info(self):
        return f"""Name : {self.name}
Type : {self.type}
Price: ${self.price}
Year : {self.year}"""
# 1 metod yaratildi va chaqirilib ishlatildi
    def setInfo(self,name,type,year,price = 4000):
        self.name = name
        self.type = type
        self.year = year
        self.price = price
        return self.name,self.type,self.year,self.price
    
car = Car("Ferrari","turbo",2024,200000)

my_dict = dict()
lst = list()
for i in range(10):
    name = input("name : ")
    typee = input("type : ")
    year = int(input("year : "))
    price = input("price : ")
    my_dict[i] = car.setInfo(name,typee,year,price)
    lst.append(my_dict[i])
lst.sort(key=lambda x : x[2])

print(lst)

