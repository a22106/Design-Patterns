class SingletonMeta(type):
    """
    메타클래스는 SIngleton 패턴을 구현하는데 사용된다.
    """
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """
        클래스를 호출할 때마다, 같은 인스턴스를 반환한다.
        cls(클래스 자신) 인스턴스가 이미 존재하는지 확인하고, 없으면 생성함.
        """
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    """
    이 클래스는 모든 싱글톤의 베이스 클래스가 된다.
    Singleton 클래스는 SingletonMeta 클래스에 의해
    단일 인스턴스만 생성되게 보장한다.
    """
    
    def __init__(self, value):
        # 클래스 인스턴스 초기화. 
        # 'value' 매개변수는 싱글톤의 데이터(인스턴스 변수)로 사용됨
        self.value = value
        
    def some_business_logic(self):
        """
        싱글톤의 메서드는 싱글톤 데이터에 접근할 수 있다.
        """
        
        # 비즈니스 로직 구현...
        pass
    
if __name__ == "__main__":
    # 객체 생성, 값 할당
    singleton = Singleton("Initial value")
    
    # 같은 클래스로 새 객체 생성
    another_singleton = Singleton("Second value")
    
    # 두 변수가 같은 객체를 가리키는지 확인
    print(singleton is another_singleton) # True
    
    # 처음 할당한 값 "Initial value"가 여전히 인스턴스에 저장되어 있는지 확인
    print(singleton.value) # Initial value