import csv
import sys

# allows csv file to be dropped on to file
try:
    dropped_file = sys.argv[1]
except:
    dropped_file = "download.csv"

# used to name output file in format "filename markers"
filename = dropped_file.split("\\").pop().split('.')[0]


def get_sec(time_str: str) -> int:
    """returns total seconds from hour:minutes:seconds string"""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def get_hms(seconds: int) -> str:
    """returns hour:minutes:seconds"""
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


# get timestamp of markers
times = []
with open(dropped_file) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        # convert twitch timestamp to edl timestamp
        # hours:minutes:seconds:frames
        t = row[0]
        t_in_secs = get_sec(t)
        t_in_secs += 3600
        times.append({"timestamp": get_hms(t_in_secs), "description": row[-1]})


# open file to write to
file = open(f"{filename} markers.edl", "w")
# write boilerplate stuff for davinci resolve edl files
file.write("TITLE: Timeline 1\n")
file.write("FCM: NON-DROP FRAME\n\n")
for index, t in enumerate(times):
    marker_count = index + 1
    new_t = get_sec(t["timestamp"]) + 1
    new_t = get_hms(new_t)
    marker_info = f"{marker_count:03d}  001      V     C        {t['timestamp']}:00 {new_t}:00 {t['timestamp']}:00 {new_t}:00\n"
    marker_info += f"{t['description']} |C:ResolveColorBlue |M:Marker {marker_count} |D:1\n\n"
    
    file.write(marker_info)

file.close()

