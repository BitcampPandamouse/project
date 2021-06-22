import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

searchnmae = '와인'
year='2020'

## 데이터 불러오기기
data = pd.read_csv('data/Filter_Data/네이버%s뉴스_%s.csv'%(str(searchnmae),str(year)),index_col=0)

## 폰트 설정
fp='./utils/NanumGothic.ttf'

## 단어 정렬
text = ''.join(v for v in data['title'])

## 삭제할 단어 추가
stopwords = ['등','더','종합','운세']

## mask
mask= np.array(Image.open('bear.png'))

## wordcloud 설정
wordcloud = WordCloud(font_path=fp, # 폰트 지정
                      background_color='white', # 배경화면 색상 설정
                      max_words=100,            # 최대 단어 갯수
                      stopwords=stopwords).generate(text)

plt.figure(figsize = (16,9)) # word cloude 크기 설정
plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear') 
plt.savefig('%swordcloud_%s.png'%(str(searchnmae),str(year)))
plt.show()

# https://hyomyo.tistory.com/68