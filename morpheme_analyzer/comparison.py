from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from khaiii import KhaiiiApi

# from konlpy.corpus import kolaw
# c = kolaw.open('constitution.txt').read()
# print(c)

# api = KhaiiiApi()
# for word in api.analyze(c):
#     print(word)

analyzers = [Hannanum(), Kkma(), KhaiiiApi()]
examples = [
    u'아버지가방에들어가신다',  # 띄어쓰기
    u'사랑해보고싶어',
    u'하늘을 나는 자동차',  # 중의성
]

for example in examples:
    print(example)
    for analyzer in analyzers:
        print()
        print(analyzer.__class__.__name__)
        if isinstance(analyzer, KhaiiiApi):
            print(*analyzer.analyze(example))
        else:
            print(analyzer.pos(example))
    print()
    print()
