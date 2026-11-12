from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
    
    @abstractmethod
    def get_shipping_details(self):
        pass