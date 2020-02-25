import glob
import os
import shutil
import tempfile

workdirectory = os.path.dirname(os.path.realpath(__file__))
# the list of files that will be kept from the original data repo
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

# temporary directory to clone the hadith data
tmp = tempfile.mkdtemp()
data_repo = "https://github.com/abdelrahmaan/Hadith-Data-Sets.git"
os.chdir(tmp)
os.system("git clone {}".format(data_repo))
repo = os.path.join(tmp, "Hadith-Data-Sets", "All Hadith Books")
parent_directory = os.path.dirname(workdirectory)
print(parent_directory)
hadith_data_folder = os.path.join(parent_directory, "hadith/data/")

# clean up the repo data folder
for _file in glob.glob(f"{hadith_data_folder}/*.csv*"):
    if os.path.exists(_file):
        os.remove(_file)

# write the clone data files into the repo data file
for filename, new_filename in final_names_mapping.items():
    current_file = os.path.join(repo, filename)
    destination_file = os.path.join(
        parent_directory, "hadith/data/", new_filename)
    shutil.move(current_file, destination_file)

shutil.rmtree(tmp)

data_files = os.path.join(hadith_data_folder, "*.csv")
os.system(f"gzip {data_files}")
