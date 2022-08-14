#!/opt/bin/lv_micropython
import network


WIFI_SSID = "MarabouDaim" # Assign your the SSID of your network
WIFI_PASS = "Artno1427" # Assign your the password of your network

# WiFi connection
print("Setup start")
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to',WIFI_SSID)
    sta_if.active(True)
    sta_if.connect(WIFI_SSID,WIFI_PASS)
    while not sta_if.isconnected():
        pass
print("Connected to Wifi\n")
