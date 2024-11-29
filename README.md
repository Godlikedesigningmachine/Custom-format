# Custom Python Projects

Welcome to my GitHub repository! This repository contains three Python files: `load.py`, `convert.py`, and `start.py`. These projects demonstrate my skills in Python programming and image processing.

## Table of Contents
- [Introduction](#introduction)
- [Project Destartions](#project-destartions)
  - [load.py](#loadpy)
  - [convert.py](#convertpy)
  - [start.py](#startpy)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository showcases my work on three distinct Python starts. Each start serves a unique purpose and highlights different aspects of my programming abilities.

## Project Destartions

### load.py

`load.py` is a Python script designed to decode a custom image format and display it using Pygame. Here are some of its key features:

- Easy decoding of binary image formats.
- Uses Pygame for rendering the image.
- Beginner friendly.

### convert.py

`convert.py` is a Python script aimed at converting PNG images to a custom format, which can later be decoded and opened using `load.py`. Key functionalities include:

- Easy and fast conversion of PNG to a custom format.
- Simple to use with clear command-line arguments.

### start.py

`start.py` is a versatile script that handles two functionalities: loading and displaying a custom image format using Pygame (`load` mode) and converting PNG images to a custom format (`convert` mode). Key features include:

- Versatile start with dual functionality.
- Combines the functionalities of `load.py` and `convert.py`.
- Clear and easy command-line interface.

## Installation

To get started with these projects, follow the steps below:

1. Clone this repository to your local machine (Requires Git to be installed):

   ```bash
   git clone https://github.com/yourusername/custom-python-projects.git
   cd custom-python-projects
   ```

2. Install the required dependencies. You can use `pip` to install any dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Here's how you can use each start:

### Running load.py

To run `load.py`, use the following command:

```bash
python load.py <custom_image_path>
```

### Running convert.py

To run `convert.py`, use the following command:

```bash
python convert.py <png_image_path> <custom_image_path>
```

### Running start.py

To run `start.py` in `load` mode, use the following command:

```bash
python start.py load <custom_image_path>
```

To run `start.py` in `convert` mode, use the following command:

```bash
python start.py convert <png_image_path> <custom_image_path>
```

## Example

### Running load.py:

```bash
python load.py file.custom
```

### Running convert.py:

```bash
python convert.py file.png file.custom
```

### Running start.py in `load` mode:

```bash
python start.py load file.custom
```

### Running start.py in `convert` mode:

```bash
python start.py convert file.png file.custom
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for visiting my GitHub repository! You can view more of my projects on my [GitHub profile](https://github.com/ayush-mann-0).