import os
import shutil

################################################################################################
working_dir = os.path.dirname(os.path.realpath(__file__))  # get the current working directory
working_dir = working_dir.replace("\\resources", "")  # remove the resources folder from the path
mypath = working_dir + "\\CGBOT"  # create a path to the CGBOT folder
print("Current directory for Unreal = ", mypath)  # print the current directory
################################################################################################

#### These folders contains the stuff that we want to move to the Unreal folders
unrealsourcepath = mypath + "\\Unreal"  # create a path to the source Unreal folder
brushpresets = mypath + "\\Unreal\\brushpresets\\"  # create a path to the source Unreal brushpresets folder
alphas =  mypath + "\\alphas\\" # create a path to the source Unreal alphas folder


################################################################################################

class Unreal:
    def __init__(self):
        # We find the Unreal path & We assign the Unreal destination paths
        self.unreal_path = self.find_unreal_path()
        #### These folders are the destination folders for the stuff that we want to move to the Unreal folders
        self.unreal_brushpresets_path = os.path.join(os.path.dirname(self.unreal_path), "ZStartup\\BrushPresets")
        self.unreal_alphas_path = os.path.join(os.path.dirname(self.unreal_path), "ZStartup\\Alphas")

        

########### Function to find the Unreal path ############
    def find_unreal_path(self):
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file == "UnrealEditor.exe":
                    self.unreal_path = os.path.join(root, file)
                    print("Unreal path found: " + self.unreal_path)
                    return self.unreal_path

################################################
#move stuff with shutil, overwrite if necessary, all files and folders and subfolders
################################################
    def move_stuff(self):
        print("Moving stuff to Unreal folders")
        shutil.copytree(brushpresets, self.unreal_brushpresets_path, dirs_exist_ok=True)
        shutil.copytree(alphas, self.unreal_alphas_path, dirs_exist_ok=True)
        print("Done moving stuff to Unreal folders")


    
    def main(self):
        print("Unreal source path found: " + unrealsourcepath)
        print("Unreal destination path found: " + self.unreal_path)
        self.move_stuff()


if __name__ == "__main__":
    unreal = Unreal()
    unreal.main()
   
            



