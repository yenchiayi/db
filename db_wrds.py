import pandas as pd  
import db.core as core
import wrds
conn_wrds = wrds.Connection()

class Database(core.Database):
    def __init__(self) -> None:
        super().__init__()
        self.conn = conn_wrds

    def raw_sql(self, sql_str:str, *args, **kwargs) -> pd.DataFrame:
        df = self.conn.raw_sql(sql_str)    
        return df

class CRSPMF(Database):
    dbname = 'crsp_q_mutualfunds'
    def __init__(self) -> None:
        super(CRSPMF, self).__init__()
        self.dbname = CRSPMF.dbname

crsp_mf = CRSPMF()

if __name__ == '__main__':
    res = crsp_mf.raw_sql('select * from crsp.monthly_returns limit 1')
    print(res)

    