import requests
from flask import Flask, request
from get_player_info import get_player_info
from get_player_lookup import get_player_lookup
from get_current_version import get_current_version
from get_traffic_top import get_traffic_top
from get_server_status import get_server_status

app = Flask(__name__)

# POST
@app.route('/', methods=['POST'])
def qqbot():
    p = "0"
    print(request.get_json())
    # 处理群聊消息
    if request.get_json().get('message_type') == 'group':

        # JSON接受消息

        # 获取发送消息过来的QQ号码
        # qq_id = request.get_json().get('sender').get('user_id')
        # 获取发送者昵称
        # qq_name = request.get_json().get('sender').get('nickname')

        # 处理接受消息QQ群
        qq_qun_id = request.get_json().get('group_id')
        # 从JSON中获取原始消息
        qq_message = request.get_json().get('raw_message')

        # 判断消息是否同时包含中文"查询"和数字
        if "定位" in qq_message and any(word.isdigit() for word in qq_message.split()):
            player_id = qq_message.split()[-1]   # 从消息中提取最后一个单词作为玩家ID
            player_info = get_player_info(player_id)    # 调用get_player_info函数获取玩家信息

            # 将玩家信息作为响应消息发送给QQ群
            resp = requests.get("http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}".format(qq_qun_id, player_info))

        if "查询" in qq_message and any(word.isdigit() for word in  qq_message.split()):
            player_id = qq_message.split()[-1]
            player_lookup = get_player_lookup(player_id)

            resp = requests.get("http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}".format(qq_qun_id, player_lookup))

        if "游戏版本" in qq_message:
            version_info = get_current_version()  # 调用函数获取版本信息

            resp = requests.get(
                "http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}".format(qq_qun_id, version_info))

        if "交通信息" in qq_message:
            traffic_info = get_traffic_top()  # 调用函数获取交通信息

            resp = requests.get(
                "http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}".format(qq_qun_id, traffic_info))

        if "服务器状态" in qq_message:
            status_info = get_server_status()  # 调用函数获取服务器信息

            resp = requests.get(
                "http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}".format(qq_qun_id, status_info))

    return p

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701) # 这里改成CQ的HTTP端口
