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


source(paste0(here::here(),"/01. Includes/data/12.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# <!-- ## TEKSTBLOK: Link1.R -->
# Gebruik de *McNemar toets* om te toetsen of er verschillen zijn voor de frequenties van een binaire[^1] variabele tussen twee gepaarde groepen.[^2]<sup>, </sup>[^3] De *McNemar toets* kan in theorie ook gebruikt worden om twee gepaarde groepen te vergelijken op een nominale variabele met meer dan twee categorieën. Deze toetspagina illustreert de toets echter voor een binaire variabele. Hoewel het dus mogelijk met de *McNemar toets* is om twee gepaarde groepen te vergelijken wat betreft een nominale variabele, wordt hiervoor echter de voorkeur gegeven aan de [Bhapkar toets](18-Bhapkar-toets-R.html).
# <!-- ## /TEKSTBLOK: Link1.R -->
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
# <!-- ## CLOSEDBLOK: Groepsgrootte0.R -->
# <!-- ## /CLOSEDBLOK: Groepsgrootte0.R -->
# 
# <!-- ## CLOSEDBLOK: Groepsgrootte1.R -->

# In[ ]:


### Definieer de groepen
December <- FOS_studenten$`FOS`[FOS_studenten$Maand == "december"]
Juni <- FOS_studenten$`FOS`[FOS_studenten$Maand == "juni"]

## Maak een frequentiematrix
FOS_studenten_frequentiematrix <- table(December, Juni)


# <!-- ## /CLOSEDBLOK: Groepsgrootte1.R -->
# 
# <!-- ## TEKSTBLOK: Groepsgrootte2.R -->
# 
# ||                      | Juni    |
# |-------------| -------------------- | -------------| ------------| 
# ||                      | FOS | geen FOS|
# |**December**| FOS      | `r FOS_studenten_frequentiematrix["ja","ja"]` | `r FOS_studenten_frequentiematrix["ja","nee"]`     |
# |            | Geen FOS | `r FOS_studenten_frequentiematrix["nee","ja"]` | `r FOS_studenten_frequentiematrix["nee","nee"]`     |
# *Tabel 1. Frequentiematrix van het aantal studenten dat een beroep doet op de FOS in december en juni.*
# 
# De cel linksboven bevat het aantal studenten dat zowel in december als juni een beroep heeft gedaan op de FOS; dit zijn er `r FOS_studenten_frequentiematrix["ja","ja"]`. De cel rechtsonder bevat het aantal studenten dat zowel in december als juni geen beroep heeft gedaan op de FOS; dit zijn er `r FOS_studenten_frequentiematrix["nee","nee"]`. Beide cellen staan op de diagonaal van de tabel en worden daarom de diagonale elementen genoemd.
# 
# In de cel rechtsboven staat het aantal studenten dat wel in december maar niet in juni een beroep op de FOS heeft gedaan; dit zijn er `r FOS_studenten_frequentiematrix["ja","nee"]`. In de cel linksonder staat het aantal studenten dat niet in december maar wel in juni een beroep op de FOS heeft gedaan; dit zijn er `r FOS_studenten_frequentiematrix["nee","ja"]`. Deze cellen zijn geen onderdeel van de diagonaal van de tabel en worden daarom de niet-diagonale elementen genoemd.
# <!-- ## /TEKSTBLOK: Groepsgrootte2.R -->
# 
# # De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `FOS_studenten`. In deze dataset is voor elke student aangegeven of ze wel of geen beroep op de FOS hebben gedaan in december en in juni. 
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(FOS_studenten)

## Laatste 6 observaties
tail(FOS_studenten)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Maand` en `FOS`. In feite laat dit zien hoeveel studenten er wel of niet een beroep doen op de FOS in december en in juni. Een kruistabel verschilt dus van een frequentiematrix. Maak de kruistabel met de functie `table()` met als argumenten de variabele `FOS_studenten$FOS`, die weergeeft of studenten wel of geen beroep op de FOS doen, en de variabele `FOS_studenten$Maand `, die het meetmoment (december of juni) weergeeft. 
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
FOS_studenten_kruistabel <- table(FOS_studenten$`FOS`, FOS_studenten$Maand)

## Print de kruistabel 
print(FOS_studenten_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per kolom berekend worden
prop.table(FOS_studenten_kruistabel, 2)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# De kruistabel laat zien dat het aantal studenten dat een beroep op de FOS heeft gedaan hoger is en het aantal studenten dat geen beroep op de FOS heeft gedaan lager is in juni. Het percentage studenten dat een beroep op de FOS heeft gedaan is toegenomen; dit is ook te zien in de kruistabel met proporties.
# 
# <!-- ## TEKSTBLOK: Data-bekijken3.R -->
# In aanvulling op de kruistabel, geeft de frequentiematrix ook een goede indruk van de data. In de frequentiematrix worden de aantallen studenten die wel of geen beroep op de FOS hebben gedaan tegen elkaar uitgezet voor december en juni. Sla daarom de variabele `FOS` apart op in twee vectoren: een voor december en een voor juni. Maak daarna de frequentiematrix.
# <!-- ## /TEKSTBLOK: Data-bekijken3.R -->
# 
# <!-- ## OPENBLOK: Data-beschrijven.R -->

# In[ ]:


## Definieer de groepen
December <- FOS_studenten$`FOS`[FOS_studenten$Maand == "december"]
Juni <- FOS_studenten$`FOS`[FOS_studenten$Maand == "juni"]

## Maak een frequentiematrix
FOS_studenten_frequentiematrix <- table(December, Juni)

## Print de frequentiematrix 
print(FOS_studenten_frequentiematrix)


# <!-- ## /OPENBLOK: Data-beschrijven.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken4.R -->
# De diagonale elementen bevatten `r FOS_studenten_frequentiematrix["ja","ja"]` en `r FOS_studenten_frequentiematrix["nee","nee"]` observaties. De niet-diagonale elementen bevatten `r FOS_studenten_frequentiematrix["ja","nee"]` en `r FOS_studenten_frequentiematrix["nee","ja"]` observaties.
# <!-- ## /TEKSTBLOK: Data-bekijken4.R -->
# 
# # McNemar toets
# 
# ## Uitvoering
# 
# <!-- ## TEKSTBLOK: McNemar-toets1.R -->
# Voer de *McNemar toets* uit om te onderzoeken of er een verschil is tussen de frequenties van de studenten dat wel of geen beroep doet op de FOS voor en na de interventie van de decaan. Gebruik de functie `exact2x2()` van het package `exact2x2` met als eerste argument de frequentiematrix `FOS_studenten_frequentiematrix`, als tweede argument `paired = TRUE` omdat er een gepaarde vergelijking wordt gemaakt en als derde argument `midp = TRUE` omdat de *mid p-value* methode gebruikt wordt.
# <!-- ## /TEKSTBLOK: McNemar-toets1.R -->
# 
# <!-- ## OPENBLOK: McNemar-toets2.R -->

# In[ ]:


library(exact2x2)

## Definieer de groepen
December <- FOS_studenten$`FOS`[FOS_studenten$Maand == "december"]
Juni <- FOS_studenten$`FOS`[FOS_studenten$Maand == "juni"]

## Maak een frequentiematrix
FOS_studenten_frequentiematrix <- table(December, Juni)

# Voer McNemar toets uit
exact2x2(FOS_studenten_frequentiematrix,
         paired = TRUE,
         midp = TRUE)


# <!-- ## /OPENBLOK: McNemar-toets2.R -->
# 
# Bereken het verschil tussen de proporties studenten dat een beroep doet op de FOS in december en juni. Op deze manier kan een (eventueel) significant resultaat geïnterpreteerd worden.
# 
# <!-- ## OPENBLOK: McNemar-toets5.R -->

# In[ ]:


## Maak een kruistabel
FOS_studenten_kruistabel <- table(FOS_studenten$`FOS`, FOS_studenten$Maand)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per kolom berekend worden
FOS_studenten_kruistabel_proporties <- prop.table(FOS_studenten_kruistabel, 2)

# Bereken het verschil in proporties
Verschil_proporties <- FOS_studenten_kruistabel_proporties["ja", "juni"] - FOS_studenten_kruistabel_proporties["ja", "december"]

# Print het verschil in proporties
Verschil_proporties


# <!-- ## /OPENBLOK: McNemar-toets5.R -->
# 
# <!-- ## TEKSTBLOK: McNemar-toets5.R -->
# * Er is een significant verschil tussen de frequenties van het aantal studenten dat wel of niet gebruik maakt van de FOS tussen december en juni, *p* < 0,0001  
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^6]
# * Het verschil in proporties is `r Round_and_format(Verschil_proporties)`, er zijn dus meer studenten die gebruik maken van de FOS in juni ten opzichte van december
# 
# <!-- ## /TEKSTBLOK: McNemar-toets5.R -->
# 
# ## Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *McNemar toets* is uitgevoerd om uit te vinden of er een verschil is in de frequenties van het aantal studenten dat wel of geen beroep doet op de FOS voor en na de interventie van de decaan. De interventie heeft als doel het aantal studenten met een functiebeperking dat een beroep doet op de FOS te verhogen. De resultaten laten een significant verschil zien tussen de frequenties voor en na de interventie (*p* < 0,0001), wat betekent dat de nulhypothese verworpen kan worden. Het verschil in de proportie studenten dat een beroep doet op de FOS is `r Round_and_format(Verschil_proporties)` . Het verschil in proporties en de kruistabel (Tabel 2) illustreren dat het percentage studenten dat een beroep doet op de FOS is toegenomen na de interventie. 
# 
# |                      | December | Juni |
# | -------------------- | -------------| ------------| 
# | **FOS** | `r FOS_studenten_kruistabel["ja","december"]`    | `r FOS_studenten_kruistabel["ja","juni"]`     |
# | **geen FOS**  | `r FOS_studenten_kruistabel["nee","december"]`      | `r FOS_studenten_kruistabel["nee","juni"]`     |
# *Tabel 2. Kruistabel van het aantal studenten dat een beroep doet op de FOS in december en juni*
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





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
# <!-- ## TEKSTBLOK: Extra_bron.R -->
# <!-- ## /TEKSTBLOK: Extra_bron.R -->
# 
