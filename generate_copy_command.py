# import the necessary packages
from imutils import paths
import argparse
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
                help="path to input directory of faces + images")
args = vars(ap.parse_args())

# getting list sub folder
print("[INFO] getting list of sub folder...")
subFolderCounter = sum([len(d) for r, d, folder in os.walk(args["dataset"])])
print("[INFO] there are {} folders".format(subFolderCounter))
sub_folders = [f.path for f in os.scandir(args["dataset"]) if f.is_dir()]
print("[INFO] done!")

# generate copy command content
copy_command_content = ""
for i, sub_folder in enumerate(sub_folders):
    copy_command_content = copy_command_content + "python get_examples.py -i {} -d examples".format(sub_folder)
    if i < sub_folders.__len__() - 1:
        copy_command_content = copy_command_content + "\n"

# write content to copy.cmd
print("[INFO] write code to copy.cmd")
f = open("copy.cmd", "w")
f.write(copy_command_content)
f.close()
print("[INFO] done!")
