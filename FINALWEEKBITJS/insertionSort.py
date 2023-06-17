def insertionSort(array): 
  for i in range( 1 , len(array)): #i start di no 1 (karena nomer pertama dianggap sudah sorted)
    key = array[i] #batas sorted
    j = i - 1 #j adalah sebelah dari key pertama
        
        
    #diitung dari J biar bisa dibandingin sama key
        
    while j >= 0 and key < array[j]: # key dibandingkan sama sebelum key (j) , dan j berhenti kalo udah gaada sebelumnya
      array[j + 1] = array[j] # j+1 (key) diganti sama j (sebelum key)
      j = j - 1 #j dikurangi biar di loop mundur, nanti assignment di atas diulangi lagi
      
      #[2,5,6,1]
      
      #[2,5,6,6]
      #[2,5,5,6]
      #[2,2,5,6] 
      
      #[1,2,5,6]
        
    array[j + 1] = key #setelah sudah dirubah semua, batas sorted dibalikin
  return array 




def binarySearchLeftmost(array, T): 
  retVal = None 
 
  left = 0 #digit pertama
  right = len(array) - 1 #panjang array
  middle = -1 # start dari -1 karena belom ada
   
  while left < right: # selama point kiri lebih kecil dari point di kanan (bergerak dari luar ke dalam (t))
    middle = (left + right) // 2 #point middle di set ke tengah kanan kiri setiap iteration loop
    
    
    # ini merubah point right sama left nya
    if array[ middle ] < T: #kalo value middle lebih kecil (leftmost) dari value yang dicari, berarti pointLeft di kanan middle
      left = middle + 1 
    else: 
      right = middle  #selain itu berarti point right jadi point middle
 
  if array[left] == T: #kalo sudah keluar loop, harusnya point left, right, middle sudah sama
    retVal = left 
     
  return retVal #return

arr = [2,6,5,1]
arr1 = [1,2,3,4,5,6]

print(binarySearchLeftmost(arr1,2))