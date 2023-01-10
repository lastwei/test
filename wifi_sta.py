import time

import pywifi as pywifi
from pywifi import const


def connect_wifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    print(ifaces.name())  # 输出无线网卡名称
    ifaces.disconnect()
    time.sleep(3)

    profile = pywifi.Profile()  # 配置文件
    # profile.ssid = "RAX3000_DQ1"  # wifi名称
    profile.auth = const.AUTH_ALG_OPEN  # 需要密码
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
    profile.ssid = "CMCC-6y72"  # wifi名称
    # profile.auth = const.AUTH_ALG_OPEN  # 不要密码
    # profile.akm.append(const.AKM_TYPE_NONE)  # 加密类型
    profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    profile.key = "12345678"  # wifi密码

    ifaces.remove_all_network_profiles()  # 删除其它配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件
    ifaces.connect(tmp_profile)
    time.sleep(5)
    isok = True

    print(const.IFACE_CONNECTED)
    print(ifaces.status())
    if ifaces.status() == const.IFACE_CONNECTED:
        print("connect successfully!")
    else:
        print("connect failed!")
    while True:
        if ifaces.status() == const.IFACE_CONNECTED:
            # print("connect successfully!")
            pass
        else:
            print("connect failed!")
        time.sleep(1)
    # return isok
connect_wifi()