# Image-Duplicate-Finder
## GUI application for finding image duplicates

Groups images based on Hamming distance of their Perceptual Hashes, shows their resolution, and provides a link for opening them with the default application.
Supports all formats supported by PIL.

![image](https://github.com/tipoima/Image-Duplicate-Finder/assets/61978315/680e0ba7-90ec-41b5-a7b3-fe1063140f7e)

Computation of hashes takes as little as minutes (for hundreds of files) to hours (for ten thousands and more). This step supports multiprocessing and, once done, hashes are pickled for future use (adding and removing files is supported, but changing an image without changing its filename will preserve its old hash).
Grouping of hashes is done on every search with runtime of several minutes even for large image sets.

## Installation
1. Clone the project
2. Run `pip install -r requirements.txt`
3. Run `python main.py`

Alternatively, download the executable from Releases.
