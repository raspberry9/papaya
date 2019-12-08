# automatically generated by the propy compiler, do not modify

# version [abc1234]
# namespace [Proto]
# md5sum [f16d695ea2d031fec7ad1283b73d84c3]

import datetime
import struct
from collections import namedtuple
from collections import OrderedDict

LoginChannel = namedtuple('LoginChannel', ('Guest', 'Google', 'GameCenter', 'Facebook'))._make((0, 1, 2, 3))


class ReqLogin(object):
    __struct_id__ = 1

    def __init__(self, user_id, password, channel):
        self.user_id = user_id
        self.password = password
        self.channel = channel

    def _asdict(self):
        return OrderedDict(
            user_id=self.user_id,
            password=self.password,
            channel=self.channel
        )

    def _asbytes(self):
        data = b''
        data += struct.pack('B', self.channel)
        _data = self.user_id.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        _data = self.password.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        return data

    @classmethod
    def _frombytes(cls, buf):
        _offset = 0
        _channel = struct.unpack('B', buf[_offset:_offset+1])[0]; _offset += 1
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _user_id = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _password = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        return cls(
            user_id=_user_id,
            password=_password,
            channel=_channel
        )


class User(object):
    __struct_id__ = 2

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def _asdict(self):
        return OrderedDict(
            user_id=self.user_id,
            user_name=self.user_name
        )

    def _asbytes(self):
        data = b''
        _data = self.user_id.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        _data = self.user_name.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        return data

    @classmethod
    def _frombytes(cls, buf):
        _offset = 0
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _user_id = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _user_name = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        return cls(
            user_id=_user_id,
            user_name=_user_name
        )


class ResLogin(User):
    __struct_id__ = 3

    def __init__(self, user_id, user_name, token, channel, friend, friends, values, created_at, last_login):
        super(ResLogin, self).__init__(user_id, user_name)
        self.token = token
        self.channel = channel
        self.friend = friend
        self.friends = friends or []
        self.values = values or []
        self.created_at = created_at
        self.last_login = last_login

    def _asdict(self):
        return OrderedDict(
            user_id=self.user_id,
            user_name=self.user_name,
            token=self.token,
            channel=self.channel,
            friend=self.friend._asdict(),
            friends=[_x._asdict() for _x in self.friends],
            values=self.values,
            created_at=self.created_at,
            last_login=self.last_login
        )

    def _asbytes(self):
        data = b''
        data += struct.pack('B', self.channel)
        _data = self.user_id.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        _data = self.user_name.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        _data = self.token.encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        _data = self.friend._asbytes()
        data += struct.pack('H', len(_data))
        data += _data
        data += struct.pack('H', len(self.friends))
        for _x in self.friends:
            _data = _x._asbytes()
            data += struct.pack('H', len(_data))
            data += _data
        data += struct.pack('H', len(self.values))
        for _x in self.values:
            data += struct.pack('q', _x)
        _data = self.created_at.isoformat().encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        _data = self.last_login.isoformat().encode('ASCII')
        data += struct.pack('H', len(_data))
        data += _data
        return data

    @classmethod
    def _frombytes(cls, buf):
        _offset = 0
        _channel = struct.unpack('B', buf[_offset:_offset+1])[0]; _offset += 1
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _user_id = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _user_name = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _token = str(buf[_offset:_offset+_len].decode('ASCII')); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _friend = User._frombytes(buf[_offset:_offset+_len]); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _friends = []
        for _ in range(_len):
            _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
            _friends.append(User._frombytes(buf[_offset:_offset+_len]));_offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _values = []
        for _ in range(_len):
            _values.append(struct.unpack('q', buf[_offset:_offset+8])[0]);_offset += 8
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _created_at = datetime.datetime.strptime(str(buf[_offset:_offset+_len].decode('ASCII')), '%Y-%m-%dT%H:%M:%S.%f'); _offset += _len
        _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
        _last_login = datetime.datetime.strptime(str(buf[_offset:_offset+_len].decode('ASCII')), '%Y-%m-%d').date(); _offset += _len
        return cls(
            user_id=_user_id,
            user_name=_user_name,
            token=_token,
            channel=_channel,
            friend=_friend,
            friends=_friends,
            values=_values,
            created_at=_created_at,
            last_login=_last_login
        )

__STRUCT_ID__ = {
    1: ReqLogin,
    2: User,
    3: ResLogin,
}

def dumps(obj):
    _data = obj._asbytes()
    _len = len(_data)
    return struct.pack('HH', _len, obj.__struct_id__) + _data

def loads(buf):
    _offset = 0
    _len = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
    _struct_id = struct.unpack('H', buf[_offset:_offset+2])[0]; _offset += 2
    cls = __STRUCT_ID__.get(_struct_id, None)
    if cls is None:
        raise ValueError("buf can not be deserialized")
    return cls._frombytes(buf[_offset:])
