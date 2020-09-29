
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", action="store_true", help="show outputs")
parser.add_argument("-n", "--name", required=True, metavar="FILENAME", help="file name")
parser.add_argument("-d", type=int, default=2, metavar="2", help="digits precision")
parser.add_argument("-f", "--folder", nargs="+", default=".", metavar="/path/to/folder", type=str, help="folder or folders")
parser.add_argument("-t", "--time", type=float, default=10.0, metavar="deltatime", help="input time delay")

arguments = parser.parse_args()
print(arguments.name)
print(arguments.time)
print(arguments.folder)
print(arguments.verbose)
print(arguments.d)