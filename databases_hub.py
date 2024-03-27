import db.db_wrds as db_wrds
from dataclasses import dataclass, fields

@dataclass(frozen=True)
class DataBaseHub:
    CRSPMF: object = db_wrds.crsp_mf

    @classmethod
    def list_all_databases(cls):
        return list(map(lambda x: x.name, fields(DB_HUB)))

dbs_hub = DataBaseHub()

if __name__ == '__main__':
    print(dbs_hub.list_all_databases())

    res = dbs_hub.CRSPMF.raw_sql('select * from crsp.monthly_returns limit 1')
    print(res)
    




    
