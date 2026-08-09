# 記帳軟體 v0.2 - 新增刪除記錄功能

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

def delete_record(index):
    if index < 0 or index >= len(records):
        print("❌ 無效的編號")
        return
    removed = records.pop(index)
    print(f"🗑️ 已刪除：{removed['description']}")

def show_records():
    if not records:
        print("目前沒有任何記錄")
        return
    print("\n📒 所有記帳記錄：")
    print("-" * 40)
    for i, r in enumerate(records):
        print(f"{i}. {r['date']} | {r['description']} | ${r['amount']} | {r['category']}")
    print("-" * 40)

def main():
    print("=== 記帳軟體 v0.2 ===")
    add_record("2025-01-01", "早餐", 80, "餐飲")
    add_record("2025-01-01", "捷運", 30, "交通")
    add_record("2025-01-02", "午餐", 120, "餐飲")
    show_records()
    print("\n刪除第 1 筆記錄...")
    delete_record(1)
    show_records()

if __name__ == "__main__":
    main()