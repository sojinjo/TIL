##1.선형리스트 예시
def add_data(friend):
    katok.append(friend)
    kLen=len(katok)
    katok[kLen-1] = friend

def insert_data(position,friend):
    katok.append(None)
    kLen=len(katok)

    for i in range(kLen-1,position,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position]=friend

def delete_data(position):
    kLen=len(katok)
    katok[position]=None

    for i in range(position+1,kLen,1):
        katok[i-1]=katok[i]
        katok[i]=None

    del(katok[kLen-1])



##2.
katok=[]
select=-1


##3.
if __name__ == "__main__" :

    while (select != 4) :
        select = int(input("선택(1~4) -->"))

        if (select ==1) :
            data= input("추가할 데이터 -->")
            add_data(data)
            print(katok)
            # pass # 추가 관련 코드

        elif (select == 2) :
            position = int(input("삽입할 위치-->"))
            data = input("추가할 데이터 -->")
            insert_data(position,data)
            print(katok)
            # pass # 삽입 관련코드

        elif (select == 3) :
            position = int(input("삭제할 위치 -->"))
            delete_data(position)
            print(katok)
            # pass # 삭제 관련 코드

        elif (select == 4) :
            print(katok)
            exit
            # pass # 종료 관련 코드

        else :
            print("1~4중에 입력하세요")
            continue