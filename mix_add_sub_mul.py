# __author__ = 'bren'

import random
from pprint import pprint
import time
rowPadding = ' '.join([' ' for e in range(10)])
inLen = 7
numLen = 5
sumRange = 99
lineNum = 3

def generateOneAdd(num2cal = 2, sumRange=999, inLen=7):
    lower_bd = 10**(len(str(sumRange))-1)
    lines = []
    for i in range(num2cal):
        lines.append(str(random.randint(lower_bd, sumRange)))
    lines[-1] = "+   " + lines[-1]
    ret = []
    for eachLine in lines:
        tmp_pad = ''.join([' ' for e in range(inLen - len(eachLine))])
        ret.append(tmp_pad + eachLine)

    ret.append(''.join(['-' for e in range(inLen)]))

    return ret

def generateOneSub(num2cal = 2, sumRange=999, inLen=7):
    lower_bd = 10**(len(str(sumRange))-1)
    lines = []
    tmp = []
    for i in range(num2cal):
        tmp.append(random.randint(lower_bd, sumRange))
    tmp.sort(reverse=True)
    lines.extend([str(e) for e in tmp])
    lines[-1] = "-   " + lines[-1]
    ret = []
    for eachLine in lines:
        tmp_pad = ''.join([' ' for e in range(inLen - len(eachLine))])
        ret.append(tmp_pad+eachLine)

    ret.append(''.join(['-' for e in range(inLen)]))

    return ret

def generateOneMul(num2cal = 2, sumRange=99, inLen=7):
    lines = []
    for i in range(num2cal):
        lines.append(str(random.randint(11, sumRange)))
    lines[-1] = "x   " + lines[-1]
    ret = []
    for eachLine in lines:
        tmp_pad = ''.join([' ' for e in range(inLen - len(eachLine))])
        ret.append(tmp_pad + eachLine)

    ret.append(''.join(['-' for e in range(inLen)]))

    return ret

def generateRandomAddSubMulAll(totNum_op = 108, num2cal = 2):

    opPool = [] #[generateOneSub(lineNum) for i in range(totNum_add)]
    for i in range(totNum_op):
        if random.random() < 0.33:
            opPool.append(generateOneSub(num2cal))
        elif random.random() < 0.66:
            opPool.append(generateOneAdd(num2cal))
        else:
            opPool.append(generateOneMul(num2cal))

    numAdd_eachLine = 9

    ret = []
    cur = []

    for i in range(totNum_op):
        each = opPool[i]
        for j in  range(len(each)):
            if len(cur)<(num2cal+1):
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
    return ret


def generateAlternateAddSubMulAll(totNum_op = 108, num2cal = 2):

    opPool = [] #[generateOneSub(lineNum) for i in range(totNum_add)]
    for i in range(totNum_op):
        cur_line = i/9
        if cur_line%3==0:
            opPool.append(generateOneAdd(num2cal))
        elif cur_line%3==1:
            opPool.append(generateOneSub(num2cal))
        else:
            opPool.append(generateOneMul(num2cal))

    numAdd_eachLine = 9

    ret = []
    cur = []

    for i in range(totNum_op):
        each = opPool[i]
        for j in  range(len(each)):
            if len(cur)<(num2cal+1):
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
    return ret


def out2txt(cur_worksheet, idxs=1, space_after_each_row=5):
    out_fn = (time.strftime("%d-%m-%Y")+"-mix"+str(idxs)+".txt")
    out_hd = open(out_fn, 'w')
    for i in range(len(cur_worksheet)):
        # one row
        out_hd.write('\n'.join([eachL for eachL in cur_worksheet[i]]))
        # add space
        out_hd.write("\n".join(["" for i in range(space_after_each_row)]))
    out_hd.close()

if __name__ == "__main__":

    # total number work sheet
    total_num_worksheet = 5


    for i in range(total_num_worksheet):
        cur_hw = generateAlternateAddSubMulAll()
        out2txt(cur_hw, idxs=i)

