import os
import json

from ai_hackathon_api.models import Company, CompanyEmotions

class EmotionsUploader:
    root_path = './emotions'

    def __init__(self):
        pass

    def walk_dir(self):
        print("walk dir")
        for root, dirs, files in os.walk(self.root_path, topdown=False):
            print("dir_name ")

            for dir_name in dirs:
                dir_path = os.path.join(self.root_path, dir_name)
                print("dir_path " + dir_path)
                for root, dirs, files in os.walk(dir_path, topdown=False):
                    pieces = dir_path.split("/")[-1]
                    company_name = pieces.replace('_', ' ')
                    for file_name in files:
                        file_path = dir_path + "/" + file_name
                        print(file_path)
                        json_dict = self.format_json(file_path)
                        self.save_emotions(company_name, file_name, json_dict)

    def save_emotions(self, company_name, file_name, json_dict):
        year = int(os.path.splitext(file_name)[0])
        try:
            print("saving" + file_name)
            print("company_name" + company_name)

            company_obj = Company.objects.get(name=company_name)
            tmp_emotions = CompanyEmotions(
                company = company_obj,
                year = year,
                emotions = json_dict
                )
            tmp_emotions.save()

        except Exception as e:
            print("save_emotions: Exception caught ")
            print(e)

    def format_json(self, file_path):
        file1 = open(file_path, 'r')
        data = json.load(file1)
        print(data)
        return data
        #lines = file1.readlines()
        count = 0
        # Strips the newline character
        json_dict = {}
        for line in lines:
            count += 1
            line = line.replace('‘', "\"")
            line = line.replace('’', "\"")
            data = json.loads(line) 
            name = data["name"]
            score = data["score"]
            json_dict[name] = score
        
        print (json_dict)
        return json_dict 

    

