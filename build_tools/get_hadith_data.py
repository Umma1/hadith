"""
تهتمّ هذه الوحدة البرمجية بتزيل البيانات من
https://github.com/abdelrahmaan/Hadith-Data-Sets.git
و معالجتها لتغيير أسماء الملفات بطريقة تتماشى مع مكتبة حديث
"""
import glob
import os
import shutil
import tempfile

workdirectory = os.path.dirname(os.path.realpath(__file__))

# أسماء الملفات التي نحتاجها
files = [
    "Maliks Muwatta.csv",
    "Musnad Ahmad ibn Hanbal.csv",
    "Sahih Bukhari.csv",
    "Sahih Muslim.csv",
    "Sunan Abu Dawud.csv",
    "Sunan Ibn Maja.csv",
    "Sunan al Darami.csv",
    "Sunan al Tirmidhi.csv",
    "Sunan al-Nasai.csv"
]
final_names_mapping = {f: f.replace(" ", "_") for f in files}

# مجلد سيتعمل وقتيا ثم يمحى
tmp = tempfile.mkdtemp()
data_repo = "https://github.com/abdelrahmaan/Hadith-Data-Sets.git"
os.chdir(tmp)
os.system("git clone {}".format(data_repo))
repo = os.path.join(tmp, "Hadith-Data-Sets", "All Hadith Books")
parent_directory = os.path.dirname(workdirectory)
print(parent_directory)
hadith_data_folder = os.path.join(parent_directory, "hadith/data/")

# نظّف مجلّد البيانات في مكتبة حديث
for _file in glob.glob(f"{hadith_data_folder}/*.csv*"):
    if os.path.exists(_file):
        os.remove(_file)

# ضع ملفات البيانات الجديدة في مجلّد البيانات في مكتبة حديث
for filename, new_filename in final_names_mapping.items():
    current_file = os.path.join(repo, filename)
    destination_file = os.path.join(
        parent_directory, "hadith/data/", new_filename)
    shutil.move(current_file, destination_file)

# محو المجلّد الوقتي
shutil.rmtree(tmp)

data_files = os.path.join(hadith_data_folder, "*.csv")
os.system(f"gzip {data_files}")
