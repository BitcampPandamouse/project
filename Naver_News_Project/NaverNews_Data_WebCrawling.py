from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
from itertools import count
import urllib.request
import pandas as pd
import datetime
import ssl



searchname = '맥주'
numbers = int(1)


result = []
dateformat = "%Y.%m.%d"
dateformatnso = "%Y%m%d"
today = datetime.datetime.now()

## url 오류 문자 확인 구문
context = ssl._create_unverified_context()
def get_request_url(url,enc='utf-8'):
    response = urllib.request.urlopen(url)
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now() + tmp + searchname+ "(" +str(page+1)+")")
            return response.read().decode(enc)
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None



#날짜 반복 구문(월단)
for num in count():
    tm = today - relativedelta(months=num+1)
    tmp = tm.strftime(dateformat)
    tmpnso = tm.strftime(dateformatnso)
    beday= today - relativedelta(months=(num+2))
    bmp = beday.strftime(dateformat)
    bmpnso = beday.strftime(dateformatnso)
    
    # 입력한 월이 카운트 num를 넘으면 break
    if num > int(numbers)-int(1):
        break

    #url 반복문
    for page in count():
        endpoint = 'https://search.naver.com/search.naver'
        params = '?where=news&sm=tab_jum'                       
        params += '&query=' + urllib.parse.quote(searchname)   
        params += '&sort=1'                                   
        params += '&ds=' + tmp                                  
        params += '&de=' + bmp                                  
        params += '&start=' + str(page)+str(1)                 
        params += '&nso=so%3Add%2Cp%3Afrom' + tmpnso + 'to' + bmpnso
        url = endpoint+params
        # print(url)
        if page > 399:
            print("뉴스의 개수가 4000개가 넘었습니다.")
            break
        
        #endpage '찾을수없음' 오류 해결 <4000개일 때 
        try: 
            respone = get_request_url(url)
            soupData = BeautifulSoup(respone, 'html.parser')
            table = soupData.find('ul',{'class' : 'list_news'})
            uls = table.find_all('div',{'class':"news_area"})
            
            #자료추출 반복문
            for store in uls:
                title = store.find('a', {'class' : 'news_tit'}).text
                yyyymm = store.find('span',{'class':"info"}).text
                if yyyymm.endswith('P') == True:
                    continue
                elif yyyymm.endswith(str('단')) == True:
                    continue
                content = store.find('a',{'class':"api_txt_lines dsc_txt_wrap"}).text
                
                ## 서울파이낸스는 다른 태그 명을 가지고 있다
                try:
                    namees = store.find('a',{'class':'info press'}).text
                except AttributeError as e:
                    break
                result.append([yyyymm]+[title]+[content]+[url])

        except AttributeError as e:
            break

df =pd.DataFrame(result)
df.to_csv("./data/test/네이버%s뉴스test.csv" %(searchname))




## 2020년 1월 1일 ~ 2021년 1월 1일


# 맥주, 소주, 와인, 전통주, 위스키, 럼, 보드카, 막걸리, 청주, 지역소주, 고량주,
# 발효주(막걸리랑 같이 동시 필터링) 중복값 제거

## 