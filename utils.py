import app
import json
#
def read_data(file_name):
    file=app.BASE_DIR+"/data/"+file_name
    test_data=[]
    with open(file,encoding="utf-8") as f:
    #转换成字典
        json_data=json.load(f)


