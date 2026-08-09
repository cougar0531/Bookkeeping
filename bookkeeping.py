# 記帳軟體 v0.3 - 新增分類統計功能

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

def show_summary():
    if not records:
        print("目前沒有任何記錄")
        return
    summary = {}
    for r in records:
        category = r["category"]
        summary[category] = summary.get(category, 0) + r["amount"]
    total = sum(summary.values())
    print("\n📊 分類統計：")
    print("-" * 40)
    for category, amount in summary.items():
        percentage = (amount / total) * 100
        print(f"{category}：${amount}（{percentage:.1f}%）")
    print("-" * 40)
    print(f"總計：${total}")

def main():
    print("=== 記帳軟體 v0.3 ===")
    add_record("2025-01-01", "早餐", 80, "餐飲")
    add_record("2025-01-01", "捷運", 30, "交通")
    add_record("2025-01-02", "午餐", 120, "餐飲")
    add_record("2025-01-02", "計程車", 200, "交通")
    add_record("2025-01-03", "晚餐", 150, "餐飲")
    show_records()
    show_summary()

if __name__ == "__main__":
    main()