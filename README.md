# coding



############# 本地开发分支合并到本地master后，推送到远程master分支#################
在写项目的时候习惯创建一个dev分支用于更新代码，等到整个或者阶段性完成的时候再合并到master上

步骤如下

# 切换到master分支
git checkout master

# 将dev分支的代合并到master
git merge dev

# 查看状态
git status

# 推送
git push origin maste









######################### 远程master分支合并到本地dev分支#####################

远程master分支的代码领先自己的分支,git 如何把master分支代码合并到自己的分支

1.首先切换到主分支

git checkout master

2.使用git pull 把领先的主分支代码pull下来

git pull

3.切换到自己的分支

git checkout xxx(自己的分支)

4.把主分支的代码merge到自己的分支

git merge master

5.git push推上去ok完成,现在 你自己分支的代码就和主分支的代码一样了

git push origin 自己分支名
————————————————
