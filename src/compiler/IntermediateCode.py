class IntermediateCode:
    intermediate_code = ""
    def init(self):
        self.intermediate_code = ""

    def add_intermediate_output(self, code):
        self.intermediate_code += code + "\n"

    def get_intermediate_code(self):
        return self.intermediate_code

    def set_intermediate_code(self, intermediate_code):
        self.intermediate_code = intermediate_code