from tests import pyunit_utils
import sys
sys.path.insert(1, "../../../")
import h2o

def iris_nfolds_getModel():
    # Connect to h2o
    h2o.init(ip,port)

    iris = h2o.import_frame(path=pyunit_utils.locate("smalldata/iris/iris.csv"))


    model = h2o.random_forest(y=iris[4], x=iris[0:4], ntrees=50, nfolds=5)
    model.show()

    model = h2o.getModel(model._key)
    model.show()

if __name__ == "__main__":
	pyunit_utils.standalone_test(iris_nfolds_getModel)
else:
	iris_nfolds_getModel()