# Git 學習筆記｜階段 2 — 上傳至 GitHub（Push）

#git #github #學習筆記

> 📅 日期：2026-07-21
> 🎯 目標：將本地專案連結到 GitHub 遠端倉庫，並完成第一次上傳

---

## 📌 本階段重點觀念

### 本地 vs 遠端的關係

```
本地電腦                        GitHub 雲端
E:\Bookkeeping\    ←→    github.com/cougar0531/Bookkeeping
  （local repo）   push        （remote repo）
                   pull
```

> **Push** = 本地 → 雲端（上傳）
> **Pull** = 雲端 → 本地（下載同步）

### origin 是什麼？
`origin` 是遠端倉庫的「暱稱」，用來代替那串很長的 GitHub 網址。
這是業界約定俗成的命名，建議保持使用 `origin`。

---

## 專案資訊

| 項目 | 內容 |
|------|------|
| GitHub 帳號 | cougar0531 |
| Repository 名稱 | Bookkeeping |
| 遠端網址 | `https://github.com/cougar0531/Bookkeeping.git` |
| 第三個 commit hash | `f2b81fb` |

---

## 步驟 2-1｜在 GitHub 建立新的 Repository

### 操作步驟
1. 登入 GitHub → 右上角 **`+`** → **New repository**
2. 填寫資訊：

| 欄位 | 填寫內容 |
|------|------|
| Repository name | `Bookkeeping` |
| Description | `Python 記帳軟體 Git 練習專案`（選填）|
| Public / Private | **Public** |
| Initialize options | ⚠️ **全部不勾選** |

3. 點 **Create repository**

> ⚠️ **為什麼初始化選項全部不勾選？**
> 本地已有 commit 歷史，若 GitHub 也自動產生檔案（README、.gitignore），
> 兩邊版本會衝突，導致 push 失敗。
> 原則：**本地已有內容 → GitHub 建空的 repo**

---

## 步驟 2-2｜連結本地專案到遠端 repo

### 指令
```bash
git remote add origin https://github.com/cougar0531/Bookkeeping.git
```

### 確認連結成功
```bash
git remote -v
```

### 預期輸出
```
origin  https://github.com/cougar0531/Bookkeeping.git (fetch)
origin  https://github.com/cougar0531/Bookkeeping.git (push)
```

> 💡 **fetch 和 push 各是什麼？**
> - `fetch`：從遠端下載資料用的網址
> - `push`：上傳資料到遠端用的網址
> 通常兩個網址一樣，代表同一個 repo 負責讀寫。

---

## 步驟 2-3｜第一次 Push 上傳

### 指令
```bash
git push -u origin main
```

### 參數說明

| 參數 | 意思 |
|------|------|
| `push` | 把本地 commit 推送到遠端 |
| `-u` | 設定預設推送目標（只有**第一次**需要加）|
| `origin` | 遠端倉庫暱稱 |
| `main` | 要推送的分支名稱 |

> ✅ **設定 `-u` 之後的好處：**
> 之後每次推送只需要輸入 `git push`，不用再加 `origin main`

### 預期輸出
```
info: please complete authentication in your browser...
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 16 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 5.97 KiB | 2.98 MiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/cougar0531/Bookkeeping.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

### 解讀輸出

| 片段 | 意思 |
|------|------|
| `Counting objects: 100% (12/12)` | 本地共 12 個物件準備上傳 |
| `Writing objects: 100% (12/12), 5.97 KiB` | 全部上傳完成 |
| `* [new branch] main -> main` | 在 GitHub 建立了 main 分支 |
| `branch 'main' set up to track 'origin/main'` | 本地 main 已追蹤遠端 main |

---

## 步驟 2-4｜GitHub 身份驗證

第一次 push 時，瀏覽器會自動開啟 GitHub 授權頁面：

```
Authorize Git Credential Manager
```

點擊 **「Authorize git-ecosystem」** 綠色按鈕即可。

> 💡 **這是什麼？**
> Git Credential Manager 是 Git for Windows 內建的憑證管理工具，
> 讓你不需要每次 push 都輸入帳號密碼。
> 授權一次後，憑證會安全地儲存在 Windows 憑證管理員裡。

授權成功後瀏覽器顯示：
```
Authentication Succeeded
You may now close this tab and return to the application.
```

---

## 🔄 日常 Push 工作流程

設定好 `-u` 之後，之後每次更新只需要：

```bash
git add .
git commit -m "你的 commit message"
git push
```

---

## 常用指令速查

```bash
git remote add origin <網址>   # 連結遠端倉庫
git remote -v                  # 查看遠端連結
git push -u origin main        # 第一次推送（設定預設目標）
git push                       # 之後的推送（簡化版）
```

---

## ✅ 階段 2 完成確認

- [x] GitHub 建立 Bookkeeping Repository（Public、空的）
- [x] `git remote add origin` 連結遠端
- [x] `git remote -v` 確認連結正確
- [x] `git push -u origin main` 第一次上傳
- [x] GitHub 身份驗證成功
- [x] GitHub 頁面確認檔案已上傳（2 Commits）

---

## 🔗 相關筆記
- [[Git學習筆記_階段1-第一次Commit]]
- [[Git學習筆記_階段3-功能迭代]]
