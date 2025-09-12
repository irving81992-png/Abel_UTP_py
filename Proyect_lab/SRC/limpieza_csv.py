import csv, sys, os, glob, statistics, math, json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN_RAW_DIR = ROOT/"DATA"/"RAW"/"datos_sucios_250_v2.csv"
OUT_PROCESSED_DIR=ROOT/"DATA"/"PROCESSED"

with open(IN_RAW_DIR,'r',encoding='utf-8') as f:
     s=f.read()
     print(s)
#BASE = Path(__file__).resolve().parents[1]
# IN_DIR = BASE / "data" / "input"
#OUT_DIR = BASE / "data" / "output"
#OUT_CSV = OUT_DIR / "Temperaturas_Procesado.csv"
#OUT_KPIS_CSV = OUT_DIR / "KPIs.csv"
# OUT_KPIS_JSON = OUT_DIR / "KPIs.json"