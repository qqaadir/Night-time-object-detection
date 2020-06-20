import glob

file_path1=r"F:/Night-time_data/Snow_20200420/group1/"
file_path2=r"F:/Night-time_data/Snow_20200420/group2/"
file_path3=r"F:/Night-time_data/Snow_20200420/group3/"
paths={file_path1, file_path2, file_path3}  # input file paths

output_files = ["g_result01.NMEA", "g_result02.NMEA", "g_result03.NMEA"] # output file names
c = 0
for p in paths:
    read_files = glob.glob(p + "*.NMEA")     # read all file with specific extension
    with open(output_files[c], "wb") as outfile:
        c = c+1
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())   # combine all files here