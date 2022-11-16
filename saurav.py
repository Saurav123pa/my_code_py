n=int(input())
x=int(input())
y=int(input())
z=int(input())
combination=[[x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1)]
ans=list(filter(lambda x:sum(x),combination))
print(ans)
