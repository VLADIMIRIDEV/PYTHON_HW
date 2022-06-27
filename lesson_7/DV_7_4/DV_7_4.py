import os
from collections import defaultdict
import django


root_dir = django.__path__[0]
django_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        result = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        django_files[result] += 1
for result, files in sorted(django_files.items()):
    print(f'{result}: {files}')