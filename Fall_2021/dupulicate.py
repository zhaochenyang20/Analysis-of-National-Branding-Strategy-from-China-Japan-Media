import json
import os
from tqdm import tqdm

# if __name__ == '__main__':
#     path = "./result"
#     dirs = os.listdir(path)
#     for file in tqdm(sorted(dirs)):
#         with open(f'./result/{file}', 'a+', encoding='utf-8',) as f:
#             data = json.load(f)
#             print(data)
            # json.dump(dic, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    path = "./result"
    dirs = os.listdir(path)
    dic = {}
    index = 0
    for file in tqdm(sorted(dirs)):
        index += 1
        try:
            with open(f'./result/{file}', 'r', encoding='utf-8', errors='ignore') as f:
                data = json.load(f, strict=False)
                dic[index] = data
        except:
            pass
    with open("./total_result.json", 'w',encoding="utf-8", errors='ignore")') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)
