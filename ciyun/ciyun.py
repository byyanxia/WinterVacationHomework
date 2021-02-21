#该脚本在原作者基础上数据做了微调，https://blog.csdn.net/weixin_43746433/article/details/89856014
import jieba.analyse
import imageio
import jieba.posseg as pseg
def jieba_cut():
    #打开停用词文件
    fr = open('sc.txt', 'r',encoding='UTF-8')
    stop_word_list = fr.readlines()
    new_stop_word_list = []
    for stop_word in stop_word_list:
        stop_word = stop_word.replace('\ufeef', '').strip()
        new_stop_word_list.append(stop_word)
    print(stop_word_list)  #输出停用词
    #输出词语出现的次数
    fr_xyj=open('trj.txt','r',encoding='utf-8')
    s=fr_xyj.read()
    words=jieba.cut(s,cut_all=False)
    word_dict={}
    word_list=''
    for word in words:
        if (len(word) > 1 and not word in new_stop_word_list):
            word_list = word_list + ' ' + word
            if (word_dict.get(word)):
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1
    fr.close()

    #按次数进行排序
    sort_words=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    print(sort_words[0:101])#输出前0-100的词

    from wordcloud import WordCloud
    color_mask =imageio.imread("1.png")
    wc = WordCloud(
            background_color="white",  # 背景颜色
            max_words=500,  # 显示最大词数
            font_path="C:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-simsun_31bf3856ad364e35_10.0.18362.1_none_cd668f05ece74044\simsun.ttc",  # 使用字体，每个人的文件路径可能不同
            min_font_size=10,
            max_font_size=60,
            width=400,
            height=860,
            mask=color_mask) # 图幅宽度
    i=str('why8')
    wc.generate(word_list)
    wc.to_file(str(i)+".png")
jieba_cut()
