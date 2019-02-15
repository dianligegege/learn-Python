from collections.abc import Iterable
from collections.abc import Iterator

print(
isinstance([],Iterable),
isinstance((),Iterable),
isinstance({},Iterable),
isinstance('acs',Iterable),
isinstance([x for x in range(10)],Iterable),
isinstance(122,Iterable)
)

print(
isinstance([],Iterator),
isinstance((),Iterator),
isinstance({},Iterator),
isinstance('acs',Iterator),
isinstance([x for x in range(10)],Iterator),
isinstance((x for x in range(10)),Iterator),
isinstance(122,Iterator)
)

print(
    isinstance(iter([]),Iterator)
)