# coding:utf-8

class seq():
    # 卷积的宽度，在cnn中，卷积的长度为词向量的长度，宽度表示包含多少词
    filter_sizes=[2,4,6]
    
    # 每种卷积的个数
    filter_nums=2

    # dropout概率
    dropout_prob=0.5

    # 规定每个句子的长度
    seqence_length=600


