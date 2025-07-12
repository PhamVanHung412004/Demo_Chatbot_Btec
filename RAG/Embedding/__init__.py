from tqdm import tqdm
from langchain.vectorstores import Chroma
import math

class VectorstoreBuilder:
    def __init__(self, embeddings, persist_directory, batch_size=100):
        """
        Khởi tạo builder cho Chroma vectorstore.
        
        Args:
            embeddings: Hàm embedding sử dụng.
            persist_directory: Đường dẫn để lưu trữ vectorstore.
            batch_size: Số lượng tài liệu xử lý mỗi lần.
        """
        self.embeddings = embeddings
        self.persist_directory = persist_directory
        self.batch_size = batch_size
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )

    def build(self, documents):
        """
        Tạo vectorstore từ danh sách tài liệu với thanh tiến trình.
        
        Args:
            documents (List): Danh sách tài liệu để thêm vào vectorstore.
        
        Returns:
            Chroma: Đối tượng vectorstore đã được thêm tài liệu.
        """
        total_docs = len(documents)
        num_batches = math.ceil(total_docs / self.batch_size)

        with tqdm(total=total_docs, desc="Embedding") as pbar:
            for i in range(0, total_docs, self.batch_size):
                batch = documents[i:i + self.batch_size]
                self.vectorstore.add_documents(documents=batch)
                pbar.update(len(batch))
                pbar.set_postfix({
                    'batch': f"{i // self.batch_size + 1}/{num_batches}",
                    'total_added': i + len(batch)
                })

        print("Persisting to disk...")
        self.vectorstore.persist()
        print("✅ Complete!")

        return self.vectorstore
