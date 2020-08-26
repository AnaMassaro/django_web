from pymongo import MongoClient
import json
import requests
import schedule
import time
import json

# response = requests.get(f'http://localhost:8000/api/note')
# comments = json.loads(response.content)
# client = MongoClient("localhost", 27017)
# db = client['projeto2']
# collection = db['nota']
#
# results = collection.find()
# dados = [results]
# print(dados)

# for r in results:
#     dados = JSONParser().parse(r)
#     print(dados)
#
#
# # def insert():
# #     collection.delete_many({})
# #     collection.insert_many(comments)
# #     print("Executando o script!")
# # schedule.every(5).seconds.do(insert)
# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)


