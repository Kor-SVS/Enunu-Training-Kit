#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
DBのモノラベルの時刻をフルラベルに書き写して、
音声ファイルの発声時刻に合ったフルラベルを生成する。

音素数と音素が完全に一致している前提で処理する。
"""

from glob import glob
from os import makedirs
from os.path import basename
from sys import argv

import utaupy as up
import yaml
from tqdm import tqdm


def copy_mono_align_time_to_full(path_mono_align_in, path_full_score_in, path_full_align_out):
    """
    モノラベルの発声時刻をフルラベルにコピーする。
    """
    mono_align_label = up.label.load(path_mono_align_in)
    full_label = up.label.load(path_full_score_in)
    # ラベル内の各行を比較する。
    for ph_mono_align, ph_full in tuple(zip(mono_align_label, full_label))[:-1]:
        # 発声開始時刻を上書き
        ph_full.start = ph_mono_align.start
        # 発声終了時刻を上書き
        ph_full.end = ph_mono_align.end
    # 最後のノートは休符だったら終了時刻は楽譜に合わせる。そうじゃなかったら手動ラベルに合わせる。
    full_label[-1].start = mono_align_label[-1].start
    if mono_align_label[-1].symbol not in ['pau', 'sil']:
        print(mono_align_label[-1].symbol)
        full_label[-1].end = mono_align_label[-1].end

    # ファイル出力
    full_label.write(path_full_align_out)


def main(path_config_yaml):
    """
    モノラベルとフルラベルのファイルを取得して処理を実行する。
    """
    with open(path_config_yaml, 'r') as fy:
        config = yaml.load(fy, Loader=yaml.FullLoader)
    out_dir = config['out_dir']

    # 出力先フォルダを作成
    full_align_dir = f'{out_dir}/full_align_round'
    makedirs(full_align_dir, exist_ok=True)

    # 時刻のもとになるモノラベルファイル一覧
    mono_align_files = sorted(glob(f'{out_dir}/mono_align_round/*.lab'))
    # コンテキストのもとになるフルラベルファイル一覧
    full_score_files = sorted(glob(f'{out_dir}/full_score_round/*.lab'))

    print('mono-LAB(mono_align_round) 시간을 full-LAB(full_score_round)로 복사 후, full_align_round에 저장 중...')
    for path_mono_align, path_full_score in zip(tqdm(mono_align_files), full_score_files):
        path_full_align = f'{full_align_dir}/{basename(path_full_score)}'
        copy_mono_align_time_to_full(path_mono_align, path_full_score, path_full_align)


if __name__ == '__main__':
    print('----------------------------------------------------------------------------------')
    print('[ Stage 0 ] [ Step 3a ]')
    print('mono_align 음소를 full_score로 복사하고 full_align으로 저장합니다.')
    print('----------------------------------------------------------------------------------')
    main(argv[1])
