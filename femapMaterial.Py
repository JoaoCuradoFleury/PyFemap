#Materiais
mat = app.feMatl

# name, type, Ex, Nuxy, Density, RefTemp, Alphax
materials = [["Material 1", cs.FMT_ISOTROPIC, 2e11, 0.3, 7850, 0, 1.2e-5],
             ["Material 2", cs.FMT_ISOTROPIC, 2e11, 0.3, 7850, 0, 1.2e-5],
             ["Material 3", cs.FMT_ISOTROPIC, 2e11, 0.3, 7850, 0, 1.2e-5]]

for i in range(0,len(materials)):
    mat.title = materials[i][0]
    mat.type = materials[i][1]
    mat.Ex = materials[i][2]
    mat.Nuxy = materials[i][3]
    mat.Density =  materials[i][4]
    mat.RefTemp =  materials[i][5]
    mat.Alphaxx =  materials[i][6]
    mat.Put(i+1)

app.feViewRegenerate(0)
