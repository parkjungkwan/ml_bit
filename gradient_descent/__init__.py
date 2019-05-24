from gradient_descent.model import GradientDescentModel
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    model = GradientDescentModel()
    model.create_model(-30, 50)
