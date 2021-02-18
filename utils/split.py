import os, os.path, shutil


def move_data(data, cur_path, tgt_path):
    if not os.path.exists(tgt_path):
        os.makedirs(tgt_path)

    for datum in data:
        cur_datum_path = os.path.join(cur_path, datum)
        tgt_datum_path = os.path.join(tgt_path, datum)
        shutil.move(cur_datum_path, tgt_datum_path)


def train_valid_split(data_path, train_valid_ratio):
    data = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]
    splitter = int(len(data) * train_valid_ratio)
    train_data, valid_data = data[:splitter], data[splitter:]

    tgt_train_path = os.path.join('../train', data_path.split('/')[-1])
    tgt_valid_path = os.path.join('../valid', data_path.split('/')[-1])

    move_data(train_data, data_path, tgt_train_path)
    move_data(valid_data, data_path, tgt_valid_path)


train_valid_split('../export/images', 0.85)
train_valid_split('../export/labels', 0.85)
