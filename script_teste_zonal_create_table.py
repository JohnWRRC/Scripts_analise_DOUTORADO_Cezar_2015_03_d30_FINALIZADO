import grass.script as grass
import os

lista_clumps=grass.mlist_grouped ('rast', pattern='*AreaHA*') ['PERMANENT']
cont_list=0
#for i in lista_clumps:
    #print i
for i in range(300):
    if i>298:
        formato='00000'+`i`
        formato=formato[-4:]        
        query='Unique_id='+`i`
        #grass.run_command('v.build',map='hex_5000_shp')
        #extrai um hegaono
        grass.run_command('v.extract',input='hex_5000_shp',out='temp',where=query,overwrite=True)
        #seta a regiao do hexagono
        grass.run_command('g.region',vect='temp')
        
        #nome de saida do buffer de 8k
        output_buffer='hexag_buffer_50kha_'+formato
        
        #criando buffer de 8k
        grass.run_command('v.buffer',input='temp',out=output_buffer,distance=8000,overwrite=True)
        #criando uma tabela
        grass.run_command('v.db.addtable', map=output_buffer,columns="id integer")
        #conectando a tabela
        grass.run_command('v.db.connect', flags='p',map=output_buffer)    
        
        #extraindo os valors do mapa clump e colocando os valores na tabela de atributo do temp para o hexago de 5ha
        #grass.run_command('v.rast.stats',vector='temp',raster=lista_clumps[cont_list],colprefix='cone',flags='c')
        
        #extraindo os valors do mapa clump e colocando os valores na tabela de atributo do temp para o hexago de 8k
        #grass.run_command('v.rast.stats',vector=output_buffer,raster=lista_clumps[cont_list],colprefix='cone',flags='c')        
        
        
        os.chdir(r'C:\resultados_conect_func_cezar\resultados_clumps')
        #txt hexag 5000
        #x=grass.read_command('v.db.select',map='temp',columns='con8k_min,con8k_max,con8k_mean,cone_sum,cone_n',fs=',')
        #txt_hexag='hexag_5kha_'+formato+'.txt'
        #table=open(txt,'w')
        #table.write(x)
        #table.close()
        
        #txt hexag 50000
        #x=grass.read_command('v.db.select',map=output_buffer,columns='cone_min,cone_max,cone_mean,cone_sum,cone_n',fs=',')
        #txt_buffer=output_buffer+'.txt'
        #table=open(txt,'w')
        #table.write(x)
        #table.close()        
        
        
        
#print x

