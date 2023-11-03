from icecream import ic
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    추상 핸들러 클래스: 모든 구체적인 핸들러들이 상속받아야 할 추상 기반 클래스
    """
    
    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        """
        체인의 다음 객체를 설정함
        - handler: 다음에 수행될 핸들러 객체
        """
        pass
    
    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        """
        요청을 처리하거나 다음 객체로 넘김
        - request: 처리할 요청
        """
        pass
    
class AbstractHandler(Handler):
    """
    핸들러의 기본 기능을 제공하는 추상 핸들러
    """
    
    _next_handler: Optional[Handler] = None
    
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # 다음 객체를 반환하여 체인 형성
        return handler
    
    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        # 다음 객체가 존재하면 다음 객체의 handle 메서드를 호출하여 요청을 넘김
        if self._next_handler:
            return self._next_handler.handle(request)
        
        # 체인의 끝에 도달하면 None 반환
        return None
    
class MonkeyHandler(AbstractHandler):
     
     def handle(self, request: Any) -> Optional[str]:
         if request == "Banana":
             # 바나나를 먹을 수 있는 원숭이(요청 Banana를 처리하고 결과 반환)
             return f"Monkey: I'll eat the {request}"
         else:
             # 요청 Banana가 아니면 체인의 다음 객체로 요청을 넘김
             return super().handle(request)
         
class SquirrelHandler(AbstractHandler):
     
     def handle(self, request: Any) -> Optional[str]:
         if request == "Nut":
             # 견과류를 먹을 수 있는 다람쥐(요청 Nut을 처리하고 결과 반환)
             return f"Squirrel: I'll eat the {request}"
         else:
             # 요청 Nut이 아니면 체인의 다음 객체로 요청을 넘김
             return super().handle(request)
         
if __name__ == "__main__":
    # 핸들러 객체 생성
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    
    # 체인 형성
    monkey.set_next(squirrel)
    
    print("Example1: 체인의 첫 번째 객체에서 요청을 처리하고 결과 출력")
    ic(monkey.handle("Nut"))
    ic(monkey.handle("Banana"))
    
    # 결과
    # Squirrel: I'll eat the Nut
    # Monkey: I'll eat the Banana
    
    print("Example2: 체인의 첫 번째 객체에서 요청을 처리하고 결과 출력")
    for request in ["Nut", "Banana", "Cup of coffee"]:
        print(f"Client: Who wants a {request}?")
        result = monkey.handle(request)
        if result:
            print(f"  {result}")
        else:
            print(f"  {request} was left untouched.")
            
    # 결과
    # Client: Who wants a Nut?
    #   Squirrel: I'll eat the Nut
    # Client: Who wants a Banana?
    #   Monkey: I'll eat the Banana
    # Client: Who wants a Cup of coffee?
    #   Cup of coffee was left untouched.
    