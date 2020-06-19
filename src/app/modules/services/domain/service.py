from .reference_value import ReferenceValue

class Service():
  
  pagado: bool

  def __init__(self, reference: ReferenceValue):
    self.reference = reference