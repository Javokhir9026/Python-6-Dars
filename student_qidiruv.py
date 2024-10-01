import os
os.system("cls")

student  = ["Muhammadali","Behruz","Javohir","Botir","Murodbek","Inomjon"]
filter_qidiruv_tizim = list(filter(lambda i : (i[0] == "A" or i[-1] == 'r'),student))
print(filter_qidiruv_tizim)