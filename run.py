from RAG import (
    get_data,
    Chunking_Data,
    VectorstoreBuilder
)
from langchain_huggingface import HuggingFaceEmbeddings
from typing import (
    List,
    Dict
)
import torch
from dataclasses import dataclass

@dataclass
class INIT_MODEL_EMBEDDING:
    embeddings : HuggingFaceEmbeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5",
            model_kwargs={'device': 'cuda' if (torch.cuda.is_available()) else 'cpu'},
            encode_kwargs={
                'normalize_embeddings': True,
                'batch_size': 32
            }
        )

def document_loader(path_data_pdf : str) -> List[str]: 
    documents : List[str] = get_data(path_data_pdf).read
    return documents

def chunking(documents) -> List[str]:
    data_split : List[str] = Chunking_Data(documents,INIT_MODEL_EMBEDDING.embeddings).run

def main() -> None:
    documents : List[str] = document_loader("dataset/dataset_IT")
    
    data_split : List[str] = chunking(documents)
    
    vectorstore = VectorstoreBuilder(
        embeddings=INIT_MODEL_EMBEDDING.embeddings,
        persist_directory="VectorDB/chroma_db",
        batch_size=100
    )

    vectorstore = builder.build(data_split)

if __name__ == "__main__":
    main()