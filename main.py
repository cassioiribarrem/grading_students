class Grading_students():
    def __init__(self, grades):
        self.grades = grades

    def rounding(self):
        updated = []
        for i in range(0, len(self.grades)):
            if self.grades[i] < 38:
                updated.append(self.grades[i])

            else:
                factor = self.grades[i] // 5
                next_up = (factor+1) * 5
                difference = next_up - self.grades[i]

                if difference < 3:
                    updated.append(next_up)

                else:
                    updated.append(self.grades[i])
        return updated

result = Grading_students([38, 19, 79, 34, 62])
result.rounding()



