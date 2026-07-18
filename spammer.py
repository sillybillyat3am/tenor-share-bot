import requests, threading

done = 0

def spam():
    global done
    while True:
        try:
            r = requests.get('https://tenor.com/vI6SARINeQ5.gif')
            done += 1
            print(f'Successfully added a share | This post now has been botted {done} shares. {r.status_code}')
        except:
            continue
while True:
    try:
        threading.Thread(target=spam).start()
    except:
        pass
