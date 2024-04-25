class Runtime:
    variables = {}
    def init(self):
        self.variables = {}

    def execute(self, intermediate_code):
        # Split the intermediate code into lines
        lines = intermediate_code.split("\n")

        for line in lines:
            line = line.strip()
            if line:
                exec(line, {}, self.variables) 
