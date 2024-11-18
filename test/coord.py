import time

from geopy.geocoders import Nominatim
from pyadb3 import ADB

import subprocess

from script.importCenterLine import direction_lite, extract_waypoints


def get_now_location_phone():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("四川省成都市青羊区")
    return location.latitude, location.longitude


def change_phone_location(lng, lat):
    adb = ADB(adb_path="E:\Program Files\platform-tools-latest-windows\platform-tools\adb.exe")
    device_serial = adb.devices
    if not device_serial:
        raise ValueError("No devices connected")

    # Run commands with root permissions if needed
    enable_gps_root_cmd = f'settings put secure location_providers_allowed gps'
    set_location_root_cmd = f'geo fix {lng} {lat}'

    # Execute commands
    try:
        # Enable GPS
        output = adb.run_shell_cmd(enable_gps_root_cmd)
        print(f"Enable GPS command output: {output.decode('utf-8')}")

        # Set the location
        output = adb.run_shell_cmd(set_location_root_cmd)
        print(f"Set location command output: {output.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")


def change_location(lng, lat):

    result = subprocess.run(['adb', 'shell', 'settings', 'get', 'secure', 'mock_location'], capture_output=True,
                            text=True,shell=True)
    print(result)


if __name__ == '__main__':
    change_location(10.2,2121)

    # try:
    #     # 输入起点、终点和途经点
    #     origin = input("请输入起点坐标(经度在前，纬度在后): ")
    #     destination = input("请输入终点坐标(经度在前，纬度在后): ")
    #     waypoints = input("请输入途经点坐标(经度在前，纬度在后，坐标点用|英文竖线隔开): ")
    #
    #     # 百度路径规划
    #     result = direction_lite(origin, destination, waypoints)
    #
    #     # 提取所有的途径点
    #     waypoints = extract_waypoints(result)
    #
    #     coords = []
    #
    #     for point in waypoints:
    #         coord = [point['lng'], point['lat']]
    #         coords.append(coord)
    #
    #     for coord in coords:
    #         change_phone_location(coord[0], coord[1])
    #         time.sleep(2)
    #         print(f"Phone location changed to: {coord[0]}, {coord[1]}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")
