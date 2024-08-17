### 문자열을 구성 요소로 가진 리스트의 경우는 숫자 리스트와 같이 사용이 가능하다

n = int(input())

lst = [input() for _ in range(n)]

lst.sort()

for i in lst:
    print(i)