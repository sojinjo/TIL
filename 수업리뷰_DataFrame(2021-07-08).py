#!/usr/bin/env python
# coding: utf-8

# # 데이터프레임(DataFrame)

# - Pandas애서 표(Table)와 같은 2차원 데이터 처리를 위해 DataFrame을 제공 
# - DataFrame은 자료(Data)를 담는 틀(Frame)
# - DataFrame을 이용하면 라벨이 있는 2차원 데이터를 생성,처리가 가능 
# - Pandas를 공부한다는 것은 결국 dataframe의 사용법을 익히고 활용하는 방법을 배운다는 것과 같다
# - 2차원 행렬 데이터에 인덱스를 붙인 것
# - 행과 열로 만들어지는 2차원 배열 구조
# - 데이프레임의 각 열은 시리즈로 구성되어 있음 : "각 열의 데이터 타입은 동일해야한다"
# - DataFrame()함수를 사용해서 생성

# ### 데이터프레임 생성:
#     - 리스트로 데이터 프레임 만들기
#         - DataFrame([[list1],[list2]])
#         - 각 List는 한 행으로 ㄱ성됨 
#         - 행의 원소 개수가 다르면 None값으로 저장 

# In[3]:


import pandas as pd
import numpy as np


# In[6]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all" #'last_expr' - 기본값


# In[6]:


# 1차원 리스트를 이용해서 df를 생성 - 원소가 각 행으로 매핑이된다 
df = pd.DataFrame(['a','b','c'])
print(df)

# 2차원 리스트를 이용해서 df를 생성 - 하위리스트가 각 행으로 매핑 
df = pd.DataFrame([['a','b','c'],["a","a","g"]]) #리스트의 리스트 (통째로 하나의 행이된다)
df


# In[7]:


# 하위리스트의 원소의 개수가 서로 다른 경우 - None 값을 저장 
df = pd.DataFrame([['a','b','c'],["a","a","g"],['a','a']]) 
df


# In[ ]:


### 딕셔너리로 데이터 프레임 생성
- dict의 key -> column name
- dict item은 데이터프레임의 column으로 정의 


# In[10]:


df1= pd.DataFrame({'A':[90,80,70],
                   'B':[85,98,75],
                   'C':[88,99,77],                   
                   'D':[87,89,86]},
                    )
df1


# In[69]:


# df의 값을 위한 dict
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}

#열방향 인덱스(컬럼명) columns=
columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']

#행방향 인덱스 index =
index=['서울','부산','인천','대구']

# pd.DataFrame(데이터,index=, columns=)

df3 = pd.DataFrame(data,index=index,columns=columns)
df3


# ### 시리즈로 데이터 프레임 생성
# -pd.DataFrame(시리즈) : 시리즈를 열로 정의 -> 1개의 시리즈가 전달 
# - 여러개의 시리즈를 이용해서 데이터 프레임 생성 : 리스트로 묶어서 전달
#     - pd.DataFrame([시리즈1,시리즈2,...]) : 리스트 원소 시리즈 1개가 한행으로 정의
# - 시리즈의 인덱스 => 컬럼명

# In[12]:


a = pd.Series([100, 200, 300], ['a', 'b', 'd'])
b = pd.Series([101, 201, 301], ['a', 'b', 'k'])
c = pd.Series([110, 210, 310], ['a', 'b', 'c'])


# In[14]:


print(pd.DataFrame(a))

pd.DataFrame([a]) #데이터는 무조건 하나로묶어서 나타내야한다(문법:pd.DataFrame(데이터,index=, columns=))


# In[15]:


pd.DataFrame([a,b,c])


# #### csv 데이터로 부터 Dataframe 생성
#  - 데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법
#  - 데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성
#  - pandas.read_csv() 함수 사용

# In[49]:


train_data = pd.read_csv('../data/train.csv')
print(train_data.shape)
train_data.head() #df의 처음 5행을 입력
train_data.head(10)
train_data.tail() #df의 마지막 5행을 출력


# #### read_csv 함수 파라미터
#  - sep - 각 데이터 값을 구별하기 위한 구분자(separator) 설정 
#  - header - header를 무시할 경우, None 설정
#  - index_col - index로 사용할 column 설정
#  - usecols - 실제로 dataframe에 로딩할 columns만 설정

# In[24]:


train_data = pd.read_csv("../data/train.csv",index_col="PassengerId",usecols=['PassengerId', 'Survived', 'Pclass', 'Name'])
train_data


# In[25]:


train_data.columns


# In[26]:


train_data.index


# #### 인덱스와 컬럼의 이해
# 
# 1. 인덱스(index)
#  - index 속성
#  - 각 아이템을 특정할 수 있는 고유의 값을 저장
#  - 복잡한 데이터의 경우, 멀티 인덱스로 표현 가능
#  
#  
# 2. 컬럼(column)
#  - columns 속성
#  - 각각의 특성(feature)을 나타냄
#  - 복잡한 데이터의 경우, 멀티 컬럼으로 표현 가능

# In[27]:


df3


# In[30]:


# df의 컬럼명(열 인덱스) 확인 - columns 속성
df3.columns


# In[29]:


# df 인덱스(행 인덱스)확인 - index 속성 
df3.index


# In[31]:


df3.index.name = "도시"
df3.columns.name = "특성"
df3


# In[37]:


# df프레임의 data값만 추출하려면 values 속성 사용하기 
df3.values
df3.values[0]


# ### dataframe 데이터 파악하기
#  - shape 속성 (row, column)
#  - describe 함수 - 숫자형 데이터의 통계치 계산
#  - info 함수 - 데이터 타입, 각 아이템의 개수 등 출력

# In[41]:


df3


# In[39]:


# data 전체 양 확인 - df.shape : (row,column)
df3.shape 


# In[43]:


df3.info()


# In[44]:


# 판다스 실수 출력 형식 변경 코드 
pd.options.display.float_format = "{:.2f}".format


# In[45]:


# DataFrame의 기본 통계량 출력 - df.describe()
df3.describe()


# In[46]:


pd.reset_option('display.float_format')


# In[47]:


train_data


# In[50]:


train_data.info()


# ### 데이터프레임 전치
# - 판다스 데이터 프레임은 전치를 포함해서 Numpy 2차원 배열에서 사용할 수 있는 속성이나 매서드를 대부분 지원함 
# - 전치 : 행과 열을 바꿈 
#         - 관련 속성 : df.T

# In[67]:


df3


# In[53]:


type(df.T)
df3.T


# In[54]:


# df3 전치
df3.T["서울"] # dtype: object


# In[ ]:


### 데이터 프레임 내용 변경 :
- 열추가,열삭제,내용갱신


# In[70]:


df3


# ### 해당열이 있으면 내용 갱신, 열이 없으면 추가
# - 열추가 : df[열이름(key)]=values
# - 열 내용 갱신 : df[열이름(key)]=values
# 

# In[71]:


# 열 내용 갱신 
# 2010-2015 증가율 변경하기
df3["2010-2015 증가율"] = df3["2010-2015 증가율"] * 100
df3


# In[81]:


# 새로운 열을 추가
df3["2005-2015 증가율"] = ((df3['2015']-df3['2005'])/df3['2005'] * 100).round(2) #2005년 대비 증가율


# In[82]:


df3


# In[83]:


del df3["2005-2015 증가율"]


# In[77]:


df3


# ### 데이터프레임 기본 인덱싱
# 1. 열기준 인덱싱
# 2. 인덱서를 사용하지않는 행기준 인덱싱
# 
# - []기호를 이용해서 인덱싱할때 주의점 : []기호는 '열 위주' 인덱싱이 원칙

# In[85]:


df3


# ### 1. 열인덱싱
# 1.열 라벨(컬럼명)을 키값으로 생각하고 인덱싱한다.
# - 인덱스로 라벨값을 하나 넣으면 시리즈 객체가 반환
# - 라벨의 배열이나 리스트를 넣으면 부분적 df 가 반환
# 

# In[87]:


#인덱스로 라벨 값 1개 사용 - 열 위주 인덱싱
type(df3["지역"])
df3["지역"]


# In[88]:


# 열 1개 접근할때는 .(다트)연산자 사용가능 :df.컬럼명
df3.지역


# In[90]:


type(df3[["지역"]])
df3[["지역"]]


# In[92]:


# 여러개의 열을 추출 - []리스트를 사용
df3[["2010","2015"]]


# ### 판다스 데이터 프레임에 열이름(컬럼명)이 문자열일 경우에는
# - 수치 인덱스를 사용할 수 없음
# - 열 인덱싱 - 위치 인덱싱 기능을 사용할 수 없다. : keyerror 발생

# - 위치 인덱싱처럼 보이는 예제

# In[96]:


np.arange(12)
np.arange(12).reshape(3,4)


# In[98]:


df5 = pd.DataFrame(np.arange(12).reshape(3,4))
df5


# In[99]:


df5


# In[100]:


df5[[1,2]]# 위치 인덱싱이 아닌 컬럼명이 숫자로 되어 있는 df의 인덱싱 


# In[102]:


#df5[[0:3]] #슬라이싱 불가!!


# ### 행 단위 인덱싱 
# - 행단위 인덱싱을 하고자 하면 인덱서라는 특수 기능을 사용하지 않는 경우 슬라이싱을 해야 함(인덱서는 바로 뒤에 배움)
# - 인덱스 값이 문자(라벨)면 문자슬라이싱도 가능하다

# In[103]:


df3


# In[105]:


df3[:1]


# In[106]:


df3[1:3]


# In[108]:


df3["서울":"인천"]


# - 개별요소 접근[열][행]

# In[109]:


df3['2015']["서울"]


# In[110]:


type(df3['2015']["서울"])


# # 데이터 프레임 인덱서 : loc, iloc
# - Pandas는 numpy행렬과 같이 쉼표를 사용한 (행 인덱스, 열 인덱스) 형식의 2차원 인덱싱을 지원
#     - 특별한 인덱서(indexer) 속성을 제공
#     
# * loc : 라벨값 기반의 2차원 인덱싱
# * iloc : 순서를 나타내는 정수 기반의 2차원 인덱싱
# 

# #### 행과 열을 동시에 인덱싱 하는 구조는 기본 자료구조 인덱스와 차이가 있음
# - df['열']
# - df[:'행'] 슬라이싱이 반드시 필요
# - df['열'][:'행']
# 

# ### 데이터 프레임에서 인덱서 사용
# #### loc, iloc 속성을 사용하는 인덱싱
# #### pandas 패키지는 [행번호,열번호] 인덱싱 불가
#     - iloc 속성 사용하면 가능
#         - iloc[행번호,열번호] - 가능
#     - loc[행제목,열제목] -가능

# In[ ]:


### loc인덱서 : 행 우선 인덱서 
- df.loc[행 인덱스 값] : 행우선 인덱싱 
- df.loc[행 인덱스 값, 열 인덱스 값]

    #### 인덱스 값 
    
    1. 인덱스 데이터(index name, column name)
    2. 인덱스 슬라이스
    3. 같은 행 인덱스를 갖는 불리언 시리즈(행 인덱싱인 경우)
        -즉, 조건식이 인덱스 값으로 사용 가능
    4. 1,2,3번 값을 반환하는 함수 
    


# In[4]:


import numpy as np
import pandas as pd


# In[9]:


#예제 df 생성
#10-21 범위의 숫자를 생성 후 3행 4열로 배치
df=pd.DataFrame(np.arange(10,22).reshape(3,4),
               index = ['a','b','c'],
               columns = ["A","B","C","D"])
df


# In[10]:


print(type(df.loc["a"]))
df.loc["a"]


# In[11]:


# 인덱스 값으로 슬라이싱 사용 
df.loc["b":"c"]


# In[12]:


df["b":"c"]  # 위 결과와 동일한 결과 출력 


# In[14]:


df.loc[["a"]]
df.loc[["a","c"]]
df.loc[["c","b","a"]] # 순서를 원하는대로 정렬도 가능 


# In[15]:


#### **boolean selection으로 row 선택하기**


# In[16]:


df


# In[17]:


df.A > 15


# In[18]:


df.loc[df.A > 15]


# In[20]:


df


# In[24]:


# 인덱스 값을 반환 하는 함수의 결과값을 사용
# 테스트 함수 작성
def sel_row(df) :
    return df.A > 15
df.A


# - loc 인덱서 슬라이싱

# In[25]:


#예제 df 생성
df2 = pd.DataFrame(np.arange(10,26).reshape(4,4),
                  columns=['a','b','c','d'])
df2 #행 인덱스 지정하지 않아서 0부터 1씩 증가되는 정수 인덱스 자동 생성


# In[26]:


df2.loc[1:2]


# In[27]:


df2[1:2]
#### 주의!!! 기본 인덱스를 사용할 경우 
#df2[1:2] # 위치 인덱싱이기 때문에 [초기위치:끝위치+1]으로 사용됨 


# #### loc 인덱서 사용해서 요소 값 접근 
# - 인덱스 값으로 행과 열을 모두 받는 경우
# - 문법 : df.loc[행 인덱스,열 인덱스]
# - 값(라벨) 인덱스 사용

# In[28]:


df


# In[29]:


df.loc["a","A"]
df["A"]["a"]


# - loc 인덱서를 사용한 원소값 변경 

# In[30]:


# a행의 A열 원소값을 50으로 변경하시오
df.loc["a","A"] = 50
df


# #### loc를 이용한 indexing 정리 

# In[32]:


# a 행의 모든 열 출력 
df.loc["a"] # 시리즈로 반환
df.loc[["a"]] # 데이터프레임으로 반환 
df.loc["a",:] # 시리즈로 반환 


# In[34]:


df.loc["a","B":"C"]
df.loc[["a"],"B":"C"]


# In[35]:


df
df.loc["a":"b"] # a,b행의 모든 열 df 형태로 반환
df.loc[["a","b"]]# a,b행의 모든 열 df 형태로 반환
df.loc[["a","b"],"B"] #a,b행의 B열 시리즈로 반환
df.loc[["a","b"],["B"]] # a,b 행의 B열 df로 반환 
df.loc[["a","b"],["B","D"]]# a,b 행의 B,D열 df로 반환 

df.loc[["a","b"],"B":"D"]# a,b 행의 B,C,D열 df로 반환


# ### iloc 인덱서(위치 인덱스)
# - 라벨(name)이 아닌 위치를 나타내는 정수 인덱스만 받는다.
# - 위치 정수값은 0부터 시작
# - 데이터프레임.iloc[행,열]

# In[36]:


df


# In[37]:


df.iloc[0,1]


# In[38]:


df.iloc[0:2] # 0행 부터 1행
df.iloc[0:1] # 0행 반환 - 데이터프레임으로 추출
df.iloc[0] # 0행 반환 - 시리즈 형태로 추출 
df.iloc[[0]] # 0행추출 - df로 추출 


# In[39]:


df.iloc[0:2,0] # 시리즈반환 (0,1행의 0열)
df.iloc[0:2,0:1] #df 반환(행,열 값 모두 슬라이싱을 사용해서) 


# In[40]:


# 위치 인덱싱이기 때문에 - 위치를 사용 가능하다 df[0:1, -2:]
df
df.iloc[0,-2] # 첫번째 행 원소의 뒤에서 두번째 원소 추출 


# In[41]:


df.iloc[0:1,-2:]

