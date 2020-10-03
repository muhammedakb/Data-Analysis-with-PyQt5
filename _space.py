import sys
from PyQt5 import QtWidgets
from _spaceForm import Ui_MainWindow
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def okuAnalizNba():
    nbaData = pd.read_csv("nba.csv")
    df = pd.DataFrame(nbaData)
    
    # Takımlardaki Oyuncu Sayısı
    oyuncuSayi = df["Team"].value_counts()
    # oyuncuSayi.head(10).plot.bar()
    # plt.legend()
    # plt.xlabel("TAKIMLAR")
    # plt.ylabel("OYUNCU SAYILARI")
    # plt.show()

    # Takımlara Göre Ortalama Maaş
    teamAvgSalary = df.groupby("Team").mean()["Salary"]
    # teamAvgSalary.plot.pie(autopct='%.2f',subplots=True)
    # plt.show()

    # Yaşı 20-25 oyuncular
    ageAralik = df[(df["Age"]<=25) & (df["Age"]>=20)][["Age","Name","Team"]].sort_values("Age", ascending = False)
   
    # En yüksek maaş
    e = df["Salary"].max()
    richest = df[df["Salary"] == e][["Name","Salary"]]
   
    # Ortalama Maaş
    avgSalary = df["Salary"].mean()
    
okuAnalizNba()

def okuAnalizYoutube():
    youtubeData = pd.read_csv("youtube-ing.csv")
    dfY = pd.DataFrame(youtubeData)

    # Like-Dislike Ortalaması
    veri = len(dfY)
    likesAvg = dfY["likes"].mean()
    dislikesAvg = dfY["dislikes"].mean()
    #print(f"{veri} tane videonun like ortalaması : {likesAvg}\n{veri} tane videonun dislike ortalaması : {dislikesAvg}")
    
    # En Çok Görüntülenen Video
    b = dfY["views"].max()
    bestView = dfY[dfY["views"] == b]["title"]
    #print(f"En çok görüntülenen video : {bestView}\nGörüntülenme Sayısı :  {b}")
    
    # En Çok Görüntülenen 5 Video
    enCokOn = dfY.sort_values(by='views',ascending=False)[["title"]]
    si = enCokOn.head()
    # si.plot.bar()
    # plt.xlabel("Video")
    # plt.ylabel("Görüntülenme Sayısı")
    # plt.show()

    # Kategoriye Göre Beğeni Ortalamaları
    likeCategory = dfY.groupby("category_id").mean().sort_values("likes",ascending=False)["likes"]
    # likeCategory.plot.bar()
    # plt.legend()
    # plt.show()

    # Kategori Video Sayısı
    categoryLength = dfY["category_id"].value_counts()
    
    # Popüler Videolar
    def likedislikeoranhesapla(dataset):
        likesList = list(dataset["likes"])
        dislikesList = list(dataset["dislikes"])
        liste = list(zip(likesList,dislikesList))
        oranListesi = []
        for like,dislike  in liste: 
            if (like + dislike) == 0:
                oranListesi.append(0)
            else:
                oranListesi.append(like/(like+dislike))
        return oranListesi
    dfY["beğeni_orani"] = likedislikeoranhesapla(dfY)
    hallettim = dfY.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]]

okuAnalizYoutube()

def okuAnalizOkul():
    okulData = pd.read_excel("dataPersonel.xlsx")
    fifaData = pd.read_csv("players_20.csv")
    dfO = pd.DataFrame(okulData)
    dfF = pd.DataFrame(fifaData)

    # "Araç gereç kullanma becerisi"
    dfO.rename(columns={'2 - Çevrimiçi eğitimde kullanılan yazılım, araç ve gereçleri kullanma becerilerim,':'Araç gereç kullanma becerisi'},inplace=True)
    skillAvg = dfO.mean()
    skillMin = dfO.min()
    skillMax = dfO.max()

    # "Öğrencilerin duyuruları takibi"
    dfO.rename(columns={'18 - Çevrimiçi eğitimde, dersle ilgili yapılan duyuru ve bilgilendirmelerin öğrenciler tarafından takip edilmesi,':'Öğrencilerin duyuruları takibi'},inplace=True)
    wantAvg = dfO.mean()
    wantMax = dfO.max()
    wantMin = dfO.min()

    # "Ders kayıtlarını tekrar izleyebilme"
    dfO.rename(columns={'20 - Çevrimiçi eğitimde, öğrencilerin ders kayıtlarını sonradan yeniden izleyebilmesi,':'Ders kayıtlarını tekrar izleyebilme'},inplace=True)
    ort = dfO.mean()

    # "Top 10 Maaş"
    # a = dfF.sort_values(by='value_eur',ascending=False)[["short_name","value_eur","team_position","club"]]
    a = dfF.groupby("short_name").mean().sort_values(by='value_eur',ascending=False)[["value_eur"]]
    topSal = a.head(10)
    # topSal.plot.bar()
    # plt.ylabel("MAAŞ")
    # plt.xlabel("OYUNCULAR")
    # plt.show()

    # "Takımların Ortalama Maaşı"
    takim = dfF.groupby("club").mean().sort_values(by='value_eur',ascending=False)["value_eur"]
    ort = dfF["value_eur"].mean()
    teamSal = takim.head()
    # plt.plot(teamSal,data=dfF)
    # plt.legend()
    # plt.title("EN ÇOK MAAŞ VEREN 5 TAKIM")

    # "Takımların Yaş Ortalaması"
    takimy = dfF.groupby("club").mean().sort_values(by='value_eur',ascending=False)[["age","value_eur"]]
    teamAge = takimy.head(5)
    # teamAge.plot.pie(autopct='%.2f',subplots=True)
    
    # "Mevkii Maaş Ortalaması"
    takimm = dfF.groupby("team_position").mean().sort_values(by='value_eur',ascending=False)[["age","value_eur"]]
    mevSal = takimm.head(10)
    # mevSal.plot.pie(autopct='%.2f',subplots=True)
    # plt.legend()
    
okuAnalizOkul()

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        nba = self.ui.cbNba
        okul = self.ui.cbOkul
        youtube = self.ui.cbYoutube

        self.ui.btnLoad.clicked.connect(self.loadItems)
        self.ui.btnShowNba.clicked.connect(self.showNba)
        self.ui.btnShowYoutube.clicked.connect(self.showYoutube)
        self.ui.btnShowOkul.clicked.connect(self.showOkul)

    def showNba(self):
        result1 = 'Nba : '
        items = self.ui.groupBox_2.findChildren(QtWidgets.QComboBox)
        for cb in items:
            if cb.currentText():
                result1 += cb.currentText()
        self.ui.cbNba.setItemData(0,"New Orleans Pelicans      19\tMemphis Grizzlies        18\tMilwaukee Bucks           16\tNew York Knicks           16\tCharlotte Hornets         15\tToronto Raptors           15\nGolden State Warriors     15\tPhoenix Suns              15\tHouston Rockets           15\tIndiana Pacers            15\tDetroit Pistons           15\tMiami Heat                15\nAtlanta Hawks             15\tSan Antonio Spurs         15\tUtah Jazz                 15\tSacramento Kings          15\tCleveland Cavaliers       15\tChicago Bulls             15\nPortland Trail Blazers    15\tOklahoma City Thunder     15\tPhiladelphia 76ers        15\tDallas Mavericks          15\tLos Angeles Lakers        15\tDenver Nuggets            15\nBoston Celtics            15\tWashington Wizards        15\tBrooklyn Nets             15\tLos Angeles Clippers      15\tMinnesota Timberwolves    14\tOrlando Magic             14")
        self.ui.cbNba.setItemData(1,"Atlanta Hawks             4.860197e+06\tBoston Celtics            4.181505e+06\tBrooklyn Nets             3.501898e+06\tCharlotte Hornets         5.222728e+06\tChicago Bulls             5.785559e+06\nCleveland Cavaliers       7.642049e+06\tDallas Mavericks          4.746582e+06\tDenver Nuggets            4.294424e+06\tDetroit Pistons           4.477884e+06\tGolden State Warriors     5.924600e+06\nHouston Rockets           5.018868e+06\tIndiana Pacers            4.450122e+06\tLos Angeles Clippers      6.323643e+06\tLos Angeles Lakers        4.784695e+06\tMemphis Grizzlies         5.467920e+06\nMiami Heat                6.347359e+06\tMilwaukee Bucks           4.350220e+06\tMinnesota Timberwolves    4.593054e+06\tNew Orleans Pelicans      4.355304e+06\tNew York Knicks           4.581494e+06\nOklahoma City Thunder     6.251020e+06\tOrlando Magic             4.297248e+06\tPhiladelphia 76ers        2.213778e+06\tPhoenix Suns              4.229676e+06\tPortland Trail Blazers    3.220121e+06\nSacramento Kings          4.778911e+06\tSan Antonio Spurs         5.629516e+06\tToronto Raptors           4.741174e+06\tUtah Jazz                 4.204006e+06\tWashington Wizards        5.088576e+06")
        self.ui.cbNba.setItemData(2,"")
        self.ui.cbNba.setItemData(3,"Name      Salary\nKobe Bryant  25000000.0 €")
        self.ui.cbNba.setItemData(4,"4842684.105381166 €")
        result = self.ui.cbNba.currentData()
        self.ui.lblNba.setText(result1.upper() + ":\n" + result)



    def showYoutube(self):
        resultY = 'YouTube : '
        itemY = self.ui.groupBox.findChildren(QtWidgets.QComboBox)
        for yt in itemY:
            if yt.currentText():
                resultY += yt.currentText()
        self.ui.cbYoutube.setItemData(0,"38916 tane videonun like ortalaması : 134519.55349984582\n38916 tane videonun dislike ortalaması : 7612.559975331483")
        self.ui.cbYoutube.setItemData(1,"Nicky Jam x J. Balvin - X (EQUIS) | Video Ofic...")
        self.ui.cbYoutube.setItemData(2,"Nicky Jam x J. Balvin - X (EQUIS) | Video Ofic...\nTe Bote Remix - Casper, Nio García, Darell, Ni...\nBad Bunny - Amorfoda | Video Oficial\nOzuna x Romeo Santos - El Farsante Remix\nChildish Gambino - This Is America (Official V...")
        self.ui.cbYoutube.setItemData(3,"category_id\tlikes\n10\t    272138.508943\n29\t    271695.733333\n24\t     81572.362012\n23\t     78431.168490\n28\t     61531.127413\n1\t      57205.523089\n22\t     46273.495899\n43\t     41836.900000\n17\t     39270.313057\n20\t     39220.127517\n27\t     38440.687090\n15\t     28629.913858\n26\t     26639.183091\n25\t     25021.685714\n2\t      24608.506944\n19\t      9674.447917")
        self.ui.cbYoutube.setItemData(4,"category_id\tviews\n10\t13754\n24\t9124\n22\t2926\n1\t2577\n26\t1928\n17\t1907\n23\t1828\n20\t1788\n25\t1225\n15\t534\n28\t518\n27\t457\n2\t144\n19\t96\n29\t90\n43\t20")
        self.ui.cbYoutube.setItemData(5,"title\t\t\t\t\tlikes\tdislikes\tbeğeni_orani\nKris Wu – Like That (Official Music Video)\t57544\t0\t1.0\nHIGHLIGHTS: MK Dons U18s 1-0 Cardiff City U18s\t30\t0\t1.0\nQUIZ : Name the Trail : A Christmas Cracker\t2\t0\t1.0\nLima Sopoaga Tribute��🔥🔥||The Unsung Her||💯💯 2017\t50\t0\t1.0\nBohemian Rhapsody (2018) - Scene Bohemian Rhap...\t71\t0\t1.0")
        resultYt = self.ui.cbYoutube.currentData()
        self.ui.lblYoutube.setText(resultY.upper() + ":\n" + resultYt)

    
    def showOkul(self):
        resultO = 'Okul & Fifa : '
        itemO = self.ui.groupBox_3.findChildren(QtWidgets.QComboBox)
        for ff in itemO:
            if ff.currentText():
                resultO += ff.currentText()
        self.ui.cbOkul.setItemData(0,"Ortalama : 4.139073\nMax : 5\nMin : 2\n\nBu analiz personellerin ortalama %82,78146'lık araç gereç kullanma becerisine sahip olduğunu gösteriyor.")
        self.ui.cbOkul.setItemData(1,"Ortalama : 3.331126\nMax : 5\nMin : 1\n\nBu analiz öğrencilerin ortalama %66,62252 oranında duyuruları takip ettiği görülmektedir.\nAynı zamanda hiç takip etmeyen ve sürekli takip edenlerde olmuştur.")
        self.ui.cbOkul.setItemData(2,"Ortalama : 3.907285\n\nBu analiz öğrencilerin ders kayıtlarını ortalama %78,1457 oranında tekrar izleyebildiğini göstermektedir.")
        self.ui.cbOkul.setItemData(3,"short_name\tvalue_eur\nNeymar Jr     105500000.0\nL. Messi       95500000.0\nK. Mbappé      93500000.0\nK. De Bruyne   90000000.0\nE. Hazard      90000000.0\nM. Salah       80500000.0\nV. van Dijk    78000000.0\nJ. Oblak       77500000.0\nP. Dybala      76500000.0\nR. Sterling    73000000.0")
        self.ui.cbOkul.setItemData(4,"FC Bayern München    2.994674e+07\nReal Madrid          2.720758e+07\nFC Barcelona         2.634242e+07\nManchester City      2.562864e+07\nJuventus             2.228712e+07")
        self.ui.cbOkul.setItemData(5,"club\t\tage\tvalue_eur\nFC Bayern München  25.130435  2.994674e+07\nReal Madrid        24.909091  2.720758e+07\nFC Barcelona       24.060606  2.634242e+07\nManchester City    24.333333  2.562864e+07\nJuventus           27.000000  2.228712e+07")
        self.ui.cbOkul.setItemData(6,"team_position\tage\tvalue_eur\nCF             27.428571  1.251786e+07\nRW             25.329193  7.080248e+06\nLW             25.543210  6.721358e+06\nRAM            28.304348  5.759348e+06\nRF             24.684211  5.675000e+06\nLF             25.210526  5.317105e+06\nLAM            27.217391  5.005435e+06\nLS             26.497436  4.817103e+06\nCAM            26.585209  4.798617e+06\nST             27.408297  4.784410e+06")
        resultOf = self.ui.cbOkul.currentData()
        self.ui.lblOkul.setText(resultO.upper() + ":\n" + resultOf)



    def loadItems(self):
        analizNba = ["Takımlardaki Oyuncu Sayısı","Takımlara Göre Ortalama Maaş","Yaşı 20-25 oyuncular","En yüksek maaş","Ortalama Maaş"]
        analizOkul = ["Araç gereç kullanma becerisi","Öğrencilerin duyuruları takibi","Ders kayıtlarını tekrar izleyebilme","Top 10 Maaş","Takımların Ortalama Maaşı","Takımların Yaş Ortalaması","Mevkii Maaş Ortalaması"]
        analizYoutube = ["Like-Dislike Ortalaması","En Çok Görüntülenen Video","En Çok Görüntülenen 5 Video","Kategoriye Göre Beğeni Ortalamaları","Kategori Video Sayısı","Popüler Videolar"]
        self.ui.cbNba.addItems(analizNba)
        self.ui.cbOkul.addItems(analizOkul)
        self.ui.cbYoutube.addItems(analizYoutube)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()