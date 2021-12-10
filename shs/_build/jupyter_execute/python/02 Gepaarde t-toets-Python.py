#!/usr/bin/env python
# coding: utf-8
---
title: "Gepaarde t-toets"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_depth: 2
    toc_float: 
      collapsed: FALSE 
    number_sections: true
    includes:
      in_header: ["../01. Includes/html/nocache.html", "../01. Includes/html/favicon.html", "../01. Includes/html/analytics.html"]
  keywords: [statistisch handboek, studiedata]
---
# <!-- ## CLOSEDBLOK: Functies.R -->

# In[1]:


get_ipython().run_cell_magic('R', '', 'library(here)\nif (!exists("Substitute_var")) {\n  ## Installeer packages en functies\n  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)\n}')


# <!-- ## /CLOSEDBLOK: Functies.R -->
# 
# <!-- ## CLOSEDBLOK: CSS -->
# <style>
# `r htmltools::includeHTML(paste0(here::here(),"/01. Includes/css/Stylesheet_SHHO.css"))`
# </style>
# <!-- ## /CLOSEDBLOK: CSS -->
# 
# <!-- ## CLOSEDBLOK: Header.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Header.R -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## CLOSEDBLOK: Reticulate.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'library(reticulate)\nknitr::knit_engines$set(python = reticulate::eng_python)')


# <!-- ## /CLOSEDBLOK: Reticulate.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '# doorlinken naar de Wilcoxon Signed Rank Test\n# linken naar blz transformeren data ')


# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/02.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *gepaarde t-toets* om te toetsen of de gemiddelden van twee (herhaalde) metingen van een groep verschillen en om te toetsen of de gemiddelden van twee gepaarde groepen van elkaar verschillen.[^1] 
# 
# # Onderwijscasus
# <div id ="casus">
# Voor het verminderen van de studielast van studenten biedt het Centrum voor Studentbegeleiding van een universiteit een cursus Plannen aan. De cursus is bedoeld om studenten beter inzicht te geven in de gevolgen van de planning van hun studielast. De cursus wordt tussen twee onderwijsperiodes in gegeven. Voor en na de cursus moeten de studenten gedurende een onderwijsperiode een logboek bijhouden over hun studiegedrag. De cursuscoördinator vraagt zich af of er een verandering in het aantal studieuren is na deelname aan de cursus.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Het gemiddeld aantal uren studeren per onderwijsperiode verandert niet na de cursus, µ~T0~ = µ~T1~  
# 
# *H~A~*: Het gemiddeld aantal uren studeren per onderwijsperiode verandert na de cursus, µ~T0~ ≠ µ~T1~ 
# </div>
# 
# # Assumpties
# Om een valide resultaat te bereiken moet er, voordat de toets kan worden uitgevoerd, aan een aantal voorwaarden voldaan worden.
# 
# ## Normaliteit
# De *gepaarde t-toets* gaat ervan uit dat de verschillen tussen de gepaarde observaties (verschilscores) normaal verdeeld zijn. Ga er bij een aantal deelnemers[^13] *n* groter dan 100 vanuit dat de *gepaarde t-toets* robuust genoeg is om uit te voeren zonder dat er voldaan is aan de assumptie van normaliteit.   
# 
# Controleer de assumptie van normaliteit met de volgende stappen:  
# 1. Controleer de verschilscores visueel met een histogram, een Q-Q plot en een boxplot.  
# 2. Toets of de verschilscores normaal verdeeld is met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (*n* < 50) met de *Shapiro-Wilk test*.[^3]<sup>, </sup>[^4]  
# 
# De eerste stap heeft als doel een goede indruk te krijgen van de verdeling van de steekproef. In de tweede stap wordt de assumptie van normaliteit getoetst. De statistische toets laat zien of de verdeling van de steekproef voldoet aan de assumptie van normaliteit.
# 
# <!-- ## TEKSTBLOK: Link1.R-->
# Als blijkt dat de verschilscores niet normaal verdeeld is, transformeer dan de afhankelijke variabele eventueel en bepaal daarna of de verschilscores wel normaal verdeeld is [^5] of gebruik de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html).[^6]<sup>, </sup>[^7]
# <!-- ## /TEKSTBLOK: Link1.R-->
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.py -->
# Er is een dataset ingeladen met het gemiddeld aantal uren studeren voor (T~0~) en na (T~1~) de cursus. De gemiddeldes per onderwijsperiode zijn afgerond op 1 decimaal in de dataframe `dfStudielogboek`. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.py -->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfStudielogboek = pd.DataFrame(r.Studielogboek)


# In[ ]:


## Eerste 5 observaties
print(dfStudielogboek.head())


# In[ ]:


## Laatste 5 observaties
print(dfStudielogboek.tail())


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# Selecteer beide groepen, sla deze op in een vector en bereken het verschil in de afhankelijke variabelen (het aantal studieuren) voor alle deelnemers (de studenten).
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Uren_studeren_T0 = dfStudielogboek[dfStudielogboek['Meetmoment'] == "T0"]['Uren_studeren']
Uren_studeren_T1 = dfStudielogboek[dfStudielogboek['Meetmoment'] == "T1"]['Uren_studeren']


# <!-- ## /OPENBLOK: Data-selecteren.py -->
# 
# <!-- ## TEKSTBLOK: Data-inspectie.py-->
# Inspecteer de data met `np.size()`, `np.mean()` en `np.std()`, door deze aan te roepen uit het package `numpy`.
# <!-- ## /TEKSTBLOK: Data-inspectie.py-->

# <!-- ## OPENBLOK: numpy-inladen.py -->

# In[ ]:


# Om het gemiddelde en de standaard deviatie te berekenen, hebben we de library 'numpy' nodig
import numpy as np


# <!-- ## OPENBLOK: numpy-inladen.py -->
# 

# <div class = "col-container">
#   <div class ="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.py -->

# In[ ]:


## aantallen, gemiddelde en standaarddeviatie voor cursus
print(len(Uren_studeren_T0))
print(np.mean(Uren_studeren_T0))
print(np.std(Uren_studeren_T0))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Data-beschrijven-2.py -->

# In[ ]:


## aantallen, gemiddelde en standaarddeviatie na tutorgesprek
print(len(Uren_studeren_T1))
print(np.mean(Uren_studeren_T1))
print(np.std(Uren_studeren_T1))


# <!-- ## /OPENBLOK: Data-beschrijven-2.py -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven.py -->

# In[ ]:


vMean_t0 = np.mean(Uren_studeren_T0)
vSD_t0 = np.std(Uren_studeren_T0)
vN_t0 = np.size(Uren_studeren_T0)
vMean_t1 = np.mean(Uren_studeren_T1)
vSD_t1 = np.std(Uren_studeren_T1)
vN_t1 = np.size(Uren_studeren_T1)


# <!-- ## /CLOSEDBLOK: Data-beschrijven.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# * Gemiddeld uren studeren T~0~ (standaardafwijking): `r Round_and_format(py$vMean_t0)` (`r Round_and_format(py$vSD_t0)`). *n* = `r py$vN_t0`.
# * Gemiddeld uren studeren T~1~ (standaardafwijking): `r Round_and_format(py$vMean_t1)` (`r Round_and_format(py$vSD_t1)`). *n* = `r py$vN_t1`.
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de verschilscores van het aantal uur studeren voor en na het volgen van de cursus visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^18] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^8]<sup>, </sup>[^9]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


## Bereken verschil in uren studeren met numpy
Uren_studeren_verschil = np.array(Uren_studeren_T1) - np.array(Uren_studeren_T0)

## Histogram met matplotlib
import matplotlib.pyplot as plt
hist = plt.hist(Uren_studeren_verschil, density = True, edgecolor = "black", bins = 12)
title = plt.title("Verschilscores uren studeren voor en na cursus")
xlab = plt.xlabel("Verschilscores uren studeren")
ylab = plt.ylabel("Frequentiedichtheid")
yax = plt.ylim([0, 0.175])
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# De histogram lijkt niet geheel symmetrisch, maar heeft één top en geen outliers. Er lijken geen grote afwijkingen van de normaalverdeling te zijn.

# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.py -->
# Gebruik de functie `probplot` van het `scipy` package om een Q-Q plot te maken, met als datapunten kleine cirkels. 
# <!-- ## /TEKSTBLOK: QQplot.py -->
# 
# <!-- ## OPENBLOK: QQplot-inladen.py -->

# In[ ]:


import scipy.stats as stats


# <!-- ## /OPENBLOK: QQplot-inladen.py -->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, kan aangenomen worden dat de data bij benadering normaal verdeeld is.
# 
# <!-- ## OPENBLOK: QQplot-1.py -->

# In[ ]:


qq = stats.probplot(Uren_studeren_verschil, dist="norm", plot=plt)
title = plt.title("Normaal Q-Q plot verschilscores uren studeren voor en na cursus")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot-1.py -->
# 
# In deze casus liggen de meeste datapunten op of vlakbij de lijn. Hoewel er bij de uiteinden van de verdeling wat afwijkingen zijn, duidt deze grafiek op een goede benadering van de normaalverdeling.
# 
# ### Boxplot
# 
# De doos van de boxplot geeft de middelste 50% van de verschilscores in studieuren uit het studielogboek weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^8]<sup>, </sup>[^9]
# 
# <!-- ## OPENBLOK: Boxplot.py -->
# ``` {python Boxplot}
# ## Boxplot
# fig, ax = plt.subplots()
# box = ax.boxplot([Uren_studeren_verschil], labels = [""])
# title = plt.title("Boxplot van verschilscores uren studeren voor en na cursus")
# plt.show()
# ```
# <!-- ## /OPENBLOK: Boxplot.py -->
# 
# De boxplotten geven de spreiding weer in de verschilscores van het aantal uur studeren voor en na het volgen van de cursus voor deelnemers aan de cursus. De boxplot is niet helemaal symmetrisch, maar beide snorreharen zijn ongeveer even lang en de mediaan ligt ongeveer in het midden. Daarom zijn de verschilscores bij benadering normaal verdeeld.
# 
# Op basis van de grafieken lijken er geen grote afwijkingen van de normaalverdeling voor de verschillen in studieuren te zijn, maar normaliteit kan ook getoetst worden met statistische toetsen.
# 
# ## Toetsen van normaliteit
# Om te controleren of de verschilscores normaal verdeeld zijn, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov 
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze test het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de steekproef significant verschillend van de normale verdeling.
# 
# <!-- ## TEKSTBLOK: Lilliefors-test1.py -->
# De standaard interpretatie van een statistische toets in Python is als volgt: `(<teststatistiek>, <p-waarde>)`. Verder wordt er standaard tweezijdig getoetst. Gebruik bij deze toets het argument `pvalmethod = "table"` om een betrouwbare p-waarde te krijgen.
# <!-- ## /TEKSTBLOK: Lilliefors-test1.py -->
# 
# <!-- ## OPENBLOK: Library-nortest.py -->

# In[ ]:


import statsmodels.stats.api as smod


# <!-- ## /OPENBLOK: Library-nortest.py -->
# 
# <!-- ## OPENBLOK: Lilliefors-test-1.py -->
# ``` {python Lilliefors Test-1, warning=FALSE}
# print(smod.lilliefors(Uren_studeren_verschil, pvalmethod="table"))
# ```
# ``` {python Lilliefors Test-1 closed, warning=FALSE, include = FALSE}
# lilliefors = smod.lilliefors(Uren_studeren_verschil, pvalmethod="table")
# print(lilliefors)
# ```
# <!-- ## /OPENBLOK: Lilliefors-test-1.py -->
# 
# <!-- ## TEKSTBLOK: Lilliefors-test-2.py -->
# De test heeft een p-waarde van `r Round_and_format(unlist(py$lilliefors[2]))`, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. De *gepaarde t-toets* kan uitgevoerd worden. 
# <!-- ## /TEKSTBLOK: Lilliefors-test-2.py -->
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke test als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de steekproef significant verschillend van de normale verdeling.
# 
# <!-- ## CLOSEDBLOK: data inladen-2.py -->

# In[ ]:


Uren_studeren_verschil_n30 = r.Uren_studeren_verschil_n30
N = len(Uren_studeren_verschil_n30)


# <!-- ## /CLOSEDBLOK: data inladen-2.py -->
# 
# <!-- ## TEKSTBLOK: Shapiro-Wilk-test.py -->
# Er is een subset van de verschillen tussen het aantal studieuren op T~0~ en T~1~ ingeladen, `Uren_studeren_verschil_n30` met daarin `r py$N` observaties. Voor een relatief kleine steekproef als deze is de *Shapiro-Wilk Test* geschikt.
# <!-- ## /TEKSTBLOK: Shapiro-Wilk-test.py -->
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.py -->
# ``` {python Shapiro-Wilk Test-1}
# print(stats.shapiro(Uren_studeren_verschil_n30))
# ```
# ``` {python Shapiro-Wilk Test-2, include = FALSE}
# swtest = stats.shapiro(Uren_studeren_verschil_n30)
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-1.py -->
# 
# <!-- ## TEKSTBLOK: Shapiro-Wilk-test-2.py -->
# Voor deze subset is de p-waarde `r Round_and_format(unlist(py$swtest[2]))`, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. De *gepaarde t-toets* kan uitgevoerd worden.  
# <!-- ## /TEKSTBLOK: Shapiro-Wilk-test-2.py -->
# 
# ## Gepaarde t-toets
# <!-- ## TEKSTBLOK: T-test.py -->
# Gebruik de functie `.DescrStatsW().ttest_mean()` van het package `statsmodels.stats.api` om een *gepaarde t-toets* uit te voeren. Gebruik als argument van de functie `DescrStatsW()` de verschilscores `Uren_studeren_verschil` en als argumenten van de functie `ttest_mean()` eerst `value = 0` om aan te geven dat het gemiddelde van de verschilscores nul is onder de nulhypothese en `alternative = 'two-sided'` om een tweezijdige toets uit te voeren. Bereken daarna het 95%-betrouwbaarheidsinterval met de functie `tconfint_mean()` met als argumenten `alpha = 0.05` om het significantieniveau aan te geven en `alternative = 'two-sided'` om aan te geven dat er een tweezijdige toets plaatsvindt.
# <!-- ## /TEKSTBLOK: T-test.py -->

# <!-- ## OPENBLOK: T-toets.py -->

# In[ ]:


## Importeer het benodigde package
import statsmodels.stats.api as smod

## Bereken verschil in uren studeren met numpy
Uren_studeren_verschil = np.array(Uren_studeren_T1) - np.array(Uren_studeren_T0)

# Voer gepaarde t-toets uit
print(smod.DescrStatsW(Uren_studeren_verschil).ttest_mean(value = 0, alternative = 'two-sided'))

# Print 95%-betrouwbaarheidsinterval
print(smod.DescrStatsW(Uren_studeren_verschil).tconfint_mean(alpha = 0.05, alternative = 'two-sided'))


# In[ ]:


# Absoluut gemiddeld verschil berekenen
absoluut_verschil = np.abs(np.mean(np.array(Uren_studeren_T1) - np.array(Uren_studeren_T0)))
print(absoluut_verschil)


# <!-- ## /OPENBLOK: T-toets.py -->
# <!-- ## CLOSEDBLOK: T-test.py -->

# In[ ]:


stat, pval, df = smod.DescrStatsW(Uren_studeren_verschil).ttest_mean(value = 0, alternative = 'two-sided')
N_tot = len(Uren_studeren_verschil)
lb, ub = smod.DescrStatsW(Uren_studeren_verschil).tconfint_mean(alpha = 0.05, alternative = 'two-sided')


# <!-- ## /CLOSEDBLOK: T-test.py -->
# <!-- ## TEKSTBLOK: T-test2.py -->
# * *t*~`r py$df`~ = `r Round_and_format(py$stat)`, *p* < 0,0001`
# * Vrijheidsgraden, *df* = *n* -1 = `r py$N_tot`-1 = `r py$df`  
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen [^10]
# * 95%-betrouwbaarheidsinterval: bij het herhalen van het experiment met verschillende steekproeven van de populatie zal 95% van de betrouwbaarheidsintervallen de daadwerkelijke parameter bevatten, het verschil tussen het aantal studieuren voor en na de cursus,  µ~verschil~ = µ~T1~ - µ~T0~. In deze casus is het interval tussen `r Round_and_format(py$lb)` en `r Round_and_format(py$ub)`. Aangezien 0 niet in dit interval zit, is er een significant verschil tussen µ~T1~ en µ~T0~.
# * het absolute verschil tussen de twee groepen is `r Round_and_format(py$absoluut_verschil)` 
# 
# <!-- ## TEKSTBLOK: T-test2.py -->
# 
# De p-waarde geeft aan of het verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Een veel gebruikte effectmaat is Cohen's *d*. Cohen's *d* geeft een gestandaardiseerd verschil weer: het verschil in gemiddelden tussen twee groepen gecorrigeerd voor de standaardafwijking van de eerste meting (T~0~). Een indicatie om *d* te interpreteren is: rond 0,3 is een klein effect, rond 0,5 is een gemiddeld effect en rond 0,8 is een groot effect.[^12]  
# 
# <!-- ## TEKSTBLOK: Cohen-d.py -->
# Er is geen Python functie voor Cohen's d. Bereken daarom de effectmaat zelf door het gemiddelde van de verschilscores `Uren_studeren_verschil` te delen door de standaardafwijking van de scores van de studenten voor de cursus `Uren_studeren_T0`. Neem de absolute waarde omdat het gebruikelijk is om een effectmaat als positief getal weer te geven.[^11]
# <!-- ## /TEKSTBLOK: Cohen-d.py  -->
# 
# <!-- ## OPENBLOK: Cohens-d-test.py -->

# In[ ]:


abs(np.mean(Uren_studeren_verschil)/np.std(Uren_studeren_T0))


# <!-- ## OPENBLOK: Cohens-d-test.py -->
# 
# <!-- ## CLOSEDBLOK: Cohens-d-test.py -->

# In[ ]:


d = abs(np.mean(Uren_studeren_verschil)/np.std(Uren_studeren_T0))


# <!-- ## /CLOSEDBLOK: Cohens-d-test.py -->
# 
# <!-- ## TEKSTBLOK: Cohens-d-test.py -->
# *d* = `r Round_and_format(py$d)`. De sterkte van het effect van de tutor op het cijfer is groot.
# <!-- ## /TEKSTBLOK: Cohens-d-test.py -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# Een *gepaarde t-toets* is uitgevoerd om te toetsen of het gemiddeld aantal uur studeren van de studenten is veranderd na deelname aan de cursus Plannen. Het verschil tussen het gemiddelde van T~0~ (*M~T0~* = `r Round_and_format(py$vMean_t0)`, *SD~T0~* = `r Round_and_format(py$vSD_t0)`) en het gemiddelde van T~1~ (*M~T1~* =`r Round_and_format(py$vMean_t1)`, *SD~T1~* = `r Round_and_format(py$vSD_t1)`) is significant, *t* ~`r py$df`~ = `r Round_and_format(py$stat)`, *p* < 0,0001. Gemiddeld studeren de studenten `r Round_and_format(py$absoluut_verschil)` uur meer na deelname aan de cursus, dit is een groot effect. Het 95%-betrouwbaarheidsinterval voor het verschil tussen het gemiddelde van beide groepen (T~1~ - T~0~) loopt van `r Round_and_format(py$lb)` tot `r Round_and_format(py$ub)`. Aan de hand van de resultaten kan geconcludeerd worden dat de studenten, na deelname aan de cursus Plannen, meer tijd besteden aan hun studie dan daarvoor.
# 

# | Meting     | N         | M            | SD         |
# | --------   | --------- | ------------ | ---------- |
# | T~0~       | `r py$vN_t0` | `r Round_and_format(py$vMean_t0)` | `r Round_and_format(py$vSD_t0)` |
# | T~1~       | `r py$vN_t1` | `r Round_and_format(py$vMean_t1)` | `r Round_and_format(py$vSD_t1)` |
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# *Tabel 1. Groepsgrootte, gemiddeld tentamencijfer en standaarddeviatie van het aantal uren door studenten besteed aan hun studie per meetmoment*

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Wikipedia (21 augustus 2019). *Student's t-test*. [Wikipedia](https://en.wikipedia.org/wiki/student%27s_t-test).
# [^2]: Lumley, T., Diehr, P., Emerson, S., & Chen, L. (2002). The importance of the normality assumption in large public health data sets. *Annu Rev Public Health, 23*, 151-69. doi: 10.1146/annurev.publheath.23.100901.140546 http://rctdesign.org/techreports/arphnonnormality.pdf 
# [^3]: Van Geloven, N. (25 september2013). *Wilcoxon signed rank toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Wilcoxon_signed_rank_toets).
# [^4]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. [Testing for Normality using SPSS Statistics](https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php).  
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).  
# [^7]: De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) maakt een rangschikking van de data. Hierdoor is de test verdelingsvrij en is normaliteit geen assumptie. Ook zijn uitbijters minder van invloed op het eindresultaat. Toch wordt er voor deze test minder vaak gekozen, doordat bij het maken van een rankschikking de data informatie verliest. Als de data wel normaal verdeeld is, heeft de [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) minder onderscheidend vermogen dan wanneer de *gepaarde t-toets* uitgevoerd zou worden.  
# [^8]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^9]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport.
# [^10]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen, houd hierbij rekening met type I en type II fouten.
# [^11]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^12]: Marshall, E., & Boggis, E. (2016). *The statistics tutor’s quick guide to commonly used statistical tests*. http://www.statstutor.ac.uk/resources/uploaded/tutorsquickguidetostatistics.pdf 
# [^13]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
# <!-- ## TEKSTBLOK: Extra-Bron.py -->
# [^13]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# <!-- ## /TEKSTBLOK: Extra-Bron.py -->
# NA
# <!-- ## /TEKSTBLOK: Extra-Bron.R -->
