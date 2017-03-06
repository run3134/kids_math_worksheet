# __author__ = 'bren'

import random
from pprint import pprint
import time
rowPadding = ' '.join([' ' for e in range(10)])

inLen = 7
numLen = 5
sumRange = 99
lineNum = 3


def generateOne(lineNum = lineNum):
    lines = []
    for i in range(lineNum):
        lines.append(str(random.randint(1, sumRange)))
    lines[-1] = "+   " + lines[-1]
    ret = []
    for eachLine in lines:
        ret.append(''.join([' ' for e in range(inLen - len(eachLine))])+eachLine)

    ret.append(''.join(['-' for e in range(inLen)]))
    return ret


def generateAll():
    lineNum = 2
    totNum_add = 108
    addPool = [generateOne(lineNum) for i in range(totNum_add)]

    numAdd_eachLine = 9

    ret = []
    cur = []

    for i in range(totNum_add):
        each = addPool[i]
        for j in  range(len(each)):
            if len(cur)<(lineNum+1):
                cur.append(each[j])
            else:
                cur[j] += each[j]
        #pprint(cur)
        #print "i=%d, len(cur)=%d, len(cur[0])=%d" % (i, len(cur), len(cur[0]))
        if (i+1) % numAdd_eachLine==0:
            ret.append(cur)
            cur = []
        else:
            for j in range(len(cur)):
                cur[j] += '  '

    #pprint(ret)
    #for i in range(len(ret)):
        #(ret[i])
        #print [eachL+"\n" for eachL in ret[i]]

    return ret

def out2txt(tot):
    out_fn = (time.strftime("%d-%m-%Y")+"addition.txt")
    out_hd = open(out_fn, 'w')
    for i in range(len(tot)):
        #(ret[i])
        out_hd.write('\n'.join([ eachL for eachL in tot[i]]))
        out_hd.write("\n".join(["" for i in range(5)]))
    #out_hd.write("")
    out_hd.close()

if __name__ == "__main__":
    cur_hw = generateAll()
    out2txt(cur_hw)

