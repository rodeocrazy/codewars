def find_even_index(arr):
  for N in range(len(arr)):
        if ((sum(arr[:N]))) == ((sum(arr[N:])) - arr[N]):
            return(N)
  
  else: return(-1)
