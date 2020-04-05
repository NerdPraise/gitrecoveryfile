# Gitrecover
### RECOVER YOUR FILES

A simple python recovery tool for git 

### Getting Started

Gitrecover was written for python 3

All you need to do is 
    
    pip install gitrecovery1

Then in the directory where the files were deleted
    
    from gitrecovery.recover import RecoverFile
    files = RecoverFile()
    files.recover_git_files()
