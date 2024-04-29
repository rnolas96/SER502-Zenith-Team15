class Runtime:
    variables = {}

    def init(self):
        self.variables = {}

    def execute(self, intermediate_code):
        # Split the intermediate code into lines
        lines = intermediate_code.split("\n")
        # print(len(lines))
        i = 0
        indent = 0

        while i < len(lines):

            # print(len(lines[i]))
            # print("regular", i, " - ", lines[i])

            if lines[i] == '{':
                indent += 1
                i += 1
                continue

            elif lines[i] == '}':
                # print("indent decrement- ", indent, "and", i)
                indent -= 1
                i += 1
                continue

            line = lines[i].strip()

            space = ""
            k = indent
            while k > 0:
                space += "\t"
                k -= 1

            lines[i] = space + line
            i += 1

        i = 0
        while i < len(lines):
            if lines[i].startswith("if") or lines[i].startswith("for") or lines[i].startswith("while"):
                combined_code = lines[i] 
                i += 1

                spaceCount = len(lines[i]) - len(lines[i].lstrip())
                
                while lines[i] == '{' or lines[i] == '}':
                    i+=1

                spaceCountInternal = len(lines[i]) - len(lines[i].lstrip())

                while i < len(lines) and (spaceCountInternal - spaceCount) > 0:
                    combined_code += "\n" + lines[i]
                    i += 1

                    while i < len(lines) and (lines[i] == '{' or lines[i] == '}'):
                        # print("comes here")
                        i+=1

                    if i < len(lines):
                        spaceCountInternal = len(lines[i]) - len(lines[i].lstrip())
                    # print("comes here", lines[i], spaceCountInternal, "and", spaceCount)

                # print("comes here", spaceCountInternal, "and", spaceCount)

                if spaceCountInternal == spaceCount:
                    # print("comes here")
                    while i < len(lines) and lines[i].startswith("elif"): 
                        # print("comes here")
                        combined_code += "\n" + lines[i]
                        i += 1

                        while i < len(lines) and (lines[i] == '{' or lines[i] == '}'):
                            i += 1

                        spaceCountElif = len(lines[i]) - len(lines[i].lstrip())
                        
                        # print("spaceCountElif - ", spaceCountElif, lines[i])

                        while i < len(lines) and (spaceCountElif - spaceCount) > 0:
                            combined_code += "\n" + lines[i]
                            i += 1

                            while i < len(lines) and (lines[i] == '{' or lines[i] == '}'):
                                i += 1

                            if i < len(lines):
                                spaceCountElif = len(lines[i]) - len(lines[i].lstrip())

                    if i < len(lines) and lines[i].startswith("else"):
                        combined_code += "\n" + lines[i]
                        i += 1

                        while i < len(lines) and (lines[i] == '{' or lines[i] == '}'):
                            i += 1
                        
                        spaceCountElse = len(lines[i]) - len(lines[i].lstrip())

                        while i < len(lines) and (spaceCountElse - spaceCount) > 0:
                            combined_code += "\n" + lines[i]
                            i += 1

                            while i < len(lines) and (lines[i] == '{' or lines[i] == '}'):
                                i += 1

                            if i < len(lines):
                                spaceCountElse = len(lines[i]) - len(lines[i].lstrip())
                
                # print("combined code", combined_code)
                exec(combined_code, {}, self.variables)
                combined_code = ""
            else:
                exec(lines[i], {}, self.variables)
                i += 1




