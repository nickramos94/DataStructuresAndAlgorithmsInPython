def add_3d(tensor1, tensor2):
    tensor3 = []
    for matrix1, matrix2 in zip(tensor1, tensor2):
        matrix3 = []
        for row1, row2 in zip(matrix1, matrix2):
            row3 = []
            for elem1, elem2 in zip(row1, row2):
                elem3 = elem1 + elem2
                row3.append(elem3)
            matrix3.append(row3)
        tensor3.append(matrix3)
    return tensor3


if __name__ == "__main__":
    tensor1 = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ]
    tensor2 = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ]
    tensor3 = add_3d(tensor1, tensor2)
    print(tensor3)
