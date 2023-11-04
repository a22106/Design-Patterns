from abc import ABC, abstractmethod
from typing import Dict

class Command(ABC):
    """
    커멘드 인터페이스: 모든 구체적인 커멘드들이 상속받아야 할 추상 기반 클래스
    """
    
    @abstractmethod
    def execute(self) -> None:
        """
        커멘드 실행 메서드
        """
        pass
    
    def undo(self) -> None:
        """
        커멘드 실행 취소 메서드
        """
        pass
    
    
class LightOnCommand(Command): # ConcreteCommand
    """
    커멘드의 구체적인 구현 클래스()
    '라이트를 켜는' 커멘드
    """
    
    def __init__(self, light) -> None:
        self._light = light
        
    def execute(self) -> None:
        # 커멘드 실행 메서드: Light 객체의 on 메서드를 호출하여 불을 켬
        self._light.on()
        
    def undo(self) -> None:
        # 커멘드 실행 취소 메서드: Light 객체의 off 메서드를 호출하여 불을 끔
        self._light.off()
        
class LightOffCommand(Command): # ConcreteCommand
    """
    커멘드의 구체적인 구현 클래스()
    '라이트를 끄는' 커멘드
    """
    
    def __init__(self, light: Light) -> None:
        self._light = light
        
    def execute(self) -> None:
        # 커멘드 실행 메서드: Light 객체의 off 메서드를 호출하여 불을 끔
        self._light.off()
        
    def undo(self) -> None:
        # 커멘드 실행 취소 메서드: Light 객체의 on 메서드를 호출하여 불을 켬
        self._light.on()
        
class Light: # Receiver Class
    """
    커멘드가 호출할 실제 객체
    """
    
    def on(self) -> None:
        print("Light is on")
        
    def off(self) -> None:
        print("Light is off")
        
class RemoteControl: # Invoker Class
    """
    커맨드 객체를 저장하고 요청을 실행하는 클래스
    """
    
    def __init__(self) -> None:
        self._commands: Dict[str, Command] = {}
        
    def register(self, command_name: str, command: Command) -> None:
        """
        커멘드를 등록하는 메서드
        - command_name: 커멘드 이름
        - command: 등록할 커멘드
        """
        self._commands[command_name] = command
        
    def execute(self, command_name: str) -> None:
        """
        커멘드를 실행하는 메서드
        - command_name: 실행할 커멘드 이름
        """
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not found")
            
    def undo(self) -> None:
        """
        실행 취소 메서드
        """
        pass
    
if __name__ == "__main__":
    # 리시버 객체 생성
    light = Light()
    
    # 커멘드 객체 생성
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    
    # 인보커 객체 생성
    remote = RemoteControl()
    
    # 커멘드 등록
    remote.register("ON", light_on)
    remote.register("OFF", light_off)
    
    # 커멘드 실행
    remote.execute("ON")
    remote.execute("OFF")
    
    # 커멘드 실행 취소
    remote.undo()