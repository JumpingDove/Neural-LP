import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="collect_all_facts python version")
    parser.add_argument('--path', default='./datasets/family', type=str, help='data file path')
    args = parser.parse_args()

    with open(os.path.join(args.path, 'all.txt'), 'w') as fo:
        for f in ['train.txt', 'facts.txt', 'valid.txt', 'test.txt']:
            with open(os.path.join(args.path, f), 'r') as fi:
                fo.write(fi.read())
