from pydantic import BaseModel

class NFL(BaseModel):
    Age: float 
    G: float 
    GS: float 
    Cmp: float 
    Att: float 
    CmpPercent: float 
    Yds: float 
    TD: float 
    TDPercent: float 
    Int: float 
    IntPercent: float 
    FirstDown: float 
    Lng: float 
    YPerA: float 
    AYPerA: float 
    YPerC: float 
    YPerG: float 
    Sk: float 
    YdsPerSk: float 
    SkPercent: float 
    NYPerA: float 
    ANYPerA: float
