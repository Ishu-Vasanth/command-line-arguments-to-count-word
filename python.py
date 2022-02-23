import sys
fp = open(sys.argv[1])
count=0
for data in fp:
    l=data.split()
    for i in l:
        count+=1
print("No of words in the file:",count)
