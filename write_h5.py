import numpy as np
import tables


def main():
    vector_size = 128
    with tables.open_file('/tmp/8GB.h5', 'w') as f:
        table = f.create_table(f.root, 'table', {
            'vector_values': tables.Float64Col(pos=0, shape=(vector_size,)),
        })
        vector = np.zeros(vector_size)
        for _ in range(8300000):
            table.row['vector_values'] = vector
            table.row.append()


if __name__ == '__main__':
    main()
