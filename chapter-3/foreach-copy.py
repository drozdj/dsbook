from metaflow import FlowSpec, step
import numpy as np

# https://onedrive.live.com/redir?resid=3E781AD654D8C9F3%214716&authkey=%21AK97gjIH12Zyvow&page=Edit&wd=target%28Quick%20Notes.one%7C93313146-b485-4c18-8ea8-8eb7827be88c%2FUntitled%20Page%7C59ef0753-6224-a240-a6cc-38b694f77358%2F%29&wdorigin=703
# NOTE: what is this workflow supposed to do?

#. TODO: increase the size of self.stats and see how long is running time for Metaflow -- Current: 2s

class ForeachFlow(FlowSpec):

    @step
    def start(self):
        self.names = ['Pogacar', 'Armstrong', 'Ulrich']
        self.ftps = [120, 400, 350]
        self.next(self.analyze_athletes, foreach='ftps')
    
    @step  #*  all 3 RUNS from below are ran at the same time -- parallel
    def analyze_athletes(self):
        print("Analyzing name. ", self.names[self.index])
        print("Analyzing ftp. ", self.ftps[self.index])
        #? how can i also get the index of self.name from self.names
        self.name = self.names[self.index]
        self.ftp = self.ftps[self.index]
        self.next(self.join) 
    
    
    @step
    # TODO: return the athelete that won (not their ftp)
    def join(self, inputs):
        self.best_ftp = max(inputs, key=lambda x: x.ftp).ftp #? .score changed to .name returns ForeachFlow 
        
        self.next(self.end)

    @step
    def end(self):
        print(self.best_ftp, 'won!')

if __name__ == '__main__':
    ForeachFlow()
