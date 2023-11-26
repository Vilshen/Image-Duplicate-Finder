import os
from PIL import Image,UnidentifiedImageError
import pandas as pd
import numpy as np
from PHash import PHash
from multiprocessing import Pool
from functools import partial


def parallelize(data, func, num_of_processes=8): #tnx https://stackoverflow.com/questions/26784164/pandas-multiprocessing-apply
    data_split = np.array_split(data, num_of_processes)
    pool = Pool(num_of_processes)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data
def run_on_subset(func, data_subset):
    return data_subset.apply(func, axis=1)
def parallelize_on_rows(data, func, num_of_processes=8):
    return parallelize(data, partial(run_on_subset, func), num_of_processes)

def callGrayscaleHash(row):
    if row['gsHash'] is None:
        with Image.open(row['path']) as img:
            return PHash.grayscaleHash(img)
    else:
        return row['gsHash']
    
def callRGBHash(row):
    if row['rgbHash'] is None:
        with Image.open(row['path']) as img:
            return PHash.RGBHash(img)
    else:
        return row['rgbHash']


class ImageCollector:
    
    def getImages(folder:str,useRGB=False,useThreading=True):
        
        scannedImages=ImageCollector.__buildDataFrame(folder)
        
        if useRGB:
            if useThreading:
                scannedImages['rgbHash']=parallelize_on_rows(scannedImages, callRGBHash)
            else:
                scannedImages['rgbHash']=scannedImages.apply(callRGBHash,axis=1)        
        else:
            if useThreading:
                scannedImages['gsHash']=parallelize_on_rows(scannedImages, callGrayscaleHash)
            else:
                scannedImages['gsHash']=scannedImages.apply(callGrayscaleHash,axis=1)
        dirHash=hash(folder)
        scannedImages.to_pickle(f"precomputedDirectories\\{dirHash}.pkl")
        
        return scannedImages
        
        
    def __buildDataFrame(folder:str):
        _,scannedImages=ImageCollector.__getPaths(folder)
        
        scannedImages=pd.DataFrame(scannedImages,columns=["path","gsHash","rgbHash"])
        dirHash=hash(folder)
        if False and os.path.isfile(f"precomputedDirectories\\{dirHash}.pkl"):
            try:
                oldDataFrame=pd.read_pickle(f"precomputedDirectories\\{dirHash}.pkl")
                scannedImages=scannedImages.fillna(oldDataFrame)
            except:
                pass
        return scannedImages
        

    def __getPaths(folder:str): #tnx https://stackoverflow.com/questions/18394147/how-to-do-a-recursive-sub-folder-search-and-return-files-in-a-list
        
        subfolders, files = [], []
        
        for f in os.scandir(folder):
            if f.is_dir():
                subfolders.append(f.path)
            if f.is_file():
                try:
                    with Image.open(f.path):
                        pass
                except UnidentifiedImageError:
                    continue
                files.append((f.path,None,None))
    
        for folder in list(subfolders):
            sf, f = ImageCollector.__getPaths(folder)
            subfolders.extend(sf)
            files.extend(f)
        return subfolders,files
    
if __name__ == "__main__":    
    ImageCollector.getImages(r"D:\1\stuff")
    
    

