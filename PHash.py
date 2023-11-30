import numpy as np
import os


class PHash:
    PI = 3.142857
    HASH_LENGTH=64
    CROP_SIZE=32
    TRANSFORM_CROP=int(np.sqrt(HASH_LENGTH))
    try:
        if not os.path.exists("precomputedArrays"):
            os.mkdir("precomputedArrays")
        cosMap=np.load(f"precomputedArrays/cosMap{CROP_SIZE}.npy")
    except ValueError:
        os.remove(f"precomputedArrays/cosMap{CROP_SIZE}.npy")
        cosMap=None
    except OSError:
        cosMap=None

    def RGBHash(img):
        imgR,imgG,imgB=img.convert("RGB").split()
        rHash=PHash.__channelHash(imgR,PHash.CROP_SIZE,PHash.TRANSFORM_CROP)
        gHash=PHash.__channelHash(imgG,PHash.CROP_SIZE,PHash.TRANSFORM_CROP)
        bHash=PHash.__channelHash(imgB,PHash.CROP_SIZE,PHash.TRANSFORM_CROP)
        out=0
        out=(out<<PHash.HASH_LENGTH)|rHash
        out=(out<<PHash.HASH_LENGTH)|gHash
        out=(out<<PHash.HASH_LENGTH)|bHash
        return out
    
    def grayscaleHash(img):
        img=img.convert("L")
        return PHash.__channelHash(img,PHash.CROP_SIZE,PHash.TRANSFORM_CROP)
    
    def __channelHash(imgChannel,cropSize,transformCrop,cosMap=None):
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
            PHash.cosMap=np.ndarray((n,n))
            for i in range(n):
                for j in range(n):
                    PHash.cosMap[i,j]=np.cos((2*i+1)*j*PHash.PI/(2*n))
            try:
                if not os.path.exists("precomputedArrays"):
                    os.mkdir("precomputedArrays")
                np.save(f"precomputedArrays/cosMap{cropSize}.npy",PHash.cosMap)
            except OSError:
                pass
            return PHash.cosMap
        if PHash.cosMap is None:
            try:
                if not os.path.exists("precomputedArrays"):
                    os.mkdir("precomputedArrays")
                PHash.cosMap=np.load(f"precomputedArrays/cosMap{cropSize}.npy")
            except ValueError:
                os.remove(f"precomputedArrays/cosMap{cropSize}.npy")
                PHash.cosMap=recomputeCosines()
            except OSError:
                PHash.cosMap=recomputeCosines()
        
        c0=1/np.sqrt(n)
        cx=c0*np.sqrt(2)

        for i in range(n):
            for j in range(n):        
                currSum=0
                for k in range(n):
                    for l in range(n):
                        currSum+=img[k][l]*PHash.cosMap[k,i]*PHash.cosMap[l,j]
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