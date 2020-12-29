sec = int(input())
min=0
min1=0
hour=0

while True:
	if sec<60:
		break
	sec-=60
	min+=1
	if min>=60:
		min=0
		min1+=1
print(min1,":",min,":",sec,sep="")