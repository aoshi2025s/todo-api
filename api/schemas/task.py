from pydantic import BaseModel,Field

#BaseModelはfastapiのスキーマモデルを表す

class TaskBase(BaseModel):
    title: str or None = Field(None,exmaple="ゴミ捨てに行く")

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

    class Config:
        from_attributes = True
