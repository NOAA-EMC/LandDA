This directory relates to the tasks necessary to implement the snow depth OI at EMC. 

The OI is based on the scheme originally developed by Brasnett at Environment Canada  (Brasnett, 1999) and its implementation at ECMWWF. It is a univariate DA update performed on snow depth, and ingests station snow depth observations and IMS scow cover observations. The latter are converted to a pseudo snow depth, based on the model snow depletion curve. For details see: 

Gichamo and Draper, A Modern Snow Data Assimilation System for NOAA’s Unified Forecast System (UFS), J Hydromet (in prep). 

Directory/Task list:

>snowOI 
Original development of OI for the Noah model at PSL. 

DA input parameters adopted directly from ECMWF (no tuning attempted).
Uses GHCN station observations in place of NRT station obs. 
Tested October, 2019 - April 2020 at C128, showed significant improvement to snow depth, reduction in T2m biases over snow cover areas.
