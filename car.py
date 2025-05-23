class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

# Methods
    def drive(self):
        print(f"you can drive  the {self.model}")

    def stop(self):
        print("stop the car")