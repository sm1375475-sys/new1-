class student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id
        self.grade=grade
class undergraduatestudent(student):
    def __init__(self, name, id, grade, major):
        super().__init__(name, id, grade)
        self.major=major 

    def display_info(self):
        print("undergraduate student")
        super().display_info()
        print("major:", self.major)

class graduatestudent(student):
    def __init__(self, name, id, grade, program_title):
        super().__init__(name, id, grade)
        self.program_title=program_title

    def display_info(self):
        print("graduate student")
        super().display_info()
        print("program titel:", self.program_title)    
           
                  