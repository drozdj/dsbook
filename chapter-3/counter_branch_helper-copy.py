from metaflow import FlowSpec, step

# NOTE: if my assumption is correct,
# 'self.count' is able to be altered when 



class CounterBranchHelperFlow(FlowSpec):

    @step
    def start(self):
        self.athlete0 = ["Jan Alrich", 340]
        self.athlete1 = ["Lance Armstrong", 500] 
        self.next(self.athlete_0, self.athlete_1) 
    
    @step
    def athlete_0(self): 
        self.next(self.join)
    
    @step
    def athlete_1(self):
        self.next(self.join)

    @step
    def join(self, inputs):
        self.count = max(self.athlete0, self.athlete1)
        self.merge_artifacts(inputs)#, exclude=['increment']) 
        self.next(self.end)

    @step
    def end(self):
        print("The final pick is: ", self.count)

if __name__ == '__main__':
    CounterBranchHelperFlow()

