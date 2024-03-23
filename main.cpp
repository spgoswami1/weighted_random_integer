#include <iostream>
#include <torch/torch.h>

struct WeightedRandomIntegerImpl: torch::nn::Module {
 WeightedRandomIntegerImpl(int num_weights): num_weights_(num_weights) {
  weights_ = register_buffer("weights", torch::rand({num_weights}));
}
 torch::Tensor forward() {
  return torch::multinomial(weights_, 1, true);
}

private:
 int num_weights_;
 torch::Tensor weights_;
};

TORCH_MODULE(WeightedRandomInteger);

int main(){
 torch::manual_seed(42);
 auto model = std::make_shared<WeightedRandomIntegerImpl>(10);
 for (int i = 0; i < 20; i++){
  torch::Tensor sample = model->forward();
  std::cout << sample.item() << std::endl;
 }
}
