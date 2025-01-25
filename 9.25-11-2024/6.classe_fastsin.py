from math import sin, radians, floor, ceil

class FastSin:
    def __init__(self):
        self.sin_values = [sin(radians(i)) for i in range(360)] 
    
    def eval(self, x: float) -> float:
        if x == int(x): 
            return self.sin_values[int(x)]
        
        x_floor = floor(x) 
        x_ceil = ceil(x)    
      
        sin_floor = self.sin_values[x_floor]  
        sin_ceil = self.sin_values[x_ceil]
        
        return sin_floor + (x - x_floor) * (sin_ceil - sin_floor) / (x_ceil - x_floor)

fast_sin = FastSin() 

print(fast_sin.eval(30)) 
print(fast_sin.eval(45.5))  
print(fast_sin.eval(90)) 
print(fast_sin.eval(180.2))  