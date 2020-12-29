sec=46979
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
	print(min1)
	if min1>=60:
		min1=0
		hour+=1
print(hour,":",min1,":",sec)