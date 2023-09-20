class RegrasProduct:
    def criarRegra(self):
        self.regras = {
            "E" : ["T", "El"],
            "El" : [["+", "T", "El"], ["@"]],
            "T" : ["F", "Tl"],
            "Tl" : [["*", "F", "Tl"], ["@"]],
            "F" : [["id"], ["(", "E", ")"]]
        }