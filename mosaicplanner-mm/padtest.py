#FOR TESTING

from PIL import Image
import MetadataHandler
import numpy as np


files = ['C:\\Program Files\\Micro-Manager-1.4\\new_tiles\\(-128.75, -50.25, -11.999)\\img_(-128.75, -50.25, -11.999)_.tif',
         'C:\\Program Files\\Micro-Manager-1.4\\new_tiles\\(-1097.5, 50.5, -7.9990000000000006)\\img_(-1097.5, 50.5, -7.9990000000000006)_.tif']
         

         
stuff = []
for i in files:
    ext = MetadataHandler.LoadMetadata(i)
    tile = Image.open(i)
    stuff.append((tile,ext))

print stuff

def pad(mosaic,tile,mosaic_extent,tile_extent):
    print mosaic_extent,"me"
    print tile_extent,"te"
    #takes mosaic and pads based on current extent(in Um) and new extent,
    #returns new mosaic and new extent

    #checking to see whether tile or mosaic has the maximum/min for extent
    if tile_extent[0] <= mosaic_extent[0]:
        print "yes"
        minx = tile_extent[0]
    else:
        minx = mosaic_extent[0]
    print minx,"MIN"    
    if tile_extent[1] >= mosaic_extent[1]:
        maxx = tile_extent[1]
    else:
        maxx = mosaic_extent[1]
        
    if tile_extent[2] <= mosaic_extent[2]:
        miny = tile_extent[2]
    else:
        miny = mosaic_extent[2]
        
    if tile_extent[3] >= mosaic_extent[3]:
        maxy = tile_extent[3]
    else:
        maxy = mosaic_extent[3]
    
    extent = (minx,maxx,miny,maxy)
    print extent,"extent"


    #can I just convert back to pixels here? also are pxUm conversions
    #intoducing error?
    px1,px2 = [i/.6 for i in mosaic_extent],[i/.6 for i in tile_extent]
    print px1,px2

    #size = tile_extent maxx - mosaic_extent minx..
    #Padding
    size_int = (abs(int(maxx/.6-minx/.6)),abs(int(maxy/.6-miny/.6)))
    
    im = Image.new('L',size_int)
##    print px1,"px1"
##    print px2,"px2"
##    print minx/.6
##    print miny/.6
    im.paste(mosaic,(int(abs(px1[1]-maxx/.6)),int(abs(px1[3]-maxy/.6))))
    im.paste(tile,(abs(int(px2[1]-maxx/.6)),int(abs(px2[3]-maxy/.6))))
    print int(px1[1]-minx/.6),int(abs(px1[3]-maxy/.6)),"m"
    print int(px2[1]-minx/.6),int(abs(px2[3]-maxy/.6))
##    print size_int
    im.show()
    im.save(os.path.join(os.getcwd(),'mosaic.tif'))
    return im,extent

import os
x = pad(stuff[0][0],stuff[1][0],stuff[0][1],stuff[1][1])
##z = pad(x[0],stuff[2][0],x[1],stuff[2][1])
##p = pad(stuff[3][0],z[0],stuff[3][1],z[1])
##r = pad(stuff[4][0],p[0],stuff[4][1],p[1])
##l = pad(stuff[5][0],r[0],stuff[5][1],r[1])

