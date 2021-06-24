import pandas as pd
import matplotlib.pyplot as plt


## 한번에 그리기
plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정
folder = ['고량주','럼','보드카','위스키','전통주','지역소주','막걸리','맥주','소주','와인']
color = ['#404040','#404040','#26467F','#955900','#BD92DE','#94D33C','#BD92DE','#A46608','#94D33C','#9C071A']

for a,c in zip(folder,color):
    df = pd.read_csv('data/Filter_Data/네이버%s뉴스_2020.csv'%(str(a))) ## 데이터 불러오기
    df_groupby = df.groupby(['yyyymm']).agg('size') ## 월별 size 그룹화
    # df_groupby.plot(color=c)
    plt.plot(df_groupby,color=c)
plt.ylim(0,9000)
plt.title('주류시장') ## 타이틀 설정
plt.xlabel('2020년 월별',loc='right') 
plt.legend(['고량주','럼','보드카','위스키','전통주','지역소주'],loc='upper left', ncol = 3, fontsize=6, frameon = False)
plt.savefig('주류 월별_%s_2020.png'%(str(folder)),dpi=1000)
plt.show()



### 분리(높은거와 낮은거) 그리기
plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정
folder = ['막걸리','맥주','소주','와인']
color = ['#BD92DE','#A46608','#94D33C','#9C071A']
   
for a,c in zip(folder,color):
    df = pd.read_csv('data/Filter_Data/네이버%s뉴스_2020.csv'%(str(a))) ## 데이터 불러오기
    df_groupby = df.groupby(['yyyymm']).agg('size') ## 월별 size 그룹화
    # df_groupby.plot(color=c)
    plt.plot(df_groupby,color=c)

plt.title('주류시장') ## 타이틀 설정
plt.xlabel('2020년 월별',loc='right') 
plt.legend(['막걸리','맥주','소주','와인'],loc='upper left', ncol = 3, fontsize=6, frameon = False)
plt.savefig('PNGdata/주류 월별_%s_2020.png'%(str(folder)))
plt.show()

plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정
folder = ['고량주','럼','보드카','위스키','전통주','지역소주']
color = ['#404040','#404040','#26467F','#955900','#BD92DE','#94D33C']
   
for a,c in zip(folder,color):
    df = pd.read_csv('data/Filter_Data/네이버%s뉴스_2020.csv'%(str(a))) ## 데이터 불러오기
    df_groupby = df.groupby(['yyyymm']).agg('size') ## 월별 size 그룹화
    # df_groupby.plot(color=c)
    plt.plot(df_groupby,color=c)

plt.title('주류시장') ## 타이틀 설정
plt.xlabel('2020년 월별',loc='right') 
plt.legend(['고량주','럼','보드카','위스키','전통주','지역소주'],loc='upper left', ncol = 3, fontsize=6, frameon = False)
plt.savefig('PNGdata/주류 월별_%s_2020.png'%(str(folder)))
plt.show()