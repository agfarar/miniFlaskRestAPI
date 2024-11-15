import requests

BASE = "http://127.0.0.1:5000/"


#response = requests.get(BASE + "helloworld/tim  ")

# response = requests.put(BASE + "video/1", {"likes": 10, "name": "Trim", "views": 100000})
# print(response.json())
# input()
# response = requests.get(BASE + "video/2")
# print(response.json())


# data = [{"likes": 78, "name": "Joe", "views": 100000},
#         {"likes": 10000, "name": "How to make REST API", "views": 80000},
#         {"likes": 35, "name": "Tim", "views": 2000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()

# response = requests.get(BASE + "video/6")
# print(response.json())



# response = requests.delete(BASE + "video/0")  
# if response.status_code == 204:
#     print("Video eliminado exitosamente.")
# else:
#     print(f"Error al eliminar el video: {response.status_code}, {response.text}")
