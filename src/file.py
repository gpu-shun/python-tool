import os
import shutil


class File:
    def __init__(self, path):
        self.__path = path
        self.parent_folder = None

    def name(self):
        # ファイル名を返す
        return os.path.basename(self.__path)
    
    def extention(self):
        # 拡張子を返す
        return os.path.splitext(self.__path)[1]
    
    def move(self, target_path: str):
        # 指定したパスにファイルを移動する
        shutil.move(self.file_path, target_path)
        self.file_path = target_path

    def rename(self):
        pass