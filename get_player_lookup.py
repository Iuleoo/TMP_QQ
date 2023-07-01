import requests

def get_player_lookup(player_id):
    # 获取用户输入的玩家ID
    # 本地调试
    # player_id = input("请输入TruckersMP玩家ID：")

    # 设置请求的URL和参数
    url = "https://api.truckyapp.com/v2/truckersmp/player"
    params = {"playerID": player_id}

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        # 发送GET请求并获取响应
        response = requests.get(url, params=params, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            # 解析JSON数据
            data = response.json()
            # 获取玩家信息
            # TMPID
            tmp_id = data["response"]["response"]["id"]
            # 玩家名称
            tmp_name = data["response"]["response"]["name"]
            # 加入日期
            real_name = data["response"]["response"]["joinDate"]
            # steamID64
            steamid64 = data["response"]["response"]["steamID64"]
            # 是否封号
            banned = data["response"]["response"]["banned"]
            if banned:
                banned = "封禁"
            else:
                banned = "正常"
            # 封号次数
            banscount = data["response"]["response"]["bansCount"]
            # 所属车队
            vtc_name = data["response"]["response"]["vtc"]["name"]
            # 车队ID获取
            vtc_id = data["response"]["response"]["vtc"]["id"]

            # 调试打印
            # print(data)
            # print(tmp_id,tmp_name,real_name,steamid64,banned,banscount)

            # 格式化玩家信息
            player_lokkup = "玩家信息如下：\n"
            player_lokkup += "TMPID：{}\n".format(tmp_id)
            player_lokkup += "玩家名称：{}\n".format(tmp_name)
            player_lokkup += "加入日期：{}\n".format(real_name)
            player_lokkup += "账户状态：{}\n".format(banned)
            player_lokkup += "封号次数：{}\n".format(banscount)
            player_lokkup += "所属车队：{}\n".format(vtc_name)
            player_lokkup += "车队链接：truckersmp.com/vtc/{}\n".format(vtc_id)
            player_lokkup += "TMP链接：truckersmp.com/user/{}\n".format(tmp_id)
            player_lokkup += "STEAM链接：steamcommunity.com/profiles/{}\n".format(steamid64)

            # 返回玩家信息
            return  player_lokkup

        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求发生异常:", e)

# 本地调试，调用函数，获取数据
# get_player_lookup()
