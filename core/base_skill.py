from abc import ABC,abstractmethod

class BaseSkill(ABC):
    @abstractmethod
    def handle(self,command:str):
        pass

    @abstractmethod
    def get_keywords(self):
        pass
    
    def can_handle(self, command: str)->bool:

        return any(word in command for word in self.get_keywords())