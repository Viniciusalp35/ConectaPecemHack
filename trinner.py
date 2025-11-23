def trinner(txt:str,chunksize=2500,feedback=200):
    size = len(txt)
    cropped = []
    for i in range(size//chunksize):
        cropped.append(txt[i*chunksize - (0 if i == 0 else feedback):(i+1)*chunksize if i!=(chunksize-1) else -1])
         
    return cropped