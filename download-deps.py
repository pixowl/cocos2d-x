from urllib.request import urlretrieve
import os  
import zipfile
import shutil
import sys


zip_name = sys.argv[1]

url_download_folder = 'https://github.com/pixowl/cocos2d-x-pxengine/releases/download'

url = url_download_folder + "/" + zip_name + "/" + zip_name + ".zip" 

workpath = os.path.dirname(os.path.realpath(__file__))

zip_folder = os.path.join(workpath, 'deps_zip')
extract_folder = os.path.join(workpath, 'deps_unzip')
external_folder = os.path.join(workpath, 'external')
zip_file_path = os.path.join(zip_folder, zip_name + ".zip")

print ("DOWLOAD DEPS LOG : zip_file_path : " + zip_file_path)



if not os.path.exists(zip_folder):
    os.mkdir(zip_folder)
if not os.path.exists(extract_folder):
    os.mkdir(extract_folder)

if not os.path.exists(zip_file_path):
    #download zip
    print ("DOWLOAD DEPS LOG : download zip ...")
    urlretrieve(url, zip_file_path)

# #unzip zip
print ("DOWLOAD DEPS LOG : unzip zip ...")
zip_ref = zipfile.ZipFile(zip_file_path, 'r')
zip_ref.extractall(extract_folder)
zip_ref.close()


# #copy deps to external folder
print ("DOWLOAD DEPS LOG : copy files ...")
shutil.rmtree(external_folder)
shutil.copytree(extract_folder, external_folder)

# #remove deps_upzip folder
print ("DOWLOAD DEPS LOG : remove temp folder ...")
shutil.rmtree(extract_folder)

print ("DOWLOAD DEPS LOG : done")


