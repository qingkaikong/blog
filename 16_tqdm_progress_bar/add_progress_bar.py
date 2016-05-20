import time
from tqdm import tqdm

# This is just a simple example using the tqdm module for a progress bar
# You can install the module using pip install tqdm

for i in tqdm(range(100)):
    #print i
    time.sleep(0.2)