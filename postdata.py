
---

# postdata.py
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from datetime import datetime, timedelta, date
import sys

AR_TZ = "America/Argentina/Buenos_Aires"  # referencia informativa

ACCEPTED_FMT = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"]

def parse_date(s: str) -> date:
    for fmt in ACCEPTED_FMT:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    raise ValueError(f"Formato de fecha no reconocido: {s}. Usa DD/MM/YYYY, YYYY-MM-DD o DD-MM-YYYY.")

def find_monday_in_window(start: date, days_min=50, days_max=58) -> date | None:
    # Busca el primer lunes entre +50 y +58 días
    for delta in range(days_min, days_max + 1):
        candidate = start + timedelta(days=delta)
        if candidate.weekday() == 0:  # 0 = lunes
            return candidate
    return None

def generate_postdated(base: date, count: int = 6) -> list[date]:
    out = []
    prev = base
    for _ in range(count):
        nxt = find_monday_in_window(prev, 50, 58)
        if nxt is None:
            raise RuntimeError(
                f"No se encontró un lunes entre 50–58 días después de {prev.strftime('%d/%m/%Y')}."
            )
        out.append(nxt)
        prev = nxt
    return out

def main():
    parser = argparse.ArgumentParser(
        description="Genera fechas de recetas postdatadas (lunes, 50–58 días entre sí)."
    )
    parser.add_argument("--base", type=str, default=None,
                        help="Fecha base (DD/MM/YYYY, YYYY-MM-DD o DD-MM-YYYY). Si no se indica, se usa hoy.")
    parser.add_argument("--count", type=int, default=6, help="Cantidad de recetas a generar (default: 6).")
    args = parser.parse_args()

    try:
        base = parse_date(args.base) if args.base else date.today()
        dates = generate_postdated(base, args.count)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Salida en formato DD/MM/YYYY
    for i, d in enumerate(dates, 1):
        print(f"{i}) {d.strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()
