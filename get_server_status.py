import re
import requests


def get_server_status():
    url = "https://api.truckyapp.com/v2/truckersmp/servers"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # 检查响应状态码，200表示请求成功
    if response.status_code == 200:
        # 解析JSON数据
        data = response.json()

        # 总计
        total_players = data["response"]["totalPlayers"]

        servers_status_players = "在线玩家总计：{}\n".format(total_players)

        # 初始化空列表以存储服务器信息
        servers_status = []

        # 遍历每个服务器信息条目，提取所需的信息并格式化
        for entry in data["response"]["servers"]:
            servers_name = entry["name"]
            players = entry["players"]
            online = entry["online"]
            maxplayers = entry["maxplayers"]
            game = entry["game"]

            # 如果游戏类型为ATS，则跳过该条目
            if game == "ATS":
                continue

            # 将英文状态转换为中文
            if str(online) == "True":
                online = "开启"
            elif str(online) == "Moderate":
                online = "关闭"

            servers_status.append("===================")
            servers_status.append(
                "服务器名称：{}\n游戏：{}\n当前状态：{}\n在线人数：{}/{}".format(servers_name.strip(), game, online, players, maxplayers))

        # 将格式化的服务器信息作为字符串返回
        return servers_status_players + "\n".join(servers_status)

    else:
        print("请求失败")
        return None

# 调用函数并打印返回的数据
# servers_status = get_server_status()
# if servers_status:
#     print(servers_status)
