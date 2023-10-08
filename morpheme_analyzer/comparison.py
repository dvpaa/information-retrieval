from konlpy.tag import Hannanum

analyzer = Hannanum()
examples = [
    u'아버지가방에들어가신다',  # 띄어쓰기
    u'나는 밥을 먹는다', u'하늘을 나는 자동차',  # 중의성 해소
    u'아이폰 기다리다 지쳐 애플공홈에서 언락폰질러버렸다 6+ 128기가실버ㅋ'
]

for example in examples:
    print(analyzer.analyze(example))