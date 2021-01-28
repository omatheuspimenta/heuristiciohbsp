## IMPLEMENTACAO DO MÉTODO DE RESOLUCAO DO PROBLEMA DE MINIMIZACAO DE SOBRAS
##
##	IOH
##
import sys
import os
import fnmatch
from time import process_time
sys.setrecursionlimit(20000)

def ppl(fin,fout):
    sys.setrecursionlimit(20000)
    arq = open(fin,"r")
    out = open(fout,"a+")
    
    def partition(arr,seg,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
  
        for j in range(low , high): 
      
            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] >= pivot: 
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
                seg[i],seg[j] = seg[j],seg[i]
      
        arr[i+1],arr[high] = arr[high],arr[i+1]
        seg[i+1],seg[high] = seg[high],seg[i+1]
        return ( i+1 ) 

    def quickSort(arr,seg,low,high): 
        if low < high: 
      
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = partition(arr, seg,low,high) 
      
            # Separately sort elements before 
            # partition and after partition 
            quickSort(arr, seg, low, pi-1) 
            quickSort(arr, seg, pi+1, high) 
    
    ## CARREGANDO O ARQUIVO
    l = []
    d = []

    for line in arq:
        if(line[0] == "L" and line[1] == ":"):
            L = int(line[2:10])
        if(line[0] == "n" and line[1] == ":"):
            n = int(line[2:10])
        if(line[0] == "l" and line[1] == ":"):
            aux = line.split(" ")
            j = 1
            while(j < len(aux)):
                l.append(int(aux[j]))
                j += 1
        if(line[0] == "d" and line[1] == ":"):
            aux = line.split(" ")
            j = 1
            while(j < len(aux)):
                d.append(int(aux[j]))
                j += 1
    arq.close()
    ## FIM DO CARREGAMENTO DO ARQUIVO

    #print (d)
    #print (l)
    n=len(d)
    # print (">> n: ",n)


    ## START TIME
    start_time = process_time()

    ## SORT OF DESCENDING ORDER
    quickSort(l,d,0,n-1)

    ## UNINDO VALORES IGUAIS PARA DIMINUIR O TAMANHO DO VETOR
    i=0
    while i<(n-1):
        if l[i]==l[i+1]:
            d[i]=d[i]+d[i+1]
            l.pop(i+1)
            d.pop(i+1)
            n=n-1
        else:
            i=i+1
        if i==n:
            break
    n=len(d)
    # print(">>>l:",l)
    ## START HEURISTIC
    soma = leftover = loss = 0
    
    bar = 1
    small_ = l[n-1]

    
    #SUM OF DEMAND ITEMS
    for i in range(n):
        soma = soma + d[i]
        
    

    while (soma > 0):
        L_hat = L
        x = [0]*n # quantidade de elementos selecionados para corte
        # print("\n************************** Itens Restantes: ",soma)
        # print (d)
        # print (l)
        for i in range(n):
            if L_hat>=l[i]:
                y = int(L_hat/l[i])
                #print ("processando: ",l[i]," L_hat:",L_hat," preciso de: ",y," tenho>",d[i])
                if(y > d[i]):
                    y = d[i]
        
                x[i] = y
                d[i] -= x[i]
                soma -= x[i]
                L_hat -= (x[i] * l[i])
        
        # print ("primeira seleção: L_hat:",L_hat)
        # for i in range(n):
        #     if x[i]>0:
        #         print(l[i],"(",x[i],")")
        if L_hat>0:
            # print("\n### TENTANDO MELHORAR!!!!")
            encontrei=0
            ideal=0
            for i in range(1,n,1):
                if ideal==1:
                    #print("**** encontrei um ideal")
                    break
                if x[i]>0:
                    L_hat_temp=L_hat+(l[i]) # vou trocar apenas uma instancia
                    L_hat_ant=L_hat
                    #print ("Removendo: ",l[i]," Nova L_hat:",L_hat_temp)
                    for j in range(i+1,n,1):
                       # print ("**** testando:",l[j],"para corte=",d[j]," usados:",x[j])
                        if (d[j]-x[j]<=0):
                                #print(">> Não existe item disponível na largura:",l[j])
                                break
                        if ideal==1:
                            #print(">> 1o laço: saindo ideal:",ideal," ou d(",j,")=",d[j]) 
                            break
                        # existe item para ser cortado na medida l[j]  if d[j]>x[j]: 
                        selec=l[j]
                        for k in range(n-1,j+1,-1):
                            #print(">>> testando:" ,l[j]," com:",l[k]," = ",l[j]+l[k])
                            if ideal==1 or l[j]+l[k]>L_hat_temp:
                                #print(">> 2o laço: saindo ideal:",ideal," ou l[j]+l[k](",l[j]+l[k],")>(",L_hat_temp,")L_hat_temp") 
                                break
                            if d[k]>x[k]: #existe item disponivel para corte
                                #print ("selec:",selec," l[k]:",l[k],"=",selec+l[k],"L_hat_temp:",L_hat_temp,"L_hat_temp-selec+l[k]:",L_hat_temp-(selec+l[k]))
                                if L_hat_temp-(selec+l[k])>=0 and L_hat_temp-(selec+l[k])<L_hat_ant:
                                    result=[0]*3
                                    result[0]=i
                                    result[1]=j
                                    result[2]=k
                                    L_hat_ant=L_hat_temp-(selec+l[k])
                                   # print ("***L_hat_ant:",L_hat_ant)
                                    encontrei=1
                                    if L_hat_temp-(selec+l[k])==0: #encontrei um ideal
                                        ideal=1
                                        
            
            if ideal==1 or encontrei==1:
                x[result[0]]-=1
                d[result[0]]+=1
                x[result[1]]+=1
                d[result[1]]-=1
                x[result[2]]+=1
                d[result[2]]-=1
                L_hat=L_hat_ant
                soma +=1
                soma -=2
               
                    
            # print (">>Segunda seleção: L_hat:",L_hat)
            aux=0
            for i in range(n):
                if x[i]>0:
                    print(l[i],"(",x[i],")")
                    aux+=l[i]*x[i]
            L_hat=L-aux
            # print ("L_hat corrigido=",L_hat)
        i = 0
        while i <= (n-1):
            if(d[i] == 0):
                l.pop(i)
                d.pop(i)
                n = n-1
            else:
                i=i+1
            if i==n:
                break
        n = len(d) 
        
        if(L_hat < small_): # determinando se e sobra ou perda
            loss += L_hat
            L_hat = L
            bar += 1
        else:
            leftover += L_hat
            L_hat = L
            bar += 1
            
    # END TIME
    end_time = process_time()
    ex_time = end_time - start_time
    

    ##WRITE IN FILE
    out.write(file)
    out.write("\n")
    out.write("leftover;")
    out.write(str(leftover))
    out.write("\n")
    out.write("perd;")
    out.write(str(loss))
    out.write("\n")
    out.write("bar;")
    out.write(str(bar))
    out.write("\n")
    out.write("time;")
    out.write(str(ex_time))
    out.write("\n")
    out.close()


for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.dat'):
        print("Loading...",file)
        aux = 'PPL_IOH_BSP.txt'
        ppl(file,aux)

#file = 'class_84.dat'
#print("Loading...",file)
#aux = 'PPL_gal.txt'
#ppl(file,aux)"
