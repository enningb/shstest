#!/usr/bin/env python
# coding: utf-8
---
title: "Chi-kwadraat toets voor onafhankelijkheid en Fisher-Freeman-Halton exact toets"
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
# <!-- ## OPENBLOK: Data-aanmaken.py -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '# TODO: Uitleg extra pagina: nominaal, ordinaal etc., afhanjeklijk en onafhankelijk  \n# TODO: Uitleg transformeren data ')


# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/16.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.py -->
# Gebruik de *Chi-kwadraat toets voor onafhankelijkheid*[^1] of de *Fisher-Freeman-Halton exact toets*[^2] om te toetsen of er een afhankelijkheid is tussen twee ongepaarde categorische variabelen. De *Fisher-Freeman-Halton exact toets* is een alternatief voor de *Chi-kwadraat toets voor onafhankelijkheid* bij een laag aantal observaties.[^2]<sup>,</sup>[^3] De *Fisher-Freeman-Halton exact toets* is een uitbreiding van de [Fisher's exact toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-Python.html) welke gebruikt wordt om te toetsen of er een verband bestaat tussen twee ongepaarde binaire variabelen, oftewel een 2x2 tabel. 
# <!-- ## /TEKSTBLOK: link1.py -->
# 
# In de huidige casus worden de *Chi-kwadraat toets voor onafhankelijkheid* en de *Fisher-Freeman-Halton exact toets* gebruikt voor een casus met een categorische variabele bestaande uit twee categorieën en een categorische variabele bestaande uit meer dan twee categorieën. Beide toetsen zijn in het algemeen te gebruiken voor alle onderzoeksvragen waarbij twee categorische variabelen die beide twee of meer categorieën bevatten getoetst worden.
# 
# # Onderwijscasus
# <div id = "casus">
# De opleidingsdirecteur van de Bachelor Antropologie vraagt zich af wat de invloed is van de instroom van studenten met een vooropleiding in het buitenland op het behalen van een positief BSA. Krijgen studenten met een vooropleiding uit bepaalde landen vaker een positief BSA dan studenten met een vooropleiding uit andere landen? Op basis van deze analyse kan de opleidingsdirecteur overwegen om bij de inrichting van het tutoraat rekening te houden met de vooropleidingen van studenten.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# H~0~: Er is geen afhankelijkheid tussen het land van de hoogste vooropleiding en het wel of niet behalen van het BSA voor studenten van de bachelor Antropologie.
# 
# H~A~: Er is een afhankelijkheid tussen het land van de hoogste vooropleiding en het wel of niet behalen van het BSA voor studenten van de bachelor Antropologie.  
# </div>
# 
# # Assumpties
# Voor een valide resultaat moeten de data aan een aantal voorwaarden voldoen voordat de toets uitgevoerd kan worden. De variabelen zijn categorisch (nominaal[^4] of ordinaal[^10]) en de observaties zijn onafhankelijk van elkaar. 
# 
# ## Groepsgrootte
# De *Chi-kwadraat toets voor onafhankelijkheid* heeft een assumptie wat betreft het aantal observaties in een kruistabel. Een kruistabel is een tabel waarin de aantallen observaties worden weergegeven per combinatie van de categorieën van beide variabelen. De kruistabel van de data in de huidige casus is te vinden in Tabel 1.   
# 
# <!-- ## TEKSTBLOK: Groepsgrootte1.R -->
# 
# |                      | NL   | GE | IT | UK | ES | BE | US |   |
# | ------------- | ---------| ------------| -------------| ---------|---------|---------|---------| ------------- |
# | **Negatief BSA** |`r BSA_kruistabel[1,1]` | `r BSA_kruistabel[1,2]`  | `r BSA_kruistabel[1,3]`  | `r BSA_kruistabel[1,4]`  | `r BSA_kruistabel[1,5]`  | `r BSA_kruistabel[1,6]`  | `r BSA_kruistabel[1,7]`  | **`r sum(BSA_kruistabel[1,1:7])`**|
# | **Positief BSA**  |`r BSA_kruistabel[2,1]`   | `r BSA_kruistabel[2,2]` | `r BSA_kruistabel[2,3]` | `r BSA_kruistabel[2,4]` | `r BSA_kruistabel[2,5]` | `r BSA_kruistabel[2,6]` | `r BSA_kruistabel[2,7]` | **`r sum(BSA_kruistabel[2,1:7])`**|
# |**Totaal** |**`r sum(BSA_kruistabel[1:2,1])`**   | **`r sum(BSA_kruistabel[1:2,2])`** | **`r sum(BSA_kruistabel[1:2,3])`**   | **`r sum(BSA_kruistabel[1:2,4])`**   | **`r sum(BSA_kruistabel[1:2,5])`**   | **`r sum(BSA_kruistabel[1:2,6])`**   | **`r sum(BSA_kruistabel[1:2,7])`**   | **`r sum(BSA_kruistabel)`** |
# *Tabel 1. Geobserveerde aantallen casus BSA en land van hoogste vooropleiding.*
# <!-- ## TEKSTBLOK: Groepsgrootte1.R -->
# 
# De *Chi-kwadraat toets voor onafhankelijkheid* wordt onbetrouwbaar als er in meer dan 20% van de cellen van de kruistabel een verwacht aantal observaties van 5 of lager is.[^5]<sup>,</sup>[^7] Gebruik in dat geval de *Fisher-Freeman-Halton toets*. Het verwachte aantal observaties in een cel is het aantal observaties dat zich volgens de nulhypothese in een cel zou moeten bevinden. Dit aantal kan worden berekend via kansrekening, uitgaande van de nulhypothese dat er geen afhankelijkheid tussen de twee variabelen is.
# 
# <!-- ## TEKSTBLOK: Groepsgrootte2.R -->
# Een voorbeeldberekening van het het verwachte aantal observaties van de studenten met een Nederlandse vooropleiding met positief BSA werkt als volgt: vermenigvuldig het totaal aantal studenten met een Nederlandse vooropleiding (`r sum(BSA_kruistabel[1:2,1])`) met het totaal aantal studenten met een positief BSA (`r sum(BSA_kruistabel[1,1:7])`) en deel dit door het totaal aantal studenten (`r sum(BSA_kruistabel)`).
# 
# * aantal studenten positief BSA: `r sum(BSA_kruistabel[1,1:7])`   
# * aantal studenten met Nederlandse vooropleiding: `r sum(BSA_kruistabel[1:2,1])`  
# * totaal aantal studenten: `r sum(BSA_kruistabel)` 
# * verwacht aantal studenten met Nederlandse vooropleiding met positief BSA: `r sum(BSA_kruistabel[1,1:7])` * `r sum(BSA_kruistabel[1:2,1])`/`r sum(BSA_kruistabel)` ≈ `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,1])/sum(BSA_kruistabel)) `.

# |                      | NL   | GE | IT | UK | ES | BE | US |   |
# | ------------- | ---------| ------------| -------------| ---------|---------|---------|---------| ------------- |
# | **Negatief BSA** |`r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,1])/sum(BSA_kruistabel)) ` | `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,2])/sum(BSA_kruistabel)) `  | `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,3])/sum(BSA_kruistabel)) `  | `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,4])/sum(BSA_kruistabel)) `  | `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,5])/sum(BSA_kruistabel)) `  | `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,6])/sum(BSA_kruistabel)) `  | `r round(sum(BSA_kruistabel[1,1:7])*sum(BSA_kruistabel[1:2,7])/sum(BSA_kruistabel)) `  | **`r sum(BSA_kruistabel[1,1:7])`**|
# | **Positief BSA**  |`r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,1])/sum(BSA_kruistabel)) `   | `r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,2])/sum(BSA_kruistabel)) ` | `r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,3])/sum(BSA_kruistabel)) ` | `r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,4])/sum(BSA_kruistabel)) ` | `r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,5])/sum(BSA_kruistabel)) ` | `r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,6])/sum(BSA_kruistabel)) ` | `r round(sum(BSA_kruistabel[2,1:7])*sum(BSA_kruistabel[1:2,7])/sum(BSA_kruistabel)) ` | **`r sum(BSA_kruistabel[2,1:7])`**|
# |**Totaal** |**`r sum(BSA_kruistabel[1:2,1])`**   | **`r sum(BSA_kruistabel[1:2,2])`** | **`r sum(BSA_kruistabel[1:2,3])`**   | **`r sum(BSA_kruistabel[1:2,4])`**   | **`r sum(BSA_kruistabel[1:2,5])`**   | **`r sum(BSA_kruistabel[1:2,6])`**   | **`r sum(BSA_kruistabel[1:2,7])`**   | **`r sum(BSA_kruistabel)`** |
# *Tabel 2. Verwachte aantallen observaties casus BSA en land van hoogste vooropleiding.*
# <!-- ## TEKSTBLOK: Groepsgrootte2.R -->
# 
# Alle verwachte aantallen observaties zijn te vinden in Tabel 2. Merk ook op dat de totalen in de rijen en kolommen gelijk zijn aan de totalen in Tabel 1, de kruistabel met de aantallen observaties. Geen van de verwachte aantallen is kleiner of gelijk aan vijf, dus er is voldaan aan de assumptie van groepsgrootte voor de *Chi-kwadraat toets voor onafhankelijkheid*.
# 
# # Post-hoc toetsen
# 
# De *Chi-kwadraat toets voor onafhankelijkheid* en *Fisher-Freeman-Halton exact toets* worden gebruikt om een afhankelijkheid aan te tonen tussen twee ongepaarde categorische variabelen. Wanneer één of beide variabelen meer dan twee categorieën bevat, worden post-hoc toetsen uitgevoerd om te bepalen welke categorieën significant van elkaar verschillen.
# 
# Als post-hoc toets voor de *Chi-kwadraat toets voor onafhankelijkheid* wordt het gestandaardiseerde residu gebruikt. Dit is het gestandaardiseerde verschil tussen het (geobserveerde) aantal observaties en het verwachte aantal observaties, waarbij gestandaardiseerd betekent dat het een gemiddelde van 0 en standaardafwijking van 1 heeft. Op deze manier kunnen de verschillende residuen met elkaar vergeleken worden, omdat ze dezelfde schaal hebben. Voor elke cel in de kruistabel kan het gestandaardiseerde residu bepaald worden. Vergelijkbaar met z-scores[^11] zijn deze residuen significant bij een waarde groter dan ± 1,96 wanneer een significantieniveau (α) van 0,05 wordt gehanteerd. Op deze manier kan bepaald worden in welke cellen er afwijkingen van de verwachte aantallen zijn. [^5]
# 
# <!-- ## TEKSTBLOK: link2.py -->
# Voor de *Fisher-Freeman-Halton exact toets* is er geen specifiek voorgeschreven post-hoc toets.[^3]<sup>,</sup>[^5] Een goede optie is het uitvoeren van losse [Fisher's exact toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-Python.html) voor elke mogelijke combinatie van 2x2 tabellen. Gebruik een correctie op de p-waarden, omdat er meerdere testen tegelijk uitgevoerd worden. Een bekende correctie is de Bonferroni methode, andere opties zijn ook mogelijk. De keuze voor een correctie is afhankelijk van het onderzoek.[^5]
# <!-- ## /TEKSTBLOK: link2.py -->
# 
# # Effectmaat
# 
# De p-waarde geeft aan of het verschil tussen twee groepen statistisch significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^5] 
# De *Chi-kwadraat toets voor onafhankelijkheid* heeft als effectmaat *w*.[^6] Een indicatie om *w* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^7]
# 
# <!-- ## TEKSTBLOK: link3.py -->
# De *Fisher-Freeman-Halton exact toets* heeft geen specifieke effectmaat. De post-hoc toets van deze toets - [Fisher's exact toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-Python.html) - gebruikt echter de odds ratio als effectmaat. De odds ratio is een effectmaat die voor zowel de *Chi-kwadraat toets voor onafhankelijkheid* als de [Fisher's exact toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-Python.html) kan worden gebruikt. Een voorwaarde is echter dat beide variabelen binair zijn. In andere woorden, er moet een 2x2 kruistabel gevormd kunnen worden. Odds is een Engelse term voor de verhouding van twee kansen, bijvoorbeeld de verhouding tussen het aantal studenten met positief BSA en negatief BSA. Een odds ratio is de verhouding tussen twee odds, dus de verhouding van de odds van studenten met Nederland als land van hoogste vooropleiding en studenten met Duitsland als land van hoogste vooropleiding. De odds ratio geeft dus een interpretatie van de verschillen tussen landen op het behalen van een positief of negatief BSA.[^5]
# <!-- ## /TEKSTBLOK: link3.py -->
# 
# # De data bekijken
# 
# <!-- ## TEKSTBLOK: Data-bekijken1.py -->
# Er is een dataset ingeladen genaamd `dfBSA_antropologie`. In deze dataset is voor elke student aangegeven wat het land van de hoogst genoten vooropleiding is en of ze een positief of negatief BSA ontvangen hebben.
# <!-- ## /TEKSTBLOK: Data-bekijken1.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


## Importeer nuttige packages
import numpy as np
import pandas as pd
import scipy.stats as sps
import statsmodels.stats as sms
import statsmodels.api as sma


# In[ ]:


dfBSA_antropologie = pd.DataFrame(r.BSA_antropologie)
dfFisher_BSA_antropologie = pd.DataFrame(r.Fisher_BSA_antropologie)


# In[ ]:


## Eerste 5 observaties
print(dfBSA_antropologie.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfBSA_antropologie.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.py -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Landen_vooropleiding` en `BSA`. Maak de kruistabel met de functie `.crosstable()` van het package `pandas` met als argumenten de variabele `dfBSA_antropologie['BSA']` (positief of negatief BSA) en `dfBSA_antropologie['Landen_vooropleiding']` (land van hoogst genoten vooropleiding).
# <!-- ## /TEKSTBLOK: Data-kruistabel1.py -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.py -->

# In[ ]:


# Maak een kruistabel
BSA_antropologie_kruistabel =  pd.crosstab(dfBSA_antropologie['BSA'], dfBSA_antropologie['Landen_vooropleiding'])

# Print de kruistabel
print(BSA_antropologie_kruistabel)

# Maak een tabel met proporties, argument 'normalize = columns' zorgt ervoor dat de proporties
# per rij berekend worden
Prop_BSA_antropologie_kruistabel = pd.crosstab(dfBSA_antropologie['BSA'], dfBSA_antropologie['Landen_vooropleiding'], normalize = 'columns')

# Print de tabel met proporties met drie decimalen
print(round(Prop_BSA_antropologie_kruistabel, 3))


# In[ ]:


UK = np.array(Prop_BSA_antropologie_kruistabel)[1,5]


# <!-- ## /OPENBLOK: Data-kruistabel2.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3.py -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat de meerderheid van de studenten een positief BSA ontvangt voor elk land van vooropleiding. Van studenten uit het Verenigd Koninkrijk (UK) haalt verhoudingsgewijs het grootste deel een positief BSA. Het percentage studenten met een positief BSA is hier (`r Round_and_format(100 * py$UK)`%).
# <!-- ## /TEKSTBLOK: Data-kruistabel3.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel4.R -->
# Bekijk in aanvulling op de kruistabel de data ook met een staafdiagram. Maak een staafdiagram van de aantallen en percentages studenten met een positief en negatief BSA voor de verschillende landen van vooropleiding. Gebruik het argument `position = "dodge"` in de functie `geom_bar()` om de aantallen weer te geven en het argument `position = "fill"` in de functie `geom_bar()` om de proporties weer te geven.
# <!-- ## /TEKSTBLOK: Data-kruistabel4.R -->
# 
# 

# In[ ]:


get_ipython().run_cell_magic('R', '', '## Bereken de frequentie voor elke combinatie van BSA advies en land van vooropleiding\nFrequenties <- aggregate(Studentnummer ~ BSA + Landen_vooropleiding, \n                         data = BSA_antropologie, \n                         FUN = length)\n## Verander de kolomnaam voor de variabele met de frequenties\ncolnames(Frequenties)[3] <- "Frequentie"\n\n## Maak een staafdiagram met ggplot2\nlibrary(ggplot2)\n\nggplot(Frequenties, \n       aes(y = Frequentie, x = Landen_vooropleiding, fill = BSA)) + \n  geom_bar(position = "dodge", stat = "identity") +\n  xlab("Landen vooropleiding") \n\nggplot(Frequenties, \n       aes(y = Frequentie, x = Landen_vooropleiding, fill = BSA)) + \n  geom_bar(position = "fill", stat = "identity") +\n  ylab("Proportie") +\n  xlab("Landen vooropleiding") ')


# De staafdiagram laat ook zien dat de meeste studenten in elk land van vooropleiding in de meerderheid een positief BSA behalen. De proportie negatieve BSA is het hoogst voor Italië en het laagst voor het Verenigd Koninkrijk.

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: Assumptie.py -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk of kleiner dan vijf is. Bereken het verwacht aantal observaties met de functie `.contingency.expected_freq()` van het `scipy.stats` package met als argument de kruistabel `BSA_antropologie_kruistabel`.
# <!-- ## /TEKSTBLOK: Assumptie.py -->
# 
# <!-- ## OPENBLOK: Assumptie1.py -->

# In[ ]:


# Maak een kruistabel
BSA_antropologie_kruistabel =  pd.crosstab(dfBSA_antropologie['BSA'], dfBSA_antropologie['Landen_vooropleiding'])

# Bereken verwachte aantallen observaties
sps.contingency.expected_freq(BSA_antropologie_kruistabel)


# <!-- ## /OPENBLOK: Assumptie1.py -->
# 
# Geen van de verwachte aantallen observaties is gelijk of kleiner dan vijf, dus de *Chi-kwadraat toets voor onafhankelijkheid* kan worden uitgevoerd.
# 
# # Chi-kwadraat toets voor onafhankelijkheid
# ## Uitvoering
# <!-- ## TEKSTBLOK: Chi2-toets.py -->
# De *Chi-kwadraat toets voor onafhankelijkheid* wordt uitgevoerd om de vraag te beantwoorden of er een afhankelijkheid is tussen het land van vooropleiding en het wel of niet halen van een positief BSA. Gebruik de functie `.stats.chi2_contingency()` van het `scipy` package met als argument de kruistabel `BSA_antropologie_kruistabel`. De weergegeven output bevat de teststatistiek, de p-waarde, het aantal vrijheidsgraden en een aantal met de verwachte aantallen observaties (in deze volgorde).
# <!-- ## /TEKSTBLOK: Chi2-toets.py -->
# 
# <!-- ## OPENBLOK: Chi2-toets.py -->

# In[ ]:


import scipy.stats as sps
sps.chi2_contingency(BSA_antropologie_kruistabel)


# <!-- ## /OPENBLOK: Chi2-toets.py -->
# 
# <!-- ## CLOSEDBLOK: Chi2-toets.py-->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Chi2-toets.py-->
# 
# Bereken de effectmaat *w* vervolgens op basis van de *&chi;^2^*-waarde van de *Chi-kwadraat toets voor onafhankelijkheid*.
# <!-- ## OPENBLOK: Chi2-toets-2.py -->

# In[ ]:


# Sla de teststatistiek op
chi2, pval, df, tab = sps.chi2_contingency(BSA_antropologie_kruistabel)

# Bereken het totaal aantal observaties als som van de kruistabel
N = np.sum(np.array(BSA_antropologie_kruistabel))

# Bereken eta squared
Eta2 = np.sqrt(chi2 / N)

# Print de effectgrootte
print(Eta2)


# <!-- ## /OPENBLOK: Chi2-toets-2.py -->

# <!-- ## TEKSTBLOK: Chi2-toets4.py-->
# * *&chi;^2^* ~`r Round_and_format(py$df)`~ = `r Round_and_format(py$chi2)`, *p* < 0,0001  
# * Vrijheidsgraden: *df* = (*k*-1)(*r*-1), waar k staat voor kolom en r voor rij. In dit geval geldt *df* = `r Round_and_format(py$df)`. 
# * p-waarde < 0,05, de H~0~ wordt verworpen.[^8]
# * Effectmaat is `r Round_and_format(py$Eta2)`, dus een klein tot gemiddeld effect
# 
# <!-- ## /TEKSTBLOK: Chi2-toets4.py-->
# 
# ## Post-hoc toets: gestandaardiseerde residuen
# 
# Voer post-hoc toetsen uit om te bepalen welke landen van hoogste vooropleiding van elkaar verschillen wat betreft de verdeling van het aantal studenten met positief en negatief BSA. Inspecteer hiervoor de Pearson residuen van de *Chi-kwadraat toets voor onafhankelijkheid* op waarden groter dan 1,96 en kleiner dan -1,96. Let op dat hier nog geen correctie voor meerdere testen plaatsvindt.[^9]
# 
# <!-- ## OPENBLOK: Chi2-toets post-hoc1.py -->

# In[ ]:


# Laad het package statsmodels.api in om de gestandaardiseerde residuën weer te geven
import statsmodels.api as sma

# Bereken de residuen 
Residuen = sma.stats.Table(BSA_antropologie_kruistabel).resid_pearson

# Print de residuen 
print(round(Residuen,3))


# <!-- ## /OPENBLOK: Chi2-toets post-hoc1.py -->
# 
# <!-- ## TEKSTBLOK: Chi2-toets post-hoc2.py -->
# * Significant hoger aantal observaties bij negatief BSA België (BE), *z* = `r Round_and_format(py$Residuen[1,"BE"])`
# * Significant hoger aantal observaties bij negatief BSA Italië (IT), *z* = `r Round_and_format(py$Residuen[1,"IT"])`
# * Significant lager aantal observaties bij negatief BSA Nederland (NL), *z* = `r Round_and_format(py$Residuen[1,"NL"])`
# * Significant lager aantal observaties bij negatief BSA Verenigd Koninkrijk (UK), *z* = `r Round_and_format(py$Residuen[1,"UK"])`
# * Significant hoger aantal observaties bij negatief BSA Verenigde Staten (US), *z* = `r Round_and_format(py$Residuen[1,"US"])`
# * Significant lager aantal observaties bij positief BSA Italië (IT), *z* = `r Round_and_format(py$Residuen[2,"IT"])`
# 
# <!-- ## /TEKSTBLOK: Chi2-toets post-hoc2.py -->
# 

# ## Rapportage
# 
# <!-- ## TEKSTBLOK: RapportageChi2.py -->
# De *Chi-kwadraat toets voor onafhankelijkheid* is uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen het land van hoogst genoten vooropleiding en het wel of niet behalen van een positief BSA. De resultaten illustreren dat de nulthypothese verworpen kan worden, *&chi;^2^* ~`r Round_and_format(py$df)`~ = `r Round_and_format(py$chi2)`, *p* < 0,0001, *w* = `r Round_and_format(py$Eta2)`. Het land van hoogst genoten vooropleiding en het behalen van een positief of negatief BSA zijn dus niet onafhankelijk van elkaar. Dat betekent dat er verschillen zijn tussen de landen wat betreft de proportie studenten met een positief BSA.
# 
# De resultaten van de post-hoc toetsen van de *Chi-kwadraat toets voor onafhankelijkheid* zijn te vinden in Tabel 3, waarin geobserveerde aantallen met asterisk significant verschillend zijn van verwachte aantallen. De geobserveerde aantallen voor de verschillende landen van hoogste vooropleiding bij een positief BSA verschillen niet significant van de verwachte aantallen. Bij een negatief BSA is er echter een aantal landen waarbij significante verschillen van het verwachte aantal zijn op te merken. Nederland (NL; *z* = `r Round_and_format(py$Residuen[1,"NL"])`) en het Verenigd Koninkrijk (UK; *z* = `r Round_and_format(py$Residuen[1,"UK"])`) hebben een lager aantal studenten met een negatief BSA dan verwacht; Italië (IT; *z* = `r Round_and_format(py$Residuen[1,"IT"])`), België (BE; *z* = `r Round_and_format(py$Residuen[1,"BE"])`) en de Verenigde Staten (US; *z* = `r Round_and_format(py$Residuen[1,"US"])`) een hoger aantal studenten met negatief BSA dan verwacht. Daarnaast heeft Italië (IT; *z* = `r Round_and_format(py$Residuen[2,"IT"])`) ook een lager aantal studenten met positief BSA dan verwacht.
# <!-- ## /TEKSTBLOK: RapportageChi2.py -->
# 
# <!-- ## TEKSTBLOK: RapportageChi3.R -->
# 
# |                      | NL   | GE | IT | UK | ES | BE | US |   |
# | ------------- | ---------| ------------| -------------| ---------|---------|---------|---------| ------------- |
# | **Positief BSA** |`r BSA_kruistabel[1,1]` | `r BSA_kruistabel[1,2]`  | `r BSA_kruistabel[1,3]`  | `r BSA_kruistabel[1,4]`  | `r BSA_kruistabel[1,5]`  | `r BSA_kruistabel[1,6]`  | `r BSA_kruistabel[1,7]`\*  | **`r sum(BSA_kruistabel[1,1:7])`**|
# | **Negatief BSA**  |`r BSA_kruistabel[2,1]`\*   | `r BSA_kruistabel[2,2]` | `r BSA_kruistabel[2,3]`\* | `r BSA_kruistabel[2,4]`\* | `r BSA_kruistabel[2,5]` | `r BSA_kruistabel[2,6]`\* | `r BSA_kruistabel[2,7]`\* | **`r sum(BSA_kruistabel[2,1:7])`**|
# |**Totaal** |**`r sum(BSA_kruistabel[1:2,1])`**   | **`r sum(BSA_kruistabel[1:2,2])`** | **`r sum(BSA_kruistabel[1:2,3])`**   | **`r sum(BSA_kruistabel[1:2,4])`**   | **`r sum(BSA_kruistabel[1:2,5])`**   | **`r sum(BSA_kruistabel[1:2,6])`**   | **`r sum(BSA_kruistabel[1:2,7])`**   | **`r sum(BSA_kruistabel)`** |
# *Tabel 3. Geobserveerde aantallen casus BSA en land van hoogste vooropleiding. Aantallen met asterisk zijn significant verschillend van verwachte aantallen.*
# <!-- ## /TEKSTBLOK: RapportageChi3.R -->

# # Fisher-Freeman-Halton exact toets
# 
# <!-- ## TEKSTBLOK: UitvoeringFFH.py -->
# De *Fisher-Freeman-Halton exact toets* wordt uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen het land van hoogst genoten vooropleiding en het wel of niet behalen van een positief BSA. Deze toets wordt in plaats van de *Chi-kwadraat toets voor onafhankelijkheid* gebruikt wanneer er in meer dan 20% van de cellen een verwacht aantal observaties van 5 of lager is. Er is een nieuwe dataset `dfFisher_BSA_antropologie` ingeladen met daarin een lager aantal observaties.
# <!-- ## /TEKSTBLOK: UitvoeringFFH.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1f.py -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Landen_vooropleiding` en `BSA`. Maak de kruistabel met de functie `.crosstable()` van het package `pandas` met als argumenten de variabele `dfFisher_BSA_antropologie['BSA']` (positief of negatief BSA) en `dfFisher_BSA_antropologie['Landen_vooropleiding']` (land van hoogst genoten vooropleiding).
# <!-- ## /TEKSTBLOK: Data-kruistabel1f.py -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2f.py -->

# In[ ]:


# Maak een kruistabel
Fisher_BSA_antropologie_kruistabel =  pd.crosstab(dfFisher_BSA_antropologie['BSA'], dfFisher_BSA_antropologie['Landen_vooropleiding'])

# Print de kruistabel
print(Fisher_BSA_antropologie_kruistabel)


# Maak een tabel met proporties, argument 'normalize = columns' zorgt ervoor dat de proporties
# per rij berekend worden
Fisher_Prop_BSA_antropologie_kruistabel = pd.crosstab(dfFisher_BSA_antropologie['BSA'], dfFisher_BSA_antropologie['Landen_vooropleiding'], normalize = 'columns')

# Print de tabel met proporties met drie decimalen
print(round(Fisher_Prop_BSA_antropologie_kruistabel, 3))


# In[ ]:


NL = np.array(Fisher_Prop_BSA_antropologie_kruistabel)[1,4]


# <!-- ## /OPENBLOK: Data-kruistabel2f.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3f.py -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat de meerderheid van de studenten een positief BSA ontvangt voor elk land van vooropleiding. Van studenten uit het Nederland (NL) haalt verhoudingsgewijs het grootste deel een positief BSA. Het percentage studenten met een positief BSA is hier (`r Round_and_format(100 * py$NL)`%).
# <!-- ## /TEKSTBLOK: Data-kruistabel3f.py -->

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: Assumptie0f.py -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk of kleiner dan vijf is. Bereken het verwacht aantal observaties met de functie `.contingency.expected_freq()` van het `scipy.stats` package met als argument de kruistabel `Fisher_BSA_antropologie_kruistabel`.
# <!-- ## /TEKSTBLOK: Assumptie0f.py -->
# 
# <!-- ## OPENBLOK: Assumptie1f.py -->

# In[ ]:


# Maak een kruistabel
Fisher_BSA_antropologie_kruistabel =  pd.crosstab(dfFisher_BSA_antropologie['BSA'], dfFisher_BSA_antropologie['Landen_vooropleiding'])

# Bereken verwachte aantallen observaties
sps.contingency.expected_freq(Fisher_BSA_antropologie_kruistabel)


# <!-- ## /OPENBLOK: Assumptie1f.py -->
# 
# Drie van de 14 (21,43%) verwachte aantallen observaties zijn kleiner dan vijf. Meer dan 20% van de verwachte aantallen observaties is kleiner of gelijk aan vijf, dus de assumptie van de groepsgroette van de *Chi-kwadraat toets voor onafhankelijkheid* houdt geen stand. De *Fisher-Freeman-Halton toets* moet inderdaad uitgevoerd worden.
# 
# ## Uitvoering
# <!-- ## TEKSTBLOK: Fisher-Freeman-Halton-exact-toets.py-->
# Voor zover bekend is er geen package om de Fisher-Freeman-Halton toets uit te voeren in Python. De Fisher exact toets kan in Python alleen uitgevoerd worden voor 2x2 kruistabellen. Deze stap kan dus in deze toetspagina niet weergegeven worden. Om de Fisher-Freeman-Halton toets uit te voeren. Bekijk de [toetspagina van de Fisher-Freeman-Halton toets in R](16-Chi-kwadraat-toets-voor-onafhankelijkheid-en-Fisher-Freeman-Halton-exact-toets-I-R.html) om deze met de programmeertaal R uit te voeren. Voor het vervolg van deze toetspagina wordt aangenomen dat de Fisher-Freeman-Halton exact toets geen significant resultaat laat zien.
# <!-- ## /TEKSTBLOK: Fisher-Freeman-Halton-exact-toets.py-->
# 
# <!-- ## OPENBLOK: Fisher-Freeman-Halton-exact-toets.py-->
# <!-- ## /OPENBLOK: Fisher-Freeman-Halton-exact-toets.py-->
# 
# <!-- ## CLOSEDBLOK: Fisher-Freeman-Halton-exact-toets1.py-->
# <!-- ## /CLOSEDBLOK: Fisher-Freeman-Halton-exact-toets1.py-->
# 
# <!-- ## TEKSTBLOK: Fisher-Freeman-Halton-exact-toets2.py-->
# <!-- ## /TEKSTBLOK: Fisher-Freeman-Halton-exact-toets2.py-->
# 
# ## Post-hoc toets: Fisher's exacte toets
# 
# <!-- ## TEKSTBLOK: Fisher-Freeman-Halton-exact-toets post-hoc1.py-->
# Omdat er geen afhankelijkheid is tussen het wel of niet halen van een positief BSA en het land van hoogste vooropleiding, hoeven er geen post-hoc toetsen uitgevoerd te worden. Indien dit wel nodig is, toets uitvoert. Voer Fisher's exact toets uit met behulp van de functie `fisher_exact()` van het package `scipy.stats` met als argumenten de kruistabel `Fisher_BSA_antropologie_kruistabel.iloc[:, 
# [i,j]]` en `alternative = 'two-sided'` om aan te geven dat er een tweezijdige alternatieve hypothese 
# getoetst moet worden. Er vindt nu dus geen correctie op de p-waarden plaats, deze kan indien gewenst handmatig doorgevoerd worden op de p-waardes. Een voorbeeld is de Bonferroni cirrectie die de p-waarde aanpast door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en hiermee de kans dat er bij toeval een verband wordt ontdekt dat er niet is te verlagen.[^5]    
# <!-- ## /TEKSTBLOK: Fisher-Freeman-Halton-exact-toets post-hoc1.py -->

# <!-- ## OPENBLOK: Fisher-Freeman-Halton-exact-toets post-hoc2.py -->
# ``` {python fisher toets post hoc, warning=FALSE, message=FALSE}
# # Maak een tabel om de p-waardes in op te slaan
# Tabel_p_waardes = np.zeros((7, 7))
# 
# # Geef de kolommen en rijen van de tabel de namen van de landen die vergeleken worden
# Landen = Fisher_BSA_antropologie_kruistabel.columns
# Tabel_p_waardes = pd.DataFrame(Tabel_p_waardes, columns = Landen, index = Landen)
# 
# # Maak een dubbele for loop om voor elke combinatie van landen Fisher's exact toets uit te voeren
# for i in range(0,7):
#   for j in range(0,7):
#     OR, pval = sps.fisher_exact(Fisher_BSA_antropologie_kruistabel.iloc[:, [i,j]], alternative = 'two-sided')
#     Tabel_p_waardes.iloc[i,j] = round(pval, 3)
# 
# # Print de tabel met p-waarden
# print(Tabel_p_waardes)
# 
# ```
# 
# <!-- ## /OPENBLOK: Fisher-Freeman-Halton-exact-toets post-hoc2.py -->
# 
# <!-- ## TEKSTBLOK: link4.py -->
# De resultaten laten de significantie zien van de [Fisher's exact toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-R.html) voor elk mogelijke combinatie van 2x2 tabellen. Geen van de post-hoc toetsen is significant, wat logisch is aangezien de *Fisher-Freeman-Halton exact toets* niet significant was.  De eerste rij bijvoorbeeld bestaat uit de p-waardes van deze toets voor de vergelijkingen van België (BE) met alle andere landen. Zo is de p-waarde van de vergelijking tussen België (BE) en Spanje (ES) 0,399.  De opmerkelijke p-waardes van 1 komen doordat de verschillen zo klein zijndat dit leidt tot een p-waarde van 1.
# <!-- ## /TEKSTBLOK: link4.py -->

# ## Rapportage
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *Fisher-Freeman-Halton exact toets* is uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen het land van hoogst genoten vooropleiding en het wel of niet behalen van een positief BSA voor een dataset met een laag aantal observaties. De nulhypothese kan niet verworpen worden, dus er lijkt geen afhankelijkheid te zijn tussen het wel of niet ontvangen van een positief BSA en het land van de hoogst genoten vooropleiding. Het percentage studenten met een positief BSA lijkt niet te verschillen per land van hoogst genoten vooropleiding. 
# 
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->

# [^1]: Van Geloven, N. (20 augustus 2015). *Chi-kwadraat toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Chi-kwadraat_toets).
# [^2]: Van Geloven, N. & Holman, R. (6 mei 2016). *Fisher's exact toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Fisher%27s_exact_toets).
# [^3]: Agresti, A. (2003). *Categorical data analysis*. Vol. 482, John Wiley & Sons.
# [^4]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw). 
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: De effectmaat *w* wordt voor de *Chi-kwadraat toets voor onafhankelijkheid* berekend door de wortel te nemen van de
# *&chi;^2^*-waarde gedeeld door het totaal aantal observaties, i.e. $\sqrt{ \frac{\chi^2}{N} }$.
# [^7]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^8]: Dit voorbeeld gaat uit van een waarschijnlijkheid van 95% en zodoende een p-waardegrens van 0,05. Dit is naar eigen inzicht aan te passen. Hou hierbij rekening met type I en type II fouten.
# [^9]: De waarde 1,96 is een z-score en correspondeert met het significantieniveau 0,05 voor een tweezijdige toets. Om te corrigeren voor meerdere testen kan een ander significantieniveau gekozen worden wat resulteert in een andere z-score om mee te vergelijken. Bij een significantieniveau van 0,01 is de z-score bijvoorbeeld 2,58. De z-score per significantieniveau is te berekenen met `abs(qnorm(alfa/2))` waarbij `alfa` het gewenste significantieniveau is.
# [^10]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^11]: Een z-score is een maat om aan te geven hoeveel een observatie afwijkt van het gemiddelde. De z-score wordt berekend door het gemiddelde van de observatie af te halen en dit daarna te delen door de standaarddeviatie, i.e. $\frac{X - \mu}{\sigma}$. In feite geeft een z-score aan hoeveel standaarddeviaties de observatie van het gemiddelde afwijkt.
