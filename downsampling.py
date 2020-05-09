import wfdb
from wfdb import processing
# import os

'''
Put this code with your dataset
'''

file = input("Please type your file name: ")
fs = input("What fs this should be downsampled to: ")

def downsampling:
    record = wfdb.rdrecord(file) # Reading signal
    ann = wfdb.rdann(file, 'ecg') # Reading annotation
    record.p_signal, record.sig_len = processing.resample_multichan(record.p_signal, ann, record.fs, fs_target = fs) # Downsample to target
    record.fs = fs # Update record's FS
    

downsampling(file, fs)