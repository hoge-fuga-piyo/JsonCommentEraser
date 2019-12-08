import sys
import re

args = sys.argv

comment_pattern = r"(\s|\t)*//"

with open(args[1], 'r', newline='') as f:
  for line in f:
    is_comment = False
    # 空行を削除:w
    if line.strip() == '':
      continue

    # コメント行を削除
    matchOB = re.match(comment_pattern, line)
    if matchOB:
      is_comment = True
    if is_comment is False:
      print(line, end='')
