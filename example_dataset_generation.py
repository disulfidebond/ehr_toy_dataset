#!/usr/bin/python3

# simple example that will generate a dataset of 1000 entries for patients with sepsis
# change all flags to "False" and repeat to generate list of patients without sepsis
header = "Patient_ID, Institution_ID, Gender, Race, BP-Systolic, Respiratory_Rate, Body_Temp, Creatinine, Heart_Rate-BPM, GCM, Sepsis Flag"
with open('file2.csv', 'w') as fWrite:
    fWrite.write(header + '\n')
for i in range(0, 1000):
    patient_ID = 110001+i
    institution_ID = 9100001+i
    genderRand = random.randrange(0,2)
    raceRand = random.randrange(1,5)
    randomizedHeartRate = randBPM(True)
    heartRateBPM, randomizedTemp = randTemp(randomizedHeartRate, True)
    l = [patient_ID, institution_ID, genderRand, raceRand, randBP(True), randRespRate(True), randomizedTemp, randCre(True), heartRateBPM, randGCM(True), "True"]
    l_castString = [str(x) for x in l]
    s = ','.join(l_castString)
    with open('file2.csv', 'a') as fWrite:
        fWrite.write(s + '\n')
