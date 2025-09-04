word=input().strip()
a=input().strip()
b=input().strip()
count=0
for i in range(len(word)-1):
    if word[i]==a and word[i+1]==b:
        count+=1
print(count)