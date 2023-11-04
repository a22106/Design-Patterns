from abc import ABC, abstractmethod

class Logger(ABC):
    """
    Logger 인터페이스를 정의하는 추상 기본 클래스
    
    모든 구체적인 Logger 클래스는 이 인터페이스를 구현해야 함
    """
    
    @abstractmethod
    def log(self, message):
        """
        메시지를 로그에 기록함
        """
        pass
    
class ConsoleLogger(Logger):
    """
    콘솔에 메시지를 출력하는 Logger 클래스
    """
    
    def log(self, message):
        print(f"Console Logger: {message}")
        
class FileLogger(Logger):
    """
    파일에 메시지를 출력하는 Logger 클래스
    """
    
    def log(self, message):
        print(f"File Logger: {message}")
        
        # 파일에 메시지를 기록하는 코드(생략)
        # with open("log.txt", "a") as f:
        #     f.write(f"File Logger: {message}\n")
        
class LoggerCreator(ABC):
    """
    로거 객체를 생성하는 추상 기본 클래스
    
    팩토리 메서드 패턴의 'Creator'에 해당
    """
    
    @abstractmethod
    def create_logger(self):
        """
        로거 객체를 생성하는 팩토리 메서드
        
        서브 클래스는 이 메서드를 구현하여 로거 객체를 생성해야 함
        """
        pass
    
    def log(self, message):
        """
        로거 객체를 생성하고 메시지를 로그에 기록함
        """
        logger = self.create_logger()
        logger.log(message)
        
class ConsoleLoggerCreator(LoggerCreator):
    """
    콘솔에 메시지를 출력하는 로거 객체를 생성하는 Creator 클래스
    """
    
    def create_logger(self):
        # 콘솔 로거 인스턴스를 생성하고 반환
        return ConsoleLogger()
    
class FileLoggerCreator(LoggerCreator):
    """
    파일에 메시지를 출력하는 로거 객체를 생성하는 Creator 클래스
    """
    
    def create_logger(self):
        # 파일 로거 인스턴스를 생성하고 반환
        return FileLogger()
    
def client_code(creator: LoggerCreator):
    """
    Creator 객체를 인자로 받아서 로그 메시지를 기록하는 함수
    """
    creator.log("Hello World!")
    
if __name__ == "__main__":
    # 콘솔 로거 생성자 객체 생성
    console_logger_creator = ConsoleLoggerCreator()
    # 콘솔 로거를 사용하여 메시지 기록
    console_logger_creator.log("This is a console log message")
    
    # 파일 로거 생성자 객체 생성
    file_logger_creator = FileLoggerCreator()
    # 파일 로거를 사용하여 메시지 기록
    file_logger_creator.log("This is a file log message")