import numpy as np

def mosh_frames(frames):
    #step through time
    for frame in frames:
        if not frame:
            continue
        #Get average vertical movement for this frame
        mean_vertical = np.mean(np.array(frame)[:,:,1])
        #step through macroblocks
        for row in frame:
            for mv in row:
                #if average is positive make 2, else make -2
                mv[1] = 2 if mean_vertical > 0 else -2
    return frames
