from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from typing import List

class get_data:
    def __init__(self, path_folder : str) -> None:
        """
        path_folder : đường dẫn đến folder chứa file pdf
        """
        self.__path_folder : str = path_folder

    #hàm đọc file pdf trong folder chuyển về dạng list
    @property
    def read(self) -> List[str]:
        loader : DirectoryLoader = DirectoryLoader(
            path=self.__path_folder,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
            show_progress=True
        )
        return loader.load()
