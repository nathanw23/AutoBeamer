# AutoBeamer

**Description**

A command line tool that generates a LaTeX Beamer presentation of images. The tool is designed to take images from a specified folder and create slides where each slide contains one image.

**Installation**

To install, *ideally* create a new environment using your preferred Python environment manager:

```conda create -n auto_beamer```

Then install the required packages as follows:

1. ```pip install -r requirements.txt```

2. ```pip install -e .```

Once installed, the tools can be used from any location on your computer. 

### Usage

The command line tool can be executed by running ```auto_beamer --folder_path``` followed by the path to the folder containing the images.

### Updating

After updating the repo (```git pull```), update the command line interface using ```pip install -e .``` at the repo root directory
