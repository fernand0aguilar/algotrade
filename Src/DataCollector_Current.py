import numpy as np
import os
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
import pandas as pd
import iexfinance
from iexfinance.stocks import get_historical_intraday
import alpaca_trade_api as ata

api = ata.REST('<key_id>', '<secret_key>')


tickers = ['MMM', "AOS", "ABT", "ABBV", "ACN", "ATVI", "AYI", "ADBE", "AAP", "AMD", "AES", "AET", "AMG", "AFL", "A", "APD", "ALK", "AKAM", "ALB", "ARE", "ALXN", "ALGN", "ALLE", "AGN", "ADS", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "APC", "ADI", "ANDV", "ANSS", "ANTM", "AON", "APA", "AIV", "AAPL", "AMAT", "APTV", "ADM", "ARNC", "AJG", "AIZ", "T", "ADSK", "ADP", "AZO", "AVB", "AVY", "BHGE", "BLL", "BAC", "BAX", "BBT", "BDX", "BRK.B", "BBY", "BIIB", "BLK", "HRB", "BA", "BKNG", "BWA", "BXP", "BSX", "BHF", "BMY", "AVGO", "BF.B", "CHRW", "CA", "COG", "CDNS", "CPB", "COF", "CAH", "KMX", "CCL", "CAT", "CBOE", "CBRE", "CBS", "CELG", "CNC", "CNP", "CTL", "CERN", "CF", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "XEC", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "CXO", "COP", "ED", "STZ", "GLW", "COST", "COTY", "CCI", "CSRA", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DAL", "XRAY", "DVN", "DLR", "DFS", "DISCA", "DISCK", "DISH", "DG", "DLTR", "D", "DOV", "DWDP", "DPS", "DTE", "DUK", "DRE", "DXC", "ETFC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ETR", "EVHC", "EOG", "EQT", "EFX", "EQIX", "EQR", "ESS", "EL", "RE", "ES", "EXC", "EXPE", "EXPD", "ESRX", "EXR", "XOM", "FFIV", "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FISV", "FLIR", "FLS", "FLR", "FMC", "FL", "F", "FTV", "FBHS", "BEN", "FCX", "GPS", "GRMN", "IT", "GD", "GE", "GGP", "GIS", "GM", "GPC", "GILD", "GPN", "GS", "GT", "GWW", "HAL", "HBI", "HOG", "HRS", "HIG", "HAS", "HCA", "HCP", "HP", "HSIC", "HES", "HPE", "HLT", "HOLX", "HD", "HON", "HRL", "HST", "HPQ", "HUM", "HBAN", "HII", "IDXX", "INFO", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JBHT", "JEC", "SJM", "JNJ", "JCI", "JPM", "JNPR", "KSU", "K", "KEY", "KMB", "KIM", "KMI", "KLAC", "KSS", "KHC", "KR", "LB", "LLL", "LH", "LRCX", "LEG", "LEN", "LUK", "LLY", "LNC", "LKQ", "LMT", "L", "LOW", "LYB", "MTB", "MAC", "M", "MRO", "MPC", "MAR", "MMC", "MLM", "MAS", "MA", "MAT", "MKC", "MCD", "MCK", "MDT", "MRK", "MET", "MTD", "MGM", "KORS", "MCHP", "MU", "MSFT", "MAA", "MHK", "TAP", "MDLZ", "MON", "MNST", "MCO", "MS", "MSI", "MYL", "NDAQ", "NOV", "NAVI", "NKTR", "NTAP", "NFLX", "NWL", "NFX", "NEM", "NWSA", "NWS", "NEE", "NLSN", "NKE", "NI", "NBL", "JWN", "NSC", "NTRS", "NOC", "NCLH", "NRG", "NUE", "NVDA", "ORLY", "OXY", "OMC", "OKE", "ORCL", "PCAR", "PKG", "PH", "PAYX", "PYPL", "PNR", "PBCT", "PEP", "PKI", "PRGO", "PFE", "PCG", "PM", "PSX", "PNW", "PXD", "PNC", "RL", "PPG", "PPL", "PX", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PSA", "PHM", "PVH", "QRVO", "QCOM", "PWR", "DGX", "RRC", "RJF", "RTN", "O", "RHT", "REG", "REGN", "RF", "RSG", "RMD", "RHI", "ROK", "COL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SCG", "SLB", "STX", "SEE", "SRE", "SHW", "SPG", "SWKS", "SLG", "SNA", "SO", "LUV", "SWK", "SBUX", "STT", "SRCL", "SYK", "STI", "SIVB", "SYMC", "SYF", "SNPS", "SYY", "TROW", "TTWO", "TPR", "TGT", "TEL", "FTI", "TXN", "TXT", "BK", "CLX", "COO", "HSY", "MOS", "TRV", "DIS", "TMO", "TIF", "TWX", "TJX", "TMK", "TSS", "TSCO", "TDG", "TRIP", "FOXA", "FOX", "TSN", "USB", "UDR", "ULTA", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI", "UTX", "UHS", "UNM", "VFC", "VLO", "VAR", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VIAB", "V", "VNO", "VMC", "WMT", "WBA", "WM", "WAT", "WEC", "WFC", "WELL", "WDC", "WU", "WRK", "WY", "WHR", "WMB", "WLTW", "WYN", "WYNN", "XEL", "XRX ", "XLNX", "XL", "XYL", "YUM", "ZBH","ZION","ZTS"]
GAIN = 1.02
LOSS = 0.98
DELAY = 0
AVERAGE_TOTAL = 1
INTERVAL = 30
RESOLUTION = 1

if AVERAGE_TOTAL >= (INTERVAL // RESOLUTION) // 2:
    raise NameError("Average Total cannot be less than half the Interval over Resolution.")
now = datetime.now()
for ticker in tickers:

        calendar = datetime.strptime(str(now.year) + "-" + str(now.month) + "-" + str(now.day), "%Y-%m-%d")
        fig = plt.Figure()
        ax = fig.add_subplot()
        finish = None
        start = None
        if now.minute - DELAY < 0:
            finish = pd.to_datetime(datetime(now.year, now.month, now.day-2, now.hour, 59-now.minute-DELAY))
        else:
            finish = pd.to_datetime(datetime(now.year, now.month, now.day-2, now.hour, now.minute-DELAY))
        if now.minute - 30 - DELAY < 0:
            start = pd.to_datetime(datetime(2020, now.month, now.day, now.hour, now.minute-DELAY + 30))
        else:
            start = pd.to_datetime(datetime(2020, now.month, now.day, now.hour, now.minute-DELAY - 30))
        try:
            data = ata.REST().polygon.historic_trades_v2(ticker, now.date(), start)
            print(data)
            ref = data.loc[start][0]
            ax.set_ylim(ref * .90, ref * 1.10)
            ax.plot(data.loc[start:finish, "price"])
            fig.savefig("current." + str(now.day) + "-" + str(now.hour) + " - " + str(now.minute)
                        + " - " + ticker + ".png", bbox_inches='tight')
            del ax.lines
        except:
            print("AHH!!")
