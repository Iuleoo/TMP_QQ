import requests
import random
import json
from hashlib import md5

# 国家名称对照表
country_mapping = {
    "Åland Islands": "奥兰群岛",
    "Austria": "奥地利",
    "Belgium": "比利时",
    "Bosnia": "波士尼亚",
    "Bulgaria": "保加利亚",
    "Croatia": "克罗地亚",
    "Cyprus": "塞浦路斯",
    "Czechia": "捷克",
    "Denmark": "丹麦",
    "Egypt": "埃及",
    "Estonia": "爱沙尼亚",
    "Faroe Islands": "法罗群岛",
    "Finland": "芬兰",
    "France": "法国",
    "Germany": "德国",
    "Greece": "希腊",
    "Hungary": "匈牙利",
    "Iceland": "冰岛",
    "Iraq": "伊拉克",
    "Ireland": "爱尔兰",
    "Isle of Man": "马恩岛",
    "Israel": "以色列",
    "Italy": "意大利",
    "Jersey": "泽西",
    "Jordan": "约旦",
    "Latvia": "拉脱维亚",
    "Lebanon": "黎巴嫩",
    "Liechtenstein": "列支敦士登",
    "Lithuania": "立陶宛",
    "Luxembourg": "卢森堡",
    "Netherlands": "荷兰",
    "North Macedonia": "北马其顿",
    "Northern Ireland": "北爱尔兰",
    "Norway": "挪威",
    "Poland": "波兰",
    "Romania": "罗马尼亚",
    "Russia": "俄罗斯",
    "Saudi Arabia": "沙特阿拉伯",
    "Serbia": "塞尔维亚",
    "Slovakia": "斯洛伐克",
    "Slovenia": "斯洛文尼亚",
    "Svalbard": "斯匹次卑尔根群岛",
    "Sweden": "瑞典",
    "Switzerland": "瑞士",
    "Syria": "叙利亚",
    "Turkey": "土耳其",
    "Ukraine": "乌克兰",
    "United Kingdom": "英国",
    "Westbank": "加拿大西岸"
}

def get_player_info(player_id):
    # 设置请求的URL和参数
    url = "https://api.truckyapp.com/v3/map/online"
    params = {"playerID": player_id}

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    # 发送GET请求并获取响应
    response = requests.get(url, params=params, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析JSON数据
        data = response.json()
        # 判断玩家是否在线
        if data["response"]["online"]:
            # 获取玩家信息
            city = data["response"]["location"]["poi"]["realName"]
            country = data["response"]["location"]["poi"]["country"]

            # 翻译城市名称
            if city == "Kirkenes":
                translated_city = translate_local(city)
            else:
                translated_city = translate_baidu(city)

            # 翻译国家名称
            translated_country = country_mapping.get(country, country)

            # 格式化玩家信息
            player_info = "玩家信息：\n"
            player_info += "🟢 玩家在线\n"
            player_info += "玩家名称：{}\n".format(data["response"]["name"])
            player_info += "TMPID：{}\n".format(data["response"]["mp_id"])
            player_info += "当前编号：{}\n".format(data["response"]["p_id"])
            player_info += "服务器名：{}\n".format(data["response"]["serverDetails"]["name"])
            player_info += "所在城市：{} ({})\n".format(translated_city, data["response"]["location"]["poi"]["realName"])
            player_info += "所在国家：{} ({})\n".format(translated_country,data["response"]["location"]["poi"]["country"])
            player_info += "DLC：{}\n".format(data["response"]["location"]["poi"]["dlc"])

            # 返回玩家信息
            return player_info
        else:
            return "🔴 玩家离线"
    else:
        return None

def translate_local(text):
    # 这里是城市本地翻译的逻辑
    # 采石场不生效
    if text == "Kirkenes - Quarry":
        return "希尔克内斯-采石场"
    elif text == "Kirkenes":
        return "希尔克内斯"
    else:
        return text

def translate_baidu(text):
    # 设置百度翻译API的参数
    appid = ''
    appkey = ''
    from_lang = 'en'
    to_lang = 'zh'
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path

    # 生成salt和sign
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + appkey)

    # 构建请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': text, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # 发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # 提取翻译结果
    if "trans_result" in result:
        translated_text = result["trans_result"][0]["dst"]
    else:
        translated_text = "翻译失败"

    return translated_text
