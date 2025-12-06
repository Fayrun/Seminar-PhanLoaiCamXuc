# test.py: run 10 representative Vietnamese sentences and compute accuracy
from model import SentimentModel
import argparse

TEST_CASES = [
    ("Hôm nay tôi rất vui vẻ", "POSITIVE"),
    ("Món ăn này thật tuyệt vời", "POSITIVE"),
    ("Dịch vụ quá tệ, không bao giờ quay lại", "NEGATIVE"),
    ("Tôi rất thất vọng về sản phẩm này", "NEGATIVE"),
    ("Thời tiết hôm nay bình thường", "NEUTRAL"),
    ("Cuốn sách có 200 trang", "NEUTRAL"),
    ("Tôi không thích cách họ làm việc", "NEGATIVE"),
    ("Sản phẩm chất lượng tốt, đáng tiền", "POSITIVE"),
    ("Cửa hàng mở cửa lúc 8 giờ sáng", "NEUTRAL"),
    ("Trải nghiệm tuyệt vời, sẽ giới thiệu bạn bè", "POSITIVE"),
]

def normalize_label(label):
    # Some pipelines return 'POSITIVE'/'NEGATIVE', others 'LABEL_0' etc.
    l = label.upper()
    if l.startswith('LABEL_'):
        # best-effort mapping (user may need to adapt)
        # We'll keep as-is and compare to expected with startswith
        return l
    return l

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=None, help="optional model override")
    args = parser.parse_args()
    model = SentimentModel(model_name=args.model) if args.model else SentimentModel()
    correct = 0
    total = len(TEST_CASES)
    for text, expected in TEST_CASES:
        res = model.predict(text)
        if 'error' in res:
            print(f"Error for '{text}': {res['error']}")
            continue
        pred = normalize_label(res['label'])
        print(f"Text: {text}\nPred: {pred} ({res['score']:.2%})\nExpected: {expected}\n---")
        # simple matching: check token presence or equality
        if expected in pred or pred in expected:
            correct += 1
    accuracy = 100.0 * correct / total
    print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})")

if __name__ == '__main__':
    main()
