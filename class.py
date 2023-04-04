# 클래스 이해해보기
# 여러 변수들을 묶어서 관리할 수 있음.
# 여러 기능들이 있음

'''기본 블랙박스 class 만들기'''
# 클래스 명은 대문자로 시작하는 단어들의 조합으로 만들면 됨.
class BlackBox:
    # b1, b2 같은 각각의 객체를 만들 때, 초기화 해주는게 init 함수이다.
    # init 함수는 객체가 생성될 때, 자동으로 실행(호출)된다.
    def __init__(self, name, price): 
        # self.name, self.price를 맴버변수라고 하는데
        # 클래스 객체마다 멤버변수의 값은, 서로 다른 값을 가질 수 있다.
        self.name = name
        self.price = price
    
    # 메소드에 전달값이 필요하다고 하면, __init__처럼 self, 뒤에 정의
    # 1. 메소드를 정의할 때 처음 전달값은 반드시 self
    # 2. 메소드 내에서는 self.name과 같은 형태로 멤버변수를 사용
    def set_travel_mode(self, min): 
        print(f'{self.name} {min}분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000) # b1 객체 생성완료

b1.set_travel_mode(20) # 맴버변수에 접근하듯이 (객체).(메소드)()
# 실행결과: 까망이 20분 동안 여행모드 ON

'''
만약 b1 객체에만 특별한 멤버변수를 추가해주고 싶다면,
ex) b1.nickname = '1호' 이렇게 추가해준다.
이때 b1 객체가 가지고 있는 멤버변수는 3개가 되고
클래스에서는 정의되지 않은, b2는 전혀 모르는 새로운 변수인 셈이다.
'''

print(isinstance(b1,BlackBox)) # b1이 BlackBox의 인스턴스인가? True

b2 = BlackBox('하양이', 100000) # b2 객체 생성완료 (b1과 독립적)
b2.set_travel_mode(10) # 하양이 10분 동안 여행모드 ON

'''
b1.set_travel_mode(20) <- 1번 코드 
BlackBox.set_travel_mode(b1, 20) <- 2번 코드
'''

#-------------------------------------------------------------------#

'''여행 모드 지원 블랙박스 class'''
# 새로운 클래스를 만들 때마다 중복되는 코드들을 적는 것은 상당히 비효율적.
# 이를 해결하기 위해 클래스의 상속이라는 개념을 사용함.
class Original_BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

'''여행 모드 지원 블랙박스 class'''
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

'''메일 발송 기능 구현 class'''
class MailSender:
    def send(self):
        print('메일 발송')

# Original_BlackBox 클래스를 그대로 물려받음.
class TravelBlackBox(Original_BlackBox, VideoMaker, MailSender): # 다중상속
    # 그러나 상속받은 클래스에서 멤버변수 sd를 추가하고 싶다면
    # __init__ 에 매개변수 sd를 추가한다.
    def __init__(self, name, price, sd):

        # 그리고 부모 클래스의 기존 멤버변수는 그대로 이용한다는 것을 나타내준다.
        '''Original_BlackBox.__init__(self, name, price)'''

        # 그러나 아래처럼 super()를 이용해 부모 클래스를 지칭할 수 있고
        # 이때 메소드의 전달값으로 self는 필요없다.
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')

c1 = TravelBlackBox('하양이', 1230043, 64)
c1.make() # 결과: 추억용 여행 영상 제작
c1.send() # 결과: 메일 발송

'''(개선) 여행 모드 지원 블랙박스'''
# 메소드 오버라이딩
class AdvancedTravelBlackBox(TravelBlackBox):
    # set_travel_mode() 메소드가 호출되었을 때
    # 여행모드 뿐만 아니라 영상제작 및 메일발송도 동시에 해야한다면?
    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')
        # 자식 클래스 내부에서 부모 클래스의 메소드를 다시 정의할 수 있다.
        self.make()
        self.send()
'''
이처럼 부모 클래스의 메소드를 자식 클래스에서 새롭게 정의하여
기존 동작을 개선하거나 새로운 동작을 수행하도록 하는 행위를
[메소드 오버라이딩] 이라고 한다.
'''       