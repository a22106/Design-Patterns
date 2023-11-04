from abc import ABC, abstractmethod

class Button(ABC):
    """
    Button 인터페이스
    모든 구체적인 버튼들이 상속받아야 할 추상 기반 클래스
    """
    
    @abstractmethod
    def render(self) -> str:
        """
        버튼 렌더링
        """
        pass
    
    @abstractmethod
    def on_click(self) -> str:
        """
        버튼 클릭
        """
        pass
    
class WindowsButton(Button):
    def render(self) -> str:
        return "Windows Button"
    
    def on_click(self) -> str:
        return "Windows Button Clicked"
    
class HTMLButton(Button):
    def render(self) -> str:
        return "HTML Button"
    
    def on_click(self) -> str:
        return "HTML Button Clicked"
    
class Dialog(ABC):
    """
    Dialog 추상 클래스
    모든 구체적인 다이얼로그들이 상속받아야 할 추상 기반 클래스
    """
    
    @abstractmethod
    def create_button(self) -> Button:
        """
        버튼 생성
        """
        pass
    
    def render(self) -> str:
        """
        다이얼로그 렌더링
        """
        # 다이얼로그에 대한 기본 렌더링 로직
        ok_button = self.create_button()
        ok_button_rendered = ok_button.render()
        ok_button_on_click = ok_button.on_click()
        result = f"Dialog: {ok_button_rendered} | {ok_button_on_click}"
        return result
    
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()
    
class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()
    
def client_code(dialog: Dialog) -> None:
    """
    Dialog 객체를 인자로 받아서 일부 기본 로직을 수행하는 함수
    팩토리 메서드를 호출하여 제품 객체를 생성 예시
    """
    print(dialog.render())
    
if __name__ == "__main__":
    # Dialog 객체 생성
    windows_dialog = WindowsDialog()
    web_dialog = WebDialog()
    
    # Dialog 렌더링
    print("Example1: Windows Dialog")
    client_code(windows_dialog)
    print()
    
    print("Example2: Web Dialog")
    client_code(web_dialog)
    print()