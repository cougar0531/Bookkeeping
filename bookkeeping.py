# 記帳軟體 v0.4 - 新增存檔/讀檔功能

import json
import os

DATA_FILE = "records.json"
records = []

def load_records():
    global records
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            records = json.load(f)
        print(f"📂 已載入 {len(records)} 筆記錄")
    else:
        records = []
        print("📂 尚無儲存資料，從空白開始")

def save_records():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"💾 已儲存 {len(records)} 筆記錄")

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
    print("=== 記帳軟體 v0.4 ===")
    load_records()
    add_record("2025-01-04", "早餐", 60, "餐飲")
    add_record("2025-01-04", "公車", 20, "交通")
    show_records()
    show_summary()
    save_records()

if __name__ == "__main__":
    main()