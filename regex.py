import re

names = re.compile(r'^(\d+.{2})?([А-ЯЁ]+\s[а-яёА-ЯЁ]+)')
dist = re.compile(r'(\d{2,3}m)')
dist_time = re.compile(r'(\d{2,3}m):\s([0-9:.]+)\s([0-9:.]+)')
dist_50 = re.compile(r'(\d?:?\d{2}\.\d{1,2})')
