#!/usr/bin/env python
# coding: utf-8

# In[10]:

import wfdb
import scipy.signal as signal
import peakutils
import numpy as np
import os
import plotly.graph_objects as go
import pandas as pd
from scipy.signal import find_peaks


# In[133]:


class loader:
    def loader_(self,rpath):
        self.records={}
        self.signal_slice={}
        self.smoothed_signal={}
        self.r_peaks={}
        flist = os.listdir(rpath)
        flist = [file for file in flist if file.endswith(".dat")]   
        for file in flist:
            self.records[file] = wfdb.rdrecord(rpath+file[:-4],channels=[0])
    def signal_slice_(self):
        for record in self.records:
            self.signal_slice[record]=np.ndarray.flatten(self.records[record].p_signal[0:1000])
    def smoothed_signal_(self):
        for record in self.records:
            self.smoothed_signal[record]=signal.cspline1d(self.signal_slice[record],lamb=1000)
    def r_peaks_(self):
        for record in self.records:
            self.r_peaks[record]=peakutils.indexes(self.smoothed_signal[record],thres=0.5,min_dist=0.1)

