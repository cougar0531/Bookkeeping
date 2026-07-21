# Git 學習筆記｜階段 0 — 環境準備

#git #github #學習筆記

> 📅 日期：2026-07-21
> 🎯 目標：建立開發環境，讓本地電腦能與 GitHub 溝通

---

## 📌 本階段重點觀念

> **GitHub 是雲端倉庫，Git 是本地的搬運工**
> 兩者缺一不可：Git 負責在本地管理版本，GitHub 負責在雲端儲存與同步。

---

## 🛠️ 環境組合

| 項目 | 選擇 |
|------|------|
| 作業系統 | Windows |
| 程式語言 | Python |
| 編輯器 | VS Code |
| 終端機 | VS Code 內建 Git Bash |
| Git | v2.55.0.windows.3 |
| GitHub 帳號 | Cougar0531 |

---

## 步驟 0-1｜安裝 Git for Windows

### 下載網址
https://git-scm.com/download/win

### 安裝過程注意選項

| 畫面 | 選擇 |
|------|------|
| 選擇預設編輯器 | Use Visual Studio Code as Git's default editor |
| 調整 PATH 環境 | Git from the command line and also from 3rd-party software |
| 預設分支名稱 | Override → 輸入 `main` |
| 其餘選項 | 全部預設 |

> ⚠️ **為什麼分支要設成 `main`？**
> GitHub 現在預設主分支名稱是 `main`，本地與遠端一致，才不會推送時發生衝突。

### 確認安裝成功
```bash
git --version
# 預期輸出：git version 2.55.0.windows.3
```

---

## 步驟 0-2｜切換 VS Code 終端機為 Git Bash

### 操作方法
1. 按 `Ctrl + Shift + P` 開啟命令面板
2. 輸入：`Terminal: Select Default Profile`
3. 選擇 **Git Bash**

### 確認成功的標誌
終端機提示符號變成：
```
User@DESKTOP-XXXXXX MINGW64 ~
$
```
看到 `MINGW64` 就代表已切換成 Git Bash ✅

---

## 步驟 0-3｜設定 Git 使用者資訊

### 指令
```bash
git config --global user.name "你的名字"
git config --global user.email "你的GitHub信箱"
```

### 確認設定
```bash
git config --global --list
```

### 預期輸出
```
core.editor=... VS Code ...
user.name=Cougar0531
user.email=cougarpeng@gmail.com
```

> ⚠️ **為什麼 Email 要和 GitHub 一致？**
> 每次 commit 都會記錄這個 Email，GitHub 靠它來辨識是哪個帳號提交的。
> Email 不一致的話，commit 紀錄在 GitHub 上不會顯示你的頭像和帳號。

---

## ✅ 階段 0 完成確認

- [x] Git 安裝完成
- [x] VS Code 終端機切換為 Git Bash
- [x] user.name 設定完成
- [x] user.email 設定完成
- [x] Git 預設編輯器設為 VS Code

---

## 🔗 相關筆記
- [[Git學習筆記_階段1-第一次Commit]]
- [[Git學習筆記_階段2-上傳GitHub]]
