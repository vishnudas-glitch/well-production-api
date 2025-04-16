import pandas as pd
import sqlite3

def load_excel_to_sqlite(excel_file: str,db_name:str,table_name:str):
    try:
        df = pd.read_excel(excel_file)
        
        annual_totals = df.groupby(
            ['API WELL  NUMBER', 'Production Year', 'OWNER NAME']
        )[['OIL', 'GAS', 'BRINE', 'DAYS']].sum().reset_index()
        
        quarter_counts = df.groupby(
            ['API WELL  NUMBER', 'Production Year']
        ).size().reset_index(name='NUM QUARTERS')
        
        final_df = pd.merge(
            annual_totals, quarter_counts,
            on=['API WELL  NUMBER', 'Production Year']
        )

        print(final_df.head())

        save_to_sqlite(final_df, db_name=db_name, table_name=table_name)

        return final_df

    except Exception as e:
        print(f"Error: {e}")
        return False


def save_to_sqlite(df: pd.DataFrame, db_name: str, table_name: str):
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
    except Exception as e:
        print(f"Failed to save data to SQLite: {e}")


if __name__ == "__main__":
    excel_file = 'scripts/well_prod_data.xls'
    load_excel_to_sqlite(excel_file=excel_file,db_name="ohio.db", table_name="well_production")
