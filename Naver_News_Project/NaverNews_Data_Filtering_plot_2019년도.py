import pandas as pd
import matplotlib.pyplot as plt

folder = ['고량주','럼','막걸리','맥주','보드카','소주','와인','위스키','전통주','지역소주']
 
for a in folder:
    df = pd.read_csv('data/네이버%s뉴스_2019년도.csv'%(str(a))) ## 데이터 불러오기
    df = df.drop_duplicates(subset=None,keep='first',inplace=False) ## 중복값 제거
    df.columns=['num','yyyymmdd','names','title','text'] ## 컬럼이름 변경
    df['yyyymm'] = df['yyyymmdd'].apply(lambda x: x[0:7]) ## yyyymm 컬럼생성
    df['mm'] = df['yyyymmdd'].apply(lambda x: x[5:7]) ## mm 컬럼생성

    ## 2021년 1월 데이터 삭제 ##
    df_drop = df[df['yyyymm']=='2020.01'].index
    df = df.drop(df_drop)
    df_drop = df[df['yyyymm']=='2018.12'].index
    df = df.drop(df_drop)
    ###########################
    df.to_csv('data/Filter_Data/네이버%s뉴스_2019.csv'%(str(a)))

plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정
folder = ['고량주','럼','막걸리','맥주','보드카','소주','와인','위스키','전통주','지역소주']
color = ['#404040','#404040','#BD92DE','#A46608','#26467F','#94D33C','#9C071A','#955900','#BD92DE','#94D33C']

for a,c in zip(folder,color):
    df = pd.read_csv('data/Filter_Data/네이버%s뉴스_2019.csv'%(str(a))) ## 데이터 불러오기
    df_groupby = df.groupby(['yyyymm']).agg('size') ## 월별 size 그룹화
    df_groupby.plot(color=c)
    
plt.title('주류시장') ## 타이틀 설정
plt.xlabel('2019년 월별',loc='right') 
plt.legend(['고량주','럼','막걸리','맥주','보드카','소주','와인','위스키','전통주','지역소주'],loc='upper left', ncol = 3, fontsize=6, frameon = False)
plt.show()