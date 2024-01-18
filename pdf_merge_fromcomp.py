import PyPDF2
import sys
import os


#function that will check the file you want is where it should be
#
def fetch_pdfs(parent_folder,file_i_want):    
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(f"{file_i_want}.pdf"):
                return (os.path.join(path,name))
                        
#create a list of files to be merged
pdf_files_to_merge=[]
while True:   
    print("Two entries are required: \n-First the path to the file's folder  e.g. C:\\Users\\....\\targetfolder \n-Secondly the file's name without extensions \n") 
    target_folder = input("Enter the path to the file's folder: ")
    target_file = input("Enter the file's name: ")
    #target_file_path = (fetch_pdfs(target_folder, target_file))
    pdf_files_to_merge.append((fetch_pdfs(target_folder, target_file)))

    continue_q = input("Enter more files? Y/N ")       
    if continue_q.upper() == "N":
        print(f"Files found to merge: {pdf_files_to_merge}")
        break

#create an object
merger = PyPDF2.PdfMerger()

#merge
for file in pdf_files_to_merge:
    merger.append(file)

print("Merge complete")

#get merged pdf file
merger.write("merged.pdf")
merger.close()
