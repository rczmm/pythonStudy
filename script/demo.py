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


def refresh_web_page(interval=0.5):
    """ 每间隔一定的秒数刷新一次网页（默认5秒），但只在Chrome浏览器下执行 """
    while True:
        if is_chrome_window():
            # 模拟按下 F5 键
            pyautogui.press('f5')
        else:
            print("Active window is not a Chrome window.")
        # 等待一定的时间间隔
        time.sleep(interval)


def get(interval=0.5):
    url = '''     http://192.168.1.147/zentao/my-team.html?zin=1'''
    headers = {
        'cookie': """lang=zh-cn; vision=rnd; device=desktop; keepLogin=on; hideMenu=false; preProductID=1; preBranch=0; za=wangliping; lastProject=1; zentaosid=2a3bc5708216fb6f63e83ea4ed6ed2c9; zp=c6294800914b7e84094b44465ac40ecd007a2239; theme=blue; tab=system; sid-3=9409881c68d78dd8cc2f3dbd4c587465; sid=9409881c68d78dd8cc2f3dbd4c587465""",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Zin-Options': '{"selector":["#configJS","title>*","body>*"],"type":"list"}',
        "X-Zin-App": "system",
        "X-Zin-Cache-Time": '0',
        'Referer': 'http://192.168.1.147/zentao/index-index-L3plbnRhby9teS10ZWFtLmh0bWw=.html'
    }
    while True:
        data = requests.get(url, headers=headers)
        time.sleep(interval)


if __name__ == "__main__":
    print("开始刷新Chrome网页，每0.5秒刷新一次。按 Ctrl+C 停止。")
    try:
        refresh_web_page()
    except KeyboardInterrupt:
        print("\n刷新停止。")
