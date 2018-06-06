import apriori
# 导入数据集
dataSet = apriori.loadDataSet('Groceries.csv')

L, suppData = apriori.apriori(dataSet, minSupport=0.03)
# minSupport<0.05
rules = apriori.generateRules(L, suppData, minConf=0.2)
# minConf<4
print(rules)





