class Car:
    def __init__(self,name,type,price,year) -> None:
        self.name = name
        self.type = type
        self.price = price
        self.year = year
# Bu get_info() metodi mashina haqida hamma malumotlarni chiqar beradi
    def get_info(self):
        return f"""Name : {self.name}
Type : {self.type}
Price: {self.price}
Year : {self.year}"""
# 1 metod yaratildi va chaqirilib ishlatildi

car = Car("Ferrari","turbo",9999999,2024)
print(car.get_info())


