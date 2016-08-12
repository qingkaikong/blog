#
#  make all the interferograms. can run them in parallel.
#
cd F1
p2p_S1A_TOPS.csh S1A20160202_100019_F1 S1A20160214_100019_F1 config.s1a.txt >& log &
cd ../F2
p2p_S1A_TOPS.csh S1A20160202_100020_F2 S1A20160214_100020_F2 config.s1a.txt >& log &
cd ../F3
p2p_S1A_TOPS.csh S1A20160202_100021_F3 S1A20160214_100021_F3 config.s1a.txt >& log &
