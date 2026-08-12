# nsysu-math524

中山大學 **MATH 524 統計學習與資料探勘（Statistical Learning and Data Mining）** Fall 2026 課程網站，採 Jekyll + GitHub Pages 部署。

- **線上站台：** <https://phonchi.github.io/nsysu-math524/>
- **授課教師：** 鍾思齊（理 SC 2002-4）
- **助教：** 張朔祐、陳任泯
- **教科書：** [An Introduction to Statistical Learning with Applications in Python](https://www.statlearning.com/)（ISLP，James / Witten / Hastie / Tibshirani / Taylor）
- **互動自學網站：** <https://phonchi.github.io/statlearning-selfstudy/>
- **歷年封存：** [Fall 2025](https://github.com/phonchi/nsysu-math524-2025) ｜ [Fall 2023](https://github.com/phonchi/nsysu-math524-2023) ｜ [Fall 2022](https://github.com/phonchi/nsysu-math524-2022) ｜ [Fall 2021](https://github.com/phonchi/nsysu-math524-2021)

---

## 資料夾結構（實際內容）

```
.
├── _config.yml              # Jekyll 設定，含課程名稱 / baseurl=/nsysu-math524 / Fall 2026
├── Gemfile, Gemfile.lock    # Ruby 依賴：minima 2.5 + github-pages gem + jekyll-feed
├── LICENSE                  # 沿用模板的 LICENSE
│
├── index.md                 # 首頁（layout: home），含 FB 社團 / Office hour / TA hour
├── lectures.md              # /lectures/ 列表頁
├── assignments.md           # /assignments/ 列表頁
├── schedule.md              # /schedule/ 自動生成課表
├── materials.md             # 自學網站、教科書、MOOC、學習資源、套件清單
├── project.md               # 期末專題（目前未掛在 nav 上）
│
├── _lectures/               # 每週講義 markdown（一檔 = 一筆 lecture frontmatter）
│   └── d                    # 佔位檔；換學期時清空本目錄，只留這一個
│
├── _assignments/            # 作業 / Quiz
│   └── a                    # 佔位檔；同上
│
├── _events/                 # 額外事件（exam / due / raw_event）
│   ├── exam2.md             # 期中考範本，front matter 目前用 <!--- ---> 註解掉
│   ├── sample_exam_due.md   # 同上
│   └── sample_raw_event.md  # 同上
│
├── _announcements/          # 公告 collection（目前兩個檔都是空的）
│
├── _data/
│   ├── nav.yml              # 上方 nav: Home / Schedule / Lectures / Assignments / Materials
│   ├── people.yml           # 講師 + 助教資料
│   ├── hw_policy.yml        # 作業繳交規定，顯示在每一頁作業上
│   ├── late_policy.yml      # 遲交政策（8 late days）
│   └── previous_offering.yml # 首頁「Previous Offerings」的歷年封存連結
│
├── _layouts/                # default / home / page / post / lectures / assignments /
│                            # assignment / class / event / schedule
├── _includes/               # nav / header / footer / head / announcements / image /
│                            # embedpdf / exam_policy / hw_policy / late_policy /
│                            # lecture_links / schedule_row_{lecture,assignment,due,exam,raw_event}
├── _sass/                   # 7 個樣式 partial：_base / _header / _layout /
│                            # _mobile-header / _syntax-highlighting / _user_vars / _fancy-image
├── _css/main.scss           # 整合 _sass partial 的入口
│
├── _images/                 # cover2 / home_page / logo / pattern / schedule_page
│   ├── pp/                  # 講師 + TA 大頭照（avatar.png 為預設）
│   └── screenshots/         # 模板 README 用的截圖
│
└── static_files/
    ├── presentations/       # 11 份章節投影片 PDF（01_Introduction … 09_Support_Vector_Machines、
    │                        #   12_Unsupervised_learning、01-06_Recap）
    │                        # 11 個 ISLP 中文版 lab notebook（Ch01 … Ch12-*-lab-zh.ipynb）
    │                        # Final_Project.pdf / Final_Group.pdf
    │                        # Mid_term_2020~2023.zip（歷年期中考）
    │                        # packages.txt（★ 勿刪，封存站的 PDF 內嵌連結指向它）
    └── assignments/         # 作業資料集 Auto.csv / College.csv / Data1.csv
                             # 作業 notebook 換學期時清空，只留 a 佔位檔
```

---

## 站台部署

走 GitHub Pages，push 到 `main` 後 Pages 會自動 build。

`_config.yml` 關鍵設定：

| 欄位 | 值 |
|---|---|
| `baseurl` | `/nsysu-math524` |
| `url` | `https://phonchi.github.io` |
| `course_name` | Statistical Learning and Data Mining |
| `course_semester` | Fall 2026 |
| `schoolname` | National Sun Yat-Sen University |
| `markdown` | kramdown |
| `permalink` | `blog/:year/:month/:title` |
| `collections` | `events` / `lectures` / `assignments` / `announcements`（皆 `output: true`） |

### 本機預覽

需要 Ruby + Bundler：

```bash
bundle install
bundle exec jekyll serve
```

開瀏覽器到 `http://localhost:4000/nsysu-math524/`。

---

## 新增 / 修改內容

### 新增講義（lecture）

在 `_lectures/` 建一個 `.md`：

```yaml
---
type: lecture
date: 2026-MM-DD
title: <Lecture title>
hide_from_announcments: true
links:
    - url: /static_files/presentations/<file>.pdf
      name: Slides
---
**Suggested Readings:**
- [Lab](https://github.com/phonchi/nsysu-math524/blob/main/static_files/presentations/<file>-lab-zh.ipynb)
- Textbook Chapter ?
- [[Recorded video]](<youtube-playlist>)
```

`links:` 的 `url` **寫成不含 baseurl 的站內絕對路徑**，`_includes/lecture_links.html` 會用 `| prepend: site.baseurl` 補上前綴。`links:` 留空不會出錯。

### 新增作業（assignment）

在 `_assignments/`：

```yaml
---
type: assignment
date: 2026-MM-DDT15:10:00
title: 'Assignment #N'
attachment:
due_event:
    type: due
    date: 2026-MM-DDT23:59:00
    description: 'Assignment #N due'
---
```

> ⚠️ **`due_event` 是必填，漏掉會讓整個站建置失敗。**
> `_layouts/schedule.html` 對 `site.assignments | map: "due_event"` 取值，少一個就會產生 nil，
> `{% include schedule_row_{{ event.type }}.html %}` 解析成不存在的 `schedule_row_.html`，Jekyll 直接中止。
> 同理，`_lectures` / `_assignments` 底下的檔案要嘛有完整 front matter、要嘛完全沒有 front matter
> （像 `d` / `a` 那樣被當成 static file），**不要留只有空 `---` 區塊的半殘檔案**。

### 新增事件（exam / due / raw_event）

在 `_events/`：

```yaml
---
type: exam      # 或 due / raw_event
date: 2026-MM-DDT09:10:00
description: 'Midterm'
hide_from_announcments: true
---
```

暫時不要顯示某筆事件時，把整個 front matter 用 `<!--- ... --->` 包起來即可（現有三個檔都是這個狀態）。

### 修改 navigation / 講師資料 / 各種政策

- 上方選單：`_data/nav.yml`
- 講師 / TA：`_data/people.yml`（圖片放 `_images/pp/`）
- 作業繳交規定：`_data/hw_policy.yml`（經 `_layouts/assignment.html` 顯示在每頁作業）
- 遲交政策：`_data/late_policy.yml`
- 歷年封存連結：`_data/previous_offering.yml`

### 修改頁面文字

- 首頁：`index.md`（FB 社團 / Office hour / TA hour）
- Materials 推薦資源：`materials.md`
- Lectures / Assignments / Schedule / Project 標題與引言：對應 `*.md`

---

## 換學期 checklist

1. 把上一學期的站台複製成封存 repo `nsysu-math524-<年>`，改它的 `baseurl`，並把裡面所有硬寫的
   `phonchi/nsysu-math524` 網址改指封存 repo 自己（notebook 的 Colab / Kaggle 徽章、
   `_lectures` 裡繞過 baseurl 的絕對路徑都要改）。**改 `.ipynb` 要用 bytes 讀寫**，
   Python text mode 的 universal newlines 會把 CRLF 正規化、等於整份檔案被改寫。
2. `_data/previous_offering.yml` 最上方加上剛封存的那一期（由新到舊，url 用 GitHub Pages 網址）。
3. 清空 `_lectures/*.md` 與 `_assignments/*.md`，各留 `d` / `a` 佔位檔（**不要**給它們 front matter）。
4. 刪掉 `static_files/assignments/` 的作業 notebook 與解答，留 `a` 佔位檔。
5. `_events/` 裡上學期的考試把 front matter 用 `<!--- --->` 包起來停用。
6. `_config.yml` 的 `course_semester` 換成新學期。
7. `_data/people.yml` 換助教；`index.md` 的 Office hour / TA hour 一併更新。
8. `_data/hw_policy.yml` 的中山網路大學連結換成新學期的課程編號。

---

## 模板出處

本站台模板源自 [kazemnejad/jekyll-course-website-template](https://github.com/kazemnejad/jekyll-course-website-template)（原作再 fork 自 [svmiller/course-website](https://github.com/svmiller/course-website)）。
