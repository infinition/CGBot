import os
import shutil

################################################################################################
working_dir = os.path.dirname(os.path.realpath(__file__))  # get the current working directory
working_dir = working_dir.replace("\\resources", "")  # remove the resources folder from the path
mypath = working_dir + "\\CGBOT"  # create a path to the CGBOT folder
print("Current directory for Substance Painter = ", mypath)  # print the current directory
################################################################################################

#### These folders contains the stuff that we want to move to the Substance painter userprofile/assets folders
spsourcepath = mypath + "\\SubstancePainter"  # create a path to the source Substance Painter folder
alphas =  mypath + "\\alphas\\" # create a path to the source Substance Painter alphas folder
colorluts = mypath + "\\SubstancePainter\\colorluts\\"  # create a path to the source Substance Painter colorluts folder
effects = mypath + "\\SubstancePainter\\effects\\"  # create a path to the source Substance Painter effects folder
emitters = mypath + "\\SubstancePainter\\emitters\\"  # create a path to the source Substance Painter emitters folder
environments = mypath + "\\SubstancePainter\\environments\\"  # create a path to the source Substance Painter environments folder
exportpresets = mypath + "\\SubstancePainter\\export-presets\\"  # create a path to the source Substance Painter export-presets folder
generators = mypath + "\\SubstancePainter\\generators\\"  # create a path to the source Substance Painter generators folder
materials = mypath + "\\SubstancePainter\\materials\\"  # create a path to the source Substance Painter materials folder
presets = mypath + "\\SubstancePainter\\presets\\"  # create a path to the source Substance Painter presets folder
procedurals = mypath + "\\SubstancePainter\\procedurals\\"  # create a path to the source Substance Painter procedurals folder
receivers = mypath + "\\SubstancePainter\\receivers\\"  # create a path to the source Substance Painter receivers folder
shaders = mypath + "\\SubstancePainter\\shaders\\"  # create a path to the source Substance Painter shaders folder
smartmasks = mypath + "\\SubstancePainter\\smart-masks\\"  # create a path to the source Substance Painter smart-masks folder
smartmaterials = mypath + "\\SubstancePainter\\smart-materials\\"  # create a path to the source Substance Painter smart-materials folder
textures =  mypath + "\\textures\\" # create a path to the source Substance Painter textures folder

################################################################################################

class SubstancePainter:
    def __init__(self):
        # We find the Substance Painter path & We assign the Substance Painter destination paths
        self.sp_path = self.find_substancepainter_path()
        #### These folders are the destination folders for the stuff that we want to move
        self.sp_alphas_path = os.path.join(os.path.dirname(self.sp_path), "assets\\alphas")
        self.sp_colorluts_path = os.path.join(os.path.dirname(self.sp_path), "assets\\colorluts")
        self.sp_effects_path = os.path.join(os.path.dirname(self.sp_path), "assets\\effects")
        self.sp_emitters_path = os.path.join(os.path.dirname(self.sp_path), "assets\\emitters")
        self.sp_environments_path = os.path.join(os.path.dirname(self.sp_path), "assets\\environments")
        self.sp_exportpresets_path = os.path.join(os.path.dirname(self.sp_path), "assets\\export-presets")
        self.sp_generators_path = os.path.join(os.path.dirname(self.sp_path), "assets\\generators")
        self.sp_materials_path = os.path.join(os.path.dirname(self.sp_path), "assets\\materials")
        self.sp_presets_path = os.path.join(os.path.dirname(self.sp_path), "assets\\presets")
        self.sp_procedurals_path = os.path.join(os.path.dirname(self.sp_path), "assets\\procedurals")
        self.sp_receivers_path = os.path.join(os.path.dirname(self.sp_path), "assets\\receivers")
        self.sp_shaders_path = os.path.join(os.path.dirname(self.sp_path), "assets\\shaders")
        self.sp_smartmasks_path = os.path.join(os.path.dirname(self.sp_path), "assets\\smart-masks")
        self.sp_smartmaterials_path = os.path.join(os.path.dirname(self.sp_path), "assets\\smart-materials")
        self.sp_textures_path = os.path.join(os.path.dirname(self.sp_path), "assets\\textures")


########### Function to find the Substance painter userprofile/assets path ############
    def find_substancepainter_path(self):
        for root, dirs, files in os.walk(os.path.join(os.environ['USERPROFILE'], "Documents", "Adobe", "Adobe Substance 3D Painter")):
            for dir in dirs:
            #if dir name contains substance painter
                if "assets" in dir:
                    #return the path
                    self.sp_path = os.path.join(root, dir)
                    print("Substance Painter path found: " + self.sp_path)
                    return self.sp_path
                         

################################################
#move stuff with shutil, overwrite if necessary, all files and folders and subfolders
################################################
    def move_stuff(self):
        print("Moving stuff to Substance Painter folder : "+ self.sp_path)
        shutil.copytree(alphas, self.sp_alphas_path, dirs_exist_ok=True)
        shutil.copytree(colorluts, self.sp_colorluts_path, dirs_exist_ok=True)
        shutil.copytree(effects, self.sp_effects_path, dirs_exist_ok=True)
        shutil.copytree(emitters, self.sp_emitters_path, dirs_exist_ok=True)
        shutil.copytree(environments, self.sp_environments_path, dirs_exist_ok=True)
        shutil.copytree(exportpresets, self.sp_exportpresets_path, dirs_exist_ok=True)
        shutil.copytree(generators, self.sp_generators_path, dirs_exist_ok=True)
        shutil.copytree(materials, self.sp_materials_path, dirs_exist_ok=True)
        shutil.copytree(presets, self.sp_presets_path, dirs_exist_ok=True)
        shutil.copytree(procedurals, self.sp_procedurals_path, dirs_exist_ok=True)
        shutil.copytree(receivers, self.sp_receivers_path, dirs_exist_ok=True)
        shutil.copytree(shaders, self.sp_shaders_path, dirs_exist_ok=True)
        shutil.copytree(smartmasks, self.sp_smartmasks_path, dirs_exist_ok=True)
        shutil.copytree(smartmaterials, self.sp_smartmaterials_path, dirs_exist_ok=True)
        shutil.copytree(textures, self.sp_textures_path, dirs_exist_ok=True)
        print("Done moving stuff to Substance Painter folder")


    
    def main(self):
        print("Substance Painter source path found: " + spsourcepath)
        print("Substance Painte destination path found: " + self.sp_path)
        self.move_stuff()


if __name__ == "__main__":
    sp = SubstancePainter()
    sp.main()
   
            



