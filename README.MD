<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Further Help](#further-help)



<!-- ABOUT THE PROJECT -->
## About The Project

The Project purpose is to identify and follow ballons.

It includes:
*  Traning a network to detect ballons of all shapes
*  Taking images and processing them
*  Navigating a drone

### Built With
* [Raspberry PI 3](www.raspberrypi.org)
* PiCamera
* Drone
* [APM Planner](http://ardupilot.org/planner2)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python on the Raspberry PI and on the computer
* tensorflow on the computer


### Installation

1. Clone the repo
```sh
git clone https:://github.com/your_username_/Project-Name.git
```
2. Follow the [drone set up guide](https://youtu.be/TFDWs_DG2QY)


<!-- USAGE EXAMPLES -->
## Usage

1. On your Raspberry PI make sure to change the ip variable in scripts/script.py to your computer's IP.
2. On your computer, go to scripts/detecting and run server.py
3. On your Raspberry, go to scripts and run server.py

### Further Help

[Model Detection Training and Usage](https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/)
