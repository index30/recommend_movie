# recommend_movie

## 映画推薦
前提として、推薦を行うユーザはすでに登録されており、いくつかの作品に対して評価を行なっているものと仮定  

### extract\_data.py  
データからユーザとジャンルごとの評価値を抽出した行列生成  

### test\_extract\_data.py  
extract\_data.pyのテストコード  

### user\_base.py  
ユーザベースのレコメンド用

### test\_user\_base.py  
user\_base.pyのテストコード

### item\_base.py  
アイテムベースのレコメンド用

### item\_base.py  
item\_base.pyのテストコード

### recommend.py  
ユーザベースか、アイテムベースでレコメンドするかを判定  

### test\_recommend.py  
recommend.pyのテストコード  

### main.py  
実行部分  
ユーザはすでに会員登録しており、IDを所持していると仮定  
IDを入力することで、IDに対応した推薦を行う  
- ユーザベース  
```
$ ./main.py rec -u [user_id]
```
- アイテムベース  
```
$ ./main.py rec -i [user_id]
```
