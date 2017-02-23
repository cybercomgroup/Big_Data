import hdf5_getters
h5 = hdf5_getters.open_h5_file_read("A/A/A/TRAAABD128F429CF47.h5")
nrsongs=get_num_songs(h5);
duration = hdf5_getters.get_duration(h5)
print("nrsongs: "+str(nrsongs))
print("duration: "+str(duration))
h5.close()
