# wfdb
Using wfdb (Waveform Database) to manipulate with waveform-type data Python

- Read the ipynb for a more interactive version
- downsampling.py can be used when pooling multiple data sets with different frequency
- 

---


---
# Application

# 1) Executive Summary
**Goal:**<br></br>
The following notebook attempts to **reproduce** the existing **1.0 accuracy model** on detecting congestive heart failure using 1-D convolutional neural networks with "only one raw electrocardiogram(ECG) heartbeat only".

**Target Study:**<br></br>
https://www.sciencedirect.com/science/article/pii/S1746809419301776#bib0255

**Motivation**<br></br>
Congestive Heart Failure (CHF) or often referred to simply as “heart failure,” as fluid builds up around the heart and causes it to pump inefficiently. CHF is an important concern for its high prevalence, high mortality rates, and sustained healthcare cost.

## 2.1 Abstract
Replicating a scientific paper has several benefits, such as validation and the advancement of the particular field's community knowledge for data analysis which may shape the industry.

## 2.2 Data
**Content:**
1. Verify local data
2. Import relevant packages

> Datasets used
1. MIT-BIH https://physionet.org/content/nsrdb/1.0.0/ - *(Non-event)* <br></br> 
18 long-term ECG recordings of normal healthy not-arrhythmic subjects (Females = 13; age range: 20 to 50) 


2. BIDMC https://physionet.org/content/chfdb/1.0.0/ - *(Event)* <br></br>
15 subjects with severe CHF (i.e., NYHA classes III-IV) (Females = 4; age range: 22 to 63)

