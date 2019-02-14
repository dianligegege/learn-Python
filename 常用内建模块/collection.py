from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

# 自定义tuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(
    p.x,
    p.y
)

# 双向列表deque
q = deque([1,2,3])
q.popleft()
q.appendleft('left')
print(q)

# 默认dict defaultdict
dd = defaultdict(lambda: 'N/A')
print(dd['d'])

# 保持dict的key顺序  OrderedDict
od = OrderedDict()
od['a'] = 1
od['d'] = 4
od['b'] = 2
od['c'] = 3
print(od) # a d b c
o = dict([('a',1),('d',4),('b',2),('c',3)])
print(o)

# counter 统计字符出现的个数
c = Counter('kgkuagalalgskfg')
print(c)
print(c['g'])
