# 변수 선언
name = "홍길동"
age = 25
height = 175.5
is_student = True

print("=== 변수 출력 ===")
print(name)
print(age)
print(height)
print(is_student)

# 자료형 확인
print("\n=== 자료형 확인 ===")
print(type(name))       # str (문자열)
print(type(age))        # int (정수)
print(type(height))     # float (실수)
print(type(is_student)) # bool (불리언)

# 문자열
print("\n=== 문자열 ===")
greeting = "안녕하세요, " + name + "!"
print(greeting)
print(f"저는 {age}살이고 키는 {height}cm입니다.")  # f-string

# 숫자 연산
print("\n=== 숫자 연산 ===")
print(10 + 3)   # 더하기
print(10 - 3)   # 빼기
print(10 * 3)   # 곱하기
print(10 / 3)   # 나누기 (실수)
print(10 // 3)  # 나누기 (정수)
print(10 % 3)   # 나머지
print(10 ** 3)  # 거듭제곱

# 리스트
print("\n=== 리스트 ===")
fruits = ["사과", "바나나", "포도"]
print(fruits)
print(fruits[0])        # 첫 번째 요소
fruits.append("딸기")   # 요소 추가
print(fruits)

# 딕셔너리
print("\n=== 딕셔너리 ===")
person = {"이름": "홍길동", "나이": 25, "직업": "학생"}
print(person)
print(person["이름"])
person["도시"] = "서울"  # 키 추가
print(person)
