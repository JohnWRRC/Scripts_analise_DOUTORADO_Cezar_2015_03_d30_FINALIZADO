import grass.script as grass
import os

lista_clumps=grass.mlist_grouped ('rast', pattern='*AreaHA*') ['PERMANENT']
del lista_clumps[0:3]

cont_list=0
for lista in lista_clumps:
    i=4501
    while i <= 5076:
        
        formato='00000'+`i`
        formato=formato[-4:]        
        query='Unique_id='+`i`
        print query
        nomehexag='hexagono_5k_'+formato
        grass.run_command('v.build',map='hex_5000_shp')
        ###extrai um hegaono
        grass.run_command('v.extract',input='hex_5000_shp',out=nomehexag,where=query,overwrite=True)
        ###seta a regiao do hexagono
        grass.run_command('g.region',vect=nomehexag)
        
        ###nome de saida do buffer de 8k
        output_buffer='hexag_buffer_50kha_'+formato
        
        ###criando buffer de 8k
        grass.run_command('v.buffer',input=nomehexag,out=output_buffer,distance=8000,overwrite=True)
        ###criando uma tabela
        grass.run_command('v.db.addtable', map=output_buffer,columns="id integer")
        ###conectando a tabela
        grass.run_command('v.db.connect', flags='p',map=output_buffer)    
        grass.run_command('v.build',map=output_buffer)
        ###extraindo os valors do mapa clump e colocando os valores na tabela de atributo do hexagono para o hexago de 5ha
        grass.run_command('g.region',vect=nomehexag)
        grass.run_command('v.rast.stats',vector=nomehexag,raster=lista,colprefix='con5k',flags='c')
        
        ###extraindo os valors do mapa clump e colocando os valores na tabela de atributo do hexagono para o hexago de 8k
        grass.run_command('g.region',vect=output_buffer)
        grass.run_command('v.rast.stats',vector=output_buffer,raster=lista,colprefix='con50k',flags='c')        
        
        
        os.chdir(r'F:\data\cezar\resultado_txts')
        ###txt hexag 5000
        x=grass.read_command('v.db.select',map=nomehexag,columns='con5k_min,con5k_max,con5k_mean,con5k_sum,con5k_n',fs=',')
        if x!='':
            escClump=lista[38:42]
            txt_hexag='hexag_5kha_'+formato+'_Clump_'+escClump+'.txt'
            table=open(txt_hexag,'w')
            table.write(x)
            table.close()
        x=''
        ###txt hexag 50000
        x=grass.read_command('v.db.select',map=output_buffer,columns='con50k_min,con50k_max,con50k_mea,con50k_sum,con50k_n',fs=',')
        if x!='':
            escClump=lista[38:42]
            txt_buffer=output_buffer+'_Clump_'+escClump+'.txt'
            table=open(txt_buffer,'w')
            table.write(x)
            table.close() 
        grass.run_command('g.remove',vect=nomehexag+','+output_buffer,flags='f')
            
        i=i+1
        
#print x

