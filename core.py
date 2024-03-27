import pandas as pd

class Database:
    def __init__(self) -> None:
        self.conn = None
        self.dbname = ''
        
    def raw_sql(self, sql_str:str, *args, **kwargs) -> pd.DataFrame:
        raise NotImplementedError('raw_sql is not yet implemented')
        # to be implemented in the the class that inheritates this class
        return pd.DataFrame()


if __name__ == '__main__':
   pass
