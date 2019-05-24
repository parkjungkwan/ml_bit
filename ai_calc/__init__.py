from ai_calc.model import CalculatorModel
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    model = CalculatorModel()
    model.create_add_model()
   # model.create_sub_model()
   # model.create_mul_model()
   # model.create_div_model()




