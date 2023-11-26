class Clustering:
    
    def hammingDistance(hash1:int,hash2:int):
        assert len(bin(hash1))==len(bin(hash2)),"Hash lengths not equal"
        
        return (hash1^hash2).bit_length()
    
    
    
if __name__=="__main__":
    pass