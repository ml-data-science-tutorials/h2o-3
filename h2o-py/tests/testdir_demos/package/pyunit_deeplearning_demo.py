from tests import pyunit_utils
import sys
sys.path.insert(1, "../../../")
import h2o

def demo_deeplearning():
    # Connect to a pre-existing cluster
    

    # Execute gbm demo
    h2o.demo(func="deeplearning", interactive=False, test=True)

if __name__ == "__main__":
	pyunit_utils.standalone_test(demo_deeplearning)
else:
	demo_deeplearning()