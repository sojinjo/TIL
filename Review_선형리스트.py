## 선형리스트예시

katok =[]

def add_data(friend) :
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

add_data("다현")
add_data("정연")
add_data("쯔위")
add_data("사나")
add_data("지효")

print(katok)

print("-------------------------------------------------")

katok = ['다현', '정연', '쯔위', '사나', '지효','모모']

def insert_data(position,friend) :
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1,position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend
insert_data(3,"미나")
print(katok)

print("-------------------------------------------------")

katok = ['다현', '정연', '쯔위', '사나', '지효']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1,kLen,1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

delete_data(1)
print(katok)

print("-------------------------------------------------")







