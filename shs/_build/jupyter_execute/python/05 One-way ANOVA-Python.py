#!/usr/bin/env python
# coding: utf-8
---
title: "One-way ANOVA"
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


get_ipython().run_cell_magic('R', '', 'options(width = 80)\n## Zodat de TukeyHSD naast elkaar geprint wordt')


# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/05.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# Gebruik de *one-way ANOVA* bij het toetsen of de gemiddelden van twee of meer onafhankelijke groepen verschillen.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# Om wervingsactiviteiten beter af te stemmen op de aankomende studenten, wil het hoofd van de afdeling Communicatie weten wat de reistijd (in minuten) is van studenten van verschillende opleidingen. Hij heeft daarom data verzameld over de reistijd van uitwonende studenten voor de opleidingen: Arabische Taal en Cultuur, Filosofie en Geschiedenis. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: De reistijden van de studenten van de drie opleidingen komen uit dezelfde verdeling en hebben dus een gezamenlijk gemiddelde
# 
# *H~A~*: De reistijden van de studenten van de drie opleidingen komen niet uit dezelfde verdeling en hebben dus een verschillend gemiddelde

# # Uitleg assumpties
# Om een valide toetsresultaat te bereiken moet de data aan een aantal voorwaarden voldoen. Controleer of de steekproef aan de volgende assumpties voldoet: normaliteit, homogeniteit van varianties en onafhankelijkheid.
# 
# De *one-way ANOVA* is een robuuste toets: als er niet voldaan is aan de assumptie van normaliteit of homogeniteit van varianties, dan kan de *one-way ANOVA* in bepaalde gevallen nog steeds uitgevoerd en geïnterpreteerd worden.[^2] Hierdoor kan het wel zijn dat de toets minder onderscheidend vermogen heeft, dan wanneer de assumpties niet geschonden worden.[^3]<sup>, </sup>[^4] Als er grote afwijkingen zijn van normaliteit of homogeniteit van varianties, is de [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) een alternatief voor de *one-way ANOVA*.[^5]<sup>, </sup>[^6]
# 
# ## Normaliteit
# De assumptie van normaliteit houdt bij de *one-way ANOVA* in dat de afhankelijke variabele normaal verdeeld is voor elke groep. Controleer de assumptie van normaliteit voor elke groep met de volgende stappen:  
# 1. Controleer de data visueel met een histogram, een boxplot of een Q-Q plot.   
# 2. Toets of de data normaal verdeeld zijn met de *Kolmogorov-Smirnov test* of bij een kleinere steekproef (n < 50) met de *Shapiro-Wilk test*.[^7]<sup>, </sup>[^8]  
# 
# De eerste stap heeft als doel een goede indruk te krijgen van de verdeling van de steekproef. In de tweede stap wordt de assumptie van normaliteit getoetst. De statistische toets laat zien of de verdeling van de observaties van een groep voldoet aan de assumptie van normaliteit. Voor alle groepen moet er voldaan zijn aan de assumptie van normaliteit.
# 
# Als er niet voldaan is aan normaliteit, is het transformeren van de data een optie.[^2] Een andere optie is het gebruik van de nonparametrische [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) waar normaliteit geen assumptie is.[^3] De *one-way ANOVA* is echter ook een robuuste toets ten opzichte van de assumptie van normaliteit. Als elke groep een aantal observaties (*n*) heeft dat groter dan 100 is,  ga er dan vanuit dat de *one-way ANOVA* robuust genoeg is om uit te voeren zonder dat de afhankelijke variabele een normale verdeling volgt.
# 
# ## Homogeniteit van varianties
# Toets met de *Levene's Test (for equality of variance)* of de variantie van iedere groep ongeveer hetzelfde is. Bij een p-waarde kleiner dan 0,05 is de variantie van de groepen significant verschillend.[^10] De *one-way ANOVA* is in bepaalde gevallen robuust als er geen homogeniteit van varianties is. Als de ratio van de grootste en kleinste steekproefgrootte van alle groepen kleiner dan 10 is en de ratio van de grootste en kleinste variantie van alle groepen kleiner dan 4 is, dan kan de *one-way ANOVA* gewoon uitgevoerd worden.[^19] Voer de [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) toets uit als er niet aan deze voorwaarden voor robuustheid is voldaan.
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^11] Voor de *one-way ANOVA* wordt de effectmaat eta squared vaak gebruikt.
# 
# De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in de lengte van de reistijd die verklaard kan worden door de opleiding. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^12]<sup>,</sup>[^13]
# 
# # Post-hoc toetsen
# De *one-way ANOVA* toetst of de groepen afkomstig zijn van eenzelfde verdeling met een gezamenlijk gemiddelde of van verschillende verdeling met een eigen gemiddelde. Voer een post-hoc toets uit om te bepalen welke groepen significant verschillen. De post-hoc toetsen voeren meestal een correctie voor de p-waarden uit, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout).
# 
# Er zijn meerdere post-hoc toetsen. De keuze voor een toets hangt onder andere af van het wel of niet schenden van de assumptie van homogeniteit van varianties:   
# * Gebruik de Tukey Honestly Significant Difference post-hoc toets bij gelijke variantie.[^14]  
# * Gebruik de Games-Howell post-hoc toets bij ongelijke variantie.[^15]  
# 
# # Toetsing assumpties
# <!-- ## TEKSTBLOK: Dataset-inladen.py -->
# Er is een dataset ingeladen met de reistijden van uitwonende studenten per opleiding genaamd `dfReistijd_per_opleiding`. 
# <!-- ## /TEKSTBLOK: Dataset-inladen.py -->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


import pandas as pd
dfReistijd_per_opleiding = pd.DataFrame(r.Reistijd_per_opleiding)


# In[ ]:


## Eerste 5 observaties
print(dfReistijd_per_opleiding.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfReistijd_per_opleiding.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# <!-- ## TEKSTBLOK: Data-bekijken2.py -->
# De dataset bevat gegevens van studenten van verschillende opleidingen. Gebruik `.unique()` om te onderzoeken welke opleidingen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.py -->
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


## Opleidingen in de data aanwezig
print(dfReistijd_per_opleiding['Opleiding'].unique())


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# Selecteer de drie groepen en sla deze op in een vector om deze makkelijker aan te kunnen roepen. 
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Reistijd_ATC = dfReistijd_per_opleiding[dfReistijd_per_opleiding['Opleiding'] == "Arabische Taal en Cultuur"]['Reistijd']
Reistijd_FIL = dfReistijd_per_opleiding[dfReistijd_per_opleiding['Opleiding'] == "Filosofie"]['Reistijd']
Reistijd_GSC = dfReistijd_per_opleiding[dfReistijd_per_opleiding['Opleiding'] == "Geschiedenis"]['Reistijd']


# <!-- ## /OPENBLOK: Data-selecteren.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.py -->
# Om meer inzicht te krijgen in de data, inspecteer de data met `len()`, `np.mean()` en `np.std())`, door deze aan te roepen uit de library `numpy`.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-inladen.py -->

# In[ ]:


# Om het gemiddelde en de standaard deviatie te berekenen, hebben we de library 'numpy' nodig
import numpy as np


# <!-- ## /OPENBLOK: Data-beschrijven-inladen.py -->
# 
# <!-- ## OPENBLOK: Data-beschrijven-1.py -->

# In[ ]:


## Aantallen, gemiddelde en standaarddeviatie voor Arabische Taal en Cultuur
print(len(Reistijd_ATC))
print(np.mean(Reistijd_ATC))
print(np.std(Reistijd_ATC))


# In[ ]:


## Aantallen, gemiddelde en standaarddeviatie voor Filosofie
print(len(Reistijd_FIL))
print(np.mean(Reistijd_FIL))
print(np.std(Reistijd_FIL))


# In[ ]:


## Aantallen, gemiddelde en standaarddeviatie voor Geschiedenis
print(len(Reistijd_GSC))
print(np.mean(Reistijd_GSC))
print(np.std(Reistijd_GSC))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
# 
# <!-- ## CLOSEDBLOK: Data-beschrijven-11.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Data-beschrijven-11.R -->
# 
# <!-- ## CLOSEDBLOK: Data-beschrijven.py -->

# In[ ]:


vM_ATC = np.mean(Reistijd_ATC)
vSD_ATC = np.std(Reistijd_ATC)
vN_ATC = np.size(Reistijd_ATC)

vM_FIL = np.mean(Reistijd_FIL)
vSD_FIL = np.std(Reistijd_FIL)
vN_FIL = np.size(Reistijd_FIL)

vM_GSC = np.mean(Reistijd_GSC)
vSD_GSC = np.std(Reistijd_GSC)
vN_GSC = np.size(Reistijd_GSC)


# <!-- ## /CLOSEDBLOK: Data-beschrijven.py -->
# 
# <!-- ## TEKSTBLOK: Datatekst-beschrijven.py -->
# * Gemiddelde reistijd Arabische Taal en Cultuur (standaarddeviatie): `r Round_and_format(py$vM_ATC)` (`r Round_and_format(py$vSD_ATC)`). *n* = `r py$vN_ATC`  
# * Gemiddelde reistijd Filosofie (standaarddeviatie): `r Round_and_format(py$vM_FIL)` (`r Round_and_format(py$vSD_FIL)`). *n* = `r py$vN_FIL`.
# * Gemiddelde reistijd Geschiedenis (standaarddeviatie): `r Round_and_format(py$vM_GSC)` (`r Round_and_format(py$vSD_GSC)`). *n* = `r py$vN_GSC`.
# 
# <!-- ## /TEKSTBLOK: Datatekst-beschrijven.py -->
# 
# ## Visuele inspectie van normaliteit
# Geef de verdeling van de reistijd voor elke opleiding visueel weer met een histogram, Q-Q plot en boxplot.
# 
# ### Histogram
# 
# Focus bij het analyseren van een histogram[^20] op de symmetrie van de verdeling, de hoeveelheid toppen (modaliteit) en mogelijke uitbijters. Een normale verdeling is symmetrisch, heeft één top en geen uitbijters.[^16]<sup>, </sup>[^17]
# 
# <!-- ## OPENBLOK: Histogram.py -->

# In[ ]:


## Histogram met matplotlib
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (15, 10))
sub1 = fig.add_subplot(1, 3, 1)
title1 = plt.title("Arabische Taal en Cultuur")
ylab = plt.ylabel("Frequentiedichtheid")
hist1 = plt.hist(Reistijd_ATC, density = True, edgecolor = "black", bins = 10)

sub2 = fig.add_subplot(1, 3, 2)
title2 = plt.title("Filosofie")
xlab = plt.xlabel("Reistijd")
hist2 = plt.hist(Reistijd_FIL, density = True, edgecolor = "black", bins = 10)

sub3 = fig.add_subplot(1, 3, 3)
title3 = plt.title("Geschiedenis")
hist3 = plt.hist(Reistijd_GSC, density = True, edgecolor = "black", bins = 12)

main = fig.suptitle('Reistijd per opleiding')
plt.show()


# <!-- ## /OPENBLOK: Histogram.py -->
# 
# De verdelingen van de opleidingen Filosofie en Geschiedenis lijken twee toppen te hebben. Alle drie de opleidingen hebben een niet geheel symmetrische verdeling, maar vertonen ook geen uitbijters. De verdeling van de opleiding Arabische taal en Cultuur is bij benadering normaal; voor de opleidingen Filosofie en Geschiedenis zijn lichte afwijkingen van de normale verdeling te zien.
# 
# ### Q-Q plot
# <!-- ## TEKSTBLOK: QQplot.py -->
# Importeer `scipy.stats` om een Q-Q plot te maken. Gebruik de functie `scipy.stats.probplot()` om een Q-Q plot te maken.
# <!-- ## TEKSTBLOK: QQplot.py -->
# 
# Als over het algemeen de meeste datapunten op de lijn liggen, neem dan aan dat de data normaal verdeeld is.
# <div class = "col-container">
#   <div class="col">
# <!-- ## OPENBLOK: QQplot1.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Reistijd_ATC, dist="norm", plot=plt)
title = plt.title("Arabische Taal en Cultuur")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot2.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Reistijd_FIL, dist="norm", plot=plt)
title = plt.title("Filosofie")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## /OPENBLOK: QQplot2.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: QQplot3.py -->

# In[ ]:


import scipy.stats as stats
qq = stats.probplot(Reistijd_GSC, dist="norm", plot=plt)
title = plt.title("Geschiedenis")
xlab = plt.xlabel("Theoretische kwantielen")
ylab = plt.ylabel("Kwantielen in data")
plt.show()


# <!-- ## OPENBLOK: QQplot3.py -->
#   </div>
# </div>
# Bij alle drie de verdelingen liggen de meeste datapunten op of vlakbij de lijn. Hoewel er bij de uiteinden van de verdeling wat afwijkingen zijn, duidt deze grafiek op een goede benadering van de normaalverdeling voor de drie verdelingen.

# ### Boxplot
# De box geeft de middelste 50% van de reistijd weer. De zwarte lijn binnen de box is de mediaan. In de staarten of snorreharen zitten de eerste 25% en de laatste 25%. Cirkels visualiseren mogelijke uitbijters.[^16]<sup>, </sup>[^17] Hoe meer de boxen overlappen, hoe waarschijnlijker er geen significant verschil is tussen de groepen. 
# 
# <!-- ## OPENBLOK: Boxplot.py -->

# In[ ]:


fig, ax = plt.subplots()
box = ax.boxplot([Reistijd_ATC, Reistijd_FIL, Reistijd_GSC], labels = ["Arabische Taal en Cultuur", "Filosofie", "Geschiedenis"])
title = plt.title("Reistijd per opleiding")
ylab = plt.ylabel("Reistijd in minuten")
plt.show()


# <!-- ## /OPENBLOK: Boxplot.py -->
# 
# De boxplotten geven de spreiding weer van de gemiddelde reistijd van uitwonende studenten voor de opleidingen Arabische Taal en Cultuur, Filosofie en Geschiedenis. De boxplotten Arabische Taal en Cultuur en Geschiedenis zien er symmetrisch uit; de boxen zijn even hoog boven als onder de mediaan en de snorreharen zijn onder en boven even groot. De boxplot van Filosofie is boven de mediaan groter dan onder de mediaan, de data kan wat scheef verdeeld zijn. De mediaan Arabische Taal en Cultuur ligt hoger dan de twee andere opleidingen.
# 
# ## Toetsen van normaliteit
# Om te controleren of de data normaal verdeeld is, kan de normaliteit getoetst worden. Twee veelgebruikte toetsen zijn: de *Kolmogorov-Smirnov test* en de *Shapiro-Wilk test*.
# 
# ### Kolmogorov-Smirnov
# De *Kolmogorov-Smirnov test* toetst het verschil tussen twee verdelingen. Standaard toetst deze toets het verschil tussen een normale verdeling en de verdeling van de steekproef. De Lilliefors correctie is vereist als het gemiddelde en de standaardafwijking niet van tevoren bekend of bepaald zijn, wat meestal het geval is bij een steekproef. Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <!-- ## TEKSTBLOK: Lilliefors-test1.py -->
# De standaard interpretatie van een statitische toets in Python is: `(<teststatistiek>, <p-waarde>)`. Verder toetst Python standaard tweezijdig.
# <!-- ## /TEKSTBLOK: Lilliefors-test1.py -->
# 
# <!-- ## OPENBLOK: Library-nortest.py -->

# In[ ]:


import statsmodels.stats.api as smod


# <!-- ## /OPENBLOK: Library-nortest.py -->
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Lilliefors-test-1.py -->
# ``` {python Lilliefors Test-1, warning=FALSE}
# print(statsmodels.stats.api.lilliefors(Reistijd_ATC, pvalmethod="table"))
# ```
# <!-- ## OPENBLOK: Lilliefors-test-1.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-2.py -->
# ``` {python Lilliefors Test-2, warning=FALSE}
# print(statsmodels.stats.api.lilliefors(Reistijd_FIL, pvalmethod="table"))
# ```
# <!-- ## OPENBLOK: Lilliefors-test-2.py -->
#   </div>
#   <div class = "col">
# <!-- ## OPENBLOK: Lilliefors-test-3.py -->
# ``` {python Lilliefors Test-3, warning=FALSE}
# print(statsmodels.stats.api.lilliefors(Reistijd_GSC, pvalmethod="table"))
# ```
# <!-- ## /OPENBLOK: Lilliefors-test-3.py -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elke groep; er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. [^18] De *one-way ANOVA* kan uitgevoerd worden.
# 
# ### Shapiro-Wilk Test
# De *Shapiro-Wilk test* is een soortgelijke toets als de *Kolmogorov-Smirnov test* en vooral geschikt bij kleine steekproeven (*n* < 50). Als de p-waarde kleiner dan 0,05 is, is de verdeling van de data significant verschillend van de normale verdeling.
# 
# <div class="col-container"> 
#   <div class="col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-3.py -->
# ``` {python Shapiro-Wilk Test-1, warning=FALSE}
# import scipy.stats as stats
# print(stats.shapiro(Reistijd_GSC))
# 
# ```
# <!-- ## /OPENBLOK: Shapiro-Wilk-test-3.py -->
#   </div>
#   <div class= "col">
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.py -->
# ``` {python Shapiro-Wilk Test-2, warning=FALSE}
# import scipy.stats as stats
# print(stats.shapiro(Reistijd_FIL))
# 
# ```
# <!-- ## OPENBLOK: Shapiro-Wilk-test-2.py -->
#   </div>
#   <div class= "col"> 
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.py -->
# ``` {python Shapiro-Wilk Test-3, warning=FALSE}
# import scipy.stats as stats
# print(stats.shapiro(Reistijd_ATC))
# ```
# <!-- ## OPENBLOK: Shapiro-Wilk-test-1.py -->
#   </div>
# </div>
# 
# De p-waarde is groter dan 0,05 voor elke groep, dus er is geen significant verschil gevonden tussen de verdeling van de steekproef en de normale verdeling. De *one-way ANOVA* kan uitgevoerd worden.
# 
# ## Toetsen van Homogeniteit van varianties
# Toets met de *Levene's test* de homogeniteit van varianties. Gebruik hiervoor de functie `leveneTest()` van het package `car` met als eerst argument de afhankelijke variabele `Reistijd_per_opleiding$Reistijd` en als tweede argument de onafhankelijke variabele `Reistijd_per_opleiding$Opleiding`.
# 
# <!-- ## OPENBLOK: Levenes-test.py -->

# In[ ]:


import scipy.stats as stats
# Geef de drie variabelen met de reistijden per opleiding als argumenten
print(stats.levene(Reistijd_ATC, Reistijd_FIL, Reistijd_GSC))


# <!-- ## /OPENBLOK: Levenes-test.py -->
# <!-- ## CLOSEDBLOK: Levenes-test.py -->

# In[ ]:


stat, pval = stats.levene(Reistijd_ATC, Reistijd_FIL, Reistijd_GSC)
vDF1 = 2
vDF2 = len(Reistijd_ATC) + len(Reistijd_FIL) + len(Reistijd_GSC) - 3


# <!-- ## /CLOSEDBLOK: Levenes-test.py -->
# <!-- ## TEKSTBLOK: Levenes-test.py -->
# * *F*~`r py$vDF1`~~,~~`r py$vDF2`~ = `r Round_and_format(py$stat)`, p-waarde = `r Round_and_format(py$pval)`, 
# * De p-waarde is groter dan 0,05, dus er is geen significant verschil gevonden tussen de groepen in spreiding.
# *  Vrijheidsgraden bestaan uit twee cijfers, het eerste cijfer (het aantal groepen - 1 = `r py$vDF1`) en het tweede cijfer (*n~1~* + *n~2~*+*n~3~* - 3 = `r py$vDF2`).  
# <!-- ## TEKSTBLOK: Levenes-test.py -->
# 
# # One-way ANOVA 
# Voer de *one-way ANOVA* uit om de vraag te beantwoorden of de gemiddelde reistijd van de studenten per opleiding verschilt.  
# <!-- ## TEKSTBLOK: ANOVA-toets.py -->
# Gebruik `.anova()` uit de package `pingouin` om een ANOVA-test uit te voeren. De argumenten van de functie zijn de dataset `data = dfReistijd_per_opleiding`, de afhankelijke variabele `dv = "Reistijd"`, de groepsvariabele `between = "Opleiding"` en `detailed = True` om aan te geven dat de functie een uitgebreide versie van de resultaten geeft.
# <!-- ## /TEKSTBLOK: ANOVA-toets.py -->  
# <!-- ## OPENBLOK: ANOVA-toets.py -->

# In[ ]:


# We importeren een library om de ANOVA toets te kunnen berekenen
import pingouin as pg


# In[ ]:


aov = pg.anova(data = dfReistijd_per_opleiding, dv = 'Reistijd', between = 'Opleiding', detailed = True)
print(aov)


# <!-- ## /OPENBLOK: ANOVA-toets.py -->
# 
# <!-- ## CLOSEDBLOK: ANOVA-toets.py -->

# In[ ]:


vDF1 = aov['DF'][0]
vDF2 = aov['DF'][1]
vF_waarde = aov['F'][0]


# <!-- ## /CLOSEDBLOK: ANOVA-toets.py -->
# 
# <!-- ## TEKSTBLOK: Eta-squared-tekst.py -->
# De effectmaat *η^2^* is in de resultaten te vinden onder `np2`.
# <!-- ## /TEKSTBLOK: Eta-squared-tekst.py -->
# 
# <!-- ## OPENBLOK: Eta-squared.py --> 
# <!-- ## /OPENBLOK: Eta-squared.py -->
# <!-- ## CLOSEDBLOK: Eta-squared.py -->

# In[ ]:


Esq = float(aov["np2"][0])


# <!-- ## /CLOSEDBLOK: Eta-squared.py -->
# 
# <!-- ## TEKSTBLOK: ANOVA-toets1.py -->
# * *F* ~`r py$vDF1`~~,~~`r py$vDF2`~ = `r Round_and_format(py$stat)`, *p* < 0,0001.
# * p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^16] 
# * Vrijheidsgraden: het aantal groepen - 1 = `r py$vDF1`; *n~1~* + *n~2~* + *n~3~*- 3 = `r py$vDF2`.
# 
# <!-- ## /TEKSTBLOK: ANOVA-toets1.py -->
# 
# # Post-hoc toets: Tukey's toets
# 
# <!-- ## TEKSTBLOK: Tukey-HSD.py -->
# Gebruik de functie `.pairwise_tukey()` met als argumenten de dataset `data = dfReistijd_per_opleiding`, de afhankelijke variabele `dv = "Reistijd"`, de groepsvariabele `between = "Opleiding"` en `effsize = "cohen"` om aan te geven dat Cohen's d als effectmaat voor de post-hoc toets wordt gebruikt.
# <!-- ## /TEKSTBLOK: Tukey-HSD.py -->
# 
# <!-- ## OPENBLOK: Tukey-HSD.py -->

# In[ ]:


print(pg.pairwise_tukey(data = dfReistijd_per_opleiding, dv = "Reistijd", between = "Opleiding", effsize = "cohen"))


# <!-- ## /OPENBLOK: Tukey-HSD.py -->
# <!-- ## CLOSEDBLOK: Tukey-HSD.py -->

# In[ ]:


THSD = pg.pairwise_tukey(data = dfReistijd_per_opleiding, dv = "Reistijd", between = "Opleiding", effsize = "cohen")
vATCvsFIL = THSD['diff'][0]
vATCvsGSC = THSD['diff'][1]
vFILvsGSC = THSD['diff'][2]
vpFILvsGSC = THSD['p-tukey'][2]


# <!-- ## /CLOSEDBLOK: Tukey-HSD.py -->
# <!-- ## TEKSTBLOK: Tukey-HSD1.py -->
# Het verschil tussen Filosofie en Arabische Taal en Cultuur is *MD* = `r Round_and_format(py$vATCvsFIL)`, *p* = 0,001.  
# Het verschil tussen Geschiedenis en Arabische Taal en Cultuur is *MD* = `r Round_and_format(py$vATCvsGSC)`, *p* = 0,001.  
# Het verschil tussen Geschiedenis en Filosofie is *MD* = `r Round_and_format(py$vFILvsGSC)`, *p* = `r Round_and_format(py$vpFILvsGSC)`.  
# <!-- ## /TEKSTBLOK: Tukey-HSD1.py -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# Een *one-way ANOVA* is uitgevoerd om te toetsen of de gemiddelde reistijd van de studenten per opleiding gelijk is aan elkaar. De opleidingen zijn: Arabische Taal en Cultuur (*M~atc~* = `r Round_and_format(py$vM_ATC)`, *SD~atc~* = `r Round_and_format(py$vSD_ATC)`), Filosofie (*M~fil~* = `r Round_and_format(py$vM_FIL)`, *SD~fil~* = `r Round_and_format(py$vSD_FIL)`) en Geschiedenis (*M~gsc~* = `r Round_and_format(py$vM_GSC)`, *SD~fil~* = `r Round_and_format(py$vSD_FIL)`; zie ook Tabel 1. De gemiddelde reistijd van de groepen verschilt significant van elkaar, *F*(`r py$vDF1`, `r py$vDF2`) = `r Round_and_format(py$vF_waarde)`, *p* < 0,0001, *η^2^* = `r Round_and_format(py$Esq)`. De sterkte van het effect van de type opleiding op de reistijd is groot.

# | Opleiding     | N          | M          | SD          |
# | ------------- | ---------- | ---------- | ----------- |
# | Arabisch      | `r Round_and_format(py$vN_ATC)` | `r Round_and_format(py$vM_ATC)` | `r Round_and_format(py$vSD_ATC)` |
# | Filosofie     | `r Round_and_format(py$vN_FIL)` | `r Round_and_format(py$vM_FIL)` | `r Round_and_format(py$vSD_FIL)` |
# | Geschiedenis  | `r Round_and_format(py$vN_GSC)` | `r Round_and_format(py$vM_GSC)` | `r Round_and_format(py$vSD_GSC)` |
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# *Tabel 1. Groepsgrootte, gemiddelde reistijd en standaarddeviatie per opleiding*
# <!-- ## TEKSTBLOK: Rapportage-tukey.py -->
# *Tukey's HSD test* is uitgevoerd om te toetsen welke van de drie gemiddelden significant verschillen. Filosofie en Arabische Taal en Cultuur verschillen significant (*MD* = `r Round_and_format(py$vATCvsFIL)`, *p* < 0,01). Tussen Geschiedenis en Arabische Taal en Cultuur is een significant verschil (*MD* = `r Round_and_format(py$vATCvsGSC)`, *p* < 0,01). Tussen Geschiedenis en Filosofie is geen significant verschil gevonden (*MD* = `r Round_and_format(py$vFILvsGSC)`, *p* = `r Round_and_format(py$vpFILvsGSC)`). 
# <!-- ## /TEKSTBLOK: Rapportage-tukey.py -->

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Van Geloven, N. (25 mei 2016). *One-way ANOVA*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/One-way_ANOVA).
# [^2]: Universiteit van Amsterdam (8 juli 2014). *One-way ANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/One-way_ANOVA).
# [^3]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese 'waar' is.  
# [^4]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^5]: Van Geloven, N. (21 maart 2018). *Kruskal Wallis*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Kruskal_Wallis).
# [^6]: De [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) maakt een rangschikking van de data. Hierdoor is de toets verdelingsvrij en is normaliteit geen assumptie. Ook zijn uitbijters minder van invloed op het eindresultaat. Toch wordt er voor deze toets minder vaak gekozen, omdat bij het maken van een rankschikking de dataset informatie verliest. Als de data wel normaal verdeeld zijn, heeft de [Kruskal-Wallis toets](10-Kruskal-Wallis-toets-R.html) minder onderscheidend vermogen dan wanneer de *one-way ANOVA* uitgevoerd zou worden.
# [^7]: Laerd statistics (2018). *Testing for Normality using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/testing-for-normality-using-spss-statistics.php. 
# [^8]: Universiteit van Amsterdam (14 juli 2014). *Normaliteit*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Normaliteit).
# [^9]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^10]: Wikipedia (7 september 2019). *Analysis of variance*. https://en.wikipedia.org/wiki/Analysis_of_variance.
# [^11]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^12]: Watson, P. (30 oktober 2019). *Rules of thumb on magnitudes of effect sizes*. [MRC Cognition and Brain Sciences Unit Wiki](http://imaging.mrc-cbu.cam.ac.uk/statswiki/FAQ/effectSize).
# [^13]: Eta-squared. (2019 May 14). Retrieved from: https://en.wikiversity.org/wiki/Eta-squared.
# [^14]: Universiteit van Amsterdam (26 augustus 2014). *MANOVA*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/MANOVA).
# [^15]: Marshall, E., & Boggis, E. (2016). *The statistics tutor’s quick guide to commonly used statistical tests*. http://www.statstutor.ac.uk/resources/uploaded/tutorsquickguidetostatistics.pdf. 
# [^16]: Outliers (13 augustus 2016). [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).
# [^17]: Uitbijters kunnen bepalend zijn voor de uitkomst van toetsen. Bekijk of de uitbijters valide uitbijters zijn en niet een meetfout of op een andere manier incorrect verkregen data. Het weghalen van uitbijters kan de uitkomst ook vertekenen, daarom is het belangrijk om verwijderde uitbijters te melden in een rapport. 
# [^18]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^19]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 86.
# [^20]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# 
# 
