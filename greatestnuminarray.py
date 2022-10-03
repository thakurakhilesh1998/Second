    X = [25, 11, 7, 75, 56];     
         
    max = X[0];    
            
    for i in range(0, len(X)):    
        #Compare elements of array with max    
       if(X[i] > max):    
           max = X[i];    
               
    print("Largest element present in given array: " + str(max));   
