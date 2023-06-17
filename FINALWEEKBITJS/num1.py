d1 = {} 
d1["One"] = 1 
d1["Two"] = 2 
 
d2 = {} 
d2["One"] = "Uno" 
d2["Two"] = "Dos" 
d2["Three"] = "Tres" 
 
for i in d2.keys(): 
    d1[i] = d2[i] 
    
print(d1)