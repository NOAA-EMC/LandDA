
  Somewhat generic Fortran code to map lat/lon pairs to location in FV3 tiles

  Most of the changable variables are near the top of the file:

     ims_size : assuming a square input ims dimension
     fv3_size : size of fv3 cube side
     ims_path : location of ims binary latitude and longitude files
     ims_lat_name : name of latitude file
     ims_lon_name : name of longitude file
     fv3_path : path to fv3 grid files
     fv3_search_order : order to search the tiles (default is most to least land grids)
