import requests
import pandas as pd
import json
import os
import time
from time import sleep
import random
import logging

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain. */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7.en-US;q=0.6',
    'cookie': "_uuid=2D10C15B1-1835-341D-ACCB-5E49B763DA10C57708infoc; buvid3=F1E4E30C-DDD1-DF2C-38B9-9D118F7765E553932infoc; DedeUserID=13083696; DedeUserID__ckMd5=8517e94b5091d187; nostalgia_conf=-1; CURRENT_PID=51cc0230-ea49-11ed-9f7b-8ffb6e5a64e9; rpdid=|(k~|J|YYk~Y0J'uY)Ju)JYuu; buvid_fp_plain=undefined; hit-new-style-dyn=1; hit-dyn-v2=1; i-wanna-go-back=-1; b_ut=5; FEED_LIVE_VERSION=V8; header_theme_version=CLOSE; LIVE_BUVID=AUTO5616833822797465; is-2022-channel=1; CURRENT_BLACKGAP=0; SESSDATA=4e046a94%2C1705913040%2Cf8ea9%2A72_NatBNN8xmyNYs9IRmkd4J37EpQbOKT9QeGeCJuggl4r-1I6m8Syeizv7bl7AD6kWl7thAAAYAA; bili_jct=be20a39ba78cf8103c6de48012d5be9f; buvid4=358881E4-089D-0D5A-5BDA-3054BFA300A658525-023072719-cW9uKfiUkwbQD2wV7iM2hA%3D%3D; b_nut=1690457259; fingerprint=78c457c4eaafaf1e9bb12cf24e348e4c; home_feed_column=5; browser_resolution=1920-931; CURRENT_QUALITY=80; PVID=1; CURRENT_FNVAL=4048; buvid_fp=78c457c4eaafaf1e9bb12cf24e348e4c; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTUyMDA2MDcsImlhdCI6MTY5NDk0MTQwNywicGx0IjotMX0.OXJeH_gfsmbN8CLDKPL1rlphSmVOk8Q_-nUIuJ0m_Rk; bili_ticket_expires=1695200607; sid=6zddnwbx; bp_video_offset_13083696=842780198194642950; b_lsid=36361A2B_18AAA1D06D6",
    'origin': 'https://www.bilibili.com'
}

def request_comments_dataframe (oid):
    url = f"https://api.bilibili.com/x/v2/reply/wbi/main?oid={oid}&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=95577f84c63876bbfab4d642a4196de0&wts=1695072139"
    response = requests.get(url,headers=headers)
    data_list = response.json()['data']['replies']
    info_list = {}
    required_info = ["member,mid","member,uname","member,sex","content,message"]
    for info_type in required_info:
        higher_label,lower_label = info_type.split(",")
        info_list[lower_label] = list()

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

    for item in data_list:
        grab_info(item,info_list)

    return info_list

print(request_comments_dataframe("795613227"))


