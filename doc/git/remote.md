```e
sh 'mkdir ~/{APP} ; cd ~/{APP}'
sh 'git init'
```
```e
sh 'git remote add gh   git@github.com:ponyatov/{APP}.git'
sh 'git remote add flic git@gitflic.ru:dponyatov/{APP.lower}.git'
```
```e
BRANCH = USER
sh 'git checkout --orphan {BRANCH}'
sh 'git add -A ; git commit -am "."'
sh 'git push -uv gh   {BRANCH}'
sh 'git push     flic {BRANCH}'
```
