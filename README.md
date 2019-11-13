## README

### Overview
This repository contains a toy dataset for use with testing and building Machine Learning (ML) models that predict clinical outcomes from patient Electronic Health Records (EHR) data. The dataset is free to use an contains no actual patient information. Several publications were referenced in an effort to data points that somewhat resembled actual clinical patient data. The data is formatted as a flatfile CSV format, and divided into "sepsis" and "non-sepsis" patients. An example is shown here:

| Patient_ID    | Institution_ID    | Gender  | Race | BP-Systolic | Respiratory_Rate | Body_Temp | Creatinine | Heart_Rate-BPM |  GCM | Sepsis Flag |
| ---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|---------:|
| 100001 | 900001 | 1 | 2 | 130 | 15 | 37.0 | 1.2 | 101 | 15 | False |

The fields are described [below](https://github.com/disulfidebond/ehr_toy_dataset/blob/master/README.md#data-fields). It is important to note that this is a toy dataset with no actual data, and is intended to be a practice tool *only*. Several assumptions are built into this dataset:

* The data has been divided into "sepsis" and "not sepsis", which are independent from each other.
* All values have been randomly generated, with the following exceptions:
  * There are equal numbers of data values with the "sepsis" and "not sepsis" flag.
  * [Temperature is linked to heart rate](https://github.com/disulfidebond/ehr_toy_dataset/blob/master/README.md#body_temp) in an effort to create a more realistic simulated dataset.
  * For data values that are linked to the "sepsis" flag, the corresponding clinical values have been shifted to artifically ensure that they match expected clinical presentation. Details on how this was done are available in each section.

### Data Fields
Each of the data fields are described below.

#### Patient_ID
This field is a randomly generated 6-digit integer, and is meant to simulate a de-identified patient identifier.

#### Institution_ID
This field is a randomly generated 6-digit integer, and is meant to simulate a de-identified institution identifier.

#### Gender
This field is a randomly generated integer, where 0 == male, and 1 == female.

#### Race
This field is a randomly generated integer, where 1 == "white", 2 == "hispanic", 3 == "black", 4 == "Asian"

#### BP-Systolic
This field is a randomly generated integer ranging from 80-180, with the following limitations:

        if sepsis_flag == True:
          # generate a random integer between 80 and 100
          return random.randrange(80, 101)
        else:
          # generate a random integer between 95 and 180
          return random.randrange(95, 181)

* Sources: [Afshar et al 2019](https://www.ncbi.nlm.nih.gov/pubmed/31306176), [Harvard Health Publishing](https://www.health.harvard.edu/blog/new-high-blood-pressure-guidelines-2017111712756), [Pitzalis et al 1998](https://www.ncbi.nlm.nih.gov/pubmed/?term=9709393)

#### Respiratory_Rate
This field is a randomly generated integer ranging from 1-60, with the following limitations:

        if sepsis_flag == True:
          # randomly generate a float between 0 and 1.0
          rValue = random.random()
          # if this value is less than 0.4, then return a very low respiratory rate
          # otherwise, return a very high respiratory rate
          if rValue < 0.4:
            return random.randrange(1, 3)
          else:
            return random.randrange(22, 61)
         else:
           # if sepsis_flag is false, generate a respiratory rate between 6 and 21
           return random.randrange(6, 22)

* Sources: [Andrew Lever 2007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2043413/)

#### Body_Temp
This field is a randomly generated float ranging from 34.0 to 40.1

It is [tied to heart rate](https://github.com/disulfidebond/ehr_toy_dataset/blob/master/README.md#heart_rate-bpm), and subject to the following limitations:

        if sepsis_flag == True:
          # randomly generate a float between 0 and 1.0
          rValue = random.random()
          # if this value is less than 0.4, then return a very low body temp
          # otherwise, return a very high body temp
          if rValue < 0.4:
            randomizedTemp = random.uniform(34.0, 36.0)
            randomizedTemp = round(randomizedTemp, 2)
          else:
            randomizedTemp = random.uniform(38.0, 40.1)
            randomizedTemp = round(randomizedTemp, 2)
        if randomizedTemp > 38.0:
          # randomly generate a temperature in Celsius from a distribution 
          # with the tail ends at slightly abnormal cold or feverish ranges
          randomizedTemp = random.uniform(36.0, 38.5)
          # update heart rate as described in literature
          modBPM = int((abs(randomizedTemp-37)/0.5)*10)
          modifiedBPM = modBPM + bpm
          return (randomizedTemp, modifiedBPM)
          
          
        if sepsis_flag == False:
          # randomly generate a temperature in Celsius from a distribution 
          # with the tail ends at slightly abnormal cold or feverish ranges
          randomizedTemp = random.uniform(36.0, 38.5)
          # update heart rate as described in literature
          modBPM = int((abs(randomizedTemp-37)/0.5)*10)
          modifiedBPM = modBPM + bpm
          return (randomizedTemp, modifiedBPM)
        
* Sources: [Davies and Maconochie 2009](https://www.ncbi.nlm.nih.gov/pubmed/?term=19700579), [Kendra Houston 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4681323/), [Afshar et al 2019](https://www.ncbi.nlm.nih.gov/pubmed/31306176)


#### Creatinine
This field is a randomly generated float ranging from 0.6 to 6.0, and is subject to the following limitations:

        if sepsis_flag == True:
          randCreatinine = round(random.uniform(1.2, 6.0), 2)
          return randCreatinine
        else:
          randCreatinine = round(random.uniform(0.5, 3.0), 2)
          return randCreatinine          

* Sources: [Afshar et al 2019](https://www.ncbi.nlm.nih.gov/pubmed/31306176), [Marik and Taeb 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5418298/), [Gül et al 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5512390/)

#### Heart_Rate-BPM
This field is a randomly generated integer ranging from 60 to 210, with the following limitations:

        if sepsis_bool == True:
          return random.randrange(140, 211)
        else:
          return random.randrange(60, 181)

* Note that this is tied to the [Body_Temp value](https://github.com/disulfidebond/ehr_toy_dataset/blob/master/README.md#body_temp)
* Sources: [Afshar et al 2019](https://www.ncbi.nlm.nih.gov/pubmed/31306176), Davies and Maconochie 2009](https://www.ncbi.nlm.nih.gov/pubmed/?term=19700579), [Kendra Houston 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4681323/)

#### GCM
This field is always 15 for non sepsis patients, and an integer ranging from 7 to 15 for sepsis patients
* Sources: [CDC](https://www.cdc.gov/masstrauma/resources/gcs.pdf)

#### Sepsis Flag
This field is True for a sepsis patient, and False for a non-sepsis patient.

