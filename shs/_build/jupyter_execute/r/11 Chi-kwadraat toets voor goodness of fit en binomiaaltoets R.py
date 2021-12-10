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


library(here)
if (!exists("Substitute_var")) {
  ## Installeer packages en functies
  source(paste0(here::here(), "/99. Functies en Libraries/00. Voorbereidingen.R"), echo = FALSE)
}


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





# <!-- ## /CLOSEDBLOK: Header.R -->
# 
# <!-- ## CLOSEDBLOK: Status.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Status.R -->
# 
# <!-- ## CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## /CLOSEDBLOK: Reticulate.R -->
# 
# <!-- ## OPENBLOK: Data-aanmaken.R -->

# In[ ]:


source(paste0(here::here(),"/01. Includes/data/11.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
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
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `Instroom_2018_totaal`. Dit is een dataframe met studentnummers en een binaire variabele die laat zien of de student wel of geen hbo vooropleiding heeft.
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(Instroom_2018_totaal)
## Laatste 6 observaties
tail(Instroom_2018_totaal)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# Het is informatief om het percentage studenten met hbo vooropleiding in de data te bepalen.
# 
# <!-- ## OPENBLOK: Data-bekijken3.R -->

# In[ ]:


100*prop.table(table(Instroom_2018_totaal$hbo_vooropleiding))


# <!-- ## /OPENBLOK: Data-bekijken3.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken4.R -->
# Het percentage studenten met hbo vooropleiding is `r Round_and_format(100*prop.table(table(Instroom_2018_totaal$hbo_vooropleiding))[1])`. Dit percentage lijkt hoger te liggen dan het landelijk percentage van 11,13%. De *Chi-kwadraat toets voor goodness of fit* of de *binomiaaltoets* toetst of dit verschil significant is.
# <!-- ## /TEKSTBLOK: Data-bekijken4.R -->
# 
# # Chi-kwadraat toets voor goodness of fit
# 
# ## Asssumptie verwachte frequenties
# 
# <!-- ## TEKSTBLOK: Assumptie.R -->
# De verwachte frequentie mag niet kleiner dan vijf zijn in 20% van de categorieën van de categorische variabele. Aangezien er een binaire variabele getoetst wordt, mag geen van beide categorieën dus minder dan vijf als verwachte frequentie hebben. Bereken de verwachte frequentie met het argument `chisq.test()$expected` van de functie `chisq.test()`. De argumenten van de functie zijn de tabel met daarin de hoeveelheid studenten met en zonder hbo vooropleiding `Tabel` en een vector die aangeeft wat de verwachte proporties[^4] zijn voor het aantal studenten met en zonder hbo vooropleiding `p = c(0.1113, 1 - 0.1113)`.
# <!-- ## /TEKSTBLOK: Assumptie.R -->

# <!-- ## OPENBLOK: Assumptie1.R -->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten met en zonder hbo vooropleiding
Tabel <- table(Instroom_2018_totaal$hbo_vooropleiding)
# Bereken de verwachte frequenties
chisq.test(Tabel, p = c(0.1113, 1 - 0.1113))$expected


# <!-- ## /OPENBLOK: Assumptie1.R -->
# 
# Geen van de verwachte frequenties is kleiner dan vijf, dus de *Chi-kwadraat toets voor goodness of fit* kan worden uitgevoerd.
# 
# ## Uitvoering
# 
# Voer de *Chi-kwadraat toets voor goodness of fit*  uit om te onderzoeken of de verdeling van het aantal studenten met en zonder hbo vooropleiding overeenkomt met de landelijke verdeling waarbij het percentage studenten met hbo vooropleiding 11,13% is.
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat1.R -->
# Gebruik de functie `chisq.test()` met als argumenten de tabel met daarin de hoeveelheid studenten met en zonder hbo vooropleiding `Tabel` en een vector die aangeeft wat de verwachte proporties zijn voor het aantal studenten met en zonder hbo vooropleiding `p = c(0.1113, 1 - 0.1113)`. Let hierbij goed op dat de volgorde van de frequenties in de tabel overeenkomt met de volgorde van de proporties zodat de toets de goede vergelijking maakt.
# <!-- ## /TEKSTBLOK: Chi-kwadraat1.R -->

# <!-- ## OPENBLOK: Chi-kwadraat2.R-->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten met en zonder hbo vooropleiding
Tabel <- table(Instroom_2018_totaal$hbo_vooropleiding)
# Voer de toets uit
chisq.test(Tabel, p = c(0.1113, 1 - 0.1113))


# <!-- ## /OPENBLOK: Chi-kwadraat2.R-->
# 
# <!-- ## CLOSEDBLOK: Chi-kwadraat3.R-->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten met en zonder hbo vooropleiding
Tabel <- table(Instroom_2018_totaal$hbo_vooropleiding)
# Voer de toets uit
chi2 <- chisq.test(Tabel, p = c(0.1113, 1 - 0.1113))

vchi2 <- Round_and_format(chi2$statistic)
vp <- Round_and_format(chi2$p.value)
vdf <- chi2$parameter

vest <- 100 * Tabel[1] / sum(Tabel)


# <!-- ## /CLOSEDBLOK: Chi-kwadraat3.R-->
# 
# <!-- ## TEKSTBLOK: Chi-kwadraat4.R-->
# * &chi;^2^~`r vdf`~ = `r vchi2`, *p* < 0,0001
# * p-waarde < 0,05, dus de H~0~ wordt verworpen.[^5]

# <!-- ## /TEKSTBLOK: Chi-kwadraat4.R-->
# 

# ## Rapportage
# <!-- ## TEKSTBLOK: Chi-kwadraat5.R-->
# De *Chi-kwadraat toets voor goodness of fit* is uitgevoerd om te onderzoeken of de verdeling van het instromende aantal studenten van een universiteit met en zonder hbo vooropleiding verschilt van de landelijke verdeling waarbij het percentage studenten met een hbo vooropleiding 11,13% is. De verdeling van de instromende studenten van de universiteit is significant verschillend van de landelijke verdeling, &chi;^2^~`r vdf`~ = `r vchi2`, *p* < 0,0001. Het percentage instromende studenten met een hbo vooropleiding is `r Round_and_format(vest)`. Aan de hand van de resultaten kan geconcludeerd worden dat het percentage studenten met een hbo vooropleiding hoger ligt dan het landelijk gemiddelde van 11,13%.
# 
# <!-- ## /TEKSTBLOK: Chi-kwadraat5.R-->
# 

# # Binomiaaltoets
# 
# ## Uitvoering
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets1.R -->
# Voer de *binomiaaltoets*  uit om te onderzoeken of de verdeling van het aantal studenten met en zonder hbo vooropleiding overeenkomt met de landelijke verdeling waarbij het percentage studenten met hbo vooropleiding 11,13% is. Deze toets is een alternatief voor de *Chi-kwadraat toets voor goodness of fit* bij een laag aantal observaties. Er is een subset `Instroom_2018_totaal_steekproef` van de dataset `Instroom_2018_totaal` ingeladen met daarin een lager aantal observaties.
# 
# Maak een tabel van de variabele `hbo_vooropleiding` om het aantal observaties per categorie te tellen. Bereken daarnaast de verwachte frequenties per categorie met het argument `chisq.test()$expected` van de functie `chisq.test()` met als argumenten de tabel met daarin de hoeveelheid studenten met en zonder hbo vooropleiding `Tabel` en een vector die aangeeft wat de verwachte proporties zijn voor het aantal studenten met en zonder hbo vooropleiding `p = c(0.1113, 1 - 0.1113)`.
# <!-- ## /TEKSTBLOK: Binomiaaltoets1.R -->
# 
# <!-- ## OPENBLOK: Binomiaaltoets2.R -->

# In[ ]:


# Maak een tabel met daarin de aantallen studenten met en zonder hbo vooropleiding
(Tabel <- table(Instroom_2018_totaal_steekproef$hbo_vooropleiding))
# Bereken de verwachte frequenties
chisq.test(Tabel, p = c(0.1113, 1 - 0.1113))$expected


# <!-- ## /OPENBLOK: Binomiaaltoets2.R -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets3.R -->
# Het aantal studenten met een hbo vooropleiding is `r table(Instroom_2018_totaal_steekproef$hbo_vooropleiding)[1]` en het aantal zonder hbo vooropleiding `r table(Instroom_2018_totaal_steekproef$hbo_vooropleiding)[2]`. De verwachte frequentie studenten met een hbo vooropleiding is `r Round_and_format(chisq.test(Tabel, p = c(0.1113, 1 - 0.1113))$expected)` wat kleiner dan vijf is. Voer daarom de *binomiaaltoets* uit, aangezien meer dan 20% van de categorieën een verwachte frequentie van vijf of minder heeft.
# <!-- ## /TEKSTBLOK: Binomiaaltoets3.R -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets4.R -->
# Tel eerst het aantal studenten met een hbo vooropleiding in de dataset. Voer daarna de *binomiaaltoets* uit met de functie `binom.test()` en met argument  `x = Aantal_studenten_hbo_vooropleiding` voor de hoeveelheid studenten met een hbo vooropleiding, `n = length(Instroom_2018_totaal_steekproef$hbo_vooropleiding)` voor de totale instroom van de universiteit, `p = 0.1113` voor de referentieproportie,  `alternative = two.sided` voor het soort toets (eenzijdig of tweezijdig) en `conf.level = 0.95` om het significantieniveau aan te geven.
# <!-- ## /TEKSTBLOK: Binomiaaltoets4.R -->

# <!-- ## OPENBLOK: Binomiaaltoets5.R -->

# In[ ]:


Aantal_studenten_hbo_vooropleiding <- length(Instroom_2018_totaal_steekproef$hbo_vooropleiding[Instroom_2018_totaal_steekproef$hbo_vooropleiding == "ja"])

binom.test(x = Aantal_studenten_hbo_vooropleiding, 
          n = length(Instroom_2018_totaal_steekproef$hbo_vooropleiding), 
          p = 0.1113, alternative = "two.sided", conf.level = 0.95)


# <!-- ## /OPENBLOK: Binomiaaltoets5.R -->
# 
# <!-- ## CLOSEDBLOK: Binomiaaltoets6.R -->

# In[ ]:


Aantal_studenten_hbo_vooropleiding <- length(Instroom_2018_totaal_steekproef$hbo_vooropleiding[Instroom_2018_totaal_steekproef$hbo_vooropleiding == "ja"])

b <- binom.test(x = Aantal_studenten_hbo_vooropleiding, 
          n = length(Instroom_2018_totaal_steekproef$hbo_vooropleiding), 
          p = 0.1113, 
          alternative = "two.sided",
          conf.level = 0.95)

bp <- Round_and_format(b$p.value)
blb <- Round_and_format(b$conf.int[1])
bub <- Round_and_format(b$conf.int[2])
bprop <- Round_and_format(b$estimate)


# <!-- ## /CLOSEDBLOK: Binomiaaltoets6.R -->
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets7.R-->
# * de geschatte proportie studenten met een hbo vooropleiding in de data is `r bprop`, het 95%-betrouwbaarheidsinterval loopt van `r blb` tot `r bub`
# * p-waarde = `r bp`, dus de H~0~ kan niet worden verworpen.[^5]  
# 
# <!-- ## /TEKSTBLOK: Binomiaaltoets7.R-->

# ## Rapportage
# 
# <!-- ## TEKSTBLOK: Binomiaaltoets8.R-->
# De *binomiaaltoets* is uitgevoerd om te onderzoeken of de verdeling van het instromende aantal studenten van een universiteit met en zonder hbo vooropleiding voor een dataset met een laag aantal observaties verschilt van de landelijke verdeling waarbij het percentage studenten met een hbo vooropleiding 11,13% is. De verdeling van het aantal instromende studenten met en zonder hbo vooropleiding is niet significant verschillend van de landelijke verdeling (*p* = `r bp`), dus de nulhypothese kan niet verworpen worden. De schatting van het percentage is `r bprop`% met een 95%-betrouwbaarheidsinterval van `r blb`% tot `r bub`% en is niet significant verschillend van het landelijk gemiddelde van 11,13%. De resultaten suggereren dat het percentage studenten met een hbo vooropleiding niet hoger ligt dan het landelijk gemiddelde van 11,13%.
# 
# <!-- ## /TEKSTBLOK: Binomiaaltoets8.R-->
# 
# 

# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





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
# <!-- ## TEKSTBLOK: Extra-Bron.R -->
# 
# <!-- ## /TEKSTBLOK: Extra-Bron.R -->
# 
