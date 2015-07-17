import grass.script as grass
import os

lista_clumps=grass.mlist_grouped ('rast', pattern='*orig_clump_mata_limpa_AreaHA') ['PERMANENT']

#lista_clumps=lista_clumps[0:2]
#listaold=['1000','120','180','240','30','350','440','500','60','720','840','90']
#cont_listold=0
#for i in lista_clumps:
    ##print i 
    #formato='00000'+listaold[cont_listold]
    #formato=formato[-4:]
    #if listaold[cont_listold] in i:
        #out_rename=i.replace(listaold[cont_listold],formato)
        #print out_rename
        #cont_listold=cont_listold+1
        #grass.run_command('g.rename',rast=i+','+out_rename)
    #if cont_listold == 12:
        #cont_listold=0
for i in lista_clumps:
    escClump=i[38:42]
    print escClump