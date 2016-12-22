# coding=utf-8
from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load("G:\\file\\ltp-data-v3.3.1\\ltp_data\\cws.model")
# segmentor.load_with_lexicon('/path/to/your/model', '/path/to/your/lexicon') # 加载模型
words = segmentor.segment("元芳你怎么看")
print "|".join(words)
segmentor.release()

"""
pyltp 分词支持用户使用自定义词典。分词外部词典本身是一个文本文件（plain text）如上lexicon，每行指定一个词，编码同样须为 UTF-8，样例如下所示
苯并芘
亚硝酸盐
"""