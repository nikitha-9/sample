# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1

for i in range(1,6):
    for j in range(1,6):
        print("(",i,",",j,")",end=" ")
    print()
print()


for i in range(1,6):
    for j in range(1,6):
        
        print(min(i,6-i,j,6-j),end=" ")
    print()

    
        