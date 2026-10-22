print("""
Task 1 - Setting Up Python Development Tools

1. Download and install Anaconda3
   Download Anaconda Distribution from https://www.anaconda.com/download
   Choose the installer for your operating system and follow its instructions.
   Open Anaconda Prompt or an initialized terminal and check:
   conda --version
   python --version

2. Install PyTorch
   Create a separate environment:
   conda create -n pytorch-env python=3.11
   conda activate pytorch-env
   Visit https://pytorch.org/get-started/locally/
   Select your operating system, Pip, Python and CPU or the appropriate GPU.
   Run the installation command provided by the selector.
   Verify the installation:
   python -c "import torch; print(torch.__version__); print(torch.rand(2, 3))"

3. Install TensorFlow 2.0
   Use a separate Python 3.7 environment for this older release on x86-64:
   conda create -n tensorflow20 python=3.7
   conda activate tensorflow20
   python -m pip install "numpy<1.19" "protobuf<4" "tensorflow==2.0.0"
   Verify the installation:
   python -c "import tensorflow as tf; print(tf.__version__)"
   Version 2.0.0 requires an older Python environment; it cannot be installed
   into a current Python 3.14 environment using its published wheels.

4. Install Visual Studio Code
   Download the installer for your system from https://code.visualstudio.com/download
   Install and open VS Code, then install the Python extension by Microsoft.
   Open the task folder and use Python: Select Interpreter to choose your environment.
   Create a Python file and run:
   print("Hello, Python!")

5. Install PyCharm
   Download PyCharm from https://www.jetbrains.com/pycharm/download/
   Follow the installation instructions for your operating system.
   Open a project and configure its Python interpreter to use the desired
   Conda environment. Create a Python file and run:
   print("Hello, Python!")

These are installation instructions. Running this file only displays them.
""")
