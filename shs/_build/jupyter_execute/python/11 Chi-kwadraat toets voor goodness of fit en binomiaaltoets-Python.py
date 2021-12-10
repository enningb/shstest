#!/usr/bin/env python
# coding: utf-8
---
title: "Chi-kwadraat toets voor goodness of fit en binomiaaltoets"
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


get_ipython().run_cell_magic('R', '', '# TODO: Uitleg extra pagina: nominaal, ordinaal etc., afhanjeklijk en onafhankelijk  \n# TODO: Uitleg transformeren data ')


# In[ ]:


get_ipython().run_cell_magic('R', '', 'source(paste0(here::here(),"/01. Includes/data/11.R"))')


# <!-- ## /OPENBLOK: Data-aanmaken.py -->
# # Toepassing
# 
# Gebruik de *Chi-kwadraat toets voor goodness of fit* om te onderzoeken of de geobserveerde frequenties van de categorieën van één categorische variabele overeenkomt met de verwachte frequenties van de categorische variabele.[^6]<sup>,</sup>[^7] Met deze toets kan een geobserveerd percentage met een bekend of verwacht percentage vergeleken worden. Gebruik de exacte *binomiaaltoets* bij een laag aantal observaties, dit wordt bij de assumpties toegelicht.[^1] 
# 
# # Onderwijscasus
# <div id = "casus">
# De controller van een universiteit is geïnteresseerd in de instroom van studenten met een hbo vooropleiding. Zij wil weten of haar universiteit relatief veel studenten met een vooropleiding in het hbo heeft in vergelijking met het landelijke gemiddelde. Op de website van de VSNU vindt ze dat studenten met een hbo vooropleiding 11,13% uitmaken van de totale instroom voor Bachelors en Masters in het wetenschappelijk onderwijs (wo) in 2018.[^2] Ze wil weten of er op haar instelling naar verhouding evenveel hbo-studenten zijn als het landelijk gemiddelde.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# H~0~: De verdeling van de vooropleiding van de instromende studenten is gelijk aan de landelijke verdeling (11,13% met een hbo vooropleiding). 
# 
# H~A~: De verdeling van de vooropleiding van de instromende studenten is niet gelijk aan de landelijke verdeling (11,13% met een hbo vooropleiding).
# </div>
# 
# # Assumpties
# 
# Om de *Chi-kwadraat toets voor goodness of fit* uit te voeren, moet de variabele nominaal[^9] of ordinaal[^8] zijn.[^6] De exacte *binomiaaltoets* vereist een binaire[^3] variabele. In deze casus is de categorische variabele binair. 
# 
# De categorieën van de variabele mogen niet overlappen, wat wil zeggen dat elke observatie slechts in een van de categorieën past. Voor de *Chi-kwadraat toets voor goodness of fit* mag in niet meer dan 20% van de categorieën van de variabele de verwachte frequentie minder dan vijf zijn. Als dit wel het geval is, gebruik dan de *binomiaaltoets*.[^7]
# 
# # De data bekijken
# 
# <!-- ## TEKSTBLOK: Data-bekijken1.py -->
# Er is een dataset ingeladen genaamd `dfInstroom_2018_totaal`. Dit is een dataframe met studentnummers en een binaire variabele die laat zien of de student wel of geen hbo vooropleiding heeft.
# <!-- ## /TEKSTBLOK: Data-bekijken1.py -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.py -->

# In[ ]:


## Importeer nuttige packages
import numpy as np
import pandas as pd
import scipy.stats as sps


# In[ ]:


dfInstroom_2018_totaal = pd.DataFrame(r.Instroom_2018_totaal)
dfInstroom_2018_totaal_steekproef = pd.DataFrame(r.Instroom_2018_totaal_steekproef)


# In[ ]:


## Eerste 5 observaties
print(dfInstroom_2018_totaal.head(5))


# In[ ]:


## Laatste 5 observaties
print(dfInstroom_2018_totaal.tail(5))


# <!-- ## /OPENBLOK: Data-bekijken2.py -->
# 
# Het is informatief om het percentage studenten met hbo vooropleiding in de data te bepalen.
# 
# <!-- ## OPENBLOK: Data-bekijken3.py -->

# In[ ]:


# Maak een tabel met percentages
Percentages = 100 * pd.crosstab(dfInstroom_2018_totaal['hbo_vooropleiding'], columns = 'count',
normalize = 'columns')

# Print de tabel
print(Percentages)


# <!-- ## /OPENBLOK: Data-bekijken3.py -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken4.py -->
# Het percentage studenten met hbo vooropleiding is `r Round_and_format(py$Percentages[1, 1])`. Dit percentage lijkt hoger te liggen dan het landelijk percentage van 11,13%. De *Chi-kwadraat toets voor goodness of fit* of de *binomiaaltoets* toetst of dit verschil significant is.
# <!-- ## /TEKSTBLOK: Data-bekijken4.py -->
# 
# # Chi-kwadraat toets voor goodness of fit
# 
# ## Asssumptie verwachte frequenties
# 
# <!-- ## TEKSTBLOK: Assumptie.py -->
# Het verwacht aantal observaties mag niet vijf of minder zijn in 20% van de categorieën van de categorische variabele. Aangezien er een binaire variabele getoetst wordt, mag geen van beide categorieën dus vijf of minder verwachte observaties hebben. Bereken het verwacht aantal observaties door de proporties van de nulhyothese (11,3% met hbo vooropleiding, dus 0,113 en 1 - 0,113) te vermenigvuldigen met het totaal aantal observaties in de dataset (`len(dfInstroom_2018_totaal)`).
# <!-- ## /TEKSTBLOK: Assumptie.py -->

# <!-- ## OPENBLOK: Assumptie1.py -->

# In[ ]:


# Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.113, 1 - 0.113])

# Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfInstroom_2018_totaal)

# Print het verwachte aantal observaties
print(Verwacht_aantal_observaties)


# <!-- ## /OPENBLOK: Assumptie1.py -->
# 
# Geen van de verwachte frequenties is kleiner dan vijf, dus de *Chi-kwadraat toets voor goodness of fit* kan worden uitgevoerd.
# 
# ## Uitvoering
# 
# Voer de *Chi-kwadraat toets voor goodness of fit*  uit om te onderzoeken of de verdeling van het aantal studenten met en zonder hbo vooropleiding overeenkomt met de landelijke verdeling waarbij het percentage studenten met hbo vooropleiding 11,13% is.
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat1.py -->
# Bereken eerst de aantallen observaties en verwachte aantallen observaties. Gebruik daarna de functie `chisquare()` van het `scipy.stats` package met als argumenten de aantallen observaties `Aantal_observaties`, de verwachte aantallen observaties `Verwacht_aantal_observaties` en `axis = None` om aan te geven dat alle waarden in de twee vorige argumenten van dezelfde dataset afkomstig zijn. Let goed op dat de volgorde van de aantallen observaties en de verwachte aantallen observaties dezelfde volgorde hebben zodat de toets de goede vergelijking maakt.
# <!-- ## /TEKSTBLOK: Chi-kwadraat1.py -->

# <!-- ## OPENBLOK: Chi-kwadraat2.py-->

# In[ ]:


## Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfInstroom_2018_totaal['hbo_vooropleiding'], columns = 'count')

## Zet het aantal observaties om in een numpy array. Gebruik de toevoeging .T om de array om te zetten in een rij
Aantal_observaties = np.array(Aantal_observaties).T

## Bereken de verwachte aantallen observaties
Verwachte_proporties = np.array([0.113, 1- 0.113])
Verwacht_aantal_observaties = Verwachte_proporties * len(dfInstroom_2018_totaal)

## voer de chi-kwadraat toets uit
sps.chisquare(Aantal_observaties, Verwacht_aantal_observaties, axis = None)


# <!-- ## /OPENBLOK: Chi-kwadraat2.py-->
# 
# <!-- ## CLOSEDBLOK: Chi-kwadraat3.py-->

# In[ ]:


## Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfInstroom_2018_totaal['hbo_vooropleiding'], columns = 'count')

## Zet het aantal observaties om in een numpy array. Gebruik de toevoeging .T om de array om te zetten in een rij
Aantal_observaties = np.array(Aantal_observaties).T

## Bereken de verwachte aantallen observaties
Verwachte_proporties = np.array([0.113, 1- 0.113])
Verwacht_aantal_observaties = Verwachte_proporties * len(dfInstroom_2018_totaal)

# Voer de chi-kwadraat toets voor goodness of fit uit
chi2, pval = sps.chisquare(Aantal_observaties, Verwacht_aantal_observaties, axis = None)

# Degrees of freedom
vdf = 1

Proporties = pd.crosstab(dfInstroom_2018_totaal['hbo_vooropleiding'], columns = 'count',
normalize = 'columns')


# <!-- ## /CLOSEDBLOK: Chi-kwadraat3.py-->
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat4.py-->
# * &chi;^2^~`r Round_and_format(py$vdf)`~ = `r Round_and_format(py$chi2)`, *p* < 0,0001
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^5]
# 
# <!-- ## /TEKSTBLOK: Chi-kwadraat4.py-->
# 

# ## Rapportage
# <!-- ## TEKSTBLOK: Chi-kwadraat5.py-->
# De *Chi-kwadraat toets voor goodness of fit* is uitgevoerd om te onderzoeken of de verdeling van het instromende aantal studenten van een universiteit met en zonder hbo vooropleiding verschilt van de landelijke verdeling waarbij het percentage studenten met een hbo vooropleiding 11,13% is. De verdeling van de instromende studenten van de universiteit is significant verschillend van de landelijke verdeling, &chi;^2^~`r Round_and_format(py$vdf)`~ = `r Round_and_format(py$chi2)`, *p* < 0,0001. Het percentage instromende studenten met een hbo vooropleiding is `r Round_and_format(py$Proporties[1, 1])`. Aan de hand van de resultaten kan geconcludeerd worden dat het percentage studenten met een hbo vooropleiding hoger ligt dan het landelijk gemiddelde van 11,13%.
# 
# <!-- ## /TEKSTBLOK: Chi-kwadraat5.py-->
# 

# # Binomiaaltoets
# 
# ## Uitvoering
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets1.py -->
# Voer de *binomiaaltoets*  uit om te onderzoeken of de verdeling van het aantal studenten met en zonder hbo vooropleiding overeenkomt met de landelijke verdeling waarbij het percentage studenten met hbo vooropleiding 11,13% is. Deze toets is een alternatief voor de *Chi-kwadraat toets voor goodness of fit* bij lage verwachte aantallen observaties. Er is een subset `dfInstroom_2018_totaal_steekproef` van de dataset `dfInstroom_2018_totaal` ingeladen met daarin een lager aantal observaties.
# 
# Maak een tabel van de variabele `hbo_vooropleiding` om het aantal observaties per categorie te tellen. Bereken het verwacht aantal observaties door de proporties van de nulhyothese (11,3% met hbo vooropleiding, dus 0,113 en 1 - 0,113) te vermenigvuldigen met het totaal aantal observaties in de dataset (`len(dfInstroom_2018_totaal)`).
# <!-- ## /TEKSTBLOK: Binomiaaltoets1.py -->
# 
# <!-- ## OPENBLOK: Binomiaaltoets2.py -->

# In[ ]:


# Bereken de aantallen observaties
Aantal_observaties = pd.crosstab(dfInstroom_2018_totaal_steekproef['hbo_vooropleiding'], columns = 'count')

# Print het aantal observaties
print(Aantal_observaties)

# Sla de verwachte proporties op in een vector
Verwachte_proporties = np.array([0.113, 1 - 0.113])

# Bereken het verwachte aantal observaties door de verwachte proporties met het totaal aantal observaties te vermenigvuldigen
Verwacht_aantal_observaties = Verwachte_proporties * len(dfInstroom_2018_totaal_steekproef)

# Print het verwachte aantal observaties
print(Verwacht_aantal_observaties)


# <!-- ## /OPENBLOK: Binomiaaltoets2.py -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets3.py -->
# Het aantal studenten met een hbo vooropleiding is `r Round_and_format(py$Aantal_observaties[1, 1])` en het aantal zonder hbo vooropleiding `r Round_and_format(py$Aantal_observaties[2, 1])`. Het verwachte aantal observaties met een hbo vooropleiding is `r Round_and_format(py$Verwacht_aantal_observaties[1])` wat kleiner dan vijf is. Voer daarom de *binomiaaltoets* uit, aangezien meer dan 20% van de categorieën een verwacht aantal observaties van vijf of minder heeft.
# <!-- ## /TEKSTBLOK: Binomiaaltoets3.py -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets4.py -->
# Bereken eerst het aantal studenten met een hbo vooropleiding in de dataset en het totaal aantal studenten in de dataset. Voer daarna de *binomiaaltoets* uit met de functie `binom_._test()` van het `scipy` package met de argumenten `x = Aantal_hbo_vooropleiding` voor de hoeveelheid studenten met een hbo vooropleiding, `n = Aantal_observaties` voor de totale instroom van de universiteit, `p = 0.1113` voor de referentieproportie en  `alternative = two-sided` voor het soort toets (eenzijdig of tweezijdig). Bereken tenslotte handmatig de proportie studenten met een hbo vooropleiding.
# <!-- ## /TEKSTBLOK: Binomiaaltoets4.py -->

# <!-- ## OPENBLOK: Binomiaaltoets5.py -->

# In[ ]:


# Bereken het aantal observaties met hbo vooropleiding
Aantal_hbo_vooropleiding = sum(dfInstroom_2018_totaal_steekproef['hbo_vooropleiding'] == 'ja')

# Bereken het totaal aantal observaties
Aantal_observaties = len(dfInstroom_2018_totaal_steekproef)

# Voer de binomiaaltoets uit
sps.binom_test(x = Aantal_hbo_vooropleiding, n = Aantal_observaties, p = 0.113, alternative = 'two-sided')

# Bereken de proportie studenten met een hbo vooropleiding
Proportie_hbo_vooropleiding = Aantal_hbo_vooropleiding / Aantal_observaties

# Print de proportie
print(Proportie_hbo_vooropleiding)


# <!-- ## /OPENBLOK: Binomiaaltoets5.py -->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets6.py -->

# In[ ]:


# Bereken het aantal observaties met hbo vooropleiding
Aantal_hbo_vooropleiding = sum(dfInstroom_2018_totaal_steekproef['hbo_vooropleiding'] == 'ja')

# Bereken het totaal aantal observaties
Aantal_observaties = len(dfInstroom_2018_totaal_steekproef)

# Voer de binomiaaltoets uit
pval = sps.binom_test(x = Aantal_hbo_vooropleiding, n = Aantal_observaties, p = 0.113, alternative = 'two-sided')


# <!-- ## /CLOSEDBLOK: Binomiaaltoets6.py -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets7.py-->
# * de geschatte proportie studenten met een hbo vooropleiding in de data is `r Round_and_format(py$Proportie_hbo_vooropleiding)`.[^8]
# * p-waarde = `r Round_and_format(py$pval)`, dus de H~0~ kan niet worden verworpen.[^5]  
# 
# <!-- ## /TEKSTBLOK: Binomiaaltoets7.py-->

# ## Rapportage
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets8.py-->
# De *binomiaaltoets* is uitgevoerd om te onderzoeken of de verdeling van het instromende aantal studenten van een universiteit met en zonder hbo vooropleiding voor een dataset met een laag aantal observaties verschilt van de landelijke verdeling waarbij het percentage studenten met een hbo vooropleiding 11,13% is. De verdeling van het aantal instromende studenten met een zonder hbo vooropleiding is niet significant verschillend van de landelijke verdeling (*p* = `r Round_and_format(py$pval)`), dus de nulhypothese kan niet verworpen worden. De schatting van het percentage is `r Round_and_format(py$Proportie_hbo_vooropleiding)`% en is niet significant verschillend van het landelijk gemiddelde van 11,13%. De resultaten suggereren dat het percentage studenten met een hbo vooropleiding niet hoger ligt dan het landelijk gemiddelde van 11,13%.
# 
# <!-- ## /TEKSTBLOK: Binomiaaltoets8.py-->
# 
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:


get_ipython().run_cell_magic('R', '', '')


# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Agresti, A. (2003). *Categorical data analysis*. Vol. 482, John Wiley & Sons.
# [^2]: Het percentage is een berekening op basis van cijfers van de Vereniging van Universiteiten (VSNU). In 2018 zijn er 102.147 studenten ingestroomd in Universitaire Bachelors en Masters. In dat zelfde jaar stroomden bij de universiteiten 11.374 studenten met een hbo vooropleiding in. Deze studenten maken dus 11,13% uit van de totale instroom.  Zie respectievelijk: Vereniging van Universiteiten (2019). *Downloadbare tabellen Studenten*. Opgehaald van de website van de VSNU: https://www.vsnu.nl/nl_NL/f_c_studenten_downloads.html. Vereniging van Universiteiten (2019). *Factsheet - Nederlandse Universiteiten Zijn Toegankelijk*. Opgehaald van de website van de VSNU: https://www.vsnu.nl/files/documenten/Nederlands%20universiteiten%20zijn%20toegankelijk%20-%20tbv%20AO%20Toegankelijkheid%20en%20Kansengelijkheid%20in%20het%20hoger%20onderwijs%20d.d.%2020-2-2019.pdf
# [^3]: Binaire variabelen: twee elkaar uitsluitende waarden, zoals ja of nee, 0 of 1, aan of uit.
# [^4]: Een proportie van een bepaalde categorie is de frequentie van de categorie gedeeld door het totaal aantal observaties. Het kan gezien worden als de kans van een bepaalde categorie en bevat een waarde tussen 0 en 1.
# [^5]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^6]: Laerd Statistics (2018). *Chi-Square Goodness-of-Fit Test in SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/chi-square-goodness-of-fit-test-in-spss-statistics.php
# [^7]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^8]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^9]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# 
# <!-- ## TEKSTBLOK: Extra-Bron.py -->
# [^8]: De proportie studenten met hbo vooropleiding en bijbehorend 95%-betrouwbaarheidsinterval worden bij deze Python functie niet weergegeven. Bij de uitvoering van *binomiaaltoets* in R zitten beide wel in de output.
# <!-- ## /TEKSTBLOK: Extra-Bron.py -->
# 
