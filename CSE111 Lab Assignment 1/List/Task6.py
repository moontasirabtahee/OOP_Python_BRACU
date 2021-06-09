n,k = map (int,input().split())
Member = list(map(int,input().split()))
out = []
for i in Member:
    if i <= 5-k:
        out.append(i)

print(len(out) //3) 