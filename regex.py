import re

names = re.compile(r'^(\d+.{2})?([А-ЯЁ]+\s[а-яёА-ЯЁ]+)')
header = re.compile(r'([а-яА-ЯёЁ]+\s\(\d{2}-\d{2}\s[а-я]{3,}\))')
dist = re.compile(r'(\d{2,3}m)')
dist_time = re.compile(r'(\d{2,3}m):\s([0-9:.]+)\s([0-9:.]+)')
