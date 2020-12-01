from CNNStrategy import CNNStrategy
import sys


class Model:

    def __init__(self, classifier, data, device, nbands, windowSize, train_y, classes):
        """Create a ML object used to train the HSI datasets.
        @param classifier: Type of classifier. Options: CNN, SVM, or RF.
        @param data: Type of data. Options: Kochia, Avocado, IP.
        @param device: Type of device used for training (Used for the CNN).
        @param nbands: Number of selected spectral ban.
        @param windowSize: Window size (Used for the CNN).
        @param train_y: Target data.
        @param classes: Number of classes.
        """
        # Set instance variables
        self.classes = classes
        self.data = data
        self.device = device
        self.nbands = nbands
        self.windowSize = windowSize

        # Set the strategy that the model will use
        if classifier == 'CNN':
            self.strategy = CNNStrategy()
        elif classifier == 'SVM':
            self.strategy = CNNStrategy()
        elif classifier == 'RF':
            self.strategy = CNNStrategy()
        else:
            sys.exit('The only available classifiers are: CNN, SVM, and RF.')

        # Define the model using the selected strategy
        self.model = self.strategy.defineModel(self.device, self.data, self.nbands,
                                               self.windowSize, self.classes, train_y)

    def trainFold(self, trainx, train_y, train, batch_size, epochs, valx, test, means, stds, filepath):
        """Train the network given a train-validation split
        @param trainx: Training set.
        @param train_y: Target data of the entire dataset (training + validation sets).
        @param train: List of training indexes
        @param batch_size: Size of the mini-batch (Used for the CNN).
        @param epochs: Number of epochs used to train a CNN.
        @param valx: Validation set.
        @param test: List of test indexes
        @param means: Mean of each spectral band calculated in the training set.
        @param stds: Standard deviation of each spectral band calculated in the training set.
        @param filepath: Path used to store the trained model.
        """
        self.strategy.trainFoldStrategy(self.model, trainx, train_y, train, batch_size, self.classes, self.device,
                                        epochs, valx, test, means, stds, filepath)

    def evaluateFold(self, valx, train_y, test, means, stds, batch_size):
        """Return the numpy target and predicted vectors as numpy vectors.
        @param valx: Validation set.
        @param train_y: Target data.
        @param test: List of test indexes
        @param means: Mean of each spectral band calculated in the training set.
        @param stds: Standard deviation of each spectral band calculated in the training set.
        @param batch_size: Size of the mini-batch (Used for the CNN).
        """
        return self.strategy.evaluateFoldStrategy(self.model, valx, train_y, test,
                                                  means, stds, batch_size, self.classes, self.device)

    def loadModel(self, path):
        """Load a saved model
        @param path: File path with the saved model.
        """
        self.strategy.loadModelStrategy(self.model, path)
