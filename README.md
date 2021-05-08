# usepandasgui
CSV(またはExcel)ファイルをPandasGUIで開く際、GUI操作でファイル指定できるようにするツールです。
普段、Pandasを使用している方がわざわざIDE等を開かなくてもPandasGUIを使ってCSV(またはExcel)ファイルを開けるようにしました。

なおPyInstaller等で実行ファイル化すると開くのに時間がかかるため、pywファイルにしております。

## 使用するための前提条件
- OS: Windows 10
- Anaconda3インストール済み
- PySimpleGUIおよびPandasGUIインストール済み

Anaconda3のインストールがまだの方は[こちら](https://docs.anaconda.com/anaconda/install/windows/)に記載の手順でインストールしてください。
Anaconda3はインストール済みでPyShimpleGUIとPandasGUIのインストールがまだの方は`pip install pysimplegui pandasgui`でインストールしてください。

## 使用方法
1. usepandasgui.pyw を任意の場所にダウンロードします
1. usepandasgui.pyw をダブルクリックします
1. 「このファイルを開く方法を選んでください。」というポップアップが出てくるので、「常にこのアプリを使って .pyw ファイルを開く」にチェックしたうえで、その他のアプリ > このPCで別のアプリを探す をクリックします
1. C:\Users\{ユーザー名}\anaconda3\pythonw.exe を選択します
1. ポップアップの[OK]ボタンをクリックします
1. "Open CSV or Excel with PandasGUI" というウィンドウが表示されるので、[Browse]ボタンをクリックして開きたいCSV(またはExcel)ファイルを選択します
1. [Submit]ボタンをクリックすると、指定したCSV(またはExcel)ファイルPandasGUIで開くことができます
