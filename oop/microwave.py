class Microwave:
    def __init__(self,brand:str,power_rating:str) -> None:
        self.brand = brand
        self.power_rating = power_rating

    def __str__(self):
        return f'{self.brand} - {self.power_rating}'