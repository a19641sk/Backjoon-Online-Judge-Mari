s,m=0,100;exec(7*'i=int(input());\nif(i%2):s+=i;m=min(m,i);\n');
if s==0:print('-1')
else:print(s);print(m)