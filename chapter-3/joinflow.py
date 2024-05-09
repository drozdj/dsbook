from metaflow import FlowSpec, step

class JoinFlow(FlowSpec):
    @step
    def start(self):
        self.nums = [1, 2, 3, 4, 5]
        self.next(self.join)

    @step
    def join(self, inputs):
        # self.highest = max(inputs )
        self.results = [input * 2 for input in self.nums]
        self.next(self.end)

    @step
    def end(self):
        print("Results:", self.results)

if __name__ == '__main__':
    JoinFlow()