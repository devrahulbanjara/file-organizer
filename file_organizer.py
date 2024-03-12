import os
import shutil

src_path="C://Users//drenergydrink//Desktop//File_Organizer"
dir_list=os.listdir(src_path)
extensions=["mp3","json","pdf","jpg","exe"]

for i in dir_list:
    if "." in i:
        index_of_dot=i.index(".")
        extension=i[index_of_dot+1::1]
        dst_path=f"C://Users//drenergydrink//Desktop//File_Organizer//{extension}//{i}"

        if extension in extensions:
            if not os.path.exists(src_path+f"//{extension}"):
                os.makedirs(src_path+f"//{extension}")
                shutil.move(src_path + f"//{i}", dst_path)
