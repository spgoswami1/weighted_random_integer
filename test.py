import torch
import subprocess
from weighted_random_integer import WeightedRandomInteger

torch.manual_seed(42)
model = WeightedRandomInteger(10)
python_samples = [model.forward().item() for _ in range(20)]
cpp_process = subprocess.Popen(["./build/sanas"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
cpp_output, _ = cpp_process.communicate()
cpp_samples = list(map(int, cpp_output.decode().split('\n')[:-1]))
try:
    assert python_samples == cpp_samples
    print("PASSED")
except:
    print("FAILED")
