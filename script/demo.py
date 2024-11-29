import pyautogui
import pygetwindow as gw
import time
import requests


def is_chrome_window():
    """检查当前活动窗口是否是Chrome浏览器"""
    try:
        win = gw.getActiveWindow()
        return 'Chrome' in win.title
    except Exception as e:
        print(f"Error checking active window: {e}")
        return False


def refresh_web_page(interval=0.3):
    """ 每间隔一定的秒数刷新一次网页（默认5秒），但只在Chrome浏览器下执行 """
    while True:
        if is_chrome_window():
            # 模拟按下 F5 键
            pyautogui.press('f5')
        else:
            print("Active window is not a Chrome window.")
        # 等待一定的时间间隔
        time.sleep(interval)

cookie_ln = """lang=zh-cn; device=desktop; keepLogin=on; hideMenu=false; preProductID=1; theme=blue; lastProject=1; docSpaceParam=%7B%22type%22%3A%22project%22%2C%22objectID%22%3A%221%22%2C%22libID%22%3A%220%22%2C%22moduleID%22%3A%220%22%2C%22browseType%22%3A%22all%22%2C%22param%22%3A%220%22%7D; preBranch=0; vision=rnd; zentaosid=4b7b9938eb3ba3f0beeb707358495713; za=luona; zp=5e9cf2f2a86a30e244d1aa75dac433cf713b9247; tab=system; sid-6=88dc79bb144c15ada88f9188d0b2a7f9; sid-5=0a67c6c03a8ea3b685bd6ed7a25e2724; sid-18=dfd588e674f203cb90dbe84b95979d85; sid=dfd588e674f203cb90dbe84b95979d85"""
def get(interval=0.5):
    url = '''http://192.168.1.147/zentao/index-index-L3plbnRhby9teS10ZWFtLWlkX2Rlc2MtMTktMTUtMS5odG1s.html'''
    headers = {
        'cookie': cookie_ln,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Zin-Options': '{"selector":["#configJS","title>*","body>*"],"type":"list"}',
        "X-Zin-App": "system",
        "X-Zin-Cache-Time": '0',
        'Referer': 'http://192.168.1.147/zentao/index-index-L3plbnRhby9teS10ZWFtLmh0bWw=.html'
    }
    while True:
        response = requests.get(url, headers=headers).json()
        if '用户名' in response:
            print(response)
        time.sleep(interval)
        # print(response)


if __name__ == "__main__":
    print("开始刷新Chrome网页，每0.5秒刷新一次。按 Ctrl+C 停止。")
    try:
        refresh_web_page()
    except KeyboardInterrupt:
        print("\n刷新停止。")
