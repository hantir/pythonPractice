import re
import os.path

input_path=r"G:\My Drive\FacebookData\groups_output_new"

for filename in os.listdir(input_path):
    fullfilename = os.path.join(input_path, filename)
    output_path = r"G:\My Drive\FacebookData\groups_output_new\all_post_comments_output.txt"

    with open(fullfilename, 'r', encoding="utf8") as file:
        for line in file:
            f = open(output_path, 'a')
            f.write(line)
        f.close()