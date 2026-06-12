import sys, os

SCRIPTS_DIR = "/home/user/git_practice/vedic-astro-skills/claude-code/skills/vedic-calculator/scripts"
sys.path.insert(0, SCRIPTS_DIR)

from engine import calculate_full_chart
from transit import calc_transit
from formatter import format_structured_data

chart = calculate_full_chart(
    year=1993, month=5, day=29,
    hour=16, minute=42,
    lat=39.9042, lon=116.4074,
    tz_str="Asia/Shanghai"
)

transit = calc_transit(
    chart['lagna']['sign_idx'],
    chart['planets']['Moon']['sign_idx'],
    "Asia/Shanghai"
)

meta = {
    'dob': '1993-05-29',
    'time': '16:42',
    'place': '北京',
    'lat': 39.9042, 'lon': 116.4074,
    'time_precision': '精确到分钟',
    'time_source': '未追问'
}

user_info = {
    'gender': '未知',
    'relationship': '未知'
}

md = format_structured_data(chart, transit, meta, user_info)
with open('/home/user/git_practice/structured_data.md', 'w', encoding='utf-8') as f:
    f.write(md)

SIGNS = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']
sav_total = sum(chart['sav'].get(s, 0) for s in SIGNS)
print(f"SAV total: {sav_total}")
assert sav_total == 337, f"SAV FAILED: {sav_total} != 337"
print("排盘完成，structured_data.md 已生成")
