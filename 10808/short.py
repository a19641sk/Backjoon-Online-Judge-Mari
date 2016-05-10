i=input();t=''
for r in range(26):t+='i.count(chr(97+%d)),'%r
exec('print('+t+')')