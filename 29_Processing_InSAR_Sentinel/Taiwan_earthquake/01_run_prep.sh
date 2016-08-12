#
# Script to pre-process a Sentinel-1a TOPS mode data set.  
#
#   Modified from examples here:
#   http://topex.ucsd.edu/gmtsar/downloads/
#   August 10, 2016
#
#   place the orbits and the *.SAFE directories in the orig directory
#
#  link the orbits, the xml files, and tiff files to the global raw directory
#  put the topo in the global topo directory
#
mkdir raw
cd raw
cp ../orig/*.txt .
ln -s ../orig/S1A_IW_SLC__1SDV_20160202T100019_20160202T100049_009766_00E469_C190.SAFE/annotation/*.xml .
ln -s ../orig/S1A_IW_SLC__1SDV_20160202T100019_20160202T100049_009766_00E469_C190.SAFE/measurement/*.tiff .
ln -s ../orig/S1A_IW_SLC__1SDV_20160214T100019_20160214T100049_009941_00E981_ABD9.SAFE/annotation/*.xml .
ln -s ../orig/S1A_IW_SLC__1SDV_20160214T100019_20160214T100049_009941_00E981_ABD9.SAFE/measurement/*.tiff .
ln -s ../topo/dem.grd .
#
#  pre-process all three subswaths
#
align_tops_esd.csh s1a-iw1-slc-vv-20160202t100019-20160202t100047-009766-00e469-004 S1A_OPER_AUX_POEORB_OPOD_20160222T121629_V20160201T225943_20160203T005943.eof.txt s1a-iw1-slc-vv-20160214t100019-20160214t100047-009941-00e981-004 S1A_OPER_AUX_POEORB_OPOD_20160305T121418_V20160213T225943_20160215T005943.eof.txt dem.grd 
align_tops_esd.csh s1a-iw2-slc-vv-20160202t100020-20160202t100048-009766-00e469-005 S1A_OPER_AUX_POEORB_OPOD_20160222T121629_V20160201T225943_20160203T005943.eof.txt s1a-iw2-slc-vv-20160214t100020-20160214t100048-009941-00e981-005 S1A_OPER_AUX_POEORB_OPOD_20160305T121418_V20160213T225943_20160215T005943.eof.txt dem.grd 
align_tops_esd.csh s1a-iw3-slc-vv-20160202t100021-20160202t100049-009766-00e469-006 S1A_OPER_AUX_POEORB_OPOD_20160222T121629_V20160201T225943_20160203T005943.eof.txt s1a-iw3-slc-vv-20160214t100021-20160214t100049-009941-00e981-006 S1A_OPER_AUX_POEORB_OPOD_20160305T121418_V20160213T225943_20160215T005943.eof.txt dem.grd 
#
#  check the config.s1a.txt and make sure it is processing from step 1 to evaluate orbital information
#
#  make the swath directories and link the appropriate stuff
#
cd ..
rm -r F1/raw
mkdir F1
cd F1
ln -s ../config.s1a.txt .
mkdir raw
cd raw
ln -s ../../raw/*F1* .
cd ..
mkdir topo
cd topo
ln -s ../../topo/dem.grd .
cd ../..
#
rm -r F2/raw
mkdir F2
cd F2
ln -s ../config.s1a.txt .
mkdir raw
cd raw
ln -s ../../raw/*F2* .
cd ..
mkdir topo
cd topo
ln -s ../../topo/dem.grd .
cd ../..
#
rm -r F3/raw
mkdir F3
cd F3
ln -s ../config.s1a.txt .
mkdir raw
cd raw
ln -s ../../raw/*F3* .
cd ..
mkdir topo
cd topo
ln -s ../../topo/dem.grd .
#
