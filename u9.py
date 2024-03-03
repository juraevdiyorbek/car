class Car:
    def __init__(self,name,type,price,year) -> None:
        self.name = name
        self.type = type
        self.price = price
        self.year = year

    def get_info(self):
        return f"""Name : {self.name}
Type : {self.type}
Price: {self.price}
Year : {self.year}"""
    

car = Car("Ferrari","turbo",9999999,2024)
print(car.get_info())


