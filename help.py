import requests

def help():
    return "help 帮助\n" \
           "查询 TMPID | 查询玩家\n" \
           "定位 TMPID | 查询玩家所在位置\n" \
           "服务器 | 查看服务器状态\n" \
           "路况S1 | 查看路况\n" \
           "游戏版本 | 查看游戏版本"

# 本地调试，调用函数，获取数据
#help()