class Car(object):
    def __init__(self,model,color,company):
        self.model=model
        self.color=color
        self.company=company
    
    def start(self):
        print("car is started")

    def stop(self):
        print("car is Stopped")

rollsroyce =Car("ghost","golden","rolls royce")
print(rollsroyce.color)