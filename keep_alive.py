import threading, requests, time

def ping_self():
    while True:
        try:
            requests.get("https://your-render-url.onrender.com/region?uid=12345678")
        except:
            pass
        time.sleep(300)  # 5 phút ping 1 lần

threading.Thread(target=ping_self).start()
