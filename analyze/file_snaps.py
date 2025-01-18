from difflibparser import DifflibParser as diff

# TODO: minify the source UI file.
class FileSnapContainer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
        file_content = open(file_path).readlines()

        self.queue = [file_content]
        self.max_size = 2
    
    def get(self): return self.queue.copy(); self.add()

    def add(self): 
        if len(self.queue):
            self.queue.pop(0)
        file_content = open(self.file_path).readlines()
        self.queue.append(file_content)
    
def diffSnaps(snaps: list):
    snaps = snaps
    file_diff = diff(snaps[0], snaps[1])
    update_only_line = filter(lambda line_data: line_data.get("code")==3, file_diff)
    return update_only_line
    

