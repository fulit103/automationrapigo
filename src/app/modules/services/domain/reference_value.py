class ReferenceValue():

  _reference: str

  def __init__(self, reference: str):
    self.guard(reference)
    self._reference = reference


  def guard(self, reference: str):
    if reference==None or reference=="":
      raise ValueError("reference no puede ser vacía o nula")

  def get(self) -> str:
    return self._reference

  def set(self, reference: str) -> None:
    self.guard(reference)
    self._reference

  def __str__(self) -> str:
    return self._reference