#!/usr/bin/env python
# coding: utf-8
---
title: "McNemar toets"
output:
  html_document:
    theme: lumen
    toc: yes
    toc_depth: 2
    toc_float: 
      collapsed: FALSE 
    number_sections: true
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


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/12.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.py -->
# Gebruik de *McNemar toets* om te toetsen of er verschillen zijn voor de frequenties van een binaire[^1] variabele tussen twee gepaarde groepen.[^2]<sup>, </sup>[^3] De *McNemar toets* kan in theorie ook gebruikt worden om twee gepaarde groepen te vergelijken op een nominale variabele met meer dan twee categorieën. Deze toetspagina illustreert de toets echter voor een binaire variabele. Hoewel het dus mogelijk met de *McNemar toets* is om twee gepaarde groepen te vergelijken wat betreft een nominale variabele, wordt hiervoor echter de voorkeur gegeven aan de [Bhapkar toets](18-Bhapkar-toets-Python.html).
# <!-- ## /TEKSTBLOK: Link1.py -->
# 
# # Onderwijscasus
# <div id = "casus">
# De decaan van een hogeschool merkt dat weinig studenten met een functiebeperking een beroep doen op de Financiële Ondersteuning Studenten (FOS). Ze besluit daarom in december een interventie te doen en stuurt al deze studenten een e-mail over de FOS. Een half jaar later (in de maand juni) maakt ze de balans op: doen studenten met een functiebeperking vaker een beroep op de FOS na de interventie?
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er is geen verschil in de verdeling van het aantal studenten voor en na de interventie dat wel of niet gebruik maakt van de FOS.
# 
# *H~A~*: Er is een verschil in de verdeling van het aantal studenten voor en na de interventie dat wel of niet gebruik maakt van de FOS.
# </div>
# 
# # McNemar toets
# 
# De *McNemar toets* toetst of er verschillen zijn tussen de frequenties van een binaire variabele tussen twee gepaarde groepen. In de huidige casus gaat het om de frequenties van studenten die wel of niet gebruik maken van de Financiële Ondersteuning Studenten (FOS). De twee gepaarde groepen zijn het meetmoment in december en het meetmoment in juni. Er zijn meerdere methoden om de p-waarde van de *McNemar toets* te berekenen. De *mid p-value* methode is het beste qua onderscheidend vermogen[^7] en type I fout[^8]. Bij deze methode wordt de p-waarde op een exacte manier berekend waarna een correctie wordt toegepast.[^9] Meer informatie over de verschillende methoden van de *McNemar toets* is te vinden in [dit artikel](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3716987/).
# 
# # Assumpties
# 
# Om de *McNemar toets* uit te voeren, moet de data aan een aantal voorwaarden voldoen. Er moet sprake zijn van gepaarde metingen, meestal twee verschillende metingen bij dezelfde steekproef. Elke meting moet binair zijn, wat betekent dat er twee categorieën zijn voor de gemeten variabele. Daarnaast mag er geen overlap zijn tussen de categorieën van de categorische variabele: elke observatie past slechts in een van beide categorieën.[^3]
# 
# # Frequentiematrix
# 
# De *McNemar toets* gaat uit van een frequentiematrix, een matrix waarin de rijen de eerste meting van de steekproef bevat en de kolommen de tweede meting. Een voorbeeld bij de casus is weergegeven in Tabel 1.
# 
# <!-- ## CLOSEDBLOK: Groepsgrootte0.py -->

# In[ ]:


import pandas as pd

dfFOS_studenten = pd.DataFrame(r.FOS_studenten)


# <!-- ## /CLOSEDBLOK: Groepsgrootte0.py -->
# 
# <!-- ## CLOSEDBLOK: Groepsgrootte1.py -->

# In[ ]:


import pandas as pd
import numpy as np

## Definieer de groepen
December = np.array(dfFOS_studenten['FOS'][dfFOS_studenten['Maand'] == 'december'])
Juni = np.array(dfFOS_studenten['FOS'][dfFOS_studenten['Maand'] == 'juni'])

## Maak een frequentiematrix
FOS_studenten_frequentiematrix =  np.array(pd.crosstab(December, Juni))


# <!-- ## /CLOSEDBLOK: Groepsgrootte1.py -->
# 
# <!-- ## TEKSTBLOK: Groepsgrootte2.py -->
# 
# ||                      | Juni    |
# |-------------| -------------------- | -------------| ------------| 
# ||                      | FOS | geen FOS|
# |**December**| FOS      | `r py$FOS_studenten_frequentiematrix[1,1]` | `r py$FOS_studenten_frequentiematrix[1,2]`     |
# |            | Geen FOS | `r py$FOS_studenten_frequentiematrix[2,1]` | `r py$FOS_studenten_frequentiematrix[2,2]`     |
# *Tabel 1. Frequentiematrix van het aantal studenten dat een beroep doet op de FOS in december en juni.*
# 
# De cel linksboven bevat het aantal studenten dat zowel in december als juni een beroep heeft gedaan op de FOS; dit zijn er `r py$FOS_studenten_frequentiematrix[1,1]`. De cel rechtsonder bevat het aantal studenten dat zowel in december als juni geen beroep heeft gedaan op de FOS; dit zijn er `r py$FOS_studenten_frequentiematrix[2,2]`. Beide cellen staan op de diagonaal van de tabel en worden daarom de diagonale elementen genoemd.
# 
# In de cel rechtsboven staat het aantal studenten dat wel in december maar niet in juni een beroep op de FOS heeft gedaan; dit zijn er `r py$FOS_studenten_frequentiematrix[1,2]`. In de cel linksonder staat het aantal studenten dat niet in december maar wel in juni een beroep op de FOS heeft gedaan; dit zijn er `r py$FOS_studenten_frequentiematrix[2,1]`. Deze cellen zijn geen onderdeel van de diagonaal van de tabel en worden daarom de niet-diagonale elementen genoemd.
# <!-- ## /TEKSTBLOK: Groepsgrootte2.py -->
# 
# # De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken1.py -->
# Er is een dataset ingeladen genaamd `dfFOS_studenten`. In deze dataset is voor elke student aangegeven of ze wel of geen beroep op de FOS hebben gedaan in december en in juni. 
# <!-- ## /TEKSTBLOK: Data-bekijken1.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


## Importeer nuttige packages
import numpy as np
import pandas as pd

## Eerste 5 observaties
print(dfFOS_studenten.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfFOS_studenten.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.py -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Maand` en `FOS`. In feite laat dit zien hoeveel studenten er wel of niet een beroep doen op de FOS in december en in juni. Een kruistabel verschilt dus van een frequentiematrix. Maak de kruistabel met de functie `.crosstab()` van het package `pandas` met als argumenten de variabele `dfFOS_studenten['FOS']`, die weergeeft of studenten wel of geen beroep op de FOS doen, en de variabele `dfFOS_studenten['Maand'] `, die het meetmoment (december of juni) weergeeft. 
# <!-- ## /TEKSTBLOK: Data-kruistabel1.py -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.py -->

# In[ ]:


## Maak een kruistabel
FOS_studenten_kruistabel = pd.crosstab(dfFOS_studenten['FOS'], dfFOS_studenten['Maand'])

## Print de kruistabel 
print(FOS_studenten_kruistabel)

## Print een tabel met proporties, tweede argument 'columns' zorgt ervoor dat de 
## proporties per kolom berekend worden
Prop_FOS_studenten_kruistabel = pd.crosstab(dfFOS_studenten['FOS'], dfFOS_studenten['Maand'], normalize = 'columns')

## Print de tabel met proporties
print(Prop_FOS_studenten_kruistabel)


# In[ ]:


FOS_studenten_kruistabel = np.array(FOS_studenten_kruistabel)


# <!-- ## /OPENBLOK: Data-kruistabel2.py -->
# 
# De kruistabel laat zien dat het aantal studenten dat een beroep op de FOS heeft gedaan hoger is en het aantal studenten dat geen beroep op de FOS heeft gedaan lager is in juni. Het percentage studenten dat een beroep op de FOS heeft gedaan is toegenomen; dit is ook te zien in de kruistabel met proporties.
# 
# <!-- ## TEKSTBLOK: Data-bekijken3.py -->
# In aanvulling op de kruistabel, geeft de frequentiematrix ook een goede indruk van de data. In de frequentiematrix worden de aantallen studenten die wel of geen beroep op de FOS hebben gedaan tegen elkaar uitgezet voor december en juni. Sla daarom de variabele `FOS` apart op in twee vectoren: een voor december en een voor juni. Maak daarna de frequentiematrix.
# <!-- ## /TEKSTBLOK: Data-bekijken3.py -->
# 
# <!-- ## OPENBLOK: Data-beschrijven.py -->

# In[ ]:


## Definieer de groepen
December = np.array(dfFOS_studenten['FOS'][dfFOS_studenten['Maand'] == 'december'])
Juni = np.array(dfFOS_studenten['FOS'][dfFOS_studenten['Maand'] == 'juni'])

## Maak een frequentiematrix
FOS_studenten_frequentiematrix =  np.array(pd.crosstab(December, Juni))

## Print de frequentiematrix 
print(FOS_studenten_frequentiematrix)


# <!-- ## /OPENBLOK: Data-beschrijven.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken4.py -->
# De diagonale elementen bevatten `r py$FOS_studenten_frequentiematrix[1,1]` en `r py$FOS_studenten_frequentiematrix[2,2]` observaties. De niet-diagonale elementen bevatten `r py$FOS_studenten_frequentiematrix[2,1]` en `r py$FOS_studenten_frequentiematrix[1,2]` observaties.
# <!-- ## /TEKSTBLOK: Data-bekijken4.py -->
# 
# # McNemar toets
# 
# ## Uitvoering
# 
# <!-- ## TEKSTBLOK: McNemar-toets1.py -->
# Voer de *McNemar toets* uit om te onderzoeken of er een verschil is tussen de frequenties van de studenten dat wel of geen beroep doet op de FOS voor en na de interventie van de decaan. Maak hiervoor eerst een frequentietabel. Voer daarna de *McNemar toets* uit met de zelf geschreven functie[^10] `McNemar_toets` met als argumenten de frequentiematrix `FOS_studenten_frequentiematrix` en `'mid'` om aa te geven dat de *mid p-value* methode gebruikt moet worden.
# <!-- ## /TEKSTBLOK: McNemar-toets1.py -->
# 
# <!-- ## OPENBLOK: McNemar-toets2.py -->

# In[ ]:


## Importeer het package scipy.stats
import scipy.stats as sps

## Definieer de groepen
December = np.array(dfFOS_studenten['FOS'][dfFOS_studenten['Maand'] == 'december'])
Juni = np.array(dfFOS_studenten['FOS'][dfFOS_studenten['Maand'] == 'juni'])

## Maak een frequentiematrix
FOS_studenten_frequentiematrix =  np.array(pd.crosstab(December, Juni))

## Definieer een functie om de mid p-waarde of de exacte p-waarde voor de McNemar toets te berekenen
def McNemar_toets(Frequentiematrix, p_waarde):
  
  ## Sla de niet-diagonale elementen op
  n12 = Frequentiematrix[0,1]
  n21 = Frequentiematrix[1,0]
  
  ## Bereken de som van de niet-diagonale elementen
  n = n12 + n21
  
  ## Bepaal het minimum van beide niet-diagonale elementen 
  n_min = min(n12,n21)
  
  ## Bereken de p-waarde als beide elementen gelijk zijn
  if n12 == n21:
    exact_p_value
    mid_p_value = 1 - sps.binom.pmf(n_min, n, 0.5)

  ## Bereken de p-waarde als beide elementen niet gelijk zijn
  else:
    exact_p_value = 2 * sps.binom.cdf(n_min, n, 0.5)
    mid_p_value = exact_p_value - sps.binom.pmf(n_min, n, 0.5)
  
  ## Retourneer de juiste p-waarde op basis van de gekozen methode
  if p_waarde == 'exact':
    return exact_p_value
  if p_waarde == 'mid':
    return mid_p_value

## Voer de McNemar toets uit met de geschreven functie
p_waarde = McNemar_toets(FOS_studenten_frequentiematrix, 'mid')

## Print de p-waarde
print(p_waarde)
    


# <!-- ## /OPENBLOK: McNemar-toets2.py -->
# 
# Bereken het verschil tussen de proporties studenten dat een beroep doet op de FOS in december en juni. Op deze manier kan een (eventueel) significant resultaat geïnterpreteerd worden.
# 
# <!-- ## OPENBLOK: McNemar-toets5.py -->

# In[ ]:


## Maak een kruistabel met proporties, tweede argument 'columns' zorgt ervoor dat de 
## proporties per kolom berekend worden
Prop_FOS_studenten_kruistabel = pd.crosstab(dfFOS_studenten['FOS'], dfFOS_studenten['Maand'], normalize = 'columns')

## Print de kruistabel
print(Prop_FOS_studenten_kruistabel)

## Bereken het verschil in proporties
Verschil_proporties = np.array(Prop_FOS_studenten_kruistabel)[0,1] -  np.array(Prop_FOS_studenten_kruistabel)[0,0]

## Print het verschil in proporties
print(Verschil_proporties)


# <!-- ## /OPENBLOK: McNemar-toets5.py -->
# 
# <!-- ## TEKSTBLOK: McNemar-toets5.py -->
# * Er is een significant verschil tussen de frequenties van het aantal studenten dat wel of niet gebruik maakt van de FOS tussen december en juni, *p* < 0,0001  
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^6]
# * Het verschil in proporties is `r Round_and_format(py$Verschil_proporties)`, er zijn dus meer studenten die gebruik maken van de FOS in juni ten opzichte van december
# 
# <!-- ## /TEKSTBLOK: McNemar-toets5.py -->
# 
# ## Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.py -->
# De *McNemar toets* is uitgevoerd om uit te vinden of er een verschil is in de frequenties van het aantal studenten dat wel of geen beroep doet op de FOS voor en na de interventie van de decaan. De interventie heeft als doel het aantal studenten met een functiebeperking dat een beroep doet op de FOS te verhogen. De resultaten laten een significant verschil zien tussen de frequenties voor en na de interventie (*p* < 0,0001), wat betekent dat de nulhypothese verworpen kan worden. Het verschil in de proportie studenten dat een beroep doet op de FOS is `r Round_and_format(py$Verschil_proporties)` . Het verschil in proporties en de kruistabel (Tabel 2) illustreren dat het percentage studenten dat een beroep doet op de FOS is toegenomen na de interventie. 
# 
# |                      | December | Juni |
# | -------------------- | -------------| ------------| 
# | **FOS** | `r py$FOS_studenten_kruistabel[1,1]`    | `r py$FOS_studenten_kruistabel[1,2]`     |
# | **geen FOS**  | `r py$FOS_studenten_kruistabel[2,1]`      | `r py$FOS_studenten_kruistabel[2,2]`     |
# *Tabel 2. Kruistabel van het aantal studenten dat een beroep doet op de FOS in december en juni*
# <!-- ## /TEKSTBLOK: Rapportage.py -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Binaire variabelen: twee elkaar uitsluitende waarden, zoals ja of nee, 0 of 1, aan of uit. 
# [^2]: Van Geloven, N., & Holman, R., (4 juni 2014). *McNemar toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/McNemar_toets). 
# [^3]: Laerd statistics (2018). *McNemar's test using SPSS Statistics*. [Laerd statistics](https://statistics.laerd.com/spss-tutorials/mcnemars-test-using-spss-statistics.php) 
# [^6]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten. 
# [^7]: Onderscheidend vermogen, in het Engels power genoemd, is de kans dat de nulhypothese verworpen wordt wanneer de alternatieve hypothese waar is.
# [^8]: Een type I fout is de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is.
# [^9]: Fagerland, M.W., Lydersen, S., & Laake, P. (2013). *The McNemar test for binary matched-pairs data: mid-p and asymptotic are better than exact conditional*. BMC medical research methodology, 13, 91. https://doi.org/10.1186/1471-2288-13-91
# 
# <!-- ## TEKSTBLOK: Extra_bron.py -->
# [^10]: Additional file 1 van Fagerland, M.W., Lydersen, S., & Laake, P. (2013). *The McNemar test for binary matched-pairs data: mid-p and asymptotic are better than exact conditional*. BMC medical research methodology, 13, 91. https://doi.org/10.1186/1471-2288-13-91 . Te vinden op https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3716987/#S1
# 
# <!-- ## /TEKSTBLOK: Extra_bron.py -->
# 
