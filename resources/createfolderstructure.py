import os

working_dir = os.path.dirname(os.path.realpath(__file__))
working_dir = working_dir.replace("\\resources", "") 
PATH = working_dir + "\\CGBOT"

####COMMON FOLDERS####
alphas =  PATH + "\\alphas\\" #ZBRUSH / BLENDER / SUBSTANCE PAINTER
textures = PATH + "\\textures\\" #ZBRUSH / BLENDER / SUBSTANCE PAINTER
hdris = PATH + "\\hdris\\" #ZBRUSH / BLENDER / SUBSTANCE PAINTER

####ZBRUSH FOLDERS####
brushpresets = PATH + "\\Zbrush\\brushpresets\\"
zbrushes = PATH + "\\Zbrush\\zbrushes\\"
zbconfig =  PATH + "\\Zbrush\\config\\"
zbhotkeys = PATH + "\\Zbrush\\hotkeys\\"
matcaps = PATH + "\\Zbrush\\matcaps\\"
zbplugins = PATH + "\\Zbrush\\plugins\\"
zbstartup = PATH + "\\Zbrush\\startup\\"
zscripts = PATH + "\\Zbrush\\zscripts\\"
ztools = PATH + "\\Zbrush\\ztools\\"
zlightcaps = PATH + "\\Zbrush\\zlightcaps\\"


####BLENDER FOLDERS####



#SUBSTANCE PAINTER FOLDERS####
spcolorluts = PATH + "\\SubstancePainter\\colorluts\\"
speffects = PATH + "\\SubstancePainter\\effects\\"
spemitters = PATH + "\\SubstancePainter\\emitters\\"
spenvironments = PATH + "\\SubstancePainter\\environments\\"
spexportpresets = PATH + "\\SubstancePainter\\export-presets\\"
spgenerators = PATH + "\\SubstancePainter\\generators\\"
spmaterials = PATH + "\\SubstancePainter\\materials\\"
sppresets = PATH + "\\SubstancePainter\\presets\\"
spbrushes = PATH + "\\SubstancePainter\\presets\\brushes\\"
spparticles = PATH + "\\SubstancePainter\\presets\\particles\\"
spprocedurals = PATH + "\\SubstancePainter\\procedurals\\"
spreceivers = PATH + "\\SubstancePainter\\receivers\\"
spshaders = PATH + "\\SubstancePainter\\shaders\\"
spsmartmasks  = PATH + "\\SubstancePainter\\smart-masks\\"
spsmartmaterials = PATH + "\\SubstancePainter\\smart-materials\\"
sptemplates = PATH + "\\SubstancePainter\\templates\\"



class CreateFolderStructure():
    def __init__(self):
        self.create_common_structure()
        self.create_zbfolder_structure()
        self.create_blfolder_structure()
        self.create_spfolder_structure()

    def create_common_structure(self):
        try:
            if not os.path.exists(PATH):
                os.makedirs(PATH)
            if not os.path.exists(alphas):
                os.makedirs(alphas)
            if not os.path.exists(textures):
                os.makedirs(textures)
            if not os.path.exists(hdris):
                os.makedirs(hdris)
            print ("Common source folders structure created")
        except OSError:
            print ("Common source folders structure creation failed")
        
    def create_zbfolder_structure(self):
        try:
            if not os.path.exists(brushpresets):
                os.makedirs(brushpresets)
            if not os.path.exists(zbrushes):
                os.makedirs(zbrushes)
            if not os.path.exists(zbconfig):
                os.makedirs(zbconfig)
            if not os.path.exists(zbhotkeys):
                os.makedirs(zbhotkeys)
            if not os.path.exists(matcaps):
                os.makedirs(matcaps)
            if not os.path.exists(zbplugins):
                os.makedirs(zbplugins)
            if not os.path.exists(zbstartup):
                os.makedirs(zbstartup)
            if not os.path.exists(zscripts):
                os.makedirs(zscripts)
            if not os.path.exists(ztools):
                os.makedirs(ztools)
            if not os.path.exists(zlightcaps):
                os.makedirs(zlightcaps)
            print ("Zbrush source folders structure created")
        except:
            print ("Zbrush source folders structure creation failed")
            

    def create_blfolder_structure(self):
        pass

    def create_spfolder_structure(self):
        try:
            if not os.path.exists(spcolorluts):
                os.makedirs(spcolorluts)
            if not os.path.exists(speffects):
                os.makedirs(speffects)
            if not os.path.exists(spemitters):
                os.makedirs(spemitters)
            if not os.path.exists(spenvironments):
                os.makedirs(spenvironments)
            if not os.path.exists(spexportpresets):
                os.makedirs(spexportpresets)
            if not os.path.exists(spgenerators):
                os.makedirs(spgenerators)
            if not os.path.exists(spmaterials):
                os.makedirs(spmaterials)
            if not os.path.exists(sppresets):
                os.makedirs(sppresets)
            if not os.path.exists(spbrushes):
                os.makedirs(spbrushes)
            if not os.path.exists(spparticles):
                os.makedirs(spparticles)
            if not os.path.exists(spprocedurals):
                os.makedirs(spprocedurals)
            if not os.path.exists(spreceivers):
                os.makedirs(spreceivers)
            if not os.path.exists(spshaders):
                os.makedirs(spshaders)
            if not os.path.exists(spsmartmasks):
                os.makedirs(spsmartmasks)
            if not os.path.exists(spsmartmaterials):
                os.makedirs(spsmartmaterials)
            if not os.path.exists(sptemplates):
                os.makedirs(sptemplates)
            print ("Substance Painter source folders structure created")
        except:
            print ("Substance Painter source folders structure creation failed")

if __name__ == "__main__":
    CreateFolderStructure()
