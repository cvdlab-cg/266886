from pyplasm import *;





GRID = COMP([INSR(PROD),AA(QUOTE)])


pillar00 = T([1,2])([0.5,0.5])(CYLINDER([ 0.5, 10 ])(36))

pillars01= STRUCT([pillar00,T(1)(10)]*5)

pillars02 = GRID([[-4,1,-5,1,-9,1,-9,1,],[1],[10]  ])

pillars0 = STRUCT([T(2)(-19)(pillars01),pillar00,pillars02]);


pillars10 = T([1,2])([0.5,0])(GRID([ [1,-9,1,-9,1,-9,1,-9,1],[1],[10] ]))

##non è chiaro se l'ultima colonna quadrata è portante.io l'ho messa nel muro.questa è
##la versione alternativa
##pillars10 = T([1,2])([0.5,0])(GRID([ [1,-9,1,-9,1,-9,1,-9,1,-9,1],[1],[10] ]))
pillars11 = GRID([ [1,-9,1,-9,1,-19,1],[1],[10] ])
pillars12 = T([1,3])([2,10])(GRID([[0.25],[0.25],[10] ]))
pillar13 = T([1,2,3])([30,0,10])(pillar00)

pillars1 = STRUCT([pillars12,T([1,2,3])([-0.5,-19,10])(pillars10),T(3)(10)(pillars11),pillar13])



pillars20 = T(3)(20)(GRID([  [1,-9,1,-9,1,-9,1,-9,1],[1],[10] ]))
pillars21 = T([3])([20])(GRID([   [1,-9,1,-29,1],[1],[10]   ]))

pillars2 = STRUCT([pillars20,T(2)(-19)(pillars21)])


pillars30 = STRUCT([    GRID([  [-0.35,0.25],[-0.35,0.25],[10] ]),T(1)(10)(GRID([   [-0.35,0.25],[-0.35,0.25],[10]]))])
pillars31 = GRID([[-20,1,-9,1,-9,1],[1],[10]])
pillars32 = T(2)(-19)(GRID([[-19.5,1,-19.5,1],[1],[10]])  )
pillar33 = T([1,2])([40,6])(GRID([[1],[1],[10]]))

pillars3 = T(3)(30)(STRUCT([pillars32,pillars30,pillars31,pillar33]))



building = STRUCT([pillars0,pillars1,pillars2,pillars3])

VIEW(building)

dom = PROD([INTERVALS(PI)(32),INTERVALS(PI)(32)])

def fullcircle(R,r):
    def fullcircle0(p):
        u,v = p;
        return (r*COS(u)+R)*COS(v),(r*COS(u)+R)*SIN(v);
    return MAP(fullcircle0)(dom)


floor01 = R([1,2])(-PI/2)(fullcircle(5,0.5));
floor02 = R([1,2])(PI)(fullcircle(1.5,0.5));
##cosi posso estrudere i muri con la versione commentata si vede il piano terra 2d
##floor03 = PROD([SOLIDIFY(POLYLINE([ [29.5,25],[-0.5,25],[-0.5,19.5],[5,19.5],[5,8],[29.5,8],[29.5,25]])),Q(1)])
floor03 = GRID([[31],[-24,1]])
floor04 = GRID([ [1],[-19.5,5] ])
floor05 = GRID([ [5],[-19.5,1] ])
floor07 = GRID([[-4,1],[-8,12] ])
floor06 = T(2)(8)(GRID([ [-7,24],[1] ]))
floor08 = GRID([[-30,1],[-9,5]])


floor04 =T(2)(-19.5)(STRUCT([   floor08,floor07,floor06,floor04,floor05,floor03,T([1,2])([29.5,19.5])(floor01)  , T([1,2])([6,8])(floor02)]))
floor0 = STRUCT([pillars0,floor04])



floor20 = GRID([ [41],[-0.5,20],[1]  ])
floor21 = GRID([ [3],[-20,6] ,[1] ])
floor22 = GRID([ [-17,24],[-20,6],[1] ])

floor2 = STRUCT([T(2)(-19.5),floor20,floor21,floor22])



floor30 = GRID([   [20],[26],[1]])
floor31 = GRID([   [-19,14],[20],[1]])
floor32 = GRID([ [-33,8],[26],[1]])
floor3 = T(2)(-19)(STRUCT([floor30,floor31,floor32]))

floor1=floor3
floor13 = T(1)(-4)(GRID([[4],[4.5],[1] ]))



floor41 = GRID([ [-20,21],[26],[1] ])
floor42 = GRID([ [20],[-19,7],[1] ])
floor43 = GRID([  [1],[20],[1]    ])
floor44 = GRID([ [20],[1],[1]  ])

floor4 = T(2)(-19)(STRUCT([floor41,floor42,floor43,floor44]))



floors = STRUCT([floor0,T(3)(10)(floor1),T(3)(20)(floor2),T(3)(30)(floor3),T(3)(40)(floor4)])

building = STRUCT([building,floors])
VIEW(building)

