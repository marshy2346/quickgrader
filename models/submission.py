class Submission:
    def __init__(self, path):
        self.path = path
        self.requirements = []

    def add_requirement(self, requirement_name):
        self.requirements.append([requirement_name, "", ""])

    def remove_requirement(self, row):
        new_requirements = []
        for r in range(0, len(self.requirements)):
            if r != row:
                new_requirements.append(self.requirements[r])
        self.requirements = new_requirements

    def get_json(self):
        requirements = []
        for r in self.requirements():
            requirements.append({
                'requirement': self.requirements[r][0],
                'value': self.requirements[r][1],
                'comments': self.requirements[r][2]
            })
        return {
            'path': path,
            'requirements': requirements
        }
