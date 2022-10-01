import websocket, json, time, threading
thing = input("Token: ")
def heartbeat(hbb, ws):
    while True:
        time.sleep(hbb)
        hb = {"op": 1,"d": "null"}
        ws.send(json.dumps(hb))
ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?encoding=json?v=9")
payload = {
    "op": 2,
    "d": {
        "token": thing,
        "properties": {
            "os": "windows",
            "browser": "Chrome",
            "device": "pc"
        },
        'large_threshold': 250,
    }
}
ws.send(json.dumps(payload))
hb_insecs = int(json.loads(ws.recv())["d"]["heartbeat_interval"] ) / 1000
threading.Thread(target=heartbeat, args=(hb_insecs ,ws)).start()

while True:
    try:
        yes = json.loads(ws.recv())
        auth = yes["d"]["author"]["username"]
        if yes["d"]["content"] == "":
            txt = yes["d"]["attachments"][0]["url"]
        else:
            txt = yes["d"]["content"]
        auth = yes["d"]["author"]["username"]
        print(f"{auth}: {txt}")
    except:
        pass

