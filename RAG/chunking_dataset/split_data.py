from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

from typing import (
    List
)
from tqdm import tqdm
import logging

class Chunking_Data:
    def __init__(self, documents: List[str], model_embedding: HuggingFaceEmbeddings) -> None:
        '''
        documents : Văn bản sau khi đã chuyển hóa từ file PDF thành file text và được lưu dưới dạng list
        model_embedding : là model embedding do mình lựa chọn để chunking data
        '''
        self.__documents : List[str] = documents
        self.__model_embedding : HuggingFaceEmbeddings = model_embedding
    
    @property
    def run(self) -> list:
        try:
            # Sử dụng SemanticChunker của LangChain
            text_splitter : SemanticChunker = SemanticChunker(
                embeddings=self.__model_embedding,
                breakpoint_threshold_type="percentile",  # hoặc "standard_deviation", "interquartile"
                breakpoint_threshold_amount=95,
                sentence_split_regex=r"(?<=[.?!])\s+",  # Regex để tách câu
            )
            
            # Hiển thị tiến độ khi split documents
            print("Đang tách văn bản...")
            chunks = []
            for i, doc in enumerate(tqdm(self.__documents, desc="Processing documents")):
                doc_chunks = text_splitter.split_documents([doc])
                chunks.extend(doc_chunks)
            return chunks
            
        except Exception as e:
            print(f"Error: {e}")
            return []