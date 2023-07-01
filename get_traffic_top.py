import re
import requests

def get_traffic_top():
    url = "https://api.truckyapp.com/v2/traffic/top"
    params = {
        "server": "sim1",
        "game": "ets2"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)

    # 检查响应状态码，200表示请求成功
    if response.status_code == 200:
        # 解析JSON数据
        data = response.json()

        # 初始化空列表以存储城市信息
        city_info = []

        city_info.append("已列出最热门城市：\n")

        # 遍历每个交通信息条目，提取所需的信息并格式化
        for entry in data["response"]:
            city_name = entry["name"]
            players = entry["players"]
            congestion_severity = entry["newSeverity"]

            # 将英文交通信息名称转换为中文
            city_name = city_name.replace("Calais", "加莱")
            city_name = city_name.replace("Duisburg", "杜伊斯堡")
            city_name = city_name.replace("Düsseldorf", "杜塞尔多夫")
            city_name = city_name.replace("Bologna", "博洛尼亚")
            city_name = city_name.replace("Brussel", "布鲁塞尔")
            city_name = city_name.replace("Frankfurt am main", "法兰克福")
            city_name = city_name.replace("Paris", "巴黎")
            city_name = city_name.replace("Rotterdam", "鹿特丹")
            city_name = city_name.replace("Lille", "里尔")
            city_name = city_name.replace("Berlin", "柏林")
            city_name = city_name.replace("Hannover", "汉诺威")
            city_name = city_name.replace("Intersection", "十字路口")
            city_name = city_name.replace("Helsinki", "赫尔辛基")
            city_name = city_name.replace("Osnabrück", "奥斯纳布吕克")

            # 使用正则表达式删除括号及其内部内容
            city_name = re.sub(r'\(.*\)', '', city_name)

            # 将英文拥挤程度转换为中文
            if congestion_severity == "Heavy":
                congestion_severity = "🟡繁忙"
            elif congestion_severity == "Moderate":
                congestion_severity = "🟢适中"
            elif congestion_severity == "Congested":
                congestion_severity = "🔴拥堵"
            elif congestion_severity == "Fluid":
                congestion_severity = "🟢畅通"

            city_info.append("城市名称：{}\n人数：{} | 拥挤程度：{}\n".format(city_name.strip(), players, congestion_severity))

        # 将格式化的城市信息作为字符串返回
        return "\n".join(city_info)

    else:
        print("请求失败")
        return None

# 调用函数并打印返回的数据
# traffic_data = get_traffic_top()
# if traffic_data:
#     print(traffic_data)
