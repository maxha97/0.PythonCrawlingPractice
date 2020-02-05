from bs4 import BeautifulSoup
import re
from urlToStr import urlToStr
from datetime import date, time, datetime, timedelta
from func import fileToStr
import json


import matplotlib.pyplot as plt
from matplotlib import font_manager, rc 
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() 
rc('font', family=font_name)

# for y in range(s, f+1):
#         print(str(y) + "년도 박스오피스 영화 및 평점")

# def viewDate():
#     ctime = datetime.now() - timedelta(days=1)
#     ctime = ctime.strftime("%Y%m%d")
#     return ctime
# date = viewDate()

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101" #+ str(date)
data = urlToStr(url)
# bs = BeautifulSoup(data, "JSON.parse")
bs = json.loads(data)
bs2 = bs["boxOfficeResult"] #또는 bs.get("boxOfficeResult")
bs3 = bs2["dailyBoxOfficeList"]
