# Poselib2Morph
ポーズライブラリのポーズリストを一気にモーフに焼き付けるアドオン:Poselib2Morph

ポーズライブラリのポーズリストを一気にshape key（モーフ）に変換するアドオンです。
フェイシャルボーンで表情を作成してポーズライブラリに保存し、shape keyに変換したい時に便利です。

## Requirements（使用条件）
* Blender 2.90.1+


## Usage（使い方）
1. アドオンを有効にします。  
2. ポーズライブラリが保存されているアーマチュアが適用されているオブジェクトを選択します。
3. メニューの「object」にある「Poselib2Morph」を押して実行します。

## Note（ご注意）
1. 不要なIKやコンストレイントをミュートしておかないと、それらが適用された状態でモーフに焼き付けてしまいます。
例えば、両手や両足のIKなどはあらかじめミュートしてください。
2. ポーズライブラリに登録されているポーズはすべて焼き付けてしまいますので、不要なデータはアドオン実行後にシェイプキーパネルのほうから削除してください。
3. This code was modified from the original project at https://github.com/12funkeys/Poselib2Morph, to be compatible with Blender 2.90.1.

## Licenses（ライセンス）
[MIT licenses](https://opensource.org/licenses/mit-license.php)

## Bugs
*
