08.05 4:14 PM
def countingValleys(n, u, d):
    level=valley=0
    for i in range(n):
        if(u[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
       elseif(d[I]==`D`):
            level-=1
     return valley

