import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family']='gulim'

folder = ['고량주','럼','막걸리','맥주','보드카','소주','와인','위스키','전통주','지역소주']
for a in folder:
    df = pd.read_csv('data/네이버%s뉴스.csv'%(str(a)))
    df = df.drop_duplicates(subset=None,keep='first',inplace=False)
    df.columns=['num','yyyymmdd','names','title','text']
    df['yyyymm'] = df['yyyymmdd'].apply(lambda x: x[0:7])
    df.shape
    
    ## 2021년 1월 데이터 삭제
    df_drop = df[df['yyyymm']=='2021.01'].index
    df = df.drop(df_drop)

    df_groupby = df.groupby(['yyyymm']).agg('size')
    #df_groupby2 = df.groupby(['yyyymmdd']).agg('size')
    df_groupby.plot()
    plt.xlabel('2020년도 월별')
    plt.legend(['고량주','럼','막걸리','맥주','보드카','소주','와인','위스키','전통주','지역소주'],loc='upper left', ncol = 3, fontsize=7, frameon = False)
plt.show()

folder = ['고량주','럼','보드카','위스키','전통주','지역소주']
for a in folder:
    df = pd.read_csv('data/네이버%s뉴스.csv'%(str(a)))
    df = df.drop_duplicates(subset=None,keep='first',inplace=False)
    df.columns=['num','yyyymmdd','names','title','text']
    df['yyyymm'] = df['yyyymmdd'].apply(lambda x: x[0:7])
    df.shape
    ## 2021년 1월 데이터 삭제
    df_drop = df[df['yyyymm']=='2021.01'].index
    df = df.drop(df_drop)


    df_groupby = df.groupby(['yyyymm']).agg('size')
    # df_groupby.columns[a]
    df_groupby.plot()
    plt.xlabel('2020년도 월별')
    plt.legend(['고량주','럼','보드카','위스키','전통주','지역소주'],loc='upper left', ncol = 3, fontsize=7, frameon = False)
plt.show()