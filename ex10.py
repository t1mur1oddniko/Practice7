prev = float(input())
count = 0  

while (curr := float(input())) != 0:  
    if curr < prev:
        count += 1  
    prev = curr  

print(count) 
