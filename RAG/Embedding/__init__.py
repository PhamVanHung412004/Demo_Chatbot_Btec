from tqdm import tqdm
from langchain.vectorstores import Chroma
import math

def create_vectorstore_with_progress(documents, embeddings, persist_directory, batch_size):
    """Tạo vectorstore với progress bar"""
    
    # Khởi tạo Chroma trống
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    
    # Chia documents thành batches
    total_docs = len(documents)
    num_batches = math.ceil(total_docs / batch_size)
    
    # Progress bar
    with tqdm(total=total_docs, desc="Bắt đầu embedding: ") as pbar:
        for i in range(0, total_docs, batch_size):
            # Lấy batch hiện tại
            batch = documents[i:i + batch_size]
            
            # Thêm batch vào vectorstore
            vectorstore.add_documents(documents=batch)
            
            # Update progress bar
            pbar.update(len(batch))
            
            # Optional: hiển thị thêm info
            pbar.set_postfix({
                'batch': f"{i//batch_size + 1}/{num_batches}",
                'total_added': i + len(batch)
            })
    
    # Persist sau khi xong
    print("Persisting to disk...")
    vectorstore.persist()
    print("✅ Complete!")
    
    return vectorstore