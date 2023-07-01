import requests

def get_player_info(player_id):
    # 设置请求的URL和参数
    # 请求示例：https://api.truckyapp.com/v3/map/online?playerID=:playerID
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
            # x = data["response"]["x"]
            # y = data["response"]["y"]
            # time = data["response"]["time"]
            # server_code = data["response"]["serverDetails"]["code"]
            real_name = data["response"]["location"]["poi"]["realName"]
            country = data["response"]["location"]["poi"]["country"]
            dlc = data["response"]["location"]["poi"]["dlc"]
            p_id = data["response"]["p_id"]
            name = data["response"]["name"]
            mp_id = data["response"]["mp_id"]
            server_name = data["response"]["serverDetails"]["name"]

            # 格式化玩家信息
            # player_info += "服务器代码：{}\n".format(server_code)
            # player_info += "X轴坐标：{}\n".format(x)
            # player_info += "Y轴坐标：{}\n".format(y)
            # player_info += "获取时间：{}\n".format(time)
            player_info = "玩家信息：\n"
            player_info += "🟢 玩家在线\n"
            player_info += "玩家名称：{}\n".format(name)
            player_info += "TMPID：{}\n".format(mp_id)
            player_info += "当前编号：{}\n".format(p_id)
            player_info += "服务器名：{}\n".format(server_name)

            player_info += "所在国家：{}\n".format(country)
            player_info += "所在城市：{}\n".format(real_name)
            player_info += "DLC：{}\n".format(dlc)

            # 返回玩家信息
            return player_info
        else:
            return "🔴 玩家离线"
    else:
        return None
