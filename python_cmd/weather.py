import requests  
from bs4 import BeautifulSoup
#获取www.tianqi.com的天气,参数：地名拼音
def data_of_tianqi(addr):
    response = requests.get("https://www.tianqi.com/"+addr+"/")
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_dd = soup.find_all(name='dd')
    tag_span = soup.find_all(name='span')[0]
    temp = str(soup.find_all(name='b')[0])[3:-4]#温度
    city_html = BeautifulSoup(str(tag_dd[0]), 'html.parser')
    city = str(city_html.find_all(name='h2'))[5:-6]#城市
    if str(tag_dd[1])[41:43]=='</':
        time=str(tag_dd[1])[17:41]
    else:
        time=str(tag_dd[1])[17:43]
    weather_and_temp = str(tag_span)[9:-7].split('</b>')
    weather = weather_and_temp[0]#天气
    temp = str(soup.find_all(name='b')[0])[3:-4]#实时温度
    temp_from_to = weather_and_temp[1]#温度范围
    shidu = str(tag_dd[3]).replace("</b>","").replace("</dd>","").split("<b>")[1]#湿度
    fengxaing = str(tag_dd[3]).replace("</b>","").replace("</dd>","").split("<b>")[2]#风向
    ziwaixian = str(tag_dd[3]).replace("</b>","").replace("</dd>","").split("<b>")[3]#紫外线
    other_info = str(tag_dd[4])[57:-12].replace('</h5><h6>','<br/>').replace('</h6><span>','<br/>').split('<br/>')#空气质量、PM、日出、日落
    print('城市：'+city)
    print('时间：'+time)
    print('天气：'+weather)
    print('实时温度：'+temp+'  '+'温度范围：'+temp_from_to)
    print(shidu+'  '+fengxaing+'  '+ziwaixian)
    print(other_info[0]+'  '+other_info[1])
    print(other_info[2]+'  '+other_info[3])
