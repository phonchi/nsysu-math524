"""115 學年度第 1 學期統計學習：期末報告隨機排序（2026-12-24）。

組別依分組表單的登記順序列出，報告順序以固定種子隨機打亂，結果可重現。
每組 15 分鐘（報告 12 分鐘＋Q&A 3 分鐘），第 5 組後下課 10 分鐘。

用法：python final_group_2026.py [輸出.xlsx] [輸出.html]
不給輸出路徑時只印出時間表；.xlsx 需要 openpyxl，.html 可用瀏覽器列印成 PDF。
"""
import random
import sys
from datetime import datetime, timedelta

SEED = 20261224
DATE = "12月24日"
START = "9:10"
SLOT_MIN = 15          # 12 分鐘報告＋3 分鐘 Q&A
BREAK_AFTER = 5        # 第 5 組報告完下課
BREAK_MIN = 10
END_LIMIT = "12:00"

# 登記順序 = 表單列序
GROUPS = [
    ["李昱瑩", "何莉文"],
    ["鄭宗祐", "郭芊妮"],
    ["林振鈺", "謝承哲"],
    ["曾子菱", "張力仁"],
    ["高紹綸", "劉兆涵", "林昱辰"],
    ["郝思嘉", "洪梓毓"],
    ["林宗利", "鄭亘妤"],
    ["葉宇祥", "葉千岱"],
    ["蕭伏廷", "林進暄", "裴韋翔"],
    ["陳偉財", "張文誠"],
]


def hm(t):
    return f"{t.hour}:{t.minute:02d}"


def schedule():
    order = list(range(1, len(GROUPS) + 1))
    random.Random(SEED).shuffle(order)
    t = datetime.strptime(START, "%H:%M")
    rows = []
    for k, reg in enumerate(order, start=1):
        end = t + timedelta(minutes=SLOT_MIN)
        rows.append({"reg": reg, "order": k, "time": f"{hm(t)}~{hm(end)}",
                     "members": GROUPS[reg - 1]})
        t = end
        if k == BREAK_AFTER:
            b_end = t + timedelta(minutes=BREAK_MIN)
            rows.append({"break": f"{hm(t)}~{hm(b_end)}"})
            t = b_end
    assert t <= datetime.strptime(END_LIMIT, "%H:%M"), "超過 12:00"
    names = [n for g in GROUPS for n in g]
    assert len(names) == len(set(names)), "組員重複"
    return rows


def write_xlsx(rows, path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, Side

    wb = Workbook()
    ws = wb.active
    assert ws is not None
    ws.title = "期末報告"
    font = Font(name="Noto Sans CJK TC", size=12)
    bold = Font(name="Noto Sans CJK TC", size=14, bold=True)
    center = Alignment(horizontal="center", vertical="center")
    thin = Side(style="thin")
    box = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.merge_cells("A1:G1")
    ws["A1"] = "115學年度第1學期統計學習　期末報告順序"
    ws["A1"].font, ws["A1"].alignment = bold, center
    header = ["登記順序", "報告順序", "日期", "報告時間", "組員一", "組員二", "組員三"]
    ws.append(header)
    for r in rows:
        if "break" in r:
            ws.append(["", "", "", r["break"], "下課", "", ""])
            ws.merge_cells(start_row=ws.max_row, start_column=5,
                           end_row=ws.max_row, end_column=7)
        else:
            m = r["members"] + [""] * (3 - len(r["members"]))
            ws.append([r["reg"], r["order"], "", r["time"], *m])
    last = ws.max_row
    ws["C3"] = DATE
    ws.merge_cells(start_row=3, start_column=3, end_row=last, end_column=3)
    for row in ws.iter_rows(min_row=2, max_row=last, max_col=7):
        for c in row:
            c.font, c.alignment, c.border = font, center, box
    for col, w in zip("ABCDEFG", [11, 11, 12, 15, 12, 12, 12]):
        ws.column_dimensions[col].width = w
    for i in range(1, last + 1):
        ws.row_dimensions[i].height = 26
    ws.page_setup.orientation = "portrait"
    ws.page_setup.fitToWidth = 1
    if ws.sheet_properties.pageSetUpPr is not None:
        ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.horizontalCentered = True
    wb.save(path)


def write_html(rows, path):
    """A4 直式表格，供瀏覽器列印成 PDF。"""
    n = len(rows)
    trs = []
    for i, r in enumerate(rows):
        date = f'<td class="date" rowspan="{n}">{DATE}</td>' if i == 0 else ""
        if "break" in r:
            trs.append(f'<tr class="brk"><td></td><td></td>{date}'
                       f'<td>{r["break"]}</td><td colspan="3">下課</td></tr>')
        else:
            m = r["members"] + [""] * (3 - len(r["members"]))
            cells = "".join(f"<td>{x}</td>" for x in m)
            trs.append(f'<tr><td>{r["reg"]}</td><td>{r["order"]}</td>{date}'
                       f'<td>{r["time"]}</td>{cells}</tr>')
    html = f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<title>期末報告順序</title><style>
@page {{ size: A4 portrait; margin: 18mm 15mm; }}
body {{ font-family: "Noto Sans CJK TC", "Microsoft JhengHei", sans-serif; margin: 0; }}
h1 {{ font-size: 18pt; text-align: center; margin: 0 0 4mm; }}
p {{ font-size: 10.5pt; text-align: center; margin: 0 0 6mm; color: #333; }}
table {{ border-collapse: collapse; width: 99%; margin: 0 auto; table-layout: fixed; font-size: 12pt; }}
th, td {{ border: 1px solid #000; text-align: center; padding: 3.2mm 1mm; }}
th {{ background: #e8e8e8; }}
.date {{ font-weight: bold; }}
.brk td {{ background: #f3f3f3; color: #444; }}
</style></head><body>
<h1>115學年度第1學期統計學習　期末報告順序</h1>
<p>每組 {SLOT_MIN} 分鐘（報告 12 分鐘＋Q&amp;A 3 分鐘）；報告順序以固定種子 {SEED} 隨機產生</p>
<table><colgroup><col style="width:12%"><col style="width:12%"><col style="width:13%">
<col style="width:21%"><col style="width:14%"><col style="width:14%"><col style="width:14%"></colgroup><thead><tr><th>登記順序</th><th>報告順序</th><th>日期</th><th>報告時間</th>
<th>組員一</th><th>組員二</th><th>組員三</th></tr></thead><tbody>
{chr(10).join(trs)}
</tbody></table></body></html>
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    rows = schedule()
    for r in rows:
        if "break" in r:
            print(f"        {r['break']:<12} 下課")
        else:
            print(f"{r['reg']:>3} {r['order']:>3}  {r['time']:<12} {'、'.join(r['members'])}")
    for out in sys.argv[1:]:
        (write_html if out.endswith(".html") else write_xlsx)(rows, out)
        print("wrote", out)
