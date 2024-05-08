from metaflow import FlowSpec, step

#working w/ two branches

class TwoBranchFlow(FlowSpec):

    @step
    def start(self):
        """Starting point"""
        print("This is start step")
        # self.creature = "cat"
        self.string = ""
        self.next(self.hello_man, self.hello_woman)

    @step #branch 0
    def hello_man(self): 
        """Hello there man!"""
        self.creature = "dolphin"
        self.string += "Hello there man!"
        self.next(self.join)

    @step # branch 1
    def hello_woman(self):
        """Hello there woman!"""
        self.creature = "dog"
        self.string += "Hello there woman!"
        self.next(self.join)

    @step #merge branch [0,1]
    def join(self, inputs):
        print(inputs.hello_man.string)
        print(inputs.hello_woman.string)
        self.creature = inputs[1].creature
        self.string = inputs[0].string
        self.next(self.end)

    @step
    def end(self):
        """Finish line"""
        print(self.creature)
        print(self.string)
        print("This is end step")

if __name__ == '__main__':
    TwoBranchFlow()
