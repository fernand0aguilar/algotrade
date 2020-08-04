from __future__ import print_function, division
import queue
import random
import numpy as np
import os

import requests
import yfinance as yf
import matplotlib.pyplot as plt
import datetime
from datetime import datetime, timedelta
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from rtstock.stock import Stock
import pytz
import os
import time
from Current import config
import threading
import bs4
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import robin_stocks
from robin_stocks import *
tickers = ["DDD","MMM","WBAI","WUBA","EGHT","AHC","AOS","ATEN","AIR","AAN","ABB","ABT","ANF","AGD","AWP","ACP","JEQ","AOD","ABM","AKR","ACEL","ACEL.W","ACN","ACCO","ATV","AYI","GOLF","ADX","PEO","AGRO","ADNT","ADT","ATGE","AAP","ADSW","WMS","ASIX","AVK","ACM","AEFC","AEB","AEG","AER","AJRD","AMG","MGR","AFL","MITT","AGCO","A","AEM","ADC","AL","APD","ALG","AGI","ALK","AIN","ALB","AA","ALC","ALEX","ALX","ARE","AQN","AQNA","AQNB","BABA","Y","ATI","ALLE","AGN","ALE","ADS","AFB","AWF","AB","AIO","CBH","NCV","NCZ","ACV","NIE","NFJ","ALSN","ALL","ALLY","PINE","ALTG","ALTG.W","AYX","ATUS","ACH","ALUS","ALUS.U","ALUS.W","AMBC","AMBC.W","AMC","AMCR","AEE","AMRC","AMOV","AMX","AAT","AXL","ACC","AEO","AEP","AEL","AXP","AFG","AFGB","AFGC","AFGH","AMH","AIG","AIG.WS","ARL","ARA","AWR","AMT","AVD","AWK","COLD","AMP","ABC","RYCE","AMN","AMRX","AP","APH","AXR","HKIB","AME","PLAN","FINS","AU","AXE","NLY","AM","AR","ANTM","ANH","AON","APA","AIV","APY","ARI","APO","AFT","AIF","APLE","AIT","ATR","APTV","ARMK","ABR","ARC","MT","ARCH","ADM","AROC","ARNC","ARCO","ACA","RCUS","ARD","ASC","AFC","ACRE","ARDC","ARES","AGX","ARGD","ARGO","ANET","AI","AIC","AIW","ARLO","AHH","ARR","AFI","AWI","ARW","AJG","APAM","ASA","ABG","ASX","ASGN","AHT","ASH","ASPN","AMK","ASB","AC","AIZ","AIZP","AGO","AZN","HOME","T","TBB","TBC","ATTO","ATH","ATKR","AT","ATCO","ATO","ATHM","ALV","AN","AZO","AVLR","AVB","AGR","AVNS","AVTR","AVYA","AVY","AVH","AVA","AXTA","AXS","AX","AXO","AZUL","AZRE","AZZ","BGS","BW","BGH","BMI","BCSF","BKR","BBN","BLL","BANC","BBAR","BBVA","BBD","BBDO","BCH","BLX","BSBR","BSAC","BSMX","SAN","CIB","BXS","BAC","BOH","BMO","NTB","BNS","BKU","BCS","BBDC","MCI","MPV","BNED","B","GOLD","BHC","BAX","BTE","BBX","BCE","BZH","BDX","BDXA","BDC","BRBR","BHE","BRK.A","BRK.B","BHLB","BERY","BBY","BEST","BGSF","BHP","BBL","BIG","BH","BH.A","BILL","BHVN","BIO","BIO.B","BITA","BJ","BKH","BKI","BSM","BB","BGIO","BFZ","CII","BHK","HYT","BTZ","DSU","BGR","BDJ","EGF","FRA","BFO","BGT","BOE","BME","BMEZ","BAF","BKT","BGY","BKN","BTA","BZM","MHE","BIT","MUI","MNE","MUA","BKK","BBK","BBF","BYM","BFK","BLE","BTT","MEN","MUC","MUH","MHD","MFL","MUJ","MHN","MUE","MUS","MVT","MYC","MCA","MYD","MYF","MFT","MIY","MYJ","MYN","MPA","MQT","MYI","MQY","BNY","BQH","BSE","BFY","BCX","BST","BSTZ","BSD","BUI","BHV","BLK","BGB","BGX","BSL","BE","APRN","BXG","BXC","DCF","DHF","DMB","DSM","LEO","BA","BCC","BCEI","BOOT","BAH","BWA","BORR","BXP","BXP","BSX","BOX","BYD","BPMP","BP","BPT","BRC","BHR","BHR","BHR","BDN","BWG","LND","BAK","BRFS","BGG","MNRL","BFAM","BEDU","BSA","BSIG","BV","EAT","BCO","BMY","BMY~","BTI","BRX","BRMK","BR","BKD","BAM","BBU","DTLABI","BIP","RA","BEP","BEP","BRO","BF.B","BRT","BC","BC","BC","BC","BKE","BVN","BBW","BG","BURL","BWXT","BY","PFH","CABO","CBT","COG","CACI","WHD","CADE","CAE","CAI","CAI","CAI","CAL","CRC","CWT","CALX","ELY","CPE","CPT","CCJ","CPB","CWH","GOOS","CM","CNI","CNQ","CP","CANG","CNNE","CAJ","CGC","CMD","COF","COF","COF","COF","COF","COF","CSU","BXMT","CPRI","CMO","CMO","CAH","CSL","KMX","CCL","CUK","CRS","CSV","CARR","CARS","CRI","CVNA","CSPR","CSLT","CTLT","CTT","EVR","RE","EVRG","EVRI","ES","EVTC","EVH","AQUA","XAN","XAN","EXPR","EXTN","EXR","XOM","FNB","FNB","FN","FDS","FICO","SFUN","FPAC","FPAC.U","FPAC.W","FTCH","FPI","FPI","FSLY","FBK","FFG","AGM","AGM.A","AGM","AGM","AGM","FRT","FRT","FSS","FHI","FMN","FDX","RACE","FOE","FG","FG.WS","FCAU","FNF","FIS","FMO","FINV","FAF","FBP","FCF","FHN","FHN","FR","AG","FRC","FRC","FRC","FRC","FRC","FRC","FFA","FMY","FDEU","FIF","FSD","FPF","FEI","FPL","FIV","FCT","FGB","FEO","FAM","FE","FIT","FPH","FVRR","FBC","DFP","PFD","PFO","FFC","FLC","FLT","FLNG","FND","FTK","FLO","FLS","FLR","FLY","FEAC.U","FMC","FMX","FL","F","F","F","FOR","FTS","FTV","FTV","FTAI","FTAI","FTAI","FSM","FBHS","FET","FBM","FCPT","FEDU","FNV","FC","FSB","BEN","FT","FI","FCX","FMS","FDP","RESI","FRO","FSK","FCN","FTSI","FF","GCV","GAB","GAB","GAB","GAB","GAB","GGZ","GGZ","GGT","GGT","GGT","GUT","GUT","GUT","GCAP","GLEO","GLEO.U","GLEO.W","GBL","GNT","GNT","GME","GCI","GPS","GTX","IT","GLOG","GLOG","GLOP","GLOP","GLOP","GLOP","GTES","GATX","GMTA","GCP","GNK","GNRC","GAM","GAM","GD","GE","GIS","GM","GCO","GEL","GEN","GNE","GNE","G","GPC","GNW","GEO","GPRK","GPJA","GGB","GTY","GFL","GFLU","GIX","GIX.U","GIX.WS","GIX~","GIL","GLT","GKOS","GSK","CO","GMRE","GMRE","GNL","GNL","GNL","GLP","GLP","GPN","GSL","GSL","GSLD","GLOB","GL","GL","GMED","GMS","GNC","GDDY","GOL","GFI","GSBD","GS","GS","GS","GS","GS","GS","GS","GER","GMZ","GRC","GPX","GGG","GRAF","GRAF.U","GRAF.W","EAF","GHM","GHC","GRAM","GVA","GPMT","GRP.U","GPK","GTN","GTN.A","AJX","AJXA","GWB","GDOT","GBX","GHL","GHG","GEF","GEF.B","GFF","GPI","GRUB","PAC","ASR","AVAL","SUPV","TV","GSX","GTT","GSH","GES","GGM","GPM","GOF","GBAB","GWRE","HRB","FUL","HAE","HAL","HBB","HBI","HNGR","HASI","HOG","HMY","HSC","HHS","HGH","HIG","HIG","HVT","HVT.A","HE","HCHC","HCA","HCI","HDB","HR","HTA","PEAK","HL","HL","HEI","HEI.A","HLX","HP","HLF","HRI","HCXY","HCXZ","HTGC","HRTG","PSV","HT","HT","HT","HT","HSY","HTZ","HES","HESM","HPE","HXL","HEXO","HCR","PCF","HGLB","HFRO","HFRO","HPR","HIW","HIL","HI","HRC","HTH","HGV","HLT","HNI","HMLP","HMLP","HEP","HFC","HD","HMC","HON","HMN","HZN","HTFA","HRL","HST","HLI","HOV","HHC","HWM","HPQ","HSBC","HSBC","HMI","HNP","HUBB","HUBS","HBM","HUD","HPP","HUM","HCFT","HII","HUN","HUYA","H","HY","IAA","IAG","IBN","IDA","IEX","IDT","INFO","ITW","IMAX","ICD","IHC","IRT","IFN","IBA","INFY","ING","IR","NGVT","INGR","IIPR","IIPR","IPHI","INSI","NSP","INSP","IBP","ITGR","I","ICE","IHG","IFS","IBM","IFF","IFFT","IGT","IP","INSW","INSW","IPV","IPV.U","IPV.WS","IPG","IPI","IVC","VBF","VCV","VTA","IHIT","IHTA","VLT","IVR","IVR","IVR","IVR","OIA","VMO","VKQ","VPV","IVZ","IQI","VVR","VTN","VGM","IIM","IRET","IRET","NVTA","INVH","IO","IQV","IRM","IRS","ICL","STAR","STAR","STAR","STAR","ITCB","ITUB","ITT","IVH","JPM","JPM","JPM","JPM","JPM","JPM","JAX","JILL","JCP","SJM","JBL","J","JHX","JHG","JOF","JBGS","JEF","JELD","JCAP","JCAP","JT","JKS","JMP","JBT","BTO","HEQ","JHS","JHI","HPF","HPI","HPS","PDT","HTD","HTY","JW.A","JW.B","JNJ","JCI","JLL","JMIA","JIH","JIH.U","JIH.WS","JNPR","JP","JE","JE","LRN","KAI","KDMN","KAMN","KSU","KSUKAR","KMF","KYN","KB","KBH","KBR","K","KEM","KMPR","WWW","WF","WK","INT","WWE","WOR","WPP","WPX","WYND","WH","XYF","XFLT","XHR","XRX","XIN","XPO","XYL","AUY","YELP","YETI","YEXT","YRD","DAO","YPF","YUMC","YUM","ZEN","ZBH","ZTS","ZTO","ZUO","ZYME", "CAT","CATO","CBZ","CBL","CBL","CBL","CBO","IGR","CBRE","CBX","FUN","CDR","CDR","CDR","CE","CLS","CELG~","CEL","CPAC","CX","CVE","CNC","CEN","CNP","CNP","EBR","EBR.B","CEPU","CCS","CTL","CDAY","CF","GIB","ECOM","CHAP","CHRA","CRL","CLDT","CMCM","CHGG","CHE","CC","CHMI","CHMI","CHMI","CHK","CHK","CPK","CVX","CHWY","CHS","CIM","CIM","CIM","CIM","CIM","DL","CEA","CHN","CGA","LFC","CHL","COE","SNP","XRF","ZNH","CHA","CHU","CYD","CMG","CHH","CB","CHT","CHD","CCX","CCX.U","CCX.WS","CCXX","CCXX.U","CCXX.W","CIEN","CI","XEC","CBB","CBB","CNK","CINR","CIR","CIT","CIT","CCAC","CCAC.U","CCAC.W","BLW","C","C","C","C","C","CFG","CFG","CFG","CIA","CIO","CIO","CVEO","CCC","CLH","CCO","EMO","CEM","CTR","CLW","CWEN","CWEN.A","CLF","CLPR","CLX","CLDR","NET","CMS","CMS","CMSA","CMSC","CMSD","CNA","CNF","CNHI","CNO","CEO","CNXM","CNX","KOF","KO","CCEP","CDE","FOF","CNS","UTF","LDP","MIE","RQI","RNP","PSF","RFI","CFX","CFXA","CL","CCH","CCH.U","CCH.WS","CXE","CIF","CXH","CMU","CLNY","CLNY","CLNY","CLNY","CLNY","CLNC","CXP","STK","CCZ","CMA","FIX","CMC","CBU","CYH","CHCT","CIG","CIG.C","CBD","SBS","ELP","CCU","CODI","CODI","CODI","CMP","CRK","CAG","CXO","CCM","CNMD","COP","CCR","CEIX","ED","STZ.B","CSTM","TCS","CLR","VLRS","CTRA","CTB","CPS","CTK","CPA","CLB","CXW","CLGX","CORR","CORR","CPLG","COR","CNR","GLW","CAAP","GYC","OFC","CTVA","CZZ","CMRE","CMRE","CMRE","CMRE","CMRE","COTY","CUZ","CVA","CVIA","CPF","CR","CRD.A","CRD.B","BAP","CS","CPG","CEQP","CEQPCR","CRT","CAPL","CCI","CCI","CCK","CRY","CTS","CUBE","CUB","CFR","CULP","CMI","CURO","CW","SRF","SRV","SZC","CWK","CUBB","CUBI","CUBI","CUBI","CUBI","CUBI","CVI","UAN","CVS","CELP","DHI","DAN","DHR","DHR","DAC","DQ","DRI","DAR","DVA","DCP","DCP","DCP","DECK","DE","DEX","DDF","DKL","DK","DELL","DLPH","DAL","DLX","DNR","DBI","DESP","DB","DXB.CL","DVN","DHX","DHT","DO","DSSI","DRH","DSX","DSX","DKS","DBD","DLR","DLR","DLR","DLR","DLR","DLR","DLR","DDS","DDT","DIN","DFS","DNI","DMYT","DMYT.U","DMYT.W","DLB","DG","D","DCUE","DRUA","DPZ","UFS","DCI","DFIN","LPG","DSL","DBL","DLY","PLOW","DEI","DOV","DVD","DOW","RDY","DRD","DRQ","DS","DS","DS","DS","DTE","DTJ","DTP","DTQ","DTW","DTY","DCO","DSE","DNP","DTF","DUC","DPG","DUK","DUK","DUKB","DUKH","DRE","DD","DXC","DY","DLNG","DLNG","DLNG","DT","DX","DX","DX","CTA","CTA","ELF","EGIF","EXP","ECC","ECCB","ECCX","ECCY","EIC","ESTE","DEA","EGP","EMN","KODK","ETN","ETV","ETW","EV","EOI","EOS","EFT","EFL","EFF","EHT","ETX","EOT","EVN","ETJ","EFR","EVF","EVG","EVT","ETO","ETG","ETB","EXD","ETY","EXG","ECT","ECL","EC","EPC","EIX","EW","EP","EE","ELAN","ELAT","ESTC","EGO","ESI","ELVT","LLY","EFC","EFC","EARN","ERJ","EME","EEX","EBS","EMR","ESRT","EIG","EDN","ENBL","ENB","ENBA","EHC","DAVA","EXK","ENIA","ENIC","ENR","ENR","ET","ETP","ETP","ETP","EPAC","ERF","ENS","E","ENLC","EBF","ENVA","NPO","ETM","EAB","EAE","EAI","ETR","ELC","ELJ","ELU","EMP","ENJ","ENO","ETIEZT","EPD","EVC","ENV","NVST","EVA","ENZ","EOG","EPAM","EPR","EPR","EPR","SWP","SWT","STN","SGU","SRT","STWD","STT","STT","STT","SPLP","SPLP","SCS","SCA","SCM","SCL","STE","STL","STL","STC","SF","SF","SF","SFB","STM","EDF","EDI","STON","SRI","STOR","GJH","GJO","GJS","SYK","MSC","RGR","SPH","SMFG","INN","INN","INN","SUM","SMLP","SUI","SLF","SXC","SU","STG","NOVA","SUN","SHO","SHO","SHO","SPN","SUP","SUZ","SWZ","SWCH","SBE","SBE.U","SBE.WS","SYF","SYF","SNX","SNV","SNV","SNV","GJP","GJR","GJT","SYY","SYX","TLRD","TWN","TSM","TAK","TAL","TGE","TALO","SKT","TPR","NGLS","TRGP","TGT","TARO","TTM","TCO","TCO","TCO","TMHC","TRP","TCP","TSI","TEL","TISI","FTI","TECK","TK","TGP","TGP","TGP","TNK","TGNA","TRC","HQH","THQ","HQL","THW","TDOC","TEO","TDY","TFX","VIV","TEF","TDA","TDE","TDI","TDJ","TDS","TU","TDF","EMF","TEI","GIM","TPX","TS","TME","THC","TNC","TEN","TVC","TVE","TDC","TEX","TX","TRNO","TTI","TEVA","TPL","TGH","TXT","TFII","AES","BK","BK","BX","CEE","SCHW","SCHW","SCHW","COO","GDV","GDV","GDV","GDV","GRX","GRX","GDL","GDL","THG","THGA","MSG","RUBI","TRV","VAM","TMO","THR","TPRE","TSLF","TCRW","TCRZ","TRI","THO","TDW","TDW.WS","TDW.WS","TIF","TLYS","TSU","TKR","TMST","TWI","TJX","TOL","TR","BLD","TTC","TD","SHLL","SHLL.U","SHLL.W","NDP","TYG","TEAF","NTG","TTP","TPZ","TOT","TSQ","TM","TRTX","TSLX","TT","TAC","TCI","TDG","RIG","TGS","TRU","TREC","TG","THS","TREX","TY","TYTPH","TRNE","TRNE.U","TRNE.W","TNET","TRN","TSE","TPVG","TPVY","GTS","TRTN","TRTN","TRTN","TRTN","TRTN","TGI","TROX","TBI","TFC","TFC","TFC","TFC","TFC","TNP","TNP","TNP","TNP","TNP","TUFN","TUP","TKC","TPB","TRQ","TPC","TWLO","TRWH","TWTR","TWO","TWO","TWO","TWO","TWO","TWO","TYL","TSN","USB","USB","USB","USB","USB","USB","USPH","SLCA","USX","UBER","UI","UBS","UDR","UGI","UGP","UMH","UMH","UMH","UMH","UA","UAA","UFI","UNF","UN","UL","UNP","UIS","UNT","UMC","UNFI","UPS","URI","USM","UZA","UZB","UZC","X","UNH","UTL","UNVR","UVV","UHT","UHS","UVE","UTI","UNM","UNMA","UE","UBA","UBP","UBP","UBP","USFD","USAC","USNA","USDP","BIF","VFC","EGY","MTN","VAL","VALE","VLO","VHI","VMI","VVV","VAPO","VAR","VGR","VEC","VEDL","VEEV","VEL","VNTR","VTR","VNE","VER","VER","VRTV","VZ","VET","VRS","VCIF","VERT.U","VRT","VRT.WS","VVI","VICI","VNCE","VIPS","SPCE","VGI","ZTR","V","VSH","VPG","VIST","VSTO","VST","VST.WS","VVNT","VVNT.W","VSLR","VMW","VOC","VCRA","VNO","VNO","VNO","VNO","VJET","IAE","IHD","VOYA","VOYA","IGA","IGD","IDE","IID","IRR","PPR","VMC","WTI","WPC","WRB","WRB","WRB","WRB","WRB","WRB","GRA","GWW","WNC","WBC","WDR","WD","WMT","DIS","HCC","WPG","WPG","WPG","WRE","WCN","WM","WAT","WSO","WSO.B","WTS","W","WBS","WBS","WEC","WEI","WRI","WMK","WBT","WFC","WFC","WFC","WFC","WFC","WFC","WFC","WFC","WFC","WFC","WFC","WFC","WFC","EOD","WELL","WCC","WST","WAL","WALA","WEA","TLI","EMD","GDO","EHI","HIX","HIO","HYI","SBI","IGI","PAI","MMU","WMC","DMO","MTT","MHF","MNP","GFY","WIW","WIA","WES","WU","WAB","WLK","WLKP","WBK","WRK","WHG","WEX","WY","WPM","WHR","WTM","WSR","WLL","WOW","WMB","WSM","WGO","WIT","WNS","OPY","ORCL","ORAN","ORC","OEC","ORN","IX","ORA","OSK","OR","SFTW","SFTW.U","SFTW.W","OTIS","OUT","OSG","OVV","OMI","OC","ORCC","OXM","ROYT","PACD","PCG","PKG","PD","PAGS","PANW","PAM","PHX","PARR","PAR","PGRE","PKE","PK","PH","PE","PSN","PRE","PRE","PRE","PRE","PRTY","PAYC","PBF","PBFX","BTU","PSO","PEB","PEB","PEB","PEB","PEB","PBA","PEI","PEI","PEI","PEI","PFSI","PMT","PMT","PMT","PAG","PNR","PEN","PFGC","PKI","PBT","PVL","PRT","PRGO","PRSP","PTR","PBR","PBR.A","PFE","GHY","ISD","PGTI","PM","PSX","PSXP","FENG","DNK","PHR","DOC","PDM","PCQ","PCK","PZC","PCM","PTY","PCN","PCI","PDI","NRGX","PGP","PHK","PKO","PFL","PFN","PMF","PML","PMX","PNF","PNI","PYN","RCS","PING","PNW","PINS","PHD","PHT","MAV","MHI","PXD","PIPR","PBI","PBI","PIC","PIC.U","PIC.WS","PJT","PAA","PAGP","PLNT","PLT","AGS","PHI","PLYM","PNC","PNC","PNC","PNM","PII","POL","POR","PKX","POST","PSTL","PPG","PPX","PPL","PYS","PYT","PQG","PDS","APTS","PBH","PVG","PRI","PRMW","PGZ","PRIF","PRIF","PRIF","PRIF","PRIF","PRIF","PRA","PG","PGR","PLD","PUMP","PRO","PROS","PBB","PBC","PBY","PB","PRLB","PFS","PJH","PRH","PRS","PRU","PUK","PUKPUK","PSB","PSB","PSB","PSB","PSB","TLK","PEG","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PSA","PHM","PSTG","PMM","PIM","PMO","PPT","NEW","PVH","PYX","PZN","QTWO","QEP","QGEN","QTS","QTS","QTS","QUAD","KWR","NX","PWR","QD","DGX","QES","QUOT","QVCC","QVCD","CTAA","CTBB","CTDD","CTV","CTY","CTZ","RRD","RMED","RDN","RFL","RL","RRC","RNGR","PACK","PACK.W","RJF","RYAM","RYN","RTX","RMAX","RC","RCA","RCB","RCP","RLGY","O","RLH","RWT","RBC","RM","RF","RF","RF","RF","RGS","RGA","RZA","RZB","RS","RELX","RNR","RNR","RNR","SOL","RENN","RPLA","RPLA.U","RPLA.W","RSG","REZI","RMD","RFP","QSR","RPAI","RVI","REVG","REV","RVLV","REX","REXR","REXR","REXR","REXR","RXN","RH","RNG","RIO","RBA","RAD","RFM","RMM","RMI","RIV","RMPLRS","OPP","RLI","RLJ","RLJ","RMG","RMG.U","RMG.WS","RRTS","RHI","ROK","RCI","ROG","ROL","ROP","RST","RY","RY","RBS","RCL","RDS.A","RDS.B","RGT","RMT","RVT","RES","RPM","RPT","RPT","RTW","RYB","R","RYI","RHP","SPGI","SBR","SB","SB","SB","SFE","SAFE","SAIL","CRM","SMM","SBH","SJT","SD","PER","SAND","SC","SAP","SAF","SAR","SSL","BFS","BFS","BFS","SCPE","SCPE.U","SCPE.W","SLB","SNDR","SWM","SAIC","SALT","SBNA","STNG","SMG","KTF","KSM","SRL","SCU","SCVX","SCVX.U","SCVX.W","SE","SA","CKH","SMHI","SDRL","SEE","SEAS","JBN","JBR","WTTR","SEM","SRE","SRE","SRE","SREA","ST","SXT","SQNS","SRG","SRG","SCI","SERV","NOW","SFL","SHAK","SJR","SHLX","SHW","SHG","SHOP","SSTK","SBSW","SIG","SBOW","SI","SPG","SPG","SSD","SHI","SITC","SITC","SITC","SITE","SIX","SJW","SKM","SKX","SKY","SLG","SLG","WORK","SM","SMAR","SNN","SNAP","SNA","SQM","SOGO","SOI","SWI","SAH","SON","SNE","SOR","SJI","SJIJ","SJIU","SCE","SCE","SCE","SCE","SCE","SO","SOJA","SOJB","SOJC","SOJD","SOLN","SCCO","LUV","SWX","SWN","SPAQ","SPAQ.U","SPAQ.W","SPE","SPE","SPB","SR","SR","SPR","SAVE","SRC","SRC","SPOT","SRLP","SPXC","FLOW","SQ","JOE","STAG","STAG","SSI","SMP","SXI","SWK", "KMT","KW","KEN","KDP","KEY","KEY","KEY","KEY","KEYS","KRC","KRP","KMB","KIM","KIM","KIM","KMI","KFS","KGC","KEX","KL","KRG","KKR","KKR","KKR","KIO","KREF","KNX","KNL","KNOP","KN","KSS","PHG","KTB","KOP","KEP","KF","KFY","KOS","KRA","KR","KRO","KT","LB","SCX","LHX","LH","LADR","LAIX","LW","LCI","LPI","LVS","LTM","LGI","LAZ","LZB","LCII","LEAF","LEA","LEE","LGC","LGC.U","LGC.WS","LM","LMHA","LMHB","LEG","JBK","KTH","KTN","KTP","LDOS","LEJU","LC","LEN","LEN.B","LII","LHC","LHC.U","LHC.WS","LEVI","LXP","LXP","LPL","DFNS","DFNS.U","DFNS.W","USA","ASG","LBRT","LSI","LITB","LNC","LIN","LNN","LN","LINX","LGF.A","LGF.B","LAD","LAC","LYV","LTHM","RAMP","LYG","SCD","LMT","L","LOMA","LPX","LOW","LXU","LTC","LUB","LL","LXFR","LDL","LYB","MTB","MDC","MHO","MAC","CLI","MFD","MGU","MIC","BMA","M","MCN","MSGE$","MSGS$","MMP","MGA","MX","MGY","MH","MH","MH","MHLA","MHNC","MAIN","MMD","MNK","MANU","MTW","MN","MAN","MFC","MRO","MPC","MMI","MCS","MPX","HZO","MKL","VAC","MMC","MLM","MAS","DOOR","MTZ","MA","MTDR","MTRN","MATX","MLP","MAXR","MMS","MXL","MEC","MBI","MKC","MKC.V","MCD","MUX","MCK","MDU","MTL","MTLMDL","MPW","MED","MCC","MCV","MCX","MDLQ","MDLX","MDLY","MD","MDT","MFAC","MFAC.U","MFAC.W","MRK","MCY","MDP","MTH","MTOR","MER","PIY","MTR","MSB","MEI","MET","MET","MET","MET","MCB","MTD","MXE","MXF","MFA","MFA","MFA","MFO","MCR","MGF","MIN","MMT","MFM","MFV","MTG","MGP","MGM","MFGP","MAA","MAA","AMPY","MLR","HIE","MTX","MG","MUFG","MIXT","MFG","MBT","MODN","MOD","MC","MOGU","MHK","MOH","TAP.A","MNR","MNR","MR","MCO","MOG.A","MOG.B","MS","MS","MS","MS","MS","MS","MS","CAF","MSD","EDD","IIF","MOS","MSI","MOV","MPLX","MRC","HJV","MSA","MSM","MSCI","MSGN","MLI","MWA","MVF","MZA","MUR","MUSA","MVO","MVC","MVCD","MYE","MYOV","NBR","NBR","NC","NTP","NTEST","NTEST.","NTEST.","NTEST.","NBHC","NFG","NGG","NHI","NOV","NPK","NNN","NNN","NRUC","SID","NSA","NSA","NTCO","NGS","NGVC","NRP","NTZ","NLS","NVGS","NNA","NM","NM","NM","NMM","NAV","NAV","NCR","NP","NNI","NPTN","NSCO","NSCO.W","NVRO","HYB","NFH","NFH.WS","GF","NWHM","IRL","NMFC","NMFX","EDU","NEWR","NRZ","NRZ","NRZ","NRZ","SNR","NYCB","NYCB","NYCB","NYT","NJR","NEU","NEM","NR","NEXA","NREF","NXRT","NHF","NEP","NEE","NEE","NEE","NEE","NEE","NEE","NEE","NEX","NGL","NGL","NGL","NMK","NMK","NLSN","NKE","NINE","NIO","NI","NI","NL","NOAH","NE","NOK","NOMD","NMR","OSB","NAT","JWN","NSC","NOA","NRT","NOC","NWN","NWE","NCLH","NVS","NVO","DNOW","NRG","NUS","NUE","NS","NS","NS","NS","NSS","NTR","JMLP","NVG","NUV","NUW","NEA","NAZ","NKX","NCB","NCA","NAC","JCE","JCO","JQC","JDD","DIAX","JEMD","JMF","NEV","JFR","JRO","NKG","JGH","JHY","JHAA","JHB","NXC","NXN","NID","NMY","NMT","NUM","NMS","NOM","JLS","JMM","NHA","NZF","NMCO","NMZ","NMI","NJV","NXJ","NRK","NYV","NNY","NAN","NUO","NPN","NQP","JPC","JPS","JPT","JPI","NAD","JRI","JRS","BXMX","SPXX","NIM","NXP","NXQ","NXR","NSL","JSD","NBB","JTD","JTA","NPV","NIQ","NVT","NVR","CTEST","CTEST.","CTEST.","CTEST.","CTEST.","CTEST.","CTEST.","OAC","OAC.U","OAC.WS","OAK","OAK","OXY","OII","OCN","OFG","OFG","OFG","OFG","OGE","OI","OIBR.C","OIS","ODC","ORI","OLN","OHI","OMC","ONDK","OGS","OLP","OCFT","OMF","OKE","ONE","ONTO","OOMA","EPR","EQM","EQT","EFX","EQNR","EQH","EQH","ETRN","EQC","EQC","ELS","EQR","EQS","ERA","EROS","ESE","ESNT","EPRT","WTRG","WTRU","ESS","EL","ETH","EURN","EEA","EB"]
login = robin_stocks.authentication.login("username", "password")
print(robin_stocks.profiles.load_account_profile())

GAIN = 1.02
LOSS = 0.98
DELAY = 0
AVERAGE_TOTAL = 1
INTERVAL = 30
RESOLUTION = 1
IMAGE_SIZE = 70
BATCH_SIZE = 1


def stockReader():
    # A set of the stock data, lol
    class StockDataset(Dataset):
        def __init__(self, root_dir, transform=None):

            self.root_dir = os.getcwd() + root_dir
            self.files = []
            for file in os.listdir(self.root_dir):
                if file.endswith('.png'):
                    self.files.append(str(file))

            self.transform = transform

        def __len__(self):
            return len(self.files)

        def __getitem__(self, idx):
            if torch.is_tensor(idx):
                idx = idx.tolist()

            img_name = self.files[idx]

            if img_name.split(".")[0] == "stable":
                self.solution = 500
            elif img_name.split(".")[0] == "rise":
                self.solution = 750
            else:
                self.solution = 250
            img_name = self.root_dir + "\\" + img_name

            image = io.imread(img_name)

            sample = {"image": image, "solution": self.solution}

            if self.transform:
                sample['image'] = self.transform(sample['image'])

            return sample

    # Apply each of the above transforms on sample.
    transformed_dataset = StockDataset(root_dir='\\DATA', transform=transforms.Compose([
        transforms.ToPILImage(),
        transforms.Grayscale(num_output_channels=3),
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5]),
    ]))

    # for i in range(len(transformed_dataset)):
    #    sample = transformed_dataset[i]
    #
    #    print(i, sample['image'].size(), sample['solution'])
    #
    #    if i == 3:
    #        break

    dataloader = DataLoader(transformed_dataset, batch_size=BATCH_SIZE, pin_memory=True,
                            shuffle=False, num_workers=0)

    test = transformed_dataset
    testloader = dataloader
    files = []
    for file in os.listdir(os.getcwd() + "\\DATA"):
        if file.endswith('.png'):
            files.append(str(file))
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        print(torch.cuda.get_device_name(0))
    else:
        device = torch.device("cpu")
    net = torchvision.models.resnet152(pretrained=False).to(device)
    net.load_state_dict(torch.load("inferenceDAYTRADE5.pt"))
    stocks = []
    net = net.eval()
    criterion = nn.CrossEntropyLoss()
    i = 0
    for data in testloader:
        images, labels = data.get("image").to(device), data.get("solution").to(device)
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        print(predicted)
        if predicted == torch.tensor([750]).to(device):
            probabilities = F.softmax(outputs, dim=1)
            if probabilities[0][750] > 0.59:
                print(probabilities[0][750])
                print(files[i])
                stocks.append(files[i].split(".")[1])
        i += 1
    if len(stocks) == 0:
        print("no stocks in this period")
    if len(stocks) <= 12 and not (len(stocks) == 0):
        buyingPower = float(robin_stocks.profiles.load_account_profile().get("portfolio_cash"))
        tradeable = buyingPower - 26400
        available = tradeable / len(stocks)
        sharesArray = []
        for stock in stocks:
            price = float(robin_stocks.get_latest_price(stock)[0])
            shares = int(available // price)
            sharesArray.append(shares)
            robin_stocks.order_buy_market(stock, shares)
            robin_stocks.order_sell_stop_loss(stock, shares, price * 0.9925)
        time.sleep(300)
        i = 0
        for stock in stocks:
            robin_stocks.order_sell_market(stock, sharesArray[i])
            i +=1

    filelist = [f for f in os.listdir(os.getcwd() + "\\DATA") if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join(os.getcwd() + "\\DATA", f))

def stockGrabber(tickers):
    if AVERAGE_TOTAL >= (INTERVAL // RESOLUTION) // 2:
        raise NameError("Average Total cannot be less than half the Interval over Resolution.")
    now = datetime.now()
    tz = pytz.timezone('US/Eastern')

    fig = plt.Figure()
    ax = fig.add_subplot()
    symbols = random.sample(tickers, 25)
    data = {}
    past = now
    future = past + timedelta(seconds=300)
    j = 0
    while datetime.now() < future:
        for symbol in symbols:
            try:
                r = requests.get("https://finance.yahoo.com/quote/" + symbol + "?p="+symbol)
                soup = bs4.BeautifulSoup(r.text, "html.parser")
                price = float(soup.find(class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").text)
                timestamps = {
                    datetime.now(): price,
                }
                if symbol in data:
                    data.get(symbol).update({datetime.now(): price})
                else:
                    data.update({symbol: timestamps})
            except:
                print("symbol could not be found")
        j += 1
        if j > 5:
            break
        time.sleep(60)
    for symbol in data:
       try:
           ref = data.get(symbol).get(next(iter(data.get(symbol))))
           ax.set_ylim(ref * .95, ref * 1.05)
           ax.set_xlim(past, datetime.now())
           ax.plot(list(data.get(symbol).keys()), list(data.get(symbol).values()))
           fig.savefig(os.getcwd() + "\\DATA\\" + "current." + symbol + ".png", bbox_inches='tight')
           del ax.lines
       except:
           print("File Created")



i = 0
if __name__ == "__main__":
    while datetime.now().hour < 15:
        print("********************************************************")
        P1 = threading.Thread(target=stockGrabber, args=(tickers,))
        P2 = threading.Thread(target=stockGrabber, args=(tickers,))
        P3 = threading.Thread(target=stockGrabber, args=(tickers,))
        P4 = threading.Thread(target=stockGrabber, args=(tickers,))
        P5 = threading.Thread(target=stockGrabber, args=(tickers,))
        P6 = threading.Thread(target=stockGrabber, args=(tickers,))
        P7 = threading.Thread(target=stockGrabber, args=(tickers,))
        P8 = threading.Thread(target=stockGrabber, args=(tickers,))
        P9 = threading.Thread(target=stockGrabber, args=(tickers,))
        P10 = threading.Thread(target=stockGrabber, args=(tickers,))
        P11 = threading.Thread(target=stockGrabber, args=(tickers,))
        P12 = threading.Thread(target=stockGrabber, args=(tickers,))
        P13 = threading.Thread(target=stockGrabber, args=(tickers,))
        P14= threading.Thread(target=stockGrabber, args=(tickers,))
        P15= threading.Thread(target=stockGrabber, args=(tickers,))
        P16= threading.Thread(target=stockGrabber, args=(tickers,))
        P17= threading.Thread(target=stockGrabber, args=(tickers,))
        P18= threading.Thread(target=stockGrabber, args=(tickers,))
        if i != 0:
            P0 = threading.Thread(target=stockReader(), )
            P0.start()
            time.sleep(2)
        P1.start()
        P2.start()
        P3.start()
        P4.start()
        P5.start()
        P6.start()
        P7.start()
        P8.start()
        P9.start()
        P10.start()
        P11.start()
        P12.start()
        P13.start()
        P14.start()
        P15.start()
        P16.start()
        P17.start()
        P18.start()
        P1.join()
        P2.join()
        P3.join()
        P4.join()
        P5.join()
        P6.join()
        P7.join()
        P8.join()
        P9.join()
        P10.join()
        P11.join()
        P12.join()
        P13.join()
        P14.join()
        P15.join()
        P16.join()
        P17.join()
        P18.join()
        i += 1


