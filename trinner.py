def trinner(txt:str,trim=5,feedback=100):
    size = len(txt)
    chunksize = size//trim
    cropped = []
    for i in range(trim):
        cropped.append(txt[i*chunksize - (0 if i == 0 else feedback):(i+1)*chunksize if i!=(trim-1) else -1])
         
    return cropped