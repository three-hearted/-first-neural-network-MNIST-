# загрузить в список тренировочный набор данных CSV-файла набора MNIST
training_data_file = open(r'C:\Users\serez\Downloads/mnist_train-1.csv', 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# тренировка нейронной сети

epochs = 5

for e in range(epochs):
    # перебрать все записи в тренировочном наборе данных
    for record in training_data_list:
        # разделяем данные с помощью запятой
        all_values = record.split(',')
        # масштабировать и сместить входные значения
        inputs = (np.asfarray(all_values[1:])/ 255.0 * 0.99) + 0.01
        # создать целевые выходные значения
        targets = np.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass