import glob
import os


def delete_latest(path):
    file_size_all = 0
    for root, _, files in os.walk(path):
        for list in files:
            fullpath = os.path.join(root, list)
            file_size = round(
                float(os.path.getsize(fullpath)/1024/1024), 4)
            file_size_all += file_size
        if file_size_all > 10:
            list_of_files = glob.glob(path+'*')
            latest_file = max(list_of_files, key=os.path.getctime)
            os.remove(latest_file)
