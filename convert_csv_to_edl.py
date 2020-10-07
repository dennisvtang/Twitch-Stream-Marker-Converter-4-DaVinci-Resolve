import csv
import sys


# allows csv file to be dropped on to file
try:
    droppedFile = sys.argv[1]
except:
    droppedFile = "download.csv"

def get_sec(time_str) -> int:
    """returns total seconds from hour:minutes:seconds string"""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def get_hms(seconds) -> str:
    """returns hour:minutes:seconds"""
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


# get timestamp of markers
times = []
with open(droppedFile) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        # convert twitch timestamp to edl timestamp
        # hours:minutes:seconds:frames
        t = row[0]
        t_in_secs = get_sec(t)
        t_in_secs += 3600
        times.append(get_hms(t_in_secs))


# open file to write to
file = open('markers.edl', "w")
# write boilerplate stuff for davinci resolve edl files
file.write("TITLE: Timeline 1\n")
file.write("FCM: NON-DROP FRAME\n\n")
for index, t in enumerate(times):
    marker_count = index + 1
    new_t = get_sec(t) + 1
    new_t = get_hms(new_t)
    marker_info = f"{marker_count:03d} 001      V     C        {t}:00 {new_t}:00 {t}:00 {new_t}:00\n"
    marker_info += " |C:ResolveColorBlue |M:Marker 1 |D:1\n\n"
    
    file.write(marker_info)

file.close()

