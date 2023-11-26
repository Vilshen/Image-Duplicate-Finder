import numpy as np
from PIL import Image
import os


class PHash:
    PI = 3.142857
    
    def RGBHash(img,hashLength=64,cropSize=32):
        transformCrop=int(np.sqrt(hashLength))
        imgR,imgG,imgB=img.convert("RGB").split()
        rHash=PHash.__channelHash(imgR,cropSize,transformCrop)
        gHash=PHash.__channelHash(imgG,cropSize,transformCrop)
        bHash=PHash.__channelHash(imgB,cropSize,transformCrop)
        out=0
        out=(out<<hashLength)|rHash
        out=(out<<hashLength)|gHash
        out=(out<<hashLength)|bHash
        return out
    
    def grayscaleHash(img,hashLength=64,cropSize=32):
        transformCrop=int(np.sqrt(hashLength))
        img=img.convert("L")
        return PHash.__channelHash(img,cropSize,transformCrop)
    
    def __channelHash(imgChannel,cropSize,transformCrop):
        imgChannel=imgChannel.resize((cropSize,cropSize))
        outArr=PHash.__discreteCosineTransform(imgChannel,cropSize)[0:transformCrop,0:transformCrop]
        median=np.median(outArr)
        outHash=0  
        for x in np.nditer(outArr):
            outHash=(outHash<<1)|int(x>=median)
        return outHash
    
        

    def __discreteCosineTransform(originalImage,cropSize):
        img=np.array(originalImage)          
        n=cropSize
        dct=np.zeros((n,n))
    
        def recomputeCosines():
            cosMap=np.ndarray((n,n))
            for i in range(n):
                for j in range(n):
                    cosMap[i,j]=np.cos((2*i+1)*j*PHash.PI/(2*n))
            try:
                if not os.path.exists("precomputedArrays"):
                    os.mkdir("precomputedArrays")
                np.save(f"precomputedArrays/cosMap{cropSize}.npy",cosMap)
            except OSError:
                pass
            return cosMap
        
        try:
            if not os.path.exists("precomputedArrays"):
                os.mkdir("precomputedArrays")
            cosMap=np.load(f"precomputedArrays/cosMap{cropSize}.npy")
        except ValueError:
            os.remove(f"precomputedArrays/cosMap{cropSize}.npy")
            cosMap=recomputeCosines()
        except OSError:
            cosMap=recomputeCosines()
        
        c0=1/np.sqrt(n)
        cx=c0*np.sqrt(2)

        for i in range(n):
            for j in range(n):        
                currSum=0
                for k in range(n):
                    for l in range(n):
                        currSum+=img[k][l]*cosMap[k,i]*cosMap[l,j]
                if i==0:
                    currSum*=c0
                else:
                    currSum*=cx
                if j==0:
                    currSum*=c0
                else:
                    currSum*=cx
                dct[i][j]=currSum
        return dct
                        
if __name__=="__main__":
    pass