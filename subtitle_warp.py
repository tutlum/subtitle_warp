"""
If your subtitles are not only offset, but also contracted, execute this script:

`python3 subtitle_warp start end filename`

where there are:

`start`:    Spperance of the first subtitle line format: 00:00:00,000

`end`:      Spperance of the last subtitle line format: 00:00:00,000

`filename`: Name of the srt file. It will be replaced!!!
          Except the file has the format: [name]-pre.srt then the new file will be [name].srt
"""


import sys
import datetime

def warp(filen, start, end):
    with open(filen, 'r') as f:
        data=f.read()
        subs=data.split("\n\n")
        offset, factor = calcOffsetFactor(subs, start, end)
        print("-"+str(-offset), factor)
        warped = "\n\n".join([clacSubs(s, offset, factor) for s in subs])
        nfilen = filen.replace("-pre", "")
        with open(nfilen, "w") as fw:
            fw.write(warped)

def calcOffsetFactor(subs, start, end):
    td1, td2 = splitTimes(subs[0].split("\n")[1])
    offset=start-td1
    td1, td2 = splitTimes(subs[-1].split("\n")[1])
    factor=end/(td1+offset)
    return offset, factor

def clacSubs(subtitle, offset, factor):
    sub=subtitle.split("\n")
    td1, td2 = splitTimes(sub[1])
    return sub[0] + "\n" + joinTime((td1 + offset) * factor, (td2 + offset) * factor) + "\n" + "\n".join(sub[2:])

def splitTimes(time):
    times=time.split(" --> ")
    return splitTime(times[0]), splitTime(times[1])

def splitTime(time):
    t1=time.replace(",",".").split(":")
    return datetime.timedelta(hours=int(t1[0]), minutes=int(t1[1]), seconds=float(t1[2]))
    
def joinTime(t1, t2):
    print(str(t1), str(t2))
    return str(t1).replace(".",",")[:11]+" --> "+str(t2).replace(".",",")[:11]

filen = sys.argv[3]
t1    = sys.argv[1]
t2    = sys.argv[2]
warp(filen, splitTime(t1), splitTime(t2))
