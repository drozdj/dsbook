from metaflow import FlowSpec, step

#working w/ three branches

#2024-05-08 15:04:06.688 [1715173444992298/end/6 (pid 419109)] Hello there alien!Hello there man!Hello there woman!.
# TODO: why is the above output in that order when I defined [hello_man,hello_woman_hello_alien]?

# TODO: why is it necessary for me to define 'self.creature = inputs[0].creature' again in function join rather than calling it from function end?

# --- 

class ThreeBranchFlow(FlowSpec):

    @step
    def start(self):
        """Starting point"""
        print("This is start step")
        self.creature = "cat"
        self.string = ""
        self.next(self.hello_man, self.hello_woman, self.hello_alien)

    @step #branch 0
    def hello_man(self): 
        """Hello there man!"""
        # self.creature = "dolphin"
        self.string += "Hello there man!"
        print(self.string)
        self.next(self.join)

    @step # branch 1
    def hello_woman(self):
        """Hello there woman!"""
        # self.creature = "dog"
        self.string += "Hello there woman!"
        print(self.string)
        self.next(self.join)
    
    @step # branch 2
    def hello_alien(self):
        """Hello there alien!"""
        self.string += "Hello there alien!"
        print(self.string)
        self.next(self.join) 

    @step #merge branch [0,1]
    def join(self, inputs):
        # print(inputs.hello_man.string)
        # print(inputs.hello_woman.string)
        self.string = [inputs[x].string for x in range(3)]
        self.creature = inputs[0].creature
        self.next(self.end)

    @step
    def end(self):
        """Finish line"""
        print(self.creature)
        print(self.string)
        print("This is end step")

if __name__ == '__main__':
    ThreeBranchFlow()
