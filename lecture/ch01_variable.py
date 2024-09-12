#주석(comment): 실행X, 메모
print("hello")  # 주석을 달아주세요.

#1.출력함수(print)
#   - ()값을 출력
#   - 변수값 확인 용도로 많이 활용
# c언어
#   - ''(char) - 문자형
#   - ""(string) - 문자열형
# Python
#   - '' or "" - 문자열형(string)
print('hello')
print("hello")

# 2. Escape Code(문자열과 함께 사용)
#   - \n: 한 줄 개행
#   - \t: 탭(기본: 8칸)
print("hello \tpython")
print("hello \npython")

# 3. 자료형(Type)
#   - Python의 모든 자료형은 객체(Object)
#   - 정수형(int)        : 3, -1, 0
#   - 실수형(float)      : 3.14, 0.0, -2.2
#   - 문자열(String)     : "Hi", 'Hi'
#   - 논리형(Boolean)    : True, False

# 4. 형 변환(Type Casting)
#   - 원하는 자료형으로 변환
#   - int()
#   - float()
#   - str()
#   - * 큰자료형 -> 작은자료형 변환(조심! 값의 손실이 생김)
#   - int("3.14") -> ERROR

# 5. 변수 선언 및 초기화
#   - num = 5
#   - type을 정의 하지 않음(동적 타이핑 언어)
#   - =(대입연산자): 우측의 값을 좌측에 대입