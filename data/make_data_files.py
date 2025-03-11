#!/usr/bin/env python

##
#  Builds the data files in the expected format from 
#
# from >> 
#VSV,VSH,VPV,VPH,RHO
#NaN,NaN,NaN,NaN
#NaN,NaN,NaN,NaN
#NaN,NaN,NaN,NaN
#NaN,NaN,NaN,NaN
#NaN,NaN,NaN,NaN
#3253.4781923066785,3243.5911548789195,5797.5117446332515,5841.516290741993,2.7091302424180017
# it looks like.. traverse z first 0-99
#                 traverse lat 31.5 -> 31.55 ... 
#                 traverse lon -125.0 ->
#

import getopt
import sys
import subprocess
import struct
import array
import math

if sys.version_info.major >= (3) :
  from urllib.request import urlopen
else:
  from urllib2 import urlopen

## at CANVAS/canvas.txt

model = "CANVAS"

dimension_x = 0
dimension_y = 0 
dimension_z = 0

lon_origin = 0
lat_origin = 0

lon_upper = 0
lat_upper = 0

def usage():
    print("\n./make_data_files.py\n\n")
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
        continue
    if path == "" :
        print("ERROR: failed to find variables from config file")
        sys.exit(1)

    fp.close()

    print("\nDownloading model file\n")

    fname="./"+"canvas.txt"
    url = path + "/" + fname
#
#    download_urlfile(url,fname)

    subprocess.check_call(["mkdir", "-p", mdir])

    # Now we need to go through the data files and put them in the correct
    # format for LSU_IV. More specifically, we need a Vp.dat

    fp = open("./canvas.txt");
    f_vs = open("./canvas/vs.dat", "wb")
    f_vp = open("./canvas/vp.dat", "wb")
    f_density = open("./canvas/density.dat", "wb")

    vs_arr = array.array('f', (-1.0,) * (dimension_x * dimension_y * dimension_z))
    vp_arr = array.array('f', (-1.0,) * (dimension_x * dimension_y * dimension_z))
    density_arr = array.array('f', (-1.0,) * (dimension_x * dimension_y * dimension_z))

    print ("dimension is", (dimension_x * dimension_y * dimension_z))

    data_nan_cnt = 0
    data_total_cnt =0;

    x_pos=0;
    y_pos=0;
    z_pos=0;

    for line in fp:
#        print("x_pos ",x_pos, " y_pos ",y_pos," z_pos ", z_pos)
        arr = line.split()

#vsv,vsh,vpv,vph,rho
        vsv = (arr[0])
        vsv_v = -1 if (vsv == "NaN") else float(vsv) 
        vsh = (arr[1])
        vsh_v = -1 if (vsh == "NaN") else float(vsh) 

        vpv = (arr[2])
        vpv_v = -1 if (vpv == "NaN") else float(vpv) 
        vph = (arr[3])
        vph_v = -1 if (vph == "NaN") else float(vph) 
     
# Voigt-averaged Vs and Vp
# equations from Panning and Romanowicz, 2006,

        if (vsv != "NaN" ) :
            vs =  math.sqrt((2 * (vsv_v * vsv_v) + (vsh_v * vsh_v))/3)
        else:
            vs=-1

        if (vpv != "NaN" ) :
            vp =  math.sqrt(((vpv_v * vpv_v) + 4 * (vph_v * vph_v))/5)
        else:
            vp=-1

        density = (arr[4])
        density_v = -1 if (density == "NaN") else float(density) 

        if (vsv == "NaN" ) :
           data_nan_cnt = data_nan_cnt + 1

        data_total_cnt = data_total_cnt + 1

        loc =z_pos * (dimension_y * dimension_x) + (x_pos * dimension_y) + y_pos
#        print("location for this..",loc)

        vs_arr[loc] = vs
        vp_arr[loc] = vp
        density_arr[loc] = density_v

#        if (data_total_cnt > 102) : return True

##"Dimensions:    (longitude: 220, latitude: 230, depth: 100)\n",
##"Coordinates:\n",
##"  * longitude  (longitude) float64 -125.0 -124.9 -124.9 ... -114.1 -114.1 -114.0\
##n",
##"  * latitude   (latitude) float64 31.5 31.55 31.6 31.65 ... 42.9 42.95 43.0\n",
##"  * depth      (depth) float64 0.0 1.01e+03 2.02e+03 ... 9.899e+04 1e+05\n",

        z_pos = z_pos + 1
        if(z_pos == dimension_z) :
          z_pos = 0;
          y_pos = y_pos+1
          if(y_pos == dimension_y) :
            y_pos=0;
            x_pos = x_pos+1
            if(x_pos == dimension_x) :
              print ("All DONE")

    vp_arr.tofile(f_vp)
    vs_arr.tofile(f_vs)
    density_arr.tofile(f_density)

    fp.close()
    f_vs.close()
    f_vp.close()
    f_density.close()

    print("Done! with NaN(", data_nan_cnt, ") total(", data_total_cnt,")")


if __name__ == "__main__":
    main()

