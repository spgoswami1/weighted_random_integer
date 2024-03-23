### Anaconda Installation, Skip if already installed
`curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh

`sh Miniconda3-latest-MacOSX-arm64.sh`

### Install pytorch through Conda
`conda install pytorch torchvision -c pytorch`

### Activate conda environment
`conda activate`

### Build and test
```mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=`python3 -c 'import torch;print(torch.utils.cmake_prefix_path)'` ..
cmake --build . --config Release
cd ..
python3 test.py```
