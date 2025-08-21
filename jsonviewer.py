#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""JSONファイルを整形して表示する"""

import json
import sys
import time

__version__ = "1.2.0"
__author__ = "t-nakayoshi (Takayoshi Tagawa)"

_app_name_ = "jsonview"

OPT_INDENT_MIN = 0
OPT_INDENT_MAX = 8
OPT_INDENT_DEFAULT = 4


def json_view(file: str, indent: int, sort: bool, ensure_ascii: bool) -> str:
    """メイン処理
    指定したJSONファイルを整形して出力する

    Args:
        file (str): JSONファイル名
        indent (int): インデント文字数
        sort (bool): ソートの有無（True=KEYでソートする）
        ensure_ascii (bool): UNICODEエスケープ（True=あり）

    Returns:
        str: JSON文字列（整形エラー時は空文字列）

    """
    json_str = ""
    try:
        with open(file, "r", encoding="utf-8") as f:
            o = json.load(f)

        json_str = json.dumps(
            o, indent=indent, sort_keys=sort, ensure_ascii=ensure_ascii
        )

    except Exception as e:
        print(f"[error] {e}")

    return json_str


if __name__ == "__main__":
    """"""
    import argparse

    from myutils.util import pause, platform_info

    def get_options(args: list[str], unittest: bool = False):
        """パラメータ解析
        argparseによるコマンドラインパラメータ解析

        Args:
            arg (list[str]): 解析する文字列リスト（通常sys.argv）
            unittest (bool): True=単体テストモード（Usage文字列を空にする）

        Returns:
            解析結果: argparse.ArgumentParser.parse_argsの出力

        Exsamples:
            >>> args = get_options(['-a','1','-b','2','--c','3'])
            >>> args = get_options(sys.argv[1:])
        """
        info: tuple = platform_info()  # 動作環境情報取得
        usage = "" if unittest else "%(prog)s [options] file"
        parser = argparse.ArgumentParser(
            prog=_app_name_, description="JSON fromatting viewer.", usage=usage
        )
        parser.add_argument("file", type=str, help="Please set JSON file name")
        parser.add_argument(
            "-i",
            "--indent",
            type=int,
            choices=range(OPT_INDENT_MIN, OPT_INDENT_MAX + 1),
            default=OPT_INDENT_DEFAULT,
            help=f"Indent columns ({OPT_INDENT_MIN}-{OPT_INDENT_MAX}, default: {OPT_INDENT_DEFAULT})",
            metavar=f"{{{OPT_INDENT_MIN}-{OPT_INDENT_MAX}}}",
        )
        parser.add_argument(
            "-s",
            "--sort",
            action="store_true",
            help="Sort by key (True), default: Not sorted (False)",
        )
        parser.add_argument(
            "-a",
            "--ensure-ascii",
            action="store_true",
            help="UNICODE escape (True), default: Not escaped (False)",
        )
        parser.add_argument(
            "-o",
            "--output",
            type=str,
            default="",
            help="Output formatted JSON file name",
        )
        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version=f"{'%(prog)s'} version {__version__} on Python {info[2]}.",
        )

        # 結果を返す
        return parser.parse_args()

    args = get_options(sys.argv[1:])
    tm_sta = time.perf_counter()
    # 処理開始
    json_str = json_view(args.file, args.indent, args.sort, args.ensure_ascii)
    #
    tm_end = time.perf_counter()

    if len(json_str):
        if len(args.output) != 0:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(json_str)
        else:
            print(f"==== {args.file} ====")
            print(json_str)
            print("========")

    print("\n")
    pause()
