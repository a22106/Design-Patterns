class Singleton:
    _instance = None # 클래스 레벨에서 단일 인스턴스를 저장하는 변수
    
    def __new__(cls, *args, **kwargs):
        # 객체의 생성을 담당
        # 여기서 클래스 인스턴스가 이미 존재하는지 확인하고, 없으면 생성함
        
        if cls._instance is None:
            # 인스턴스가 없으면, 상위 클래스의 __new__ 메서드를 호출하여 인스턴스 생성
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance
    
    def __init__(self, value = None):
        if not self.initialized:
            self.value = value
            self.initialized = True
    
if __name__ == "__main__":
    # Singleton 클래스의 인스턴스 생성
    singleton1 = Singleton(value="First value")
    singleton2 = Singleton(value="Second value")
    
    # 두 객체가 같은지 확인
    print(singleton1 is singleton2) # True
    print(singleton1.value) # First value
    print(singleton2.value) # First value