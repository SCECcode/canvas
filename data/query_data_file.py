#!/usr/bin/env python

##
# query the latlon mesh with latlon
#


import getopt
import sys
import subprocess
import struct
import numpy as np


try:
  fp = open('./config','r')
except:
  print("ERROR: failed to open config file")
  sys.exit(1)

    ## look for model_data_path and other varaibles
lines = fp.readlines()
for line in lines :
        if line[0] == '#' :
          continue
        parts = line.split('=')
        if len(parts) < 2 :
          continue;
        variable=parts[0].strip()
        val=parts[1].strip()

        if (variable == 'model_dir') :
            model=val
            continue
        if (variable == 'model_data_path') :
            path = val + '/' + model
            continue
        if (variable == 'model_dir') :
            mdir = "./"+val
            continue
        if (variable == 'nx') :
            dimension_x = int(val)
            continue
        if (variable == 'ny') :
            dimension_y = int(val)
            continue
        if (variable == 'nz') :
            dimension_z = int(val)
            continue
        if (variable == 'top_right_corner_lon') :
            lon_upper = float(val)
            continue
        if (variable == 'top_right_corner_lat') :
            lat_upper = float(val)
            continue
        if (variable == 'bottom_left_corner_lon') :
            lon_origin = float(val)
            continue
        if (variable == 'bottom_left_corner_lat') :
            lat_origin = float(val)
            continue
        continue

if path == "" :
    print("ERROR: failed to find variables from config file")
    sys.exit(1)

fp.close()





#######################

rdelta_lon = (lon_upper - lon_origin )/(dimension_x-1)
rdelta_lat = (lat_upper - lat_origin)/(dimension_y-1)
delta_lon = float('%1.2f'%rdelta_lon)
delta_lat = float('%1.2f'%rdelta_lat)

## last in slice
#last
target_lon = -114.0
target_lat = 42.0
target_depth =  99000
#first
#target_lon = -125.0
#target_lat = 31.5
#target_depth =  99000

## origin
#target_lon = -125.0
#target_lat = 31.5
#target_depth = 0


def main():

    zone=10
    f_vp = open("./canvas/vp.dat")
    vp_arr = np.fromfile(f_vp, dtype=np.float32)
    f_vp.close()


    if (target_lon == lon_origin) :
        x_pos=0
    else:
        x_pos= int(abs(round((target_lon - lon_origin) / delta_lon)))

    if (target_lat == lat_origin) :
        y_pos=0
    else:
        y_pos=int(round((target_lat - lat_origin) / delta_lat))

    z_pos = int(target_depth/1000)

    offset=z_pos * (dimension_y * dimension_x) + (y_pos * dimension_x) + x_pos

    vp=vp_arr[offset];

    print ("offset:", offset)
    print ("xyz:", x_pos,y_pos,z_pos,"(",target_lat,target_lon,target_depth, ")--> vp ", vp)
    print ("Done!")

if __name__ == "__main__":
    main()


