from dorothy import Dorothy

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        self.a = dot.cyan
        self.b = dot.magenta 
        dot.music.start_file_stream("images/taylor.wav", fft_size=64)
        dot.start_record(end=30000)
        
    def draw(self):
        #Get x position as fraction of screen 
        dot.background(dot.black)
        fft_vals = dot.music.fft()
        w = dot.width//8
        for i in range(8):
            val = fft_vals[i]*50
            dot.fill((val,val,val))
            dot.rectangle((i*w,0),((i+1)*w,dot.height))
        

            

MySketch()          