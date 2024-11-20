import datetime
import json
import time

import requests

from script.importCenterLine import direction_lite, extract_waypoints

url = "http://110.185.163.49:22222/stage-api/ins/app/listTasksApp"

authorization = """Bearer eyJhbGciOiJIUzUxMiJ9.eyJ0ZW5hbnRfaWQiOiI0NDIxMSIsIm9zIjoiQ2hyb21lIiwidXNlcl9pZCI6MjA5LCJ1c2VyX2tleSI6IjdjMDIzNTYzLWM4OWYtNDU0ZC05MGZlLWQ1NTE5YTdmZDA3MSIsImRlcHRfbmFtZSI6IjQ0MjExIiwiZGVwdF9pZCI6NDE5LCJ1c2VybmFtZSI6ImxuIn0.3msnhzu6NVcV2Cis5f4fuLT_A-GEkaYJwYwlNvP1prp4-nHYiBAd7cDVi_ybnpM3-6OZJnm4axpIDnYZpiYobQ"""

headers = {
    'authorization': authorization,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'content-type': 'application/json'
}

request_data = {
    "pageNum": 1,
    "pageSize": 10,
}


def get_coords():
    # 输入起点、终点和途经点
    # origin = input("请输入起点坐标(经度在前，纬度在后): ")
    # destination = input("请输入终点坐标(经度在前，纬度在后): ")
    # waypoints = input("请输入途经点坐标(经度在前，纬度在后，坐标点用|英文竖线隔开): ")

    origin = """104.091373,29.674351"""
    destination = """104.070878,29.654352"""
    waypoints = """104.089423,29.672201|104.083306,29.673425|104.081374,29.673205|104.081357,29.670997|104.069652,29.671193|104.067554,29.666827|104.072459,29.662873|104.077525,29.662841|104.077903,29.654618|"""
    # 百度路径规划
    result = direction_lite(origin, destination, waypoints)

    # 提取所有的途径点
    return extract_waypoints(result)


def get_current_time_plus_two_seconds():
    current_time = datetime.datetime.now()
    future_time = current_time + datetime.timedelta(seconds=2)
    return future_time.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    response = requests.post(url, headers=headers, data=json.dumps(request_data))
    if response.status_code == 200:
        taskList = response.json()
        taskId = taskList['data']['records'][1]['taskId']
        track_url = f'''http://110.185.163.49:22222/stage-api/ins/app/uploadTaskTrace'''
        points = get_coords()
        coords = []
        i = 0
        for point in points:
            time.sleep(2)
            coord = {
                "lat": point['lat'],
                "lng": point['lng'],
                "time": get_current_time_plus_two_seconds()
            }
            print("轨迹点加1,{}".format(coord))
            coords.append(coord)
            i += 1

            if i % 20 == 0:
                track_data = {
                    "taskId": taskId,
                    "positions": coords
                }
                response_track = requests.post(track_url, headers=headers, data=json.dumps(track_data))
                if response_track.status_code == 200:
                    print("上传轨迹点{}个成功，正在继续赶路！".format(len(coords)))
