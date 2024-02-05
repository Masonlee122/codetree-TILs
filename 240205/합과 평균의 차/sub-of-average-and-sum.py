a,b,c = map(int,input().split())

sum_ = a+b+c
avg_ = int(sum_/3)
sub_ = sum_ - avg_

print(sum_,avg_,sub_,sep='\n')