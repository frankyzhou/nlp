# -*- coding: utf-8 -*-
from pyltp import SentenceSplitter
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
print '\n'.join(sents)