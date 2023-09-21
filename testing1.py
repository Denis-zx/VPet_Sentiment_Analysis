import requests
import pandas as pd
import wordcloud
import jieba

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain. */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7.en-US;q=0.6',
    'cookie': "_uuid=2D10C15B1-1835-341D-ACCB-5E49B763DA10C57708infoc; buvid3=F1E4E30C-DDD1-DF2C-38B9-9D118F7765E553932infoc; DedeUserID=13083696; DedeUserID__ckMd5=8517e94b5091d187; nostalgia_conf=-1; CURRENT_PID=51cc0230-ea49-11ed-9f7b-8ffb6e5a64e9; rpdid=|(k~|J|YYk~Y0J'uY)Ju)JYuu; buvid_fp_plain=undefined; hit-new-style-dyn=1; hit-dyn-v2=1; i-wanna-go-back=-1; b_ut=5; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; LIVE_BUVID=AUTO5616833822797465; is-2022-channel=1; CURRENT_BLACKGAP=0; SESSDATA=4e046a94%2C1705913040%2Cf8ea9%2A72_NatBNN8xmyNYs9IRmkd4J37EpQbOKT9QeGeCJuggl4r-1I6m8Syeizv7bl7AD6kWl7thAAAYAA; bili_jct=be20a39ba78cf8103c6de48012d5be9f; buvid4=358881E4-089D-0D5A-5BDA-3054BFA300A658525-023072719-cW9uKfiUkwbQD2wV7iM2hA%3D%3D; b_nut=1690457259; fingerprint=78c457c4eaafaf1e9bb12cf24e348e4c; home_feed_column=5; browser_resolution=1920-931; CURRENT_QUALITY=80; PVID=1; CURRENT_FNVAL=4048; buvid_fp=78c457c4eaafaf1e9bb12cf24e348e4c; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTUyMDA2MDcsImlhdCI6MTY5NDk0MTQwNywicGx0IjotMX0.OXJeH_gfsmbN8CLDKPL1rlphSmVOk8Q_-nUIuJ0m_Rk; bili_ticket_expires=1695200607; sid=6zddnwbx; bp_video_offset_13083696=842780198194642950; b_lsid=36361A2B_18AAA1D06D6",
    'origin': 'https://www.bilibili.com'
}

required_info = ["member,mid","member,uname","member,sex","content,message"]

def grab_info (item,info_list):
        #Retrive info in current layer
        for info_type in required_info:
            higher_label,lower_label = info_type.split(",")
            info_list[lower_label].append(item[higher_label][lower_label])
        
        #Retrive info in lower layer
        try:
            for new_item in item["replies"]:
                grab_info(new_item,info_list)
        except:
            return

def request_comments_dataframe (bvid):
    url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={bvid}'
    response = requests.get(url,headers=headers)
    response = response.json()
    count = response['data']['page']["count"]

    comment_dataframe_allpage = pd.DataFrame(columns=[info_type.split(",")[1] for info_type in required_info])

    for i in range (1,count,20):
        pagenum = i//20 + 1
        print(f"working on page {pagenum}")
        url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={pagenum}&type=1&oid={bvid}'
        response = requests.get(url,headers=headers)
        data_list = response.json()['data']['replies']
        info_list = {}
        
        for info_type in required_info:
            higher_label,lower_label = info_type.split(",")
            info_list[lower_label] = list()

    
        for item in data_list:
            grab_info(item,info_list)

        cur_page_comment = pd.DataFrame(info_list)
        comment_dataframe_allpage = pd.concat([comment_dataframe_allpage,cur_page_comment],ignore_index=True)

        if pagenum == 10:
            break
        
    return comment_dataframe_allpage


def get_oid(bvid):
    oid_url = "https://api.bilibili.com/x/player/pagelist?bvid={}".format(bvid)
    response = requests.get(oid_url, headers=headers)
    oid = response.json()['data'][0]['cid']
    return oid


bvid_list_tamo = ["BV1TL411575E","BV1Vs4y1R7dL","BV1Ty4y1k7Ms","BV1Ph41187SP"]
bvid_list_poki = ["BV1bG4y1g7CY","BV1ub411K7Rg","BV1Us411y7Xb","BV1Cs411y7YX","BV1N84y1H7dP"]

for bvid in bvid_list_poki:
    oid = get_oid(bvid)
    print(oid)
    comment_df = request_comments_dataframe(bvid)
    all_comment = ""
    for comment in comment_df["message"]:
        all_comment+= comment
        all_comment += "\n"
    
    
    ls = jieba.lcut(all_comment) # 生成分词列表
    text = ' '.join(ls) # 连接成字符串  
    stopwords = ["的","是","了"] # 去掉不需要显示的词
    wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color='white',
                         max_words=100,stopwords=stopwords)
    # msyh.ttc电脑本地字体，写可以写成绝对路径
    wc.generate(text) # 加载词云文本
    wc.to_file(f"{bvid}.png") # 保存词云文件







