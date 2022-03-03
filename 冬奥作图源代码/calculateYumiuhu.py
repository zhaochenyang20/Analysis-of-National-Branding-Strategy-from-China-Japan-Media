import json


if __name__ == "__main__":
    filePosi = r"C:\Users\liuy\Desktop\SRT\SRT\yahoo中国_五輪_選手_2021-10-22-12_33_35.json"
    with open(filePosi,'r',encoding='utf-8',errors = 'ignore') as f:
        getDicts = json.load(f)
        print(len(getDicts))