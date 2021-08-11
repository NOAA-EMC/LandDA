#!/bin/ksh

# script to generate pseudo ensemble members for use in LETKF-OI.

python=/contrib/anaconda/anaconda2-4.4.0/bin/python2.7

dir_in='mem_base' # directory with original restarts
file_stub='20191215.120000.' # start of file name for original restarts

b=30 # back ground error std.

n_ens=2

# no changes needed below here

dir_out='mem_det'

rm -rf mem_pos mem_neg mem_det

#$python convert_to_jedi.py $file_stub $res $dir_in $dir_out

cp -r $dir_in mem_pos
cp -r $dir_in mem_neg

$python letkf_create_ens.py $file_stub $b $n_ens

if [[ n_ens -eq 3 ]]; then 
        cp -r $dir_in  mem_det 
fi
