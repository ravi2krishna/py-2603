# With Abstraction -> Abstract Classes 

# Laptop Contract: Government said these are must features for building laptops 

# Abstract Class 
from abc import ABC, abstractmethod 
class Laptop(ABC):
    
    # Abstract Methods 
    @abstractmethod
    def processor(self):
        pass 
    
    @abstractmethod    
    def ram(self):
        pass
    
    @abstractmethod    
    def hdd(self):
        pass
   
    @abstractmethod       
    def nw(self):
        pass
        
# Implementations -> Companies who wants to manufacture Laptops 
class Dell(Laptop):
    
    def processor(self):
        print("Dell Laptop With Processor")
        
    def ram(self):
        print("Dell Laptop With RAM")
        
    def hdd(self):
        print("Dell Laptop With Hard Disk")    
        
    def nw(self):
        print("Dell  Laptop With Wifi")
        
class Lenovo(Laptop):
    
    def hdd(self):
        print("Lenovo Laptop With Hard Disk")    
        
    def nw(self):
        print("Lenovo Laptop With Wifi")

# TypeError: Can't instantiate abstract class Lenovo without an implementation for abstract methods 'processor', 'ram'

    def processor(self):
        print("Lenovo Laptop With Processor")
        
    def ram(self):
        print("Lenovo Laptop With RAM")
        
# End Users 
print("Customer Buying Dell Laptop")
dell = Dell()
dell.processor()
dell.ram()
# TypeError: Can't instantiate abstract class Dell without an implementation for abstract methods 'hdd', 'nw'


print("Customer Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.hdd()
lenovo.nw()
