#!/usr/bin/env python3
# Copyright (c) 2021 oatsu
"""
eval.list と dev.list と train.list を生成する。
utt_list.txtは作らなくていい気がする。
data/list/eval.list
data/list/dev.list
data/list/train.list

全ファイルから12個おきにevalとdevに入れる。dev以外の全ファイルをtrainに入れる。
"""

from glob import glob
from os import makedirs
from os.path import basename, expanduser, join, splitext
from sys import argv
from typing import Union

import yaml
from natsort import natsorted


def generate_train_list(out_dir, interval: Union[int, None] = None):
    """
    utt.list
    eval.list
    dev.list
    train.list
    """
    # 学習対象のファイル一覧を取得
    utt_list = glob(f'{join(out_dir)}/acoustic/wav/*.wav')
    utt_list = natsorted([splitext(basename(path))[0] for path in utt_list])
    len_utt_list = len(utt_list)
    if len_utt_list == 0:
        raise Exception(f'"{join(out_dir)}/acoustic/wav"에 wav 파일들이 없습니다.')

    if interval is None:
        for i in (23, 19, 17, 13, 11):
            if (i < len_utt_list + 5) and (len_utt_list % i != 0):
                interval = i
                break
        else:
            interval = 13

    # 評価用が5分の1より多いと困るので
    elif interval <= 5:
        raise ValueError('인수 "interval"은 5보다 커야합니다.')
    makedirs(join(out_dir, 'list'), exist_ok=True)

    print(f'generate_train_list.py: 간격 = {interval}')

    # 各種曲名リストを作る
    eval_list = [songname for idx, songname in enumerate(utt_list) if idx % interval == 0]
    dev_list = [songname for idx, songname in enumerate(utt_list) if idx % interval == 5]
    train_list = [songname for idx, songname in enumerate(utt_list)
                  if (idx % interval != 0 and idx % interval != 5)]

    # ファイルの出力パス
    path_utt_list = join(out_dir, 'list', 'utt_list.txt')
    path_eval_list = join(out_dir, 'list', 'eval.list')
    path_dev_list = join(out_dir, 'list', 'dev.list')
    path_train_list = join(out_dir, 'list', 'train_no_dev.list')
    # ファイル出力
    with open(path_utt_list, mode='w', newline='\n') as f_utt:
        f_utt.write('\n'.join(utt_list))
    with open(path_eval_list, mode='w', newline='\n') as f_utt:
        f_utt.write('\n'.join(eval_list))
    with open(path_dev_list, mode='w', newline='\n') as f_utt:
        f_utt.write('\n'.join(dev_list))
    with open(path_train_list, mode='w', newline='\n') as f_utt:
        f_utt.write('\n'.join(train_list))


def main(path_config_yaml):
    """
    フォルダを指定して実行
    """
    with open(path_config_yaml, 'r') as fy:
        config = yaml.load(fy, Loader=yaml.FullLoader)
    out_dir = expanduser(config['out_dir'])
    generate_train_list(out_dir)


if __name__ == '__main__':
    main(argv[1].strip('"'))
