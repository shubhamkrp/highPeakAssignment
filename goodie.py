
filename = "input3.txt"

with open(filename, 'r') as f:
    content=f.readlines()

#store the content of file as an array line by line and remove any extra spaces
content=[x.strip() for x in content]

#print(content)
k=content[0][21]
try:
    k=int(k)
except:
    print("Error")
#print(k)
original_dict={}
for i in range(4,len(content)):
    key,value=content[i].split(":")
    original_dict[key]=int(value)

sorted_dictionary=dict(sorted(original_dict.items(), key = lambda kv:(kv[1], kv[0])))
#print(sorted_dictionary)
price=[]
for i in sorted_dictionary.values():
    price.append(i)
#print(price)
n=len(sorted_dictionary)
mini=0 #minimum price of goodie to be distributed
maxi=0 #maximum price of goodie to be distributed
#to store the minimum difference between the chosen goodie with highest price and the lowest price
result = +2147483647
temp=0
for i in range(n-k+1):
    if result>price[i+k-1] - price[i]:
        
        result=price[i+k-1] - price[i]
        if temp!=result:
            mini=price[i]
            maxi=price[i+k-1]
    
#print(result)

f = open("output3.txt", "w")
f.write("Here the goodies that are selected for distribution are:\n\n")
for i,j in sorted_dictionary.items():
    if int(j)>=mini and int(j)<=maxi:
        f.write(str(i)+": "+str(j)+"\n")

f.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(result))
    
f.close()

