import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumGothic' # 폰트 설정

folder = ['고량주','럼','막걸리','맥주','보드카','소주','와인','위스키','전통주','지역소주']
color = ['#404040','#404040','#BD92DE','#A46608','#26467F','#94D33C','#9C071A','#955900','#BD92DE','#94D33C']
   
for a in folder:

    df = pd.read_csv('data/Filter_Data/네이버%s뉴스_2020.csv'%(str(a))) 
    df2 = pd.read_csv('data/Filter_Data/네이버%s뉴스_2019.csv'%(str(a))) 
    df_groupby = df.groupby(['mm']).agg('size') ## 월별 size 그룹화
    df2_groupby = df2.groupby(['mm']).agg('size')
    
    plt.plot(df_groupby)
    plt.plot(df2_groupby)
    plt.title(a) ## 타이틀 설정
    plt.legend(['2020년도','2019년도']) 
    plt.show()

