# загрудить тестовый набор данных
test_data_file = open(r'C:\Users\serez\Downloads/mnist_test_2.csv', 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# тестирование нейронной сети

scorecard = []

# перебрать все данные в тестовом наборе данных
for record in test_data_list:
    # разделить данные запятой
    all_values = record.split(',')
    # первым значением будет правильный ответ
    correct_label = int(all_values[0])
    # масштабировать и сместить входные значения
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # опрос сети
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    # присоединить оценку ответа сети к концу списка
    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass

    pass
