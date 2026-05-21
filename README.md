# 🎓 Hệ thống Tư vấn Tuyển sinh Giáo dục Đại học

[![Framework](https://img.shields.io/badge/Framework-LangChain-green)](https://python.langchain.com/)
[![Graph](https://img.shields.io/badge/Orchestration-LangGraph-blue)](https://langchain-ai.github.io/langgraph/)
[![Database](https://img.shields.io/badge/VectorDB-ChromaDB-orange)](https://www.trychroma.com/)
[![UI](https://img.shields.io/badge/Frontend-Streamlit-red)](https://streamlit.io/)

## 📖 Giới thiệu
Dự án xây dựng một **AI Agent** chuyên dụng để hỗ trợ tư vấn tuyển sinh cho trường Đại học Công nghệ XYZ. Hệ thống sử dụng kiến trúc **RAG (Retrieval-Augmented Generation)** để cung cấp thông tin chính xác từ các tài liệu đề án tuyển sinh (PDF) và tra cứu điểm chuẩn từ cơ sở dữ liệu có cấu trúc (JSON).

Hệ thống được thiết kế để hoạt động như một chuyên viên tư vấn chuyên nghiệp, chính xác và thân thiện, giúp thí sinh và phụ huynh giải đáp các thắc mắc về:
*   Điểm chuẩn các năm.
*   Chỉ tiêu và tổ hợp xét tuyển.
*   Học phí và các chính sách ưu đãi.
*   Quy chế tuyển sinh và các mốc thời gian quan trọng.

---

## 📋 Mục lục
*   [Giới thiệu](#-giới-thiệu)
*   [Thành viên thực hiện](#-thành-viên-thực-hiện)
*   [Kiến trúc hệ thống](#-kiến-trúc-hệ-thống)
*   [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
*   [Hướng dẫn cài đặt](#-hướng-dẫn-cài-đặt)
*   [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
*   [Công nghệ sử dụng](#-công-nghệ-sử-dụng)

---

## 👤 Thành viên thực hiện & Đóng góp
| Họ tên | Vai trò | Công việc phụ trách & Đóng góp chính |
| :--- | :--- | :--- |
| **Lê Quốc Nam** | Đồng phát triển | **Cấu hình môi trường chạy, tối ưu hóa cấu trúc Git, tích hợp dữ liệu hệ thống và kiểm thử.** |
| **Lê Khánh Hoàng** | Trưởng nhóm | Nghiên cứu và xây dựng cấu trúc luồng LangGraph, RAG và thiết kế giao diện Chatbot. |
| **Trương Xuân Hưng** | Đồng phát triển | Xây dựng tài liệu báo cáo và nội dung tổng kết hệ thống. |

---

## 🏗️ Kiến trúc hệ thống
Hệ thống được xây dựng dựa trên quy trình **Reasoner-ToolNode** của LangGraph:
1.  **Reasoner (Bộ não)**: Sử dụng mô hình LLM Qwen2.5 (qua Hugging Face API) để phân tích ý định câu hỏi của người dùng.
2.  **Tools (Công cụ trợ lý)**:
    *   `tra_cuu_thong_tin`: Truy xuất ngữ cảnh từ dữ liệu PDF Đề án tuyển sinh (RAG) sử dụng ChromaDB.
    *   `tra_cuu_diem_chuan`: Thực hiện truy vấn dữ liệu có cấu trúc từ tệp JSON chứa điểm chuẩn các năm.
3.  **State Management**: Quản lý lịch sử hội thoại, ngữ cảnh RAG và hồ sơ học sinh theo thời gian thực qua State của LangGraph.

---

## 📂 Cấu trúc thư mục
```text
ChatBotTuVanTuyenSinh/
├── data/
│   ├── admissions/      # Chứa tài liệu đề án tuyển sinh định dạng PDF
│   └── diem_chuan_2025.json # Dữ liệu điểm chuẩn có cấu trúc (JSON)
├── src/
│   ├── agents/          # Định nghĩa cấu hình hệ thống AI Agent
│   ├── graph/           # Xây dựng luồng workflow đồ thị (State, Nodes, Graph)
│   └── tools/           # Các công cụ hỗ trợ truy xuất thông tin
├── chroma_db/           # Cơ sở dữ liệu Vector lưu trữ dữ liệu embeddings
├── frontend1.py         # Giao diện người dùng Chatbot chạy bằng Streamlit
├── ingest.py            # Script xử lý trích xuất văn bản PDF và nạp vào ChromaDB
├── requirements.txt     # Danh sách toàn bộ thư viện phụ thuộc
├── .env                 # File chứa khóa cấu hình môi trường (HF_TOKEN)
└── README.md            # Tài liệu dự án dành cho nhà tuyển dụng
```

---

## 🛠️ Hướng Dẫn Cài Đặt Và Chạy Cục Bộ (Setup & Run)

Nhà tuyển dụng có thể dễ dàng chạy thử nghiệm chatbot cục bộ theo các bước chi tiết sau:

### 1. Chuẩn bị môi trường (Prerequisites)
*   Cài đặt **Python 3.10** trở lên trên hệ điều hành máy của bạn.
*   Một API Token từ Hugging Face (Tạo hoàn toàn miễn phí tại [huggingface.co](https://huggingface.co/) -> Settings -> Access Tokens).

### 2. Cài đặt chi tiết qua môi trường ảo (Virtual Environment)
Mở Terminal/PowerShell tại thư mục dự án và chạy các lệnh:
```bash
# Tạo môi trường ảo riêng biệt
python -m venv .venv

# Kích hoạt môi trường ảo
# Trên Windows (PowerShell):
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; .venv\Scripts\Activate.ps1
# Trên Windows (Command Prompt):
.venv\Scripts\activate
# Trên macOS/Linux:
source .venv/bin/activate

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 3. Cấu hình khóa API Token
Tạo file `.env` tại thư mục gốc của dự án (hoặc mở file `.env` đã có sẵn) và điền mã thông báo Hugging Face của bạn:
```env
HF_TOKEN=mã_huggingface_token_của_bạn_ở_đây
```

---

## 🚀 Hướng dẫn sử dụng chi tiết (Execution)

### Bước 1: Nạp tài liệu tuyển sinh vào Cơ sở dữ liệu Vector (VectorDB Ingestion)
Đặt tệp PDF đề án tuyển sinh của trường vào thư mục `data/admissions/` (ví dụ `De_an_tuyen_sinh_2026.pdf`), sau đó tiến hành chạy script để bóc tách văn bản, nhúng embeddings và lưu vào Chroma Vector Database:
```bash
python ingest.py
```
*Hệ thống sẽ quét tài liệu PDF, phân đoạn và tạo các vector nhúng (embeddings) lưu trữ cục bộ trong thư mục `chroma_db/`.*

### Bước 2: Khởi chạy Giao diện Chatbot tư vấn
Chạy ứng dụng Web tương tác Streamlit:
```bash
streamlit run frontend1.py
```
Ứng dụng sẽ tự động mở trang web giao diện tư vấn tuyển sinh tại địa chỉ cục bộ: `http://localhost:8501`.

---

## 💻 Công nghệ sử dụng chính (Tech Stack)
*   **Ngôn ngữ lập trình**: Python 3.10+
*   **Mô hình ngôn ngữ (LLM)**: Qwen2.5-72B-Instruct (via Hugging Face Serverless API)
*   **Framework AI**: LangChain & LangGraph (Quản lý trạng thái và luồng quyết định đồ thị Agent)
*   **Cơ sở dữ liệu Vector**: ChromaDB với Hugging Face Embeddings
*   **Giao diện người dùng**: Streamlit UI responsive, tối ưu trải nghiệm tương tác trực quan.

