import gkeepapi
import time

keep = gkeepapi.Keep()
keep.login('19sudburyflat', '*nf1$19SbAv')

while True:
    gnote = keep.get(
        "1hPKZsJQPinVZQG_2qEbQE0YYlb5yOg94jDbgTIT8r7XHlRW2jMxCKdw3JEXTYO6G")
    print("\tShopping list\n")

    for i in gnote.items:
        if "☑ " in str(i):
            continue
        print(i)
    keep.dump()
    keep.sync()

    time.sleep(60)
    print("------------------------\n")
