# Git 學習筆記｜階段 1 — 建立專案 ＋ 第一次 Commit

#git #github #學習筆記

> 📅 日期：2026-07-21
> 🎯 目標：理解「版本快照」的概念，學習 git init → git add → git commit 三步驟

---

## 📌 本階段重點觀念

### 什麼是 Commit？
> Commit 就是幫專案拍一張「版本快照」。
> 每次 commit 都會記錄：**誰、在什麼時候、改了什麼**。
> 未來任何時候都可以回到這個快照的狀態。

### Git 的三個區域

```
工作目錄          暫存區             本地倉庫
(Working Dir) → (Staging Area) → (Repository)
     │                │                │
  你寫的檔案      git add 後       git commit 後
                  等待提交          正式存檔
```

---

## 專案資訊

| 項目 | 內容 |
|------|------|
| 本地路徑 | `E:\Bookkeeping` |
| 主程式 | `bookkeeping.py` |
| 第一個 commit hash | `0a88c95` |

---

## 步驟 1-1｜初始化 Git 專案

### 指令
```bash
git init
```

### 預期輸出
```
Initialized empty Git repository in E:/Bookkeeping/.git/
```

### 這個指令做了什麼？
在專案資料夾裡建立一個隱藏的 `.git` 資料夾，這是 Git 用來記錄所有版本歷史的地方。

> ⚠️ **注意：**
> - `git init` 只需要執行**一次**
> - 不要刪除 `.git` 資料夾，刪掉就等於清除所有版本歷史

---

## 步驟 1-2｜建立第一個 Python 檔案

### 用 VS Code 開啟專案資料夾
```bash
code .
```
> `code .` 的意思是：用 VS Code 開啟「目前這個資料夾（`.`）」

### 建立 `bookkeeping.py`
在 VS Code 左側檔案總管新增檔案，貼上基本架構程式碼後 `Ctrl + S` 儲存。

---

## 步驟 1-3｜第一次 git add + git commit

### 完整流程

#### ① 查看目前狀態
```bash
git status
```
- 紅色檔名 = **Untracked**（Git 看到但還沒追蹤）
- 綠色檔名 = **Staged**（已加入暫存區，準備 commit）

#### ② 將檔案加入暫存區
```bash
git add bookkeeping.py
```
或加入全部檔案：
```bash
git add .
```

#### ③ 執行 commit
```bash
git commit -m "feat: 建立記帳軟體基本架構"
```

### 預期輸出
```
[main (root-commit) 0a88c95] feat: 建立記帳軟體基本架構
 1 file changed, 34 insertions(+)
 create mode 100644 bookkeeping.py
```

### 解讀輸出

| 片段 | 意思 |
|------|------|
| `main` | 目前所在的分支名稱 |
| `root-commit` | 這是專案的**第一個** commit |
| `0a88c95` | 這個版本的唯一識別碼（commit hash）|
| `1 file changed, 34 insertions(+)` | 新增 1 個檔案，共 34 行程式碼 |

---

## 📝 Commit Message 寫法慣例

良好的 commit message 格式：
```
類型: 簡短說明做了什麼
```

| 類型 | 用途 |
|------|------|
| `feat` | 新增功能 |
| `fix` | 修復 bug |
| `docs` | 更新文件或筆記 |
| `refactor` | 重構程式碼（不影響功能）|
| `chore` | 雜項（更新設定檔等）|

> 💡 **養成寫清楚 commit message 的習慣**
> 這是留給未來的自己（或團隊成員）看的版本記錄，
> 三個月後回來看 "修改了一些東西" 完全不知道改了什麼！

---

## 🔄 常用指令速查

```bash
git status          # 查看目前狀態
git add <檔案>      # 將指定檔案加入暫存區
git add .           # 將所有變更加入暫存區
git commit -m "訊息" # 提交版本快照
git log             # 查看 commit 歷史記錄
```

---

## ✅ 階段 1 完成確認

- [x] `git init` 初始化專案
- [x] 建立 `bookkeeping.py`
- [x] `git add` 加入追蹤
- [x] 第一次 `git commit` 成功（hash: `0a88c95`）

---

## 🔗 相關筆記
- [[Git學習筆記_階段0-環境準備]]
- [[Git學習筆記_階段2-上傳GitHub]]
