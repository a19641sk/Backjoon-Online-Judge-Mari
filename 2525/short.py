h,m=map(int,input().split());n=60*h+m+int(input());print(n//60%24,n%60)
#h,m=map(int,input().split());t=int(input());n=(60*h+m+t)%1440;print('{:02d}'.format(n//60),'{:02d}'.format(n%60))