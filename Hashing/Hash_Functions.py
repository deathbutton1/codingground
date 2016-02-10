def division_hash(k,r):
    return k%r
    
def multiplication_hash(k,r):
    A = (5**.5-1)/2 # arbitrary number (0,1)
    M = (A*k)%1
    return int(M*r)

def test_hash(hash_func,r,tests):
    results = [0]*r
    for k in range(tests):
        results[hash_func(k,r)]+=1
    return results
    
print(test_hash(multiplication_hash,100,1000000))

