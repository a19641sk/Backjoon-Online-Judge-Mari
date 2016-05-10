t=input();n=''
for i in t:
	o=ord(i)
	if 64<o<78 or 96<o<110:n+=chr(o+13)
	elif 77<o<91 or 109<o<123:n+=chr(o-13)
	else:n+=i
print(n)