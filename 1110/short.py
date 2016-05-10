def c(n):
 S=str(n);return[S,'0'+S][n<10]
i=int;n=o=c(i(input()));t=0
while 1:
 n=c(i(n[1])*10+(i(n[0])+i(n[1]))%10);t+=1
 if n==o:break;
print(t)