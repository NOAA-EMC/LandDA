import numpy as np
from netCDF4 import Dataset
import sys

# calculate the desired standard deviation
#b= 30. 

if (len(sys.argv) != 4): 
    print('argument error, usage: letkf_create back_error n_ens' ) 

fstub=sys.argv[1]
b = float(sys.argv[2]) 
n = float(sys.argv[3])

if (n==2): 
    offset=b/np.sqrt(2)
elif (n==3):
    offset=b 
else:
     print('ERROR: number of ensemble members can only be 2 or 3') 

print('adjusting by '+str(offset))

sign = [1,-1]
ens_dirs=['mem_pos','mem_neg'] 

for ens in range(2): 

    for tt in range(6):
        # open file 
        out_netcdf = ens_dirs[ens]+'/'+fstub+'sfc_data.tile'+str(tt+1)+'.nc'
        ncOut = Dataset(out_netcdf, "r+")  
        # add offset to the snow
        var_array = ncOut.variables["snwdph"][:]
        var_array = var_array + sign[ens]*offset
        ncOut.variables["snwdph"][0,:,:] = var_array[:]
        ncOut.close()
