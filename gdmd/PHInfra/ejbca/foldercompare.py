import filecmp
from filecmp import dircmp
import difflib
import os
from dotenv import load_dotenv

load_dotenv()
confdump=os.getenv('confdump_path')
confdump_old=os.getenv('confdumpold_path')
def print_diff_files(dcmp):
	
	for name in dcmp.diff_files:
		file1st = dcmp.left + "\\" + name
		file2nd = dcmp.right + "\\" + name
		print(file2nd, " file changed")
		file2 = open(file1st, encoding="utf-8")
		file1 = open(file2nd, encoding="utf-8")
		diff = difflib.ndiff(file1.readlines(), file2.readlines())
		delta = ''.join(x[2:] for x in diff if x.startswith('- '))
		print (delta)
	for sub_dcmp in dcmp.subdirs.values():
		print_diff_files(sub_dcmp)
	if dcmp.left_only:
		print (dcmp.left, dcmp.left_only, " file removed")
	if dcmp.right_only:
		print (dcmp.right, dcmp.right_only, " file added")
# add original file first and updated file second
dcmp = dircmp(confdump_old, confdump) 
print()
print_diff_files(dcmp)
