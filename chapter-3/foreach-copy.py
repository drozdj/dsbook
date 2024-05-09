from metaflow import FlowSpec, step
import numpy as np

# https://onedrive.live.com/redir?resid=3E781AD654D8C9F3%214716&authkey=%21AK97gjIH12Zyvow&page=Edit&wd=target%28Quick%20Notes.one%7C93313146-b485-4c18-8ea8-8eb7827be88c%2FUntitled%20Page%7C59ef0753-6224-a240-a6cc-38b694f77358%2F%29&wdorigin=703
# NOTE: what is this workflow supposed to do?


class ForeachFlow(FlowSpec):

    @step
    def start(self):
        self.stats = ['Pogacar', 'Armstrong', 'Ulrich']
        self.next(self.analyze_athletes, foreach='stats')
    
    @step  #NOTE: all 3 RUNS from below are ran at the same time -- paralel
    def analyze_athletes(self):        # RUN 1               | RUN 2                    | RUN 3
        print("Analyzing", self.input) # "Analyzing Pogacar" | "Analyzing Armstrong"    | "Analyzing Ulrich"
        self.stat = self.input         # stat = 'Pogacar'    | stat = 'Armstrong'       | stat = 'Ulrich'
        self.score = len(self.stat)    # score = 7           | score = 9                | score =  6
        self.next(self.join) 
    
    @step
    def join(self, inputs):
        #     inputs ^
        # RUN 1.   
        # RUN 2.
        # RUN 3.
        
        self.best = max(inputs, key=lambda x: x.score).stat #TODO: <- how does it work?
        self.next(self.end)

    @step
    def end(self):
        print(self.best, 'won!')

if __name__ == '__main__':
    ForeachFlow()
