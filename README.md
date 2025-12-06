# Ứng dụng phân loại cảm xúc tiếng Việt (Đồ án)

**Mô tả ngắn:** Ứng dụng demo phân loại cảm xúc tiếng Việt sử dụng model pre-trained `vinai/phobert-base` thông qua HuggingFace `pipeline`. Đây là phiên bản inference-only (không fine-tune), phù hợp với yêu cầu đồ án.

## Files
- `app.py` - Streamlit app (UI) để nhập câu và lưu kết quả vào SQLite.
- `model.py` - Wrapper sử dụng `transformers.pipeline` để load model & inference.
- `database.py` - Module quản lý SQLite (lưu lịch sử).
- `test.py` - Script chạy 10 test case & in accuracy.
- `requirements.txt` - Các package cần thiết.

## Hướng dẫn chạy
1. Tạo môi trường ảo (khuyến nghị):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
   ```
2. Cài dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy ứng dụng Streamlit:
   ```bash
   streamlit run app.py
   ```
   - Lần chạy đầu tiên sẽ tải model `vinai/phobert-base` (~400MB). Cần kết nối Internet.
4. Chạy test:
   ```bash
   python test.py
   ```

## Gợi ý cho đồ án
- Nếu máy của bạn không có GPU, pipeline sẽ chạy trên CPU (chậm hơn).
- Nếu muốn model nhẹ hơn, thay `vinai/phobert-base` bằng `distilbert-base-multilingual-cased` trong `model.py`.
- Bạn có thể mở rộng giao diện, thêm export CSV/PDF, hoặc API endpoints nếu cần.

## Ghi chú
- Đây là project *inference-only* theo yêu cầu đồ án; không bao gồm phần training/fine-tuning.
