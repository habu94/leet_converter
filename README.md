# leet_coverter
入力された文字列をleet文字列に変換するプログラムです  
大文字はアルファベット全文字対応、小文字は変換可能な文字のみ変換できます  
パブリッシャーで入力された文字を転送、サブスクライバで変換しています  

## leet文字とは
アルファベットを記号などで表した文字で、ゲームの名前が他の人と被って使えない場合などに用いられます  

Wikipedia  
[https://ja.wikipedia.org/wiki/Leet](https://ja.wikipedia.org/wiki/Leet)

## 動作環境
- Ubuntu 20.04 WSL
- Raspberry Pi4
- ROS(noetic)

## 実行準備
ディレクトリに入り
  ```bash
  cd catkin_ws/src
  ```
以下のコードを実行
  ```bash
  git clone https://github.com/habu94/leet_converter.git
  ```
  ```bash
  cd ~/catkin_ws
  catkin_make
  ```
 
## 実行方法
端末を3つ立ち上げ、1つ目でroscoreを実行
  ```bash
  roscore
  ```
2つ目の端末でパブリッシャーを起動
  ```bash
  rosrun leet_converter reed.py
  ```
3つ目の端末でサブスクライバを起動
  ```bash
  rosrun leet_converter convert.py
  ```
パブリッシャー側でアルファベットを入力し、Enterキーを押すとサブスクライバ側で変換されたものが表示されます  
変換できないものは元の文字がそのまま表示されます

## 実行動画
動画のリンク  
[https://youtu.be/3DZ8aFdFzug](https://youtu.be/3DZ8aFdFzug)
