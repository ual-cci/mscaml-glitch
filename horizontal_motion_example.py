
def mosh_frames(frames):
    for frame in frames:
        if not frame:
            continue
        #step through time
        for block in frame:
            #step through macroblocks
            for delta in block:
                # col contains the horizontal and vertical components of the vector
                # set vertical motion to 0
                delta[1] = 0

    return frames
