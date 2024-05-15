import re
import os.path

input_path=r"G:\My Drive\FacebookData\groups"

for filename in os.listdir(input_path):
    fullfilename = os.path.join(input_path, filename)
    filename = os.path.basename(fullfilename)
    output_path = r"G:\My Drive\FacebookData\groups_output_new\\"

    with open(fullfilename, 'r', encoding="utf8") as file:
        pi = 0
        ci = 0
        for line in file:
            post_line = re.sub(r"\\\"story\\\":{\\\"message\\\":{\\\"text\\\":\\\"", "post_start", line)
            post_line = re.sub(r"\\\"},\\\"referenced_sticker\\\"", "post_end", post_line)
            post_line = re.sub(r"\\\",\\\"delight_ranges\\\":\[],\\\"image_ranges\\\"", "post_end", post_line)
            post_pattern = re.compile(r"(post_start)(.*?)(post_end)")
            for match in post_pattern.finditer(post_line):
                # print(match.group(2))
                f = open(output_path + filename + "_posts.txt", 'a')
                pi = pi + 1
                f.write(str(pi) + ':' + match.group(2) + "\n")
                f.close()

            cmnt_line = re.sub(r"\\\"depth\\\":0,\\\"body\\\":{\\\"text\\\":\\\"", "cmnt_start", post_line)
            cmnt_line = re.sub(r"\\\"color_ranges\\\":\[],\\\"text\\\":\\\"", "cmnt_start", cmnt_line)
            cmnt_line = re.sub(r"\\\",\\\"ranges\\\":\[]},\\\"attachments\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\",\\\"ranges\\\":\[{\\\"__typename\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\",\\\"translation_type\\\":\\\"ORIGINAL\\\"}", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\"},\\\"message_truncation_line_limit\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\",\\\"__module_operation_CometUFICommentTextBodyRenderer_comment\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\"__module_operation_CometUFICommentDisabledNotice_feedback\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\"comet_sections\\\":{\\\"action_link\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\"__module_operation_CometFeedStoryMessageMatchRenderer_story\\\"", "cmnt_end", cmnt_line)
            cmnt_line = re.sub(r"\\\"},\\\"group_content_views\\\":{\\\"edges\\\"", "cmnt_end", cmnt_line)
            cmnt_pattern = re.compile(r"(cmnt_start)(.*?)(cmnt_end)")
            for match in cmnt_pattern.finditer(cmnt_line):
                # print(match.group(2))
                f = open(output_path + filename + "_comments.txt", 'a')
                ci = ci + 1
                f.write(str(ci) + ':' + match.group(2) + "\n")
                f.close()
