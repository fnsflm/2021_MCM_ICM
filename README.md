# 2021美赛D题代码

>   代码全部为后期整理, 代码涉及路径的部分需要更改

## 赛题( 所有)

`2021_MCM-ICM_Problems` 文件夹, c题数据已解压, 数据未进行任何修改

## 数据

`data`文件夹, 第四问数据复制粘贴, 并部分有修改

 ## 第一问

`first`文件夹

`first/network_pic` 绘制网络图, 包括社区划分后的

`first/network_parameter` 衡量网络依赖性的三个参数, clastering_ceofficent, katz, characteristic path length的代码和结果

`first/network_community`社区划分算法的代码和结果

三个参数计算[代码展示](https://nbviewer.jupyter.org/github/fnsflm/2021_MCM_ICM/blob/master/first/network_parameter/network_norm.ipynb)

## 第二问

`second`文件夹

主要对数据进行了一些分类和处理

`second/music_pca.xlsx`(原名new.xlsx)13特征进行pca处理后的结果, 需要取前四个

`second/stastic.*`统计一下不同的特征

`second/music_year.ipynb`代码: 将`music_pca.xlsx`或者`data/full_music_data.csv`先按各个流派分开, 再将相同年份的合并, 并求出流派半径和流派方差(具体定义见论文)

其余为数据文件

## 第四问

`fourth`求了线性回归

## 2.567

`2.567`文件夹

废案, 对第五题第二问和67问的思考和部分实现

## 第五问

`fifth`文件夹

`fifth/distance_genre`, `fifth/feature_genre.jpg`,`fifth/feature_time.jpg`, 各个流派流派半径,流派方差和数量变化图

`feature_time.ipynb`绘图代码

`statistic*` 对第一问三参数结果的统计

`fifth.docx` 对第五问的分析

## article(忽略)

队友的部分图片和论文

## 其它

`art_genre.tsv`因为人名中有逗号, 所以改成了tsv格式, 重新整理的身份标识和原身份标识,人名,流派,katz结果的对应关系, 经常用于excel的vlookup函数进行匹配填表

