
# operacje na plikach, folderach itp.
import os
import sys
import shutil
import platform


print("listowanie:", os.listdir("../Dzien01"))
print("Biezacy folder:", os.getcwd())
if not os.path.exists("tmp"):
    os.mkdir("tmp")
else:
    print("folder jest i go usuwam")
    os.removedirs("tmp")

curr_dir = os.getcwd()
file_name = curr_dir + os.sep + "plik.txt"
file_name = os.path.join(curr_dir, "plik.txt")
print(file_name)
print("separator folderow:", os.sep)


print(platform.system())
print(platform.architecture())
print(platform.processor())
print(platform.java_ver())

shutil.copy("001-file-system.py", "001-file-system-kopia.py")

import tempfile
print("katalog tmp: ", tempfile.gettempdir())
with tempfile.TemporaryFile("wt", prefix="marian") as fd:
    fd.write("Hello world!")
    fd.write("Hello world!")
print("plik powinien być usunięty")

with tempfile.TemporaryDirectory() as tmpdir:
    print("katalog:", tmpdir)
    file_name = os.path.join(tmpdir, "log.txt")
    with open(file_name,"wt") as fd:
        fd.write("abcd")
print("folder powinien byc usuniety")

print("="*30)
print("odczyt linii polecen:", sys.argv)
