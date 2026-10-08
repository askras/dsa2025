"""
Удаление столбца full_name из CSV-файла.

Использование:
    python clear_pd.py <исходный.csv> <новый.csv>
"""
import argparse
import sys
from pathlib import Path

import pandas as pd


def drop_full_name(df: pd.DataFrame) -> pd.DataFrame:
    """Удаляет столбец full_name (без учёта регистра и пробелов)."""
    for col in df.columns:
        if str(col).strip().lower() == "full_name":
            return df.drop(columns=[col])
    return df


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Читает CSV, удаляет столбец full_name и записывает новый файл."
    )
    parser.add_argument("src", help="Путь к исходному CSV-файлу.")
    parser.add_argument("dst", help="Путь к выходному CSV-файлу.")
    args = parser.parse_args()

    src = Path(args.src)
    dst = Path(args.dst)

    if not src.exists():
        print(f"❌ Файл {src} не найден.")
        sys.exit(1)

    df = pd.read_csv(src, encoding="utf-8-sig")
    n_cols_before = df.shape[1]
    df_out = drop_full_name(df)
    n_removed = n_cols_before - df_out.shape[1]

    df_out.to_csv(dst, index=False, encoding="utf-8")

    print(f"📂 Исходный файл: {src}")
    print(f"👥 Строк: {len(df)}")
    print(f"🗑  Удалено столбцов «full_name»: {n_removed}")
    if n_removed == 0:
        print("⚠️  Столбец 'full_name' в файле отсутствует — записана копия без изменений.")
    print(f"✅ Результат сохранён в {dst}")


if __name__ == "__main__":
    main()
