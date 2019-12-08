from __future__ import print_function
import time
import json
import pickle
try:
    import cPickle
except:
    import _pickle as cPickle
import datetime
import sample
from sample import User, ResLogin

# create sample class
friend = User(user_id='asdfaefwe', user_name='scvberdfsdf')
friends = [friend for _ in range(10)]
values = [x for x in range(10)]
obj = ResLogin(
    user_id='adeee',
    user_name='wwgdsfgre',
    token='esdfgergvbnsrfg',
    channel=sample.LoginChannel.Guest,
    friend=friend,
    friends=friends,
    values=values,
    created_at=datetime.datetime.now(),
    last_login=datetime.datetime.now().date(),
)

def perf(func, obj, times=100000):
    begin = time.time()
    for _ in range(times):
        bytebuffer = func(obj)
    return time.time() - begin

print(sample.loads(sample.dumps(obj))._asdict())
assert sample.loads(sample.dumps(obj))._asdict() == obj._asdict(), 'ERROR: papaya dumps/loads failed.'

# print('papaya dumps:', perf(sample.dumps, obj))
# print('papaya loads:', perf(sample.loads, sample.dumps(obj)))
# print('pickle dumps:', perf(pickle.dumps, obj))
# print('pickle loads:', perf(pickle.loads, pickle.dumps(obj)))
# print('cPickle dumps:', perf(cPickle.dumps, obj))
# print('cPickle loads:', perf(cPickle.loads, cPickle.dumps(obj)))
