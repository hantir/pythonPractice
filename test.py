from PIL import Image
import os

def convertImage(path, filename):
    img = Image.open(path+filename)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(r"C:\Users\srinivas\OneDrive\Desktop\temp2\\"+filename, "PNG")
    print("Successful")

for filename in os.listdir(r"C:\Users\srinivas\OneDrive\Desktop\temp2\\"):
    #print(r"C:\Users\srinivas\PycharmProjects\pythonPractice\temp\\"+filename)
    convertImage(r"C:\Users\srinivas\OneDrive\Desktop\temp2\\", filename)