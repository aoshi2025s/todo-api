from pydantic import BaseModel,Field
import datetime


#BaseModelはfastapiのスキーマモデルを表す

class TaskBase(BaseModel):
    title: str or None = Field(None,exmaple="ゴミ捨てに行く")
    due_date: datetime.date or None = Field(None,exmaple="2024-12-01")

class Task(TaskBase):
    id: int
    #TaskBaseでTaskとTaskCreateの共通項を抽象
    #title: str or None = Field(None,example="ゴミ捨てに行く")
    done: bool = Field(False,description="完了フラグ")

    class Config: #DB操作で使用
        from_attributes = True
        #orm_mode = Trueだとhas been renamedっていうメッセージでる

class TaskCreate(TaskBase):
    #TaskBaseに抽象
    #title: str or None = Field(None,example="ゴミ捨てに行く")
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    #orm_mode=TrueはTaskCreateResponseがDBモデルのオブジェクトを受け取り、
    #レスポンススキーマに変換
    class Config:
        from_attributes = True
