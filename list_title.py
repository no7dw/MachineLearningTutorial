import re
import os
import sys
reg = '###.*\n'
if len(sys.argv)>1:
    walk_dir = sys.argv[1]
else:
    walk_dir = '.'
#print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
#print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        if file_path.endswith('.md'):
            print('%s' % (file_path))
            with open(file_path, 'r') as f:
                f_content = f.read()
                result = re.findall(reg, f_content)
                if len(result):
                    print(result[0])
                #else:
                #    print('file %s not contains title\n' % file_path)

