import wordcloud
import matplotlib.pyplot as plt
import matplotlib
import json
import os

# 中文字体路径
fontpath = json.load(open("./config.json",'r'))['fontpath']

wc = wordcloud.WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    repeat=True,
    font_path=fontpath)


word_count = []
labels = []
y = []
amount = 0

# 读入文件
files = os.listdir("./input")
for filename in files:
    file = open("./input/"+filename,"r",encoding='utf-8')
    str=file.readline()
# 解析文件内容
    while(str != ""):
        amount+=1
        strs=str.split(' ')
        cnt = int(strs[1])
        y.append(cnt)
        labels.append(strs[0])
        for i in range(cnt):
            word_count.append(strs[0])
        str=file.readline()

# 生成词云
wc.generate(" ".join(word_count))
wc.to_file('./output/wordcloutd.jpg')

x= list(range(1,amount+1))

# 生成柱状图
matplotlib.rcParams['font.sans-serif']=['SimHei']
plt.barh(x,y,align='center',color='g',tick_label=labels)
for a,b in zip(x,y):
    plt.text(b+1,a-0.15,"   %0.f" % b,ha="center",va="bottom",fontsize=12)
plt.savefig("./output/bar.jpg")