def randTemp(bpm, sepsisBool):
    import random
    # generate a randomized temperature in Celsius
    # with the tail ends at slightly abnormal cold or feverish ranges
    randomizedTemp = random.uniform(36.0, 38.5)
    modifiedBPM = int()
    rValue = random.random()
    # if this is a sepsis patient value, then recreate the randomized temp based on set criteria
    if sepsisBool:
        if rValue < 0.4:
            randomizedTemp = random.uniform(34.0, 36.0)
            randomizedTemp = round(randomizedTemp, 2)
        else:
            randomizedTemp = random.uniform(38.0, 40.1)
            randomizedTemp = round(randomizedTemp, 2)
    # update heart rate as noted in the literature if temp is slightly feverish to feverish
    if randomizedTemp > 38.0:
        modBPM = int((abs(randomizedTemp-37)/0.5)*10)
        modifiedBPM = bpm + modBPM
    else:
        modifiedBPM = bpm
    return (modifiedBPM, randomizedTemp)

def randBPM(sepsisBool):
    import random
    # if this is a sepsis patient value, then artifically elevate the heart rate
    if sepsisBool:
        randomizedBPM = random.randrange(140, 210)
        return randomizedBPM
    else:
        randomizedBPM = random.randrange(60, 180)
        return randomizedBPM

def randRespRate(sepsisBool):
    import random
    # if this is a sepsis patient value, then set the Respiratory Rate to either < 2 or > 22
    rValue = random.random()
    if sepsisBool:
        if rValue > 0.4:
            randomizedRespRate = random.randrange(1, 3)
            return randomizedRespRate
        else:
            randomizedRespRate = random.randrange(22, 61)
            return randomizedRespRate
    else:
        randomizedRespRate = random.randrange(6, 22)
        return randomizedRespRate

def randGCM(sepsisBool):
    import random
    if not sepsisBool:
        return 15
    else:
        randGCM = random.randrange(7, 15)
        return randGCM

def randCre(sepsisBool):
    import random
    if sepsisBool:
        randCreatinine = round(random.uniform(1.2, 6.0), 2)
        return randCreatinine
    else:
        randCreatinine = round(random.uniform(0.5, 3.0), 2)
        return randCreatinine

def randBP(sepsisBool):
    import random
    if not sepsisBool:
        randomizedBP = random.randrange(95, 181)
        return randomizedBP
    else:
        randomizedBP = random.randrange(80, 101)
        return randomizedBP


def convertSparse(kw, val):
    lookupDict = {'temp' : [37.0,38.0], 'GCM' : 15, 'BPM': 140, 'RR': [4, 21], 'cre': 4.0, 'sysBP': 95}
    # temp: [lt,gt], GCM: lt, BPM: gt, RR: [lt,gt], cre: gt, sysBP: gt
    # 1 == SepsisTrue, 0 == SepsisFalse
    try:
        lookupKW = lookupDict[kw]
        if kw == 'temp':
            if val < lookupKW[0] or val > lookupKW[1]:
                return 1
            else:
                return 0
        if kw == 'GCM':
            if val < lookupKW:
                return 1
            else:
                return 0
        if kw == 'BPM':
            if val > lookupKW:
                return 1
            else:
                return 0
        if kw == 'RR':
            if val < lookupKW[0] or val > lookupKW[1]:
                return 1
            else:
                return 0
        if kw == 'cre':
            if val > lookupKW:
                return 1
            else:
                return 0
        if kw == 'sysBP':
            if val > lookupKW:
                return 1
            else:
                return 0
        print('Error, kw not found')
        return None
    except KeyError:
        print('Error, check kw val')
        return None
