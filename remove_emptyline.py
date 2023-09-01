class RemoveEmptyLines:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def strip_void_lines(self):
        with open(self.file1, 'r') as f2, open(self.file2, 'w') as f2_updated:
            for line in f2:
                if line.strip():
                    f2_updated.write(line)


RemoveEmptyLines('f11', 'f22').strip_void_lines()
