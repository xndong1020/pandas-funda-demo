import json
import os
import pandas as pd

walk_dir = './artworks'

results = []
COLS_TO_USE = ['id', 'all_artists', 'title', 'medium', 'dateText', 'acquisitionYear', 'height', 'width', 'units']

for root, _, files in os.walk(walk_dir):
    # print('--\nroot = ' + root, files)
    for file in files:
        file_path = os.path.join(root, file)

        # only load json files
        if file_path.endswith('json'):
            # print(file_path)
            with open(file_path) as f:
                content = json.load(f)
                # results.append(content)

                data = {}
                # check if the key is in COLS_TO_USE list
                for k, v in content.items():
                    if k in COLS_TO_USE:
                        # if type of the value is string, do rstrip
                        if isinstance(v, str):
                            data[k] = v.rstrip()
                        else:
                            data[k] = v
                    else:
                        continue

                results.append(data)


df = pd.DataFrame(results)
print(df)
