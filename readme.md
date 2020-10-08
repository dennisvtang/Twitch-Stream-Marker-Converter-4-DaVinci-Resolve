# Twitch marker importer 4 DaVinci Resolve
Twitch marker importer 4 DaVinci Resolve converts twitch's csv file for stream markers into a edl file which DaVinci Resolve can import onto a project's timeline. 

## Features
- includes description and creator of the marker in the markers created in DaVinci Resolve

# Usage
1. Rename csv file to something appropriate as the program will output the file "csv's filename markers"
2. Drag and drop csv file onto "converter.py" or "converter.exe"
3. Import resulting edl file onto the timeline

Using the compiled version

![compiled demo](img/compiled_demo.gif)

Using the python script version

![python script demo](img/script_demo.gif)

Importing edl file onto a timeline
![importing into resolve demo](img/importing_into_resolve.gif)


# Todo
- [ ] apply markers directly to individual files rather than entire timeline
- [ ] allow for batch convert of csv files
- [ ] support for other editors