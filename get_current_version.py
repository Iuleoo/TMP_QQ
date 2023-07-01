import requests

def get_current_version():
    # 设置请求的URL和参数
    url = "https://api.truckyapp.com/v2/truckersmp/version"

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        # 发送GET请求并获取响应
        response = requests.get(url, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            # 解析JSON数据
            data = response.json()

            # 获取版本信息
            # TMP版本号
            truckersmp_version = data["response"]["name"]
            # 欧卡版本号
            est2_version = data["response"]["supported_game_version"]
            # 美卡版本号
            ats_version = data["response"]["supported_ats_game_version"]

            # 格式化玩家信息
            current_version_info = "版本信息：\n"
            current_version_info += "TMP版本号：{}\n".format(truckersmp_version)
            current_version_info += "欧卡版本号：{}\n".format(est2_version)
            current_version_info += "美卡版本号：{}\n".format(ats_version)

            # 返回版本信息
            return current_version_info

        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求发生异常:", e)

# 本地调试，调用函数，获取数据
# current_version()

