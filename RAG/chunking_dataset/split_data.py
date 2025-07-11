from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

from typing import (
    List
)

class Chunking_Data:
    def __init__(self, documents: List[str], model_embedding: HuggingFaceEmbeddings) -> None:
        '''
        documents : Văn bản sau khi đã chuyển hóa từ file PDF thành file text và được lưu dưới dạng list
        model_embedding : là model embedding do mình lựa chọn để chunking data
        '''
        self.__documents : List[str] = documents
        self.__model_embedding : HuggingFaceEmbeddings = model_embedding
    
    def get_chunks(self) -> list:
        try:
            # Sử dụng SemanticChunker của LangChain
            text_splitter = SemanticChunker(
                embeddings=self.__model_embedding,
                breakpoint_threshold_type="percentile",  # hoặc "standard_deviation", "interquartile"
                breakpoint_threshold_amount=95,
                sentence_split_regex=r"(?<=[.?!])\s+",  # Regex để tách câu
            )
            
            # Split documents
            chunks = text_splitter.split_documents(self.__documents)
            return chunks
            
        except Exception as e:
            print(f"Error: {e}")
            return []