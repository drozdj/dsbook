from metaflow import FlowSpec, step
import numpy as np

class ForeachFlow(FlowSpec):

    @step
    def start(self):
        self.athletes = ['Pogacar', 'Armstrong', 'Ulrich']
        self.ftp = [100,200,300] 
        self.next(self.analyze_athletes, foreach='athletes')
    
    @step
    def analyze_athletes(self):
        print("Analyzing", self.input)
        self.athletes = self.input
        self.top_ftp = np.argmax(self.ftp)
        self.next(self.join)
    
    @step
    def join(self, inputs):
        
        self.next(self.end)

    @step
    def end(self):
        print(self.best, 'won!')

if __name__ == '__main__':
    ForeachFlow()

