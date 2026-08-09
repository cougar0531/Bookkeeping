# Git 學習筆記｜階段 3 — 功能迭代 ＋ 多次版本提交

#git #github #學習筆記

> 📅 日期：2026-07-21
> 🎯 目標：養成「小步提交」習慣，體驗版本歷史的價值，學習進退版操作

---

## 📌 本階段重點觀念

### 為什麼要「小步提交」？

> 每完成一個小功能就 commit 一次，不要累積很多變更才一次 commit。

好處：
- 每個版本的變動範圍小，出問題時容易找到原因
- commit message 可以寫得清楚具體
- 隨時可以退回到任何一個穩定版本
- GitHub 上的版本歷史清晰易讀

### 標準開發流程（每次功能完成後）

```bash
git add .                    # 1. 加入暫存區
git commit -m "feat: 說明"   # 2. 存版本快照
git push                     # 3. 同步到 GitHub
```

---

## 版本迭代記錄

| 版本 | Commit Hash | 新增功能 |
|------|-------------|------|
| v0.1 | `0a88c95` | 基本架構（新增、顯示記錄）|
| v0.2 | `d9cd328` | 新增刪除記錄功能 |
| v0.3 | `da2c346` | 新增分類統計功能 |
| v0.4 | `bbff19e` | 新增存檔／讀檔功能 ＋ .gitignore |

---

## 步驟 3-1｜v0.2 刪除記錄功能

### 新增的核心程式碼

```python
def delete_record(index):
    if index < 0 or index >= len(records):
        print("❌ 無效的編號")
        return
    removed = records.pop(index)
    print(f"🗑️ 已刪除：{removed['description']}")
```

### Commit 指令
```bash
git add bookkeeping.py
git commit -m "feat: 新增刪除記錄功能 v0.2"
git push
```

---

## 步驟 3-2｜v0.3 分類統計功能

### 新增的核心程式碼

```python
def show_summary():
    summary = {}
    for r in records:
        category = r["category"]
        summary[category] = summary.get(category, 0) + r["amount"]
    total = sum(summary.values())
    for category, amount in summary.items():
        percentage = (amount / total) * 100
        print(f"{category}：${amount}（{percentage:.1f}%）")
    print(f"總計：${total}")
```

### Commit 指令
```bash
git add bookkeeping.py
git commit -m "feat: 新增分類統計功能 v0.3"
git push
```

---

## 步驟 3-3｜v0.4 存檔／讀檔功能 ＋ .gitignore

### 新增的核心程式碼

```python
import json
import os

DATA_FILE = "records.json"

def load_records():
    global records
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            records = json.load(f)

def save_records():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
```

### 為什麼要執行兩次驗證？

第一次執行：
```
📂 尚無儲存資料，從空白開始   ← 沒有舊資料
💾 已儲存 2 筆記錄            ← 寫入 records.json
```

第二次執行：
```
📂 已載入 2 筆記錄            ← 成功讀回！證明存檔有效
```

> 只執行一次無法確認資料是真的「存起來」了，
> 還是只存在記憶體裡、程式關掉就消失。

---

## 步驟 3-4｜建立 .gitignore

### 什麼是 .gitignore？
告訴 Git「哪些檔案不需要追蹤」的設定檔。

### 建立指令
```bash
echo "records.json" > .gitignore
```

### 哪些檔案應該放進 .gitignore？

| 類型 | 範例 | 原因 |
|------|------|------|
| 資料檔 | `records.json` | 每個人資料不同，不應共用 |
| 環境設定 | `.env` | 含有密碼、金鑰等敏感資訊 |
| 暫存檔 | `__pycache__/` | 自動產生，不需要版本控制 |
| 系統檔 | `.DS_Store` | Mac 系統自動產生，無意義 |

### Commit 指令
```bash
git add bookkeeping.py .gitignore
git commit -m "feat: 新增存檔讀檔功能 v0.4，新增 .gitignore"
git push
```

---

## ⏪ 進退版操作

### 查看版本歷史

```bash
git log --oneline
```

範例輸出：
```
bbff19e feat: 新增存檔讀檔功能 v0.4，新增 .gitignore
da2c346 feat: 新增分類統計功能 v0.3
d9cd328 feat: 新增刪除記錄功能 v0.2
f2b81fb docs: 新增 Git 學習筆記 階段0 & 階段1
0a88c95 feat: 建立記帳軟體基本架構
```

---

### 方式一｜查看舊版本（安全，不影響現在版本）

```bash
# 切換到指定版本查看
git checkout 0a88c95

# 看完後回到最新版
git checkout main
```

> ✅ 這個操作完全安全，只是「時光旅行」去看看，不會改變任何東西。
> 回到 main 後一切恢復正常。

---

### 方式二｜撤銷指定版本（建立新 commit 來反轉）

```bash
git revert bbff19e
```

> 💡 **revert 的特點：**
> - 不會刪除歷史記錄
> - 建立一個新的 commit 來「撤銷」指定版本的變更
> - 是最安全的退版方式，適合已經 push 到 GitHub 的版本

---

### 進退版方式比較

| 方式 | 指令 | 適合情境 | 會改變歷史？|
|------|------|------|------|
| 查看舊版 | `git checkout <hash>` | 只是想看看舊版長什麼樣 | ❌ 不會 |
| 撤銷版本 | `git revert <hash>` | 想取消某個版本的變更 | ❌ 不會（新增 commit）|

> ⚠️ **Git 最重要的保證：**
> 只要 commit 過，任何版本都找得回來，永遠不怕改壞！

---

## 🔄 常用指令速查

```bash
git log --oneline          # 查看版本歷史（簡潔版）
git log                    # 查看版本歷史（完整版）
git checkout <hash>        # 切換到指定版本查看
git checkout main          # 回到最新版本
git revert <hash>          # 撤銷指定版本（安全退版）
git status                 # 查看目前狀態
git diff                   # 查看尚未 commit 的變更內容
```

---

## ✅ 階段 3 完成確認

- [x] v0.2 刪除記錄功能 commit + push
- [x] v0.3 分類統計功能 commit + push
- [x] v0.4 存檔／讀檔功能 commit + push
- [x] 建立 `.gitignore` 排除 `records.json`
- [x] GitHub 確認共 6 個 Commits
- [x] 理解進退版操作（checkout / revert）

---

## 🔗 相關筆記
- [[Git學習筆記_階段2-上傳GitHub]]
- [[Git學習筆記_階段4-Clone與Pull]]
