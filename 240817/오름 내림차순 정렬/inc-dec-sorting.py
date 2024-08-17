## 정렬은 보통 리스트를 활용하여 정렬 또는 딕셔너리를 활용한 정렬이 있다
## 1. 리스트를 활용한 정렬
## 리스트 함수를 활용 : 오름차순 방식에 sort / 내림차순에는 reverse = True 값을 적용한 sort 함수 사용한다
## 리스트를 반환하는 함수 사용 : sorted 함수를 활용


## 문제 1번 
n  = int(input())
lst = list(map(int,input().split()))

lst1 = sorted(lst)
lst2 = sorted(lst,reverse=True)

print(*lst1)
print(*lst2)