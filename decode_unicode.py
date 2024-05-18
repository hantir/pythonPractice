import re
import os.path
from unidecode import unidecode

input_path=r"G:\My Drive\FacebookData\extracted"

for filename in os.listdir(input_path):
    fullfilename = os.path.join(input_path, filename)
    output_path_ascii = r"G:\My Drive\FacebookData\output\all_post_comments_decode_output_ascii.txt"
    output_path_non_ascii = r"G:\My Drive\FacebookData\output\all_post_comments_decode_output_non_ascii.txt"
    exp_output_path_ascii = r"G:\My Drive\FacebookData\output\exp_all_post_comments_decode_output_ascii.txt"
    exp_output_path_non_ascii = r"G:\My Drive\FacebookData\output\exp_all_post_comments_decode_output_non_ascii.txt"

    with open(fullfilename, 'r', encoding="utf8") as file:
        for line in file:
            f_ascii = open(output_path_ascii, 'a', encoding="utf8")
            f_non_ascii = open(output_path_non_ascii, 'a', encoding="utf8")
            exp_f_ascii = open(exp_output_path_ascii, 'a', encoding="utf8")
            exp_f_non_ascii = open(exp_output_path_non_ascii, 'a', encoding="utf8")
            try:
                line1=line.replace("\\n","\\\\n").encode('utf8').decode('unicode-escape')
                if(line1.encode('utf8').decode('unicode-escape').isascii()):
                    print("ascii " + line1.encode('utf8').decode('unicode-escape'))
                    f_ascii.write(line1.encode('utf8').decode('unicode-escape'))
                else:
                    print("non ascii " + line1.encode('utf8').decode('unicode-escape'))
                    f_non_ascii.write(line1.encode('utf8').decode('unicode-escape'))
            except:
                if (line1.isascii()):
                    exp_f_ascii.write(line)
                    print("in exception ascii " + line.encode('utf8').decode('unicode-escape'))
                else:
                    print(unidecode(line1))
                    exp_f_non_ascii.write(line)
                    print("in exception non ascii " + line.encode('utf8').decode('unicode-escape'))
        f_ascii.close()
        f_non_ascii.close()