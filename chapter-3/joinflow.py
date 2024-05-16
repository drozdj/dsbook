from metaflow import FlowSpec, step

class JoinFlow(FlowSpec):
    @step
    def start(self):
        self.nums = [10, 40, 3, 500, 5]
        self.next(self.analyze, foreach='nums')

    #NOTE: without this middle step, we are unable to dynamic branch
    @step
    def analyze(self):
        self.result = self.input        
        self.next(self.join)

    @step
    def join(self, inputs):
        # print(inputs[1].result)
         
        self.highest = max(inputs, key=lambda x: x.result).result 
        # self.results = [input * 2 for input in self.nums]
        self.next(self.end)

    @step
    def end(self):
        print("Results:", self.highest)

if __name__ == '__main__':
    JoinFlow()