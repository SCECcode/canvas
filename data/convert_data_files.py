#!/usr/bin/env python
##
# Builds the data files in the expected format 
# from CANVAS_model.txt (stored over at CARC)
#
# from : Lat Lon Depth Vp Vpv Vph Vs Vsv Vsh
#
#   NOTE:  this simplified method only work for dataset
#          with no 'rotation'.  
#          ie. right square/rectangle mesh
## 

import getopt
import sys
import subprocess
import struct
import array

if sys.version_info.major >= (3) :
  from urllib.request import urlopen
else:
  from urllib2 import urlopen

## at CANVAS_model.txt
model = "CANVAS"

#
dimension_x = 0
dimension_y = 0 
dimension_z = 0 

lon_origin = 0
lat_origin = 0  

lon_upper = 0 
lat_upper = 0 

def usage():
    print("\n./create_data_files.py\n\n")
    sys.exit(0)

def download_urlfile(url,fname):
  try:
    response = urlopen(url)
    CHUNK = 16 * 1024
    with open(fname, 'wb') as f:
      while True:
        chunk = response.read(CHUNK)
        if not chunk:
          break
        f.write(chunk)
  except:
    e = sys.exc_info()[0]
    print("Exception retrieving and saving model datafiles:",e)
    raise
  return True

def main():

    # Set our variable defaults.
    path = ""
    mdir = ""

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
        if (variable == 'bottom_left_corner_lon') :
            lon_origin = float(val)
            continue
        if (variable == 'bottom_left_corner_lat') :
            lat_origin = float(val)
            continue
        if (variable == 'top_right_corner_lon') :
            lon_upper = float(val)
            continue
        if (variable == 'top_right_corner_lat') :
            lat_upper = float(val)
            continue

        continue
    if path == "" :
        print("ERROR: failed to find variables from config file")
        sys.exit(1)

    fp.close()

    delta_lon = (lon_upper - lon_origin )/(dimension_x-1)
    delta_lat = (lat_upper - lat_origin)/(dimension_y-1)
#for ycoord in xrange(dimension_y):
#   yloc = lat_origin + (ycoord * delta_lat)
#  print "yloc - ",yloc
#for xcoord in xrange(dimension_x):
#   xloc = lon_origin + (xcoord * delta_lon)
#   print  "xloc - ",xloc


    # Now we need to go through the data files and put them in the correct
    # format for CANVAS. More specifically, we need a Vp.dat

    print("\nDownloading model file\n")

    fname="./"+"CANVAS_Model.txt"
    url = path + "/" + fname
    download_urlfile(url,fname)

    print("\nWriting out CANVAS data files\n")

    subprocess.check_call(["mkdir", "-p", mdir])

    f = open(fname)
    f_vp = open(mdir+"/vp.dat", "wb")
    f_vs = open(mdir+"/vs.dat", "wb")

#    print("size of model, ",dimension_x * dimension_y * dimension_z)

    vp_arr = array.array('f', (-1.0,) * (dimension_x * dimension_y * dimension_z))

# from : Lat Lon Depth Vp Vpv Vph Vs Vsv Vsh
    vp_nan_cnt = 0
    vs_nan_cnt = 0
    total_cnt =0;
    for line in f:
        arr = line.split()
        lat_v = float(arr[0])
        lon_v = float(arr[1])
        depth_v = float(arr[2])
        vp = float(arr[3])
        vs = float(arr[6])
        total_cnt = total_cnt + 1

        if(vp == "NaN") :
            vp_nan_cnt=vp_nan_cnt+1
            vp=-9999
        if(vs == "NaN") :
            vs_nan_cnt=vs_nan_cnt+1
            vs=-9999

        y_pos = int(round((lat_v - lat_origin) / delta_lat))
        x_pos = int(round((lon_v - lon_origin) / delta_lon))
        z_pos = int(depth_v)

        loc =z_pos * (dimension_y * dimension_x) + (y_pos * dimension_x) + x_pos

        vp_arr[loc] = vp
        vs_arr[loc] = vs

#        if( tmp != "NaN" ):
#          print x_pos," ",y_pos," ",z_pos," >> ",lon_v," ",lat_v," ",depth_v," ",vp 
#        else:
#          print "NAN", x_pos," ",y_pos," ",z_pos," >> ",lon_v," ",lat_v," ",depth_v," ",vp 

    vp_arr.tofile(f_vp)
    vs_arr.tofile(f_vs)

    f.close()
    f_vp.close()
    f_vs.close()

    print("Done! with NaN", "vp(", vp_nan_cnt,") vs(", vs_nan_cnt, ") total", total_cnt)

if __name__ == "__main__":
    main()

