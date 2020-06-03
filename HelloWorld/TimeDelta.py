from datetime import datetime as dt

for i in range(int(input())):

    t1 = input()
    t2 = input()
    frmat = '%a %d %b %Y %H:%M:%S %z'
    print(int(abs((dt.strptime(t1, frmat) - dt.strptime(t2, frmat)).total_seconds())))