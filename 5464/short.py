p=input;i=int;r=range;q=[];S=[];N,M=map(i,p().split());W=[0];m=0
def c(I):
 global m,q
 for s in r(N):
 	if S[s][0]==0:S[s][0]=I;m+=S[s][1]*W[I];break;
 	if s==N-1:q+=[I]
for _ in r(N):S+=[[0,i(p())]]
for _ in r(M):W+=[i(p())]
for _ in r(2*M):
 I=i(p())
 if I>0:c(I);
 else:
 	for s in r(N):
 	 if S[s][0]==-I:S[s][0]=0
 	if q!=[]:c(q[0]);q=q[1:]
print(m)
