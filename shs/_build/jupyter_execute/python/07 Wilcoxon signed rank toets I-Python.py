#!/usr/bin/env python
# coding: utf-8
---
title: "Wilcoxon signed rank toets"
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
# 
# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/07.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.py-->
# Gebruik de *Wilcoxon signed rank toets* om te toetsen of de som van de rangnummers van de verdelingen van twee gepaarde groepen van elkaar verschillen.[^1] Deze toets is een alternatief voor de [gepaarde t-toets](02-Gepaarde-t-toets-Python.html) als de verschilscores van de gepaarde groepen niet normaal verdeeld zijn. Alleen als de verdeling van de verschilscores symmetrisch is, kan de *Wilcoxon signed rank toets* gebruikt worden om een verschil tussen de medianen van gepaarde groepen te toetsen.[^3] Als de verdeling van verschilscores niet symmetrisch is, gebruik dan de gepaarde [tekentoets](27-Tekentoets-II-Python.html) om medianen te toetsen.
# <!-- ## /TEKSTBLOK: link1.py-->
# 
# # Onderwijscasus
# <div id ="casus">
# 
# De directeur van de Academie Mens & Maatschappij wil bekijken hoe het inkomen van zijn alumni zich ontwikkelt nadat zij zijn afgestudeerd. Hij is nieuwsgierig of het inkomen gedurende deze jaren groeit of juist stagneert voor deze alumni. Deze informatie is interessant om te gebruiken bij voorlichtingsactiviteiten van de Academie. Hij bekijkt het bruto jaarinkomen van de alumni één jaar na afstuderen en vergelijkt het met het bruto jaarinkomen vijf jaar na afstuderen. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil in de som van rangnummers van de verdeling tussen het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar na afstuderen en vijf jaar na afstuderen.
# 
# *H~A~*: Er is een verschil in de som van rangnummers van de verdeling tussen het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar na afstuderen en vijf jaar na afstuderen. Een van beide verdelingen bevat hogere waarden wat betreft het bruto jaarinkomen.
#  
# </div>
# 
# # Assumpties
# <!-- ## TEKSTBLOK: link2.py-->
# Het meetniveau van de afhankelijke variabele is ordinaal[^10] of continu.[^1] In deze toetspagina staat een casus met continue data centraal; een casus met ordinale data is te vinden in [een andere toetspagina](22-Wilcoxon-signed-rank-toets-II-Python.html).
# 
# De *Wilcoxon signed rank toets* is een alternatief voor de [gepaarde t-toets](02-Gepaarde-t-toets-Python.html). Een voordeel van de *Wilcoxon signed rank toets* is dat de data niet aan de assumptie van normaliteit hoeven te voldoen. Maar als de data wel normaal verdeeld is, heeft de *Wilcoxon signed rank toets* minder onderscheidend vermogen[^4] dan de [gepaarde t-toets](02-Gepaarde-t-toets-Python.html).[^5] Vandaar dat ondanks het voordeel van de grotere robuustheid minder vaak voor de *Wilcoxon signed rank toets* gekozen wordt. 
# <!-- ## /TEKSTBLOK: link2.py-->
# 
# ## Verdeling steekproef
# 
# De *Wilcoxon signed rank toets* schrijft geen assumpties voor over de verdeling van de verschilscores (verschillen tussen beide meetmomenten voor alle deelnemers[^19]).[^5] In principe toetst de *Wilcoxon signed rank toets* een hypothese over het verschil tussen de verdelingen van twee gepaarde groepen. De *Wilcoxon signed rank toets* maakt een rangschikking van de absolute waarden van de verschilscores en telt vervolgens de rangnummers op voor de positieve en negatieve verschilscores. Het verschil tussen de som van de positieve en negatieve rangnummers bepaalt de significantie van de toets. 
# 
# Als er geen symmetrische verdeling van verschilscores is, doet de *Wilcoxon signed rank toets* een uitspraak over het verschil tussen verdelingen. Een verschil tussen verdelingen kan meerdere oorzaken hebben. De top of toppen van de verdelingen kunnen verschillend zijn, maar ook de spreiding van de verdeling kan verschillen. In alle gevallen is er echter een verschil tussen de som van de rangnummers van de verdelingen. In andere woorden, de ene verdeling bevat hogere waarden dan de andere verdeling. Benoem daarom de sommen van positieve en negatieve rangnummers in de rapportage en visualiseer de verdeling van beide gepaarde groepen om duidelijk te maken op welke manier de verdelingen van elkaar verschillen.
# 
# <!-- ## TEKSTBLOK: link3.R-->
# Als de verschilscores echter symmetrisch zijn, toetst de *Wilcoxon signed rank toets* ook een hypothese over het verschil tussen de medianen van twee gepaarde groepen. In dat geval heeft de *Wilcoxon signed rank toets* een hoger onderscheidend vermogen[^4] dan de [tekentoets](06-Tekentoets-R.html) om medianen te toetsen.[^5] De [tekentoets](06-Tekentoets-R.html) vereist niet dat de verschilscores symmetrisch zijn en toetst alleen een hypothese over het verschil tussen medianen van gepaarde groepen.
# <!-- ## /TEKSTBLOK: link3.R-->
# 
# # Effectmaat
# 
# De p-waarde geeft aan of een (mogelijk) verschil tussen twee groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^6] 
# 
# De *Wilcoxon signed rank toets* heeft als effectmaat *r*. Een indicatie om *r* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^8] De effectmaat *r* wordt voor de *Wilcoxon signed rank toets* berekend door de *z*-waarde behorend bij de p-waarde van de toets te delen door de wortel van het aantal deelnemers, i.e. $\frac{z}{\sqrt{N}}$.[^8] Een correlatie tussen twee variabelen wordt vaak ook aangeduid met het symbool *r*. Beide zijn effectmaten, maar er is verder geen verband tussen de correlatie en de effectmaat van de *Wilcoxon signed rank toets*.

# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.py-->
# Er is data ingeladen met het bruto jaarinkomen van alumni van de Academie Mens & Maatschappij genaamd `dfAlumni_jaarinkomens`. De directeur wil een vergelijking maken tussen het inkomen één jaar na afstuderen (meetmoment T~1~) en vijf jaar na afstuderen (meetmoment T~2~).
# <!-- ## /TEKSTBLOK: Dataset-inladen.py-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.py -->
# Gebruik `<dataframe>.head()` en `<dataframe>.tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken.py -->

# In[ ]:


# Pandas library importeren
import pandas as pd


# In[ ]:


import pandas as pd
dfAlumni_jaarinkomens = pd.DataFrame(r.Alumni_jaarinkomens)


# In[ ]:


## Eerste 6 observaties
print(dfAlumni_jaarinkomens.head(6))


# In[ ]:


## Laatste 6 observaties
print(dfAlumni_jaarinkomens.tail(6))


# <!-- ## /OPENBLOK: Data-bekijken.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven.py-->
# Bekijk de grootte en de mediaan  van de data met `len()` en `numpy.median()` van het `numpy` package. Omdat inkomens vaak een scheve verdeling hebben, is de mediaan informatiever dan het gemiddelde.
# <!-- ## /TEKSTBLOK: Data-beschrijven.py-->
# <!-- ## OPENBLOK: Data-selecteren.py -->

# In[ ]:


Alumni_jaarinkomens_T1 = dfAlumni_jaarinkomens[dfAlumni_jaarinkomens["Meetmoment"] == "T1"]["Inkomen"]
Alumni_jaarinkomens_T2 = dfAlumni_jaarinkomens[dfAlumni_jaarinkomens["Meetmoment"] == "T2"]["Inkomen"]


# <!-- ## /OPENBLOK: Data-selecteren.py -->
# 
# <div class="col-container">
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-1.py -->

# In[ ]:


import numpy as np
print(len(Alumni_jaarinkomens_T1))
print(np.median(Alumni_jaarinkomens_T1))


# <!-- ## /OPENBLOK: Data-beschrijven-1.py -->
#   </div>
#   <div class="col">
# <!-- ## OPENBLOK: Data-beschrijven-2.py -->
# ``````{python Data beschrijven 2, collapse=TRUE}
# print(len(Alumni_jaarinkomens_T2))
# print(np.median(Alumni_jaarinkomens_T2))
# ```
# <!-- ## /OPENBLOK: Data-beschrijven-2.py -->
#   </div>
# </div>
# <!-- ## CLOSEDBLOK: Data-beschrijven-2.py -->

# In[ ]:


vMed_T1 = np.median(Alumni_jaarinkomens_T1)
vN_T1 = len(Alumni_jaarinkomens_T1)
vMed_T2 = np.median(Alumni_jaarinkomens_T2)
vN_T2 = len(Alumni_jaarinkomens_T2)


# <!-- ## /CLOSEDBLOK: Data-beschrijven-2.py -->
# 
# <!-- ## TEKSTBLOK: Data-beschrijven3.py-->
# 
# * Mediaan bruto jaarinkomen op T~1~: `r paste0("€",format(py$vMed_T1, scientific = FALSE))` 
# * Mediaan bruto jaarinkomen op T~2~: `r paste0("€",format(py$vMed_T2, scientific = FALSE))` 
# * Aangezien de gegevens gepaard zijn, zijn de groepsgroottes op beide meetmomenten gelijk: *n~T1~* = `r py$vN_T1` en *n~T2~* = `r py$vN_T2`
# 
# <!-- ## /TEKSTBLOK: Data-beschrijven3.py-->
# 
# ## De data visualiseren
# 
# Maak een histogram[^18] om de verdeling van de bruto jaarinkomens van de alumni één jaar en vijf jaar na afstuderen visueel weer te geven.[^11]
# 
# <!-- ## OPENBLOK: Histogram1.py -->

# In[ ]:


## Histogram met matplotlib
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (15, 10))
sub1 = fig.add_subplot(1, 2, 1)
title1 = plt.title("Een jaar na afstudereren")
hist1 = plt.hist(Alumni_jaarinkomens_T1, density = True, edgecolor = "black", bins = 29)

sub2 = fig.add_subplot(1, 2, 2)
title2 = plt.title("Vijf jaar na afstudereren")
hist2 = plt.hist(Alumni_jaarinkomens_T2, density = True, edgecolor = "black", bins = 31)

main = fig.suptitle('Bruto jaarinkomen alumni Mens & Maatschappij')
plt.show()


# <!-- ## /OPENBLOK: Histogram1.py -->
# 
# Op beide meetmomenten is te zien dat de meeste alumni tussen de 0 en €35.000 euro per jaar verdienen en dat een paar alumni hierboven zit. Beide verdelingen hebben één top, maar zijn niet symmetrisch omdat de meerderheid van de observaties links van de top ligt. Beide verdeling lijken niet echt op elkaar qua vorm en spreiding.
# 
# Maak vervolgens een histogram van de verschilscores om te onderzoeken of deze verdeling symmetrisch is.
# 
# <!-- ## OPENBLOK: Histogram2.py -->

# In[ ]:


# Maak een variabele met de verschilscores
Alumni_verschilscores = np.array(Alumni_jaarinkomens_T2) - np.array(Alumni_jaarinkomens_T1)

## Histogram met matplotlib
import matplotlib.pyplot as plt
hist = plt.hist(Alumni_verschilscores, density = True, edgecolor = "black", bins = 9)
title = plt.title("Verschilscores bruto jaarinkomen alumni Mens & Maatschappij")
xlab = plt.xlabel("Verschilscores")
ylab = plt.ylabel("Frequentiedichtheid")
plt.show()


# <!-- ## /OPENBLOK: Histogram2.py -->
# 
# De verdeling van de verschilscores bevat voornamelijk positieve waarden en een paar negatieve waarden; de meeste alumni zijn er dus in bruto jaarinkomen op vooruitgegaan. De verdeling is niet symmetrisch. Gebruik de *Wilcoxon signed rank toets* dus niet om een uitspraak te doen over het verschil in medianen.
# 
# ## Wilcoxon signed rank toets
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets.py -->
# Voer de *Wilcoxon signed rank toets* uit om de vraag te beantwoorden of de verdeling van de bruto jaarinkomens van alumni verschillend is voor de inkomens één jaar en vijf jaar na afstuderen. Gebruik de functie `wilcoxon()` van het `scipy` package met als eerste argument de jaarinkomens vijf jaar na afstuderen `Alumni_jaarinkomens_T2`, als tweede argument de jaarinkomens één jaar na afstuderen `Alumni_jaarinkomens_T1` en als derde argument `alternative = 'two-sided'` om tweezijdig te toetsen.
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets.py -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets.py -->

# In[ ]:


import scipy.stats as sp
sp.wilcoxon(Alumni_jaarinkomens_T2, 
Alumni_jaarinkomens_T1,
alternative = 'two-sided')


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets.py -->
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets2.py -->
# Bereken de effectmaat *r* vervolgens op basis van de p-waarde van de *Wilcoxon signed rank toets*.

# In[ ]:


# Sla de p-waarde op
stat, pval = sp.wilcoxon(Alumni_jaarinkomens_T2, Alumni_jaarinkomens_T1, alternative = 'two-sided')

# Bereken de effectgrootte voor een tweezijdige toets
Effectmaat = sp.norm.ppf(pval/2) / np.sqrt(len(Alumni_jaarinkomens_T1))
# Bereken de effectgrootte voor een eenzijdige toets
#r = sp.norm.ppf(pval) / np.sqrt(len(Alumni_jaarinkomens_T1))

# Print de effectgrootte (vaak weergegeven als absolute waarde)
print(np.abs(Effectmaat))


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets2.py -->
# 
# Bereken de aantallen en de sommen van positieve en negatieve rangnummers op basis van de verschilscores.
# 
# <!-- ## OPENBLOK: Wilcoxon-signed-rank-toets3.py -->

# In[ ]:


# Bereken verschilscores
Verschilscores = np.array(Alumni_jaarinkomens_T2) - np.array(Alumni_jaarinkomens_T1)

# Rangschik de absolute waarden van verschilscores met scipy.rankdata()
Rangnummers = sp.rankdata(np.abs(Verschilscores))

# Maak een vector met daarin de tekens (plus of min) van verschilscores) met numpy.sign()
Tekens = np.sign(Verschilscores)

# Bereken het aantal en de som van de positieve rangnummers
N_positief = len(Tekens[Tekens == 1])
Som_positief = np.sum(Rangnummers[Tekens == 1])

# Bereken het aantal en de som van de negatieve rangnummers
N_negatief = len(Tekens[Tekens == -1])
Som_negatief = np.sum(Rangnummers[Tekens == -1])


# <!-- ## /OPENBLOK: Wilcoxon-signed-rank-toets3.py -->

# <!-- ## CLOSEDBLOK: Wilcoxon-signed-rank-toets.py -->

# In[ ]:


stat, pval = sp.wilcoxon(Alumni_jaarinkomens_T2, Alumni_jaarinkomens_T1, alternative = 'two-sided')


# <!-- ## /CLOSEDBLOK: Wilcoxon-signed-rank-toets.py -->
# 
# <!-- ## TEKSTBLOK: Wilcoxon-signed-rank-toets4.py -->
# * *V* = `r Round_and_format(py$stat)`, *p* < 0,0001 , *r* = `r Round_and_format(abs(as.numeric(py$Effectmaat)))`
# * p-waarde < 0,05, dus de H~0~ wordt verworpen[^9]
# * De toetsstatistiek *V* is in deze casus gelijk aan de som van de negatieve rangnummers
# * Het aantal positieve rangnummers is `r py$N_positief`; de som is `r format(round(py$Som_positief), scientific = FALSE)`
# * Het aantal negatieve rangnummers is `r py$N_negatief`; de som is `r round(py$Som_negatief)`
# * De som van de positieve rangnummers is hoger dan de som van de negatieve rangnummers De verdeling van de bruto jaarinkomens bevat dus hogere waarden vijf jaar na afstuderen.
# * Effectmaat is `r Round_and_format(abs(as.numeric(py$Effectmaat)))`, dus een groot effect
# 
# <!-- ## /TEKSTBLOK: Wilcoxon-signed-rank-toets4.py -->
# 
# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *Wilcoxon signed rank toets* is uitgevoerd om de vraag te beantwoorden of de verdeling van het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij verschillend is voor de inkomens één jaar na afstuderen en vijf jaar na afstuderen. De resultaten van de toets laten zien dat er een significant verschil is tussen het bruto jaarinkomen van de alumni van de Academie Mens & Maatschappij één jaar en vijf jaar na afstuderen, *V* = `r Round_and_format(py$stat)`, *p* < 0,0001, *r* = `r Round_and_format(abs(py$Effectmaat))`. Er zijn `r py$N_positief` alumni die vijf jaar na afstuderen meer verdienen dan één jaar na afstuderen (som van rangnummers is `r format(round(py$Som_positief), scientific = FALSE)`) en er zijn `r py$N_negatief` alumni die vijf jaar na afstuderen minder verdienen dan één jaar na afstuderen (som van rangnummers is `r py$Som_negatief`). Alumni lijken dus meer te verdienen wanneer ze vijf jaar afgestudeerd zijn.
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Wilcoxon Signed-Rank Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/wilcoxon-signed-rank-test-using-spss-statistics.php
# [^3]: Statistics How To (27 mei 2018). *One Sample Median Test*. [Statistics How to](https://www.statisticshowto.datasciencecentral.com/one-sample-median-test/).
# [^4]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese waar is.  
# [^5]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^6]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^8]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^9]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^10]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^11]: De breedte van de staven van het histogram worden hier automatisch bepaald, maar kunnen handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^12]: Bij de *Wilcoxon signed rank toets* en andere nonparametrische toetsen wordt de data eerst gerangschikt zodat elke observatie een rangnummer toegewezen krijgt. Deze rangnummers worden vervolgens gebruikt om de toets uit te voeren.
# [^18]: De breedte van de staven van het histogram wordt vaak automatisch bepaald, maar kan handmatig aangepast worden. Aangezien de breedte van de staven bepalend zijn voor de indruk die de visualisatie geeft, is het verstandig om hier goed op te letten.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
