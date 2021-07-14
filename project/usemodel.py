import joblib
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def rain_chances(places):
    loctime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    year=loctime[0:4]
    mon=loctime[5:7]
    day=int(loctime[8:10])-1
    data=pd.read_csv(r"./station.csv")
    place=places
    loca=data["loca"].loc[data["loca"].str.contains(place)].unique()
    # loca=data["loca"].unique()
    for loc in loca:
        stno=os.listdir(r".\model\\"+str(loc))#model檔
    # print(stno)
        olo=[]
        for st in stno:
            re=pd.read_json(r".\target\\"+str(st[0:6])+"\\12-target.json")#target檔
            path=r".\model\\"+str(loc)+"\\"+str(st)#model檔
            lr=joblib.load(path)
            url = "http://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station="+str(st[0:6])+"&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker="
            url = url + str(year) + "-" + str(mon).zfill(2)
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find(id='MyTable').tbody
            titles = table.find('tr', 'second_tr').find_all('th')
            title = []
            for j in range(0, len(titles)):
                result = titles[j].text
                title.append(result)
            rows = table.find_all('tr')
            weather = {}
            for col in range(0, 28, 1):
                d = []
                if col == 2 or col == 7 or col == 13 or col == 16 or col == 17 or col == 21 or col == 27:
                    for r in rows[2:]:
                        index = col * 2 + 1
                        value = r.contents[index].string
                        value = "".join(value.split())
                        d.append(value)
                    weather[d[0]] = d[1::]
            for v in weather.values():
                num = v.count('T')
                while (num > 0):
                    i = v.index('T')
                    v[i] = '0.1'
                    num = num - 1
                num1 = v.count('X')
                num2 = v.count('')
                num3 = v.count('...')
                num4 = v.count('/')
                numt=num1+num2+num3+num4
                if  (numt > 0):
                    for k in weather.keys():
                        a=weather[k]
                        a=["-9999"if x == "X" else x for x in a]
                        a=["-9999" if x == '' else x for x in a]
                        a=["-9999" if x == "..." else x for x in a]
                        a=["-9999" if x == "/" else x for x in a]
                        weather[k]=a  
            obs=pd.DataFrame.from_dict(weather)
            obs=obs[obs.astype(float)>=0]
            obs=obs.dropna(subset=["Precp"])
            head=list(obs.columns)
            head.remove("Precp")
            obs=obs[head].dropna(axis="columns")
            for i in re.keys():
                a=re[i]
                a=[-9999 if x == "/" else x for x in a]
                re[i]=a
            re=re[re.astype(float)>=0]
            head=list(obs.columns)
            re=re[head]
            yes=obs.tail(1)
            try:
                sc=StandardScaler()
                re_std=sc.fit_transform(re)
                yes_std=sc.transform(yes)
                pca = PCA(n_components=2)
                re_pca = pca.fit_transform(re_std)
                yes_pca = pca.transform(yes_std)
                pred=lr.predict(yes_pca)
                olo.append(pred[0])
            except ValueError:
                pass
        olo=np.array(olo).mean()*100
        return olo