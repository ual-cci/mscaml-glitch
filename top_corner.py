import numpy as np

def mosh_frames(frames):
    #step through time
    for frame in frames:
        if not frame:
            continue
        #step through macroblocks
        n_rows = len(frame)
        for i, row in enumerate(frame):
            n_cols = len(row)
            for j, mv in enumerate(row):
                if i < n_rows//2 and j < n_cols//2:
                    mv[0] = np.random.random()
                    mv[1] = np.random.random()
                    

    return frames
