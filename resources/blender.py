import os
import shutil

################################################################################################
working_dir = os.path.dirname(os.path.realpath(__file__))  # get the current working directory
working_dir = working_dir.replace("\\resources", "")  # remove the resources folder from the path
mypath = working_dir + "\\CGBOT"  # create a path to the CGBOT folder
print("Current directory for Blender = ", mypath)  # print the current directory
################################################################################################

#### These folders contains the stuff that we want to move to the Zbrush folders
myzbrushsourcepath = mypath + "\\Zbrush"  # create a path to the source Zbrush folder
mybrushespresets = mypath + "\\Zbrush\\mybrushespresets\\"  # create a path to the source Zbrush brushespresets folder
mybrusheslb = mypath + "\\Zbrush\\mybrusheslb\\"  # create a path to the source Zbrush brusheslb folder
myalphas =  mypath + "\\myalphas\\" # create a path to the source Zbrush alphas folder
myconfig =  mypath + "\\Zbrush\\myconfig\\" # create a path to the source Zbrush config folder
myhotkeys = mypath + "\\Zbrush\\myhotkeys\\"    # create a path to the source Zbrush hotkeys folder

################################################################################################

class Blender:
    def __init__(self):
        # We find the Zbrush path & We assign the Zbrush destination paths
        self.zbrush_path = self.find_zbrush_path()
        #### These folders are the destination folders for the stuff that we want to move to the Zbrush folders

        self.zbrush_brushespresets_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\BrushPresets")
        self.zbrush_brusheslb_path = os.path.join(os.path.dirname(self.zbrush_path), "ZBrushes")
        self.zbrush_alphas_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\\Alphas")
        self.zbrush_config_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\ConfigFiles")
        self.zbrush_hotkeys_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\Hotkeys")
        

########### Function to find the Zbrush path ############
    def find_zbrush_path(self):
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file == "ZBrush.exe":
                    self.zbrush_path = os.path.join(root, file)
                    print("Zbrush path found: " + self.zbrush_path)
                    return self.zbrush_path
################################################
#move stuff with shutil, overwrite if necessary, all files and folders and subfolders
################################################
    def move_stuff(self):
        print("Moving stuff to Zbrush folders")
        shutil.copytree(mybrushespresets, self.zbrush_brushespresets_path, dirs_exist_ok=True)
        shutil.copytree(mybrusheslb, self.zbrush_brusheslb_path, dirs_exist_ok=True)
        shutil.copytree(myalphas, self.zbrush_alphas_path, dirs_exist_ok=True)
        shutil.copytree(myconfig, self.zbrush_config_path, dirs_exist_ok=True)
        shutil.copytree(myhotkeys, self.zbrush_hotkeys_path, dirs_exist_ok=True)
        print("Done moving stuff to Zbrush folders")


    
    def main(self):
        print("Zbrush source path found: " + myzbrushsourcepath)
        print("Zbrush destination path found: " + self.zbrush_path)
        self.move_stuff()


if __name__ == "__main__":
    zbrush = Zbrush()
    zbrush.main()
   
            



