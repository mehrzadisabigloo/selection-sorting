def selection(list):
    
    for i in range(len(list)):
        low=list[i]
        
        for j in range(i+1,len(list)):
            if list[j]<low:
                low=list[j]
                k=j
                
        if low!=list[i]:
            list[i],list[k]=list[k],list[i]  
        
    print(list)       

a=[5,4,11,11,45,77,3,55,7,2,3,3,4]
selection(a)