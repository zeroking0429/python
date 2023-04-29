'''
2023.04.29
kim se yeong
조건문 연습 if, if-else
#문제 정의
    입력받은 성적이 90이상이면 "합격", 아니면 "불합격"을 출력
#문제 분석
    변수-Score(score)
#알고리즘
    1. 변수 선언
        score에 점수를 정수로 입력
    2. 프로그램 논리(선택 : if-else)
        (조건식)
        [
            if score >= 90:
                print("합격")
            else:
                print("불합격")
        ]
'''

score = int(input("input score : "))
if score >= 90: # 조건식
    print("합격") # True
else:
    print("불합격") # False

print("수고했습니다.") # always