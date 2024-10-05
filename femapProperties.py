# Propriedades
prop = app.feProp

#Mass
#name, type, mass
Massproperties = [["Mass 1", 27, 0.1],
                  ["Mass 2", 27, 0.1],
                  ["Mass 3", 27, 0.1],
                  ]

for i in range(0, len(Massproperties)):
    prop.title = Massproperties[i][0]
    prop.type = Massproperties[i][1]

    dimensions = Massproperties[i][2]
    a =[]
    for j in range(0,78):
        a.append(0.0)

    a[7] = Massproperties[i][2]
    tuple_dimensions= tuple(a)

    prop.pmat = tuple_dimensions
    prop.Put(prop.NextEmptyID())

#BEAM
# nome, type, material id, shape,dimensions []
BEAMproperties = [["propriedade 1", 5, 1, 22,[0.1,0.1,0.0,0.0,0.0,0.01]],
                  ["propriedade 2", 5, 2, 19,[0.15,0.07,0.07,0.004,0.009,0.009]]
                  ]
              

for i in range(0,len(BEAMproperties)):
    prop.title = BEAMproperties[i][0]
    prop.type = BEAMproperties[i][1]
    prop.matlID = BEAMproperties[i][2]
    prop.ComputeStdShape(BEAMproperties[i][3], BEAMproperties[i][4], 0, 0, False, False, False)

    prop.Put(prop.NextEmptyID())

app.feViewRegenerate(0)

#PLATE
# nome, type, material id, dimensions []
PLATEproperties = [["Placa 1", 17, 1, [0.1, 0.2, 0.3, 0.4]],
                   ["Placa 2", 17, 1, [0.1, 0.2, 0.3, 0.4]],
                   ["Placa 3", 17, 1, [0.1, 0.2, 0.3, 0.4]],
                   ["Placa 4", 17, 1, [0.1, 0.2, 0.3, 0.4]]
                   ]


for i in range(0,len(PLATEproperties)):
    prop.title = PLATEproperties[i][0]
    prop.type = PLATEproperties[i][1]
    prop.matlID = PLATEproperties[i][2]

    dimensions = PLATEproperties[i][3]
    tuple_dimensions = tuple(dimensions) + (0,) * (78 - len(dimensions))

    prop.pmat = tuple_dimensions
    prop.Put(prop.NextEmptyID())

app.feViewRegenerate(0)
