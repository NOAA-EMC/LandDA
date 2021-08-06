This directory relates to tasks necessary to convert the snow depth OI into JEDI. 

The OI has been implemented as a special case of the LETKF within the fv3-bundle of JEDI: 

https://github.com/JCSDA-internal/fv3-bundle.git

In brief: we run the LETKF with two (or three) ensemble members, using "artificial" ensemble members that have been created by perturbing the forecast snow depth to give an ensemble with the background error that the OI uses. We then use R localization to create increments with spatial patterns that approximate the OI.

To run the OI, need to: 

1. Generate artificial ensemble members.

See code in create_ens. 

Originally we created two ensemble members (the minimum needed to calculate an ensemble standard deviation). However, JEDI applies QC based on the model states in the last ensemble member, which has been artificially perturbed. To get around this we are currently using three ensemble members, with the 3rd member equal to the forecast ( so that the QC is then applied using the values in the forecast). Sergey is working on adding code to JEDI so that the QC is applied to the ensemble mean. Once this code is in place, we will revert to using only two ensemble members. Can switch between 2 and 3 members by commenting out the appropriate block in create_ens.

2. Call the JEDI executable. 

This will output an increment at every grid cell globally.  See below for task list.

3. Read in the increment file output by JEDI, and add it to the model snow depth state. 

This will be done in UFS_UTILS, following the approach Clara coded for soil increments.

Need to also: 
-screen to only apply increments over land 
-limit analyses snow depth to be non-negative 
-update the SWE to be consistent with the SD updates.



######################################

Sub-tasks required to create the JEDI increment under step 2 above.

1. Adding the OI algorithm as a special case of the LETKF.
 
Status: complete. 

To run the OI, use the letkf_snow testcase. Latest yaml is in this directory.

2. Adding snow depth-specific code, including QC and interpolation routines. 

Status:  work completed, except for removal of duplicate observations
-need to update the JEDI test case to include QC
(wait for Sergey to implement QC on ensmeble mean, and for Youlong to add station  ID to the GHCN file so that we can remove duplicates)

See yaml in this directory. Will also need land.yaml from this directory to replace the one in the JEDI distribution.

3. Evaluation of global OI algorithm within JEDI, against the PSL version. 

Status: comparison shows some differences where more than one ob is assimilated. Sergey and Clara are investigating.

