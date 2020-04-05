import subprocess
from pathlib import Path


class RecoverFile():
    def __init__(self):
        print("This works mostly on recently added-to-git files")
        print("This is not magic, follow the steps")

    def recover_recent_deleted(self):
        print("Don't be lazy\nGo and check the recycle bin")

    def recover_git_files (self):
        bash = "git fsck --full"
        process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode("utf8")
        output = output.split("dangling blob")
        if error:
            if Path.exists("errors"):
                pass
            else:
                Path.mkdir("errors")
            with open(f"errors/error.txt") as error_file:
                error_file.write(error)

        for line in output[1:]:
            hash = line[0:7]
            print("Hash", hash)
            bashCommand = "git cat-file -p "+ hash  
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            code_put, error = process.communicate()
            print(f"done {hash}")
            text = code_put.decode(errors="ignore")
            with open(f"recovery/{hash}.txt", "wb") as file:
                file.write(code_put)
