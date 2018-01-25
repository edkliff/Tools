import psutil, datetime

while True:
    p = psutil.cpu_percent(5)
    m = psutil.swap_memory().percent
    v = psutil.virtual_memory().percent
    time = datetime.datetime.now().isoformat()
    print(time, p, m, v)