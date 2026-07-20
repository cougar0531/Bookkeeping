# 記帳軟體 v0.1 - 基本架構

records = []

def add_record(date, description, amount, category):
    record = {
        "date": date,
        "description": description,
        "amount": amount,
        "category": category
    }
    records.append(record)
    print(f"✅ 已新增：{date} | {description} | ${amount} | {category}")

def show_records():
    if not records:
        print("目前沒有任何記錄")
        return
    print("\n📒 所有記帳記錄：")
    print("-" * 40)
    for r in records:
        print(f"{r['date']} | {r['description']} | ${r['amount']} | {r['category']}")
    print("-" * 40)

def main():
    print("=== 記帳軟體 v0.1 ===")
    # 測試資料
    add_record("2025-01-01", "早餐", 80, "餐飲")
    add_record("2025-01-01", "捷運", 30, "交通")
    add_record("2025-01-02", "午餐", 120, "餐飲")
    show_records()

if __name__ == "__main__":
    main()