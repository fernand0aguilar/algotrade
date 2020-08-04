# algotrade
A machine learning approach to predicting the stock market. Not recommended for use in particularly volitile markets. This applies to both training and release.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
I am working on posting algotrade versions that do not require to be a daytrader. I have them built, but need to find them.
Note: Nvidia based Graphics Card Recommended
Successfully Built on Windows Machine
### Prerequisites

Things you need to install

```
Python - Anaconda Recommended
PIP
PyTorch
Numpy
MatPlotLib
Pandas
RobinStocks
```

### Installing

Create a model using the datacollector and algotrade script. This is done by setting a range for year, month, and day inside the data collector script. Then run the algotrade file to generate the model. Next run the client by replacing the line in robinstocks username and password with your robinhood account info.
There are different versions, but this one runs in real time.

## Pull Requests

Feel free to make a request, however I likely will not take note of it until later this year when it can be verified to work. 

## Authors

* **Sebastian Quinard** - *Main Contributor*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
