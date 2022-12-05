# coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

#df = pd.read_csv('D:\\PhD\\77-小论文\\20211130-DrRank\\Data\\demo-rawdata.csv', index_col=0)
df = pd.read_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\adjacency_matrix.csv', index_col=0)
df = df.T  # 矩阵转置
print(df)
G = nx.from_pandas_adjacency(df=df, create_using=nx.DiGraph())

# 中心度计算
DgrCnt = nx.degree_centrality(G)
InDgrCnt = nx.in_degree_centrality(G)
OutDgrCnt = nx.out_degree_centrality(G)
BtwnCnt = nx.betweenness_centrality(G)
EgnCnt = nx.eigenvector_centrality(G, max_iter=1000)  # 注意小于1000次迭代可能不收敛

# 数据可视化
print(nx.info(G))
plt.figure(figsize=(10, 10))
plt.title("Ph.D. Exchange Networks 博士互聘网络", fontsize=20, fontproperties="SimHei")
#nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True, node_size=666, alpha=0.5, font_size=10, node_color='red')
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True, node_size=666, alpha=0.5, font_size=10, node_color='red')
plt.show()

# PageRank计算
pr = nx.pagerank(G)
print("PageRank:", pr)

# Hits计算
#hits = nx.hits(G)  # within 100 iterations
#print("Hits", hits)

df_DgrCnt = pd.DataFrame.from_dict(DgrCnt, orient='index')
df_InDgrCnt = pd.DataFrame.from_dict(InDgrCnt, orient='index')
df_OutDgrCnt = pd.DataFrame.from_dict(OutDgrCnt, orient='index')
df_BtwnCnt = pd.DataFrame.from_dict(BtwnCnt, orient='index')
df_EgnCnt = pd.DataFrame.from_dict(EgnCnt, orient='index')
df_Pr = pd.DataFrame.from_dict(pr, orient='index')
#df_Hits = pd.DataFrame.from_dict(hits[0], orient='index')

df_DgrCnt.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\DgrCnt.csv')
df_InDgrCnt.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\InDgrCnt.csv')
df_OutDgrCnt.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\OutDgrCnt.csv')
df_BtwnCnt.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\BtwnCnt.csv')
df_EgnCnt.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\EgnCnt.csv')
df_Pr.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\PageRank.csv')
#df_Hits.to_csv('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\Hits.csv')
