import scipy.special as sc
import numpy as np


# определение класса нейронной сети
class neuralNetwork:
    # инициализировать нейронную сеть
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # задать количество узлов по входном, скрытом и выходном слое
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # коэффициент обучения
        self.lr = learningrate

        # использоване сигмоиды в качестве функции активации
        self.activation_function = lambda x: sc.expit(x)

        pass

     # тренировка нейронной сети
    def train(self, inputs_list, targets__list):
        # преобразовать список входных значений в двухмерный массив
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2), T

        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = np.dot(self.wih, inputs)
        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)

        # рассчитать входящие сигналы для выходного слоя
        final_inputs = np.dot(self.who, hidden_outputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)

        # ошибки выходного слоя = (целевое значение - фактическое)
        output_errors = targets - final_outputs
        # ошибки скрытого слоя - это ошики output_error, распределенные пропорционально весовым коэффициентам связей и рекомбинированные на скрыых узлах
        hidden_errors = np.dot(self.who.T, output_errors)

        # обновить весовые коэффициенты для связей между скрытым и выходынм слоями
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                     numpy.transpose(hidden_outputs))
        # обновить весовые коэффициенты для связей между входным и скрытым слоями
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.traspose(inpits))
        pass

    # опрос нейронной сети
    def query(self, inputs_list):
        # преобразовать список входных значений в двумерный массив
        inputs = np.array(inputs_list, ndmin=2).T
        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = np.dot(self.wih, inputs)
        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)

        # рассчитать входящие сигналы для выходного слоя
        final_inputs = np.dot(self.who, hidden_outputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)

        return final_inputs