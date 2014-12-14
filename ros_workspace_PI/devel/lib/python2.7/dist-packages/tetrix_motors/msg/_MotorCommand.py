"""autogenerated by genpy from tetrix_motors/MotorCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MotorCommand(genpy.Message):
  _md5sum = "831d9cb0d2fac073c1d0cfa479541f07"
  _type = "tetrix_motors/MotorCommand"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 run_time
string[] motor_names
int8[] motor_speeds
int8[] motor_accelerations


"""
  __slots__ = ['run_time','motor_names','motor_speeds','motor_accelerations']
  _slot_types = ['float32','string[]','int8[]','int8[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       run_time,motor_names,motor_speeds,motor_accelerations

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MotorCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.run_time is None:
        self.run_time = 0.
      if self.motor_names is None:
        self.motor_names = []
      if self.motor_speeds is None:
        self.motor_speeds = []
      if self.motor_accelerations is None:
        self.motor_accelerations = []
    else:
      self.run_time = 0.
      self.motor_names = []
      self.motor_speeds = []
      self.motor_accelerations = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_f.pack(self.run_time))
      length = len(self.motor_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.motor_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.motor_speeds)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.motor_speeds))
      length = len(self.motor_accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.motor_accelerations))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.run_time,) = _struct_f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.motor_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.motor_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.motor_speeds = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.motor_accelerations = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_f.pack(self.run_time))
      length = len(self.motor_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.motor_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.motor_speeds)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.motor_speeds.tostring())
      length = len(self.motor_accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.motor_accelerations.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.run_time,) = _struct_f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.motor_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.motor_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.motor_speeds = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.motor_accelerations = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f = struct.Struct("<f")
