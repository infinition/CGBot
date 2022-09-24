import os
import shutil

################################################################################################
working_dir = os.path.dirname(os.path.realpath(__file__))  # get the current working directory
working_dir = working_dir.replace("\\resources", "")  # remove the resources folder from the path
mypath = working_dir + "\\CGBOT"  # create a path to the CGBOT folder
print("Current directory for Zbrush = ", mypath)  # print the current directory
################################################################################################

#### These folders contains the stuff that we want to move to the Zbrush folders
zbrushsourcepath = mypath + "\\Zbrush"  # create a path to the source Zbrush folder
brushpresets = mypath + "\\Zbrush\\brushpresets\\"  # create a path to the source Zbrush brushpresets folder
zbrushes = mypath + "\\Zbrush\\zbrushes\\"  # create a path to the source Zbrush zbrushes folder
alphas =  mypath + "\\alphas\\" # create a path to the source Zbrush alphas folder
config =  mypath + "\\Zbrush\\config\\" # create a path to the source Zbrush config folder
hotkeys = mypath + "\\Zbrush\\hotkeys\\"    # create a path to the source Zbrush hotkeys folder
matcaps = mypath + "\\Zbrush\\matcaps\\"    # create a path to the source Zbrush matcaps folder
zbplugins = mypath + "\\Zbrush\\plugins\\"  # create a path to the source Zbrush zbplugin folder
zbstartup = mypath + "\\Zbrush\\startup\\"  # create a path to the source Zbrush zbstartup folder
zscripts = mypath + "\\Zbrush\\zscripts\\"  # create a path to the source Zbrush zscripts folder
ztools = mypath + "\\Zbrush\\ztools\\"      # create a path to the source Zbrush ztools folder
zlighcaps = mypath + "\\Zbrush\\zlightcaps\\"  # create a path to the source Zbrush zlightcaps folder

################################################################################################

class Zbrush:
    def __init__(self):
        # We find the Zbrush path & We assign the Zbrush destination paths
        self.zbrush_path = self.find_zbrush_path()
        #### These folders are the destination folders for the stuff that we want to move to the Zbrush folders
        self.zbrush_brushpresets_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\BrushPresets")
        self.zbrush_zbrushes_path = os.path.join(os.path.dirname(self.zbrush_path), "ZBrushes")
        self.zbrush_alphas_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\Alphas")
        self.zbrush_config_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\ConfigFiles")
        self.zbrush_hotkeys_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\Hotkeys")
        self.zbrush_matcaps_path = os.path.join(os.path.dirname(self.zbrush_path), "ZData\\Materials\\MatCap")
        self.zbrush_plugins_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\Plugins")
        self.zbrush_startup_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\Startup")
        self.zbrush_zscripts_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\ZScripts")
        self.zbrush_ztools_path = os.path.join(os.path.dirname(self.zbrush_path), "ZStartup\\ZPlugs64")
        self.zbrush_zlightcaps_path = os.path.join(os.path.dirname(self.zbrush_path), "ZLightCaps")
        

########### Function to find the Zbrush path ############
    def find_zbrush_path(self):
        for root, dirs, files in os.walk("C:\\"):
            for file in files:
                if file == "ZBrush.exe":
                    self.zbrush_path = os.path.join(root, file)
                    #print("Zbrush path found: " + self.zbrush_path)
                    return self.zbrush_path
################################################
#move stuff with shutil, overwrite if necessary, all files and folders and subfolders
################################################
    def move_stuff(self):
        print("Moving stuff to Zbrush folders")
        shutil.copytree(brushpresets, self.zbrush_brushpresets_path, dirs_exist_ok=True)
        shutil.copytree(zbrushes, self.zbrush_zbrushes_path, dirs_exist_ok=True)
        shutil.copytree(alphas, self.zbrush_alphas_path, dirs_exist_ok=True)
        shutil.copytree(config, self.zbrush_config_path, dirs_exist_ok=True)
        shutil.copytree(hotkeys, self.zbrush_hotkeys_path, dirs_exist_ok=True)
        shutil.copytree(matcaps, self.zbrush_matcaps_path, dirs_exist_ok=True)
        shutil.copytree(zbplugins, self.zbrush_plugins_path, dirs_exist_ok=True)
        shutil.copytree(zbstartup, self.zbrush_startup_path, dirs_exist_ok=True)
        shutil.copytree(zscripts, self.zbrush_zscripts_path, dirs_exist_ok=True)
        shutil.copytree(ztools, self.zbrush_ztools_path, dirs_exist_ok=True)
        shutil.copytree(zlighcaps, self.zbrush_zlightcaps_path, dirs_exist_ok=True)
        print("Done moving stuff to Zbrush folders")


    
    def main(self):
        print("Zbrush source path found: " + zbrushsourcepath)
        print("Zbrush destination path found: " + self.zbrush_path)
        self.move_stuff()


if __name__ == "__main__":
    zbrush = Zbrush()
    zbrush.main()
   
            



