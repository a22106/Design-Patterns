# 메타클래스 방식 싱글톤 패턴

from abc import ABC, abstractmethod

class Product(ABC):
    """
    Product 인터페이스
    모든 구체적인 제품들이 상속받아야 할 추상 기반 클래스
    """
    
    @abstractmethod
    def use(self) -> str:
        """
        제품 사용
        """
        pass
    
class ConcreteProductA(Product):
    def use(self) -> str:
        return "Using product A"
    
class ConcreteProductB(Product):
    def use(self) -> str:
        return "Using product B"
    
class Creator(ABC):
    """
    Creator 추상 클래스
    모든 구체적인 생성자들이 상속받아야 할 추상 기반 클래스
    """
    
    @abstractmethod
    def factory_method(self) -> Product:
        """
        제품을 생성하는 팩토리 메서드
        """
        pass
    
    def some_operation(self) -> str:
        """
        일부 기본 로직을 구현하는 메서드
        생성된 제품 객체를 사용
        팩토리 메서드를 호출하여 제품 객체를 얻음
        """
        product = self.factory_method()
        # 제품 객체를 사용
        result = f"Creator: The same creator's code has just worked with {product.use()}"
        return result
    
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()
    
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()
    
def client_code(creator: Creator) -> None:
    """
    Creator 객체를 인자로 받아서 일부 기본 로직을 수행하는 함수
    팩토리 메서드를 호출하여 제품 객체를 생성 예시
    """
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="\n\n")
    
    