import os
import shutil
from pathlib import Path

def collect_pdfs_from_subfolders(source_dir, destination_dir):
    """
    Thu thập tất cả file PDF từ các folder con và chuyển vào một folder đích
    
    Args:
        source_dir (str): Đường dẫn folder gốc chứa các folder con
        destination_dir (str): Đường dẫn folder đích để chứa tất cả PDF
    """
    
    # Tạo folder đích nếu chưa tồn tại
    os.makedirs(destination_dir, exist_ok=True)
    
    # Đếm số file đã sao chép
    copied_files = 0
    
    # Duyệt qua tất cả file và folder con
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Kiểm tra file có phải PDF không
            if file.lower().endswith('.pdf'):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)
                
                # Xử lý trường hợp file trùng tên
                counter = 1
                original_name = file
                while os.path.exists(destination_file):
                    name, ext = os.path.splitext(original_name)
                    file = f"{name}_{counter}{ext}"
                    destination_file = os.path.join(destination_dir, file)
                    counter += 1
                
                try:
                    # Sao chép file
                    shutil.copy2(source_file, destination_file)
                    print(f"Đã sao chép: {source_file} -> {destination_file}")
                    copied_files += 1
                except Exception as e:
                    print(f"Lỗi khi sao chép {source_file}: {e}")
    
    print(f"\nHoàn thành! Đã sao chép {copied_files} file PDF.")

def move_pdfs_from_subfolders(source_dir, destination_dir):
    """
    Di chuyển (cắt-dán) tất cả file PDF từ các folder con vào một folder đích
    
    Args:
        source_dir (str): Đường dẫn folder gốc chứa các folder con
        destination_dir (str): Đường dẫn folder đích để chứa tất cả PDF
    """
    
    # Tạo folder đích nếu chưa tồn tại
    os.makedirs(destination_dir, exist_ok=True)
    
    # Đếm số file đã di chuyển
    moved_files = 0
    
    # Duyệt qua tất cả file và folder con
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Kiểm tra file có phải PDF không
            if file.lower().endswith('.pdf'):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)
                
                # Xử lý trường hợp file trùng tên
                counter = 1
                original_name = file
                while os.path.exists(destination_file):
                    name, ext = os.path.splitext(original_name)
                    file = f"{name}_{counter}{ext}"
                    destination_file = os.path.join(destination_dir, file)
                    counter += 1
                
                try:
                    # Di chuyển file
                    shutil.move(source_file, destination_file)
                    print(f"Đã di chuyển: {source_file} -> {destination_file}")
                    moved_files += 1
                except Exception as e:
                    print(f"Lỗi khi di chuyển {source_file}: {e}")
    
    print(f"\nHoàn thành! Đã di chuyển {moved_files} file PDF.")

# Cách sử dụng
if __name__ == "__main__":
    # Thay đổi đường dẫn theo nhu cầu của bạn
    source_directory = "C:/Documents"  # Folder gốc chứa các folder con
    destination_directory = "C:/All_PDFs"  # Folder đích để chứa tất cả PDF
    
    print("Chọn chế độ:")
    print("1. Sao chép file PDF (giữ nguyên file gốc)")
    print("2. Di chuyển file PDF (xóa file gốc)")
    
    choice = input("Nhập lựa chọn (1 hoặc 2): ")
    
    if choice == "1":
        collect_pdfs_from_subfolders(source_directory, destination_directory)
    elif choice == "2":
        move_pdfs_from_subfolders(source_directory, destination_directory)
    else:
        print("Lựa chọn không hợp lệ!")

# Phiên bản đơn giản hơn (chỉ sao chép)
def simple_pdf_collector(source_dir, destination_dir):
    """Phiên bản đơn giản để sao chép tất cả PDF"""
    os.makedirs(destination_dir, exist_ok=True)
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                source = os.path.join(root, file)
                dest = os.path.join(destination_dir, file)
                
                # Tự động đổi tên nếu file đã tồn tại
                counter = 1
                while os.path.exists(dest):
                    name, ext = os.path.splitext(file)
                    dest = os.path.join(destination_dir, f"{name}_{counter}{ext}")
                    counter += 1
                
                shutil.copy2(source, dest)
                print(f"Sao chép: {file}")

# Sử dụng đơn giản:
simple_pdf_collector("Đồ họa", "dataset/dataset_Graphics")