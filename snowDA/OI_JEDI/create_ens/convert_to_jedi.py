import numpy as np
import os
from netCDF4 import Dataset
import os
import sys

if (len(sys.argv) != 5):
    print('argument error, usage: convert_to_jedi file_stub resolution dir_in dir_out' )

fstub=sys.argv[1]
res=int(sys.argv[2])
dir_in = sys.argv[3] 
dir_out = sys.argv[4] 


for itm in range(6):
    input_netcdf = dir_in+'/'+fstub+'sfc_data.tile'+str(itm + 1)+'.nc'
    out_netcdf = dir_out+'/'+fstub+'sfc_data.tile'+str(itm + 1)+'.nc'

    ncIn = Dataset(input_netcdf, "r+") 
    ncOut = Dataset(out_netcdf, "w", format='NETCDF4')
    ncOut.createDimension("Time", None)
    var_t = ncOut.createVariable('Time', 'f8', ('Time',))
    attDict_var = {'_FillValue': np.NaN, 'long_name': 'Time', 'units': 'time level', "cartesian_axis": "T"}
    ncOut.variables["Time"].setncatts(attDict_var)
    var_t[:] = np.arange(1) + 1
    ncOut = Dataset(out_netcdf, "r+", format='NETCDF4')
    ncOut.createDimension("xaxis_1", res)
    ncOut.createDimension("yaxis_1", res)
    ncOut.createDimension("zaxis_1", 1)
    ncOut.createDimension("zaxis_2", 4)

    ncOut.createVariable("xaxis_1", "f8", ("xaxis_1",))
    ncOut.createVariable("yaxis_1", "f8", ("yaxis_1",))
    ncOut.createVariable("zaxis_1", "f8", ("zaxis_1",))
    ncOut.createVariable("zaxis_2", "f8", ("zaxis_2",))


    attDict_var = {'_FillValue': np.NaN, 'long_name': 'xaxis_1', 'units': 'none', "cartesian_axis": "X"}
    ncOut.variables["xaxis_1"].setncatts(attDict_var)
    attDict_var = {'_FillValue': np.NaN, 'long_name': 'yaxis_1', 'units': 'none', "cartesian_axis": "Y"}
    ncOut.variables["yaxis_1"].setncatts(attDict_var)

    attDict_var = {'_FillValue': np.NaN, 'long_name': 'zaxis_1', 'units': 'none', "cartesian_axis": "Z"}
    ncOut.variables["zaxis_1"].setncatts(attDict_var)
    attDict_var = {'_FillValue': np.NaN, 'long_name': 'zaxis_2', 'units': 'none', "cartesian_axis": "Z"}
    ncOut.variables["zaxis_2"].setncatts(attDict_var)

    z1_var_ar = [ 
                 "slmsk", "tsea", "sheleg", "tg3", "zorl", "alvsf", "alvwf", "alnsf", "alnwf",
                 "facsf", "facwf", "vfrac", "canopy", "f10m", "t2m", "q2m", "vtype", "stype", "uustar", "ffmm",
                 "ffhh",
                 "hice", "fice", "tisfc", "tprcp", "srflag", "snwdph", "shdmin", "shdmax", "slope", "snoalb",
                 "tref", "z_c", "c_0", "c_d", "w_0", "w_d", "xt", "xs", "xu", "xv", "xz", "zm", "xtts", "xzts",
                 "d_conv", "ifd", "dt_cool", "qrain"]
    z2_var_ar = ["stc", "smc", "slc"]

    for varz1 in z1_var_ar:
        dataType = ncIn.variables[varz1].datatype
        ncOut.createVariable(varz1, dataType, ("Time", "zaxis_1", "yaxis_1", "xaxis_1",))
        varAtts_ref = ncIn.variables[varz1].ncattrs()
        attDict_ref = dict.fromkeys(varAtts_ref)
        for attName in varAtts_ref:
            attDict_ref[attName] = getattr(ncIn.variables[varz1], attName)

        attDict_ref['_FillValue'] = 9.96920996838687e+36
        ncOut.variables[varz1].setncatts(attDict_ref)
        var_array = ncIn.variables[varz1][:]
        print(var_array.shape)
        ncOut.variables[varz1][0, 0, :, :] = var_array[:]

    for varz1 in z2_var_ar:
        dataType = ncIn.variables[varz1].datatype
        ncOut.createVariable(varz1, dataType, ("Time", "zaxis_2", "yaxis_1", "xaxis_1",))
        varAtts_ref = ncIn.variables[varz1].ncattrs()
        attDict_ref = dict.fromkeys(varAtts_ref)
        for attName in varAtts_ref:
            attDict_ref[attName] = getattr(ncIn.variables[varz1], attName)
        attDict_ref['_FillValue'] = 9.96920996838687e+36
        ncOut.variables[varz1].setncatts(attDict_ref)
        var_array = ncIn.variables[varz1][:]
        print(var_array.shape)
        ncOut.variables[varz1][0, :, :, :] = var_array[:]

    ncOut.close()
    ncIn.close()
