#!/usr/bin/python3

# simple example that will generate a dataset of 1000 entries for patients with sepsis
# change all flags to "False" and repeat to generate list of patients without sepsis
header = "Patient_ID, Institution_ID, Gender, Race, DateTime_Admission, DateTime_Discharged, BP-Systolic, Respiratory_Rate, Body_Temp, Creatinine, Heart_Rate-BPM, GCM, Sepsis Flag"
with open('toy_dataset_sepsis-withTimestamp.csv', 'w') as fWrite:
    fWrite.write(header + '\n')
for i in range(0, 1000):
    # create a random integer to adjust the admission date
    dateRandomizer = random.randrange(0,30)
    # create a random integer to adjust the discharge time
    dateTimeRandomizer = random.randrange(0,12)
    # create a randomized timestamp using the dateRandomizer variable
    rDateAdmission = datetime.fromtimestamp((datetime.now() + timedelta(days=dateRandomizer)).timestamp())
    rDateAdmission_timestampStr = rDateAdmission.strftime('%H%M%S-%m%d%Y')
    # create a randomized timestamp using the dateTimeRandomizer variable
    rDateDischarge_timestampStr = datetime.fromtimestamp((rDateAdmission + timedelta(hours=dateTimeRandomizer)).timestamp()).strftime('%H%M%S-%m%d%Y')
    patient_ID = 110001+i
    institution_ID = 9100001+i
    genderRand = random.randrange(0,2)
    raceRand = random.randrange(1,5)
    randomizedHeartRate = randBPM(True)
    heartRateBPM, randomizedTemp = randTemp(randomizedHeartRate, True)
    l = [patient_ID, institution_ID, genderRand, raceRand, rDateAdmission_timestampStr, rDateDischarge_timestampStr, randBP(True), randRespRate(True), randomizedTemp, randCre(True), heartRateBPM, randGCM(True), "True"]
    l_castString = [str(x) for x in l]
    s = ','.join(l_castString)
    with open('toy_dataset_sepsis-withTimestamp.csv', 'a') as fWrite:
        fWrite.write(s + '\n')
