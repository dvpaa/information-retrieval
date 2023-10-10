from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from khaiii import KhaiiiApi


analyzers = [Hannanum(), Kkma(), KhaiiiApi()]
examples = [
    u'아버지가방에들어가신다',  # 띄어쓰기
    u'사랑해보고싶어',
    u'하늘을 나는 자동차',  # 중의성 해소
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
