Brief: Development and testing of OI for the Noah model at PSL. This is the pre-JEDI version.

Status: complete.

Details: DA input parameters adopted directly from ECMWF (no tuning attempted).
Uses GHCN station observations in place of NRT station obs.
Tested October, 2019 - April 2020 at C128, showed significant improvement to snow depth, reduction in T2m biases over snow cover areas.

Directories: 
src contains the code. Compiles on hera. 
test contains the C48 testcase for hera.
