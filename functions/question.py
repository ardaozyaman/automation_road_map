class Question:

  def __init__(self, ID: int, answerFunc: callable):
   self.ID = ID
   self._answerFunc = answerFunc
   self._description = "not filled"

  def getAnswerFunc(self):
   return self._answerFunc

  def setAnswerFunc(self, answerFunc : callable):
    self._answerFunc = answerFunc

  def setDescription(self,description:str):
    self._description = description
  
  def getDescription(self):
    return self._description


