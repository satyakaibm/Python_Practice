with open("IPfile.txt",'r') as filed:
    ipadd = filed.readlines()
    ipa = []
    for line in ipadd:
        ipadr = line.split("-")
        ipa.append(ipadr[0])

ipa.sort()
ip={}
count=1
for i in (ipa):
    if i in ip:    
        count = count+1
        ip[i] = count        
    else:
        count = 1
        ip[i] = count

for i,v in ip.items():
    print(i,v)
