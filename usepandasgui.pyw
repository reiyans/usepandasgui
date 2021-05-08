# coding: utf-8

import re
import sys

import pandas as pd
import pandasgui
import PySimpleGUI as sg


def main():
    # PandasGUIで開くCSV or ExcelファイルのパスをGUIで取得
    layout = [
        [sg.Text("File"), sg.InputText(), sg.FileBrowse(key="filepath")],
        [sg.Submit(), sg.Cancel()],
    ]
    window = sg.Window("Open CSV or Excel with PandasGUI", layout)
    event, values = window.read()
    window.close()

    # パスからファイルタイプを取得
    filepath = values["filepath"]
    filename = re.sub(r".+/(.+)", "\\1", filepath)
    filetype = re.sub(r".+\.(.+)", "\\1", filename)

    # CSVまたはExcelのどちらか判定してDataFrameを生成
    if filetype == "csv":
        try:
            df = pd.read_csv(filepath, encoding="utf-8")
        except Exception as e:
            df = pd.read_csv(filepath, encoding="cp932")
    elif filetype == "xlsx" or filetype == "xls":
        df = pd.read_excel(filepath)
    else:
        sg.popup_error("Please select CSV or Excel.", title="Error")
        sys.exit()

    # PandasGUIでDataFrameを開く
    pandasgui.show(df)


if __name__ == "__main__":
    main()
