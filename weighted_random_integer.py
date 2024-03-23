import torch

class WeightedRandomInteger(torch.nn.Module):
    def __init__(self, num_weights):
        self.num_weights = num_weights
        self.weights = torch.rand((num_weights,))

    def forward(self):
        with torch.no_grad():
            return torch.multinomial(self.weights, 1, True)

#torch.manual_seed(42)
#model = WeightedRandomInteger(10)

#for i in range(20):
#    sample = model.forward()
#    print(sample.item())

