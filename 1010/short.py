f=lambda n,k:k<1or f(n-1,k-1)*n//k;i=input;exec(int(i())*'k,n=map(int,i().split());print(f(n,k));')