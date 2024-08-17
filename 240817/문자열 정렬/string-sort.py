### 문자열 내 문자 정렬

## 문자열의 정렬의 경우는 sort() 함수를 사용할 수 없다 -> sort는 리스트의 경우만 사용 가능하다
## 해결 방법
## 1. 문자열을 리스트로 변환 후에 다시 문자열로 변경하기 (list(str) ->.join(list(str)))
## 2. sorted 함수 사용 : 결과값이 리스트이므로 다시 문자열로 변경해주어야 한다

str_ = input()

sorted_lst= sorted(str_)
sorted_str = "".join(sorted_lst)
print(sorted_str)