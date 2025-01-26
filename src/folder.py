import os
from typing import List

import file


class Folder:
    def __init__(self, path):
        self.__path = path
        self.parent_folder = None

    def all_child_files(self) -> List[any]:
        files = [File(f) for f in os.listdir(self.__path) if os.path.isfile(os.path.join(folder_path, f))]

    def all_files(self):
        pass