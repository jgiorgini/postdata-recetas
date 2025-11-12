# postdata-recetas
Genera las próximas 6 fechas de recetas "postdatadas": siempre en **lunes** y **50–58 días** después de la anterior.

Regla:
- Base = fecha de la última receta (si no se pasa, se usa hoy).
- Cada nueva receta cae en **lunes** y está **entre 50 y 58 días** después de la anterior (se elige el primer lunes que cumpla).

## Uso (CLI Python)
```bash
python postdata.py --base "12/11/2025" --count 6
# o
python postdata.py              # usa la fecha de hoy del sistema
