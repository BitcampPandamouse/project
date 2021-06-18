import pandas as pd
import matplotlib.pyplot as plt

## 폰트 설치
plt.rcParams['font.family']='gulim'



## 데이터 불러오기
df = pd.read_csv('data/네이버주류시장뉴스test.csv')

# 1. colums 수정
df.columns=['num','yyyymmdd','names','title','text']

# 2. 중복값 제거
df = df.drop_duplicates(subset=None,keep='first',inplace=False)
df.info()

# 3. 그룹화(날짜별)
df_groupby = df.groupby(['yyyymm']).size()

df_groupby.plot()

# 저장
df.to_csv('./data/네이버%s결과피터링.csv'%("맥주"), index=False)
