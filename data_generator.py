import subprocess
from shutil import copyfile
import os
import glob


class DataGenerator:

    """
    Prepares data files and generates training data (.json)
    for Rasa NLU. For retraining - new files with positive
    and negative examples should be added to ./chatette/input
    and paths to those files provided in generate() method.
    """

    def __init__(self):
        self.POS_OUTPUT_PATH = "chatette/template_data/pos.txt"
        self.NEG_OUTPUT_PATH = "chatette/template_data/neg.txt"
        self.TEMPLATE_PATH = "chatette/template_data/template_travel.txt"
        self.OUTPUT_DIR_PATH = "chatette/output/"


    def read_list(self, path):
        with open(path, 'r') as f:
            lst = f.readlines()
        return lst


    def write_list(self, path, lst):
        with open(path, 'w') as f:
            f.writelines(lst)


    def prepare_input(self, positive_examples, negative_examples):

        pos = self.read_list(positive_examples)
        neg = self.read_list(negative_examples)

        # Lowercase and remove new line symbols and
        pos_clean = [x.lower().replace("\n", "") for x in pos]
        neg_clean = [x.lower().replace("\n", "") for x in neg]

        # Remove all pos examples fom neg list and format files
        pos = ["~[pos]\n"] + ["\t" + x for x in pos]
        neg = ["~[neg]\n"] + ["\t" + x + "\n" for x in neg_clean if x not in pos_clean]

        self.write_list(self.POS_OUTPUT_PATH, pos)
        self.write_list(self.NEG_OUTPUT_PATH, neg)


    def generate(self, positive_examples, negative_examples):

        self.prepare_input(positive_examples, negative_examples)

        stdout_message = subprocess.check_output([
            "python",
            "-m", "chatette",
            self.TEMPLATE_PATH,
            "-o", self.OUTPUT_DIR_PATH,
            "-f"
        ])

        files = glob.glob('data/*')
        for f in files:
            os.remove(f)

        copyfile(self.OUTPUT_DIR_PATH + "train/output.json", "data/output.json")
        print("Data generation finished. Output in: " + self.OUTPUT_DIR_PATH + "train/output.json")



# Run
if __name__ == "__main__":

    dg = DataGenerator()
    dg.generate(
        positive_examples="chatette/input/places.txt",
        negative_examples="chatette/input/random.txt"
    )
