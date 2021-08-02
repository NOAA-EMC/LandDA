This directory relates to tasks necessary to convert the snow depth OI into JEDI. 

The OI has been implemented as a special case of the LETKF within the fv3-bundle of JEDI: 

https://github.com/JCSDA-internal/fv3-bundle.git

Tasks include: 

1. Adding the OI algorithm as a special case of the LETKF.
 
Status: complete. 

To run the OI, use the letkf_snow testcase.

2. Adding snow depth-specific code, including QC and interpolation routines. 

Status: 
-land-ice mask QC is outstanding. 
-update the JEDI test case to include QC (wait for Sergey to implement QC on ensmeble mean). 

3. Evaluation of global OI algorithm within JEDI, against the PSL version. 

Status: only done for single obs. cases. 

