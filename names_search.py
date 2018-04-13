
n=int(input())
names=[[0 for x in range(35)] for y in range(0,n)]
for i in range(0,n):
	names[i]=input()
flag=0
s=str(input())
for i in range(0,n):
	if str(names[i])==s:
		print('Position', i+1)
		flag=1
		
if flag==0:
	print('Not Found')