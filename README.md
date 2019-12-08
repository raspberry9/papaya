## Papaya serializer

#### Benchmark

- Unit: seconds, 100000 times

##### Python2.7.10
```
papaya dumps: 3.00451493263
papaya loads: 4.9945268631
pickle dumps: 12.829200983
pickle loads: 10.1364731789
cPickle dumps: 2.95752096176
cPickle loads: 1.46191596985
```

##### Python3.6.5
```
papaya dumps: 2.7513370513916016
papaya loads: 4.618807792663574
pickle dumps: 0.6620302200317383
pickle loads: 0.5566840171813965
cPickle dumps: 0.6621103286743164
cPickle loads: 0.5490219593048096
```

##### Pypy2.7.13
```
papaya dumps: 0.255007982254
papaya loads: 0.295555114746
pickle dumps: 1.38837099075
pickle loads: 1.37777900696
cPickle dumps: 1.5719909668
cPickle loads: 1.1190969944
```

##### Pypy3.5.3
```
papaya dumps: 0.20515894889831543
papaya loads: 0.24214792251586914
pickle dumps: 2.5867369174957275
pickle loads: 1.5509419441223145
cPickle dumps: 2.1558609008789062
cPickle loads: 1.3358619213104248
```
