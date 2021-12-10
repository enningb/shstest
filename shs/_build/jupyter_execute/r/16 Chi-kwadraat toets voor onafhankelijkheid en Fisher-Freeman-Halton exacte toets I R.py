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


source(paste0(here::here(),"/01. Includes/data/16.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# <!-- ## TEKSTBLOK: link1.R -->
# Gebruik de *Chi-kwadraat toets voor onafhankelijkheid*[^1] of de *Fisher-Freeman-Halton exact toets*[^2] om te toetsen of er een afhankelijkheid is tussen twee (ongepaarde) categorische variabelen. De *Fisher-Freeman-Halton exact toets* is een alternatief voor de *Chi-kwadraat toets voor onafhankelijkheid* bij een laag aantal observaties, dit wordt bij de assumpties toegelicht.[^2]<sup>,</sup>[^3] De *Fisher-Freeman-Halton exact toets* is een uitbreiding van de [Fisher's exacte toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-R.html) welke gebruikt wordt om te toetsen of er een verband bestaat tussen twee ongepaarde binaire variabelen, oftewel een 2x2 tabel. 
# <!-- ## /TEKSTBLOK: link1.R -->
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
# Als post-hoc toets voor de *Chi-kwadraat toets voor onafhankelijkheid* wordt het gestandaardiseerde residu gebruikt. Dit is het gestandaardiseerde verschil tussen het (geobserveerde) aantal observaties en het verwachte aantal observaties, waarbij gestandaardiseerd betekent dat het een gemiddelde van 0 en standaardafwijking van 1 heeft. Op deze manier kunnen de verschillende residuen met elkaar vergeleken worden, omdat ze dezelfde schaal hebben. Voor elke cel in de kruistabel kan het gestandaardiseerde residu bepaald worden. Vergelijkbaar met z-scores[^11] zijn deze residuen significant bij een waarde groter dan ± 1,96 wanneer een significantieniveau (α) van 0,05 wordt gehanteerd. Op deze manier kan bepaald worden in welke cellen er afwijkingen van de verwachte aantallen zijn.[^5]
# 
# <!-- ## TEKSTBLOK: link2.R -->
# Voor de *Fisher-Freeman-Halton exact toets* is er geen specifiek voorgeschreven post-hoc toets.[^3]<sup>,</sup>[^5] Een goede optie is het uitvoeren van losse [Fisher's exacte toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-R.html) voor elke mogelijke combinatie van 2x2 tabellen. Gebruik een correctie op de p-waarden, omdat er meerdere testen tegelijk uitgevoerd worden. Een bekende correctie is de Bonferroni methode, andere opties zijn ook mogelijk.[^5] 
# <!-- ## /TEKSTBLOK: link2.R -->
# 
# # Effectmaat
# 
# De p-waarde geeft aan of het verschil tussen twee groepen statistisch significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^5] 
# De *Chi-kwadraat toets voor onafhankelijkheid* heeft als effectmaat *w*.[^6] Een indicatie om *w* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^7]
# 
# <!-- ## TEKSTBLOK: link3.R -->
# De *Fisher-Freeman-Halton exact toets* heeft geen specifieke effectmaat. De post-hoc toets van deze toets - [Fisher's exacte toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-R.html) - gebruikt echter de odds ratio als effectmaat. De odds ratio is een effectmaat die voor zowel de *Chi-kwadraat toets voor onafhankelijkheid* als de [Fisher's exacte toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-R.html) kan worden gebruikt. Een voorwaarde is echter dat beide variabelen binair zijn. In andere woorden, er moet een 2x2 kruistabel gevormd kunnen worden. Odds is een Engelse term voor de verhouding van twee kansen, bijvoorbeeld de verhouding tussen het aantal studenten met positief BSA en negatief BSA. Een odds ratio is de verhouding tussen twee odds, bijvoorbeeld de verhouding van de odds van studenten met Nederland als land van hoogste vooropleiding en studenten met Duitsland als land van hoogste vooropleiding. De odds ratio geeft dus een interpretatie van de verschillen tussen landen op het behalen van een positief of negatief BSA.[^5]
# <!-- ## /TEKSTBLOK: link3.R -->
# 
# # De data bekijken
# 
# <!-- ## TEKSTBLOK: Data-bekijken1.R -->
# Er is een dataset ingeladen genaamd `BSA_antropologie`. In deze dataset is voor elke student aangegeven wat het land van de hoogst genoten vooropleiding is en of ze een positief of negatief BSA ontvangen hebben.
# <!-- ## /TEKSTBLOK: Data-bekijken1.R -->
# 
# <!-- ## OPENBLOK: Data-bekijken2.R -->

# In[ ]:


## Eerste 6 observaties
head(BSA_antropologie)

## Laatste 6 observaties
tail(BSA_antropologie)


# <!-- ## /OPENBLOK: Data-bekijken2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de variabelen `Landen_vooropleiding` en `BSA`. Maak de kruistabel met de functie `table()` met als argumenten de variabele `BSA_antropologie$BSA` (positief of negatief BSA) en `BSA_antropologie$Landen_vooropleiding` (land van hoogst genoten vooropleiding). 
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:



## Maak een kruistabel
BSA_antropologie_kruistabel <- table(BSA_antropologie$BSA, BSA_antropologie$Landen_vooropleiding)

## Print de kruistabel 
print(BSA_antropologie_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per kolom berekend worden
prop.table(BSA_antropologie_kruistabel, 2)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3.R -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat de meerderheid van de studenten een positief BSA ontvangt voor elk land van vooropleiding. Van studenten uit het Verenigd Koninkrijk (UK) haalt verhoudingsgewijs het grootste deel een positief BSA. Het percentage studenten met een positief BSA is hier `r Round_and_format(100 * prop.table(BSA_antropologie_kruistabel, 2)[2,6])`%.
# <!-- ## /TEKSTBLOK: Data-kruistabel3.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel4.R -->
# Bekijk in aanvulling op de kruistabel de data ook met een staafdiagram. Maak een staafdiagram van de aantallen en percentages studenten met een positief en negatief BSA voor de verschillende landen van vooropleiding. Gebruik het argument `position = "dodge"` in de functie `geom_bar()` om de aantallen weer te geven en het argument `position = "fill"` in de functie `geom_bar()` om de proporties weer te geven.
# <!-- ## /TEKSTBLOK: Data-kruistabel4.R -->
# 
# 

# In[ ]:


## Bereken de frequentie voor elke combinatie van BSA advies en land van vooropleiding
Frequenties <- aggregate(Studentnummer ~ BSA + Landen_vooropleiding, 
                         data = BSA_antropologie, 
                         FUN = length)
## Verander de kolomnaam voor de variabele met de frequenties
colnames(Frequenties)[3] <- "Frequentie"

## Maak een staafdiagram met ggplot2
library(ggplot2)

ggplot(Frequenties, 
       aes(y = Frequentie, x = Landen_vooropleiding, fill = BSA)) + 
  geom_bar(position = "dodge", stat = "identity") +
  xlab("Landen vooropleiding") 

ggplot(Frequenties, 
       aes(y = Frequentie, x = Landen_vooropleiding, fill = BSA)) + 
  geom_bar(position = "fill", stat = "identity") +
  ylab("Proportie") +
  xlab("Landen vooropleiding") 


# De staafdiagram laat ook zien dat de meeste studenten in elk land van vooropleiding in de meerderheid een positief BSA behalen. De proportie negatieve BSA is het hoogst voor Italië en het laagst voor het Verenigd Koninkrijk.

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: Assumptie.R -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk of kleiner dan vijf is. Bereken het verwachte aantal observaties met het argument `chisq.test()$expected` van de functie `chisq.test()` met als argumenten de variabelen `BSA_antropologie$BSA` (positief of negatief BSA) en `BSA_antropologie$Landen_vooropleiding` (landen van hoogst genoten vooropleiding).
# <!-- ## /TEKSTBLOK: Assumptie.R -->
# 
# <!-- ## OPENBLOK: Assumptie1.R -->

# In[ ]:


# Bereken het verwacht aantal observaties per cel van de kruistabel
Tabel_assumptie <- chisq.test(BSA_antropologie$BSA, BSA_antropologie$Landen_vooropleiding)$expected
# Print de tabel
Tabel_assumptie
# Extra: bereken het percentage verwachte aantallen observaties van vijf of minder
100 * (sum(Tabel_assumptie <= 5) / length(Tabel_assumptie))


# <!-- ## /OPENBLOK: Assumptie1.R -->
# 
# Geen van de verwachte aantallen observaties is gelijk of kleiner dan vijf, dus de *Chi-kwadraat toets voor onafhankelijkheid* kan worden uitgevoerd.
# 
# # Chi-kwadraat toets voor onafhankelijkheid
# ## Uitvoering
# <!-- ## TEKSTBLOK: Chi2-toets.R -->
# De *Chi-kwadraat toets voor onafhankelijkheid* wordt uitgevoerd om de vraag te beantwoorden of er een afhankelijkheid is tussen het land van vooropleiding en het wel of niet halen van een positief BSA. Gebruik de functie `chisq.test()` met als argumenten de variabelen `BSA_antropologie$BSA` (positief of negatief BSA) en `BSA_antropologie$Landen_vooropleiding` (landen van hoogst genoten vooropleiding).
# <!-- ## /TEKSTBLOK: Chi2-toets.R -->
# 
# <!-- ## OPENBLOK: Chi2-toets.R -->

# In[ ]:


chisq.test(BSA_antropologie$BSA, BSA_antropologie$Landen_vooropleiding)


# <!-- ## /OPENBLOK: Chi2-toets.R -->
# 
# <!-- ## CLOSEDBLOK: Chi2-toets.R-->

# In[ ]:


Chi2 <- chisq.test(BSA_antropologie$BSA, BSA_antropologie$Landen_vooropleiding)
vChi2 <- Round_and_format(Chi2$statistic)
vP <- Round_and_format(Chi2$p.value)
vDF <- Chi2$parameter


# <!-- ## /CLOSEDBLOK: Chi2-toets.R-->
# 
# Bereken de effectmaat *w* vervolgens op basis van de *&chi;^2^*-waarde van de *Chi-kwadraat toets voor onafhankelijkheid*.
# <!-- ## OPENBLOK: Chi2-toets-2.R -->

# In[ ]:


# Sla de teststatistiek op
Chi2_teststatistiek <- chisq.test(BSA_antropologie$BSA, BSA_antropologie$Landen_vooropleiding)$statistic

# Bereken het totaal aantal observaties als som van de kruistabel
N <- nrow(BSA_antropologie)

# Bereken eta squared
w <- sqrt(Chi2_teststatistiek / N)

# Print effectgrootte
paste("Effectgrootte is",w)


# <!-- ## /OPENBLOK: Chi2-toets-2.R -->

# <!-- ## TEKSTBLOK: Chi2-toets4.R-->
# * *&chi;^2^* ~`r vDF`~ = `r vChi2`, *p* < 0,0001  
# * Vrijheidsgraden: *df* = (*k*-1)(*r*-1), waar k staat voor kolom en r voor rij. In dit geval geldt *df* = `r vDF`. 
# * p-waarde < 0,05, de H~0~ wordt verworpen.[^8]
# * Effectmaat is `r Round_and_format(w)`, dus een klein tot gemiddeld effect
# 
# <!-- ## /TEKSTBLOK: Chi2-toets4.R-->
# 
# ## Post-hoc toets: gestandaardiseerde residuen
# 
# Voer post-hoc toetsen uit om te bepalen welke landen van hoogste vooropleiding van elkaar verschillen wat betreft de verdeling van het aantal studenten met positief en negatief BSA. Inspecteer hiervoor de Pearson residuen van de *Chi-kwadraat toets voor onafhankelijkheid* op waarden groter dan 1,96 en kleiner dan -1,96. Let op dat hier nog geen correctie voor meerdere testen plaatsvindt.[^9]
# 
# <!-- ## OPENBLOK: Chi2-toets post-hoc1.R -->

# In[ ]:


resultaat <- chisq.test(BSA_antropologie$BSA, BSA_antropologie$Landen_vooropleiding)
resultaat$residuals


# <!-- ## /OPENBLOK: Chi2-toets post-hoc1.R -->
# 
# <!-- ## TEKSTBLOK: Chi2-toets post-hoc2.R-->
# * Significant hoger aantal observaties bij negatief BSA België (BE), *z* = `r Round_and_format(resultaat$residuals["Negatief","BE"])`
# * Significant hoger aantal observaties bij negatief BSA Italië (IT), *z* = `r Round_and_format(resultaat$residuals["Negatief","IT"])`
# * Significant lager aantal observaties bij negatief BSA Nederland (NL), *z* = `r Round_and_format(resultaat$residuals["Negatief","NL"])`
# * Significant lager aantal observaties bij negatief BSA Verenigd Koninkrijk (UK), *z* = `r Round_and_format(resultaat$residuals["Negatief","UK"])`
# * Significant hoger aantal observaties bij negatief BSA Verenigde Staten (US), *z* = `r Round_and_format(resultaat$residuals["Negatief","US"])`
# * Significant lager aantal observaties bij positief BSA Italië (IT), *z* = `r Round_and_format(resultaat$residuals["Positief","IT"])`
# 
# <!-- ## /TEKSTBLOK: Chi2-toets post-hoc2.R-->
# 

# ## Rapportage
# 
# <!-- ## TEKSTBLOK: RapportageChi2.R -->
# De *Chi-kwadraat toets voor onafhankelijkheid* is uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen het land van hoogst genoten vooropleiding en het wel of niet behalen van een positief BSA. De resultaten illustreren dat de nulthypothese verworpen kan worden, *χ^2^* ~`r vDF`~ ≈ `r vChi2`, *p* < 0,0001, *w* = `r Round_and_format(w)`. Het land van hoogst genoten vooropleiding en het behalen van een positief of negatief BSA zijn dus niet onafhankelijk van elkaar. Dat betekent dat er verschillen zijn tussen de landen wat betreft de proportie studenten met een positief BSA.

# De resultaten van de post-hoc toetsen van de *Chi-kwadraat toets voor onafhankelijkheid* zijn te vinden in Tabel 3, waarin geobserveerde aantallen met asterisk significant verschillend zijn van verwachte aantallen. De geobserveerde aantallen voor de verschillende landen van hoogste vooropleiding bij een positief BSA verschillen niet significant van de verwachte aantallen. Bij een negatief BSA is er echter een aantal landen waarbij significante verschillen van het verwachte aantal zijn op te merken. Nederland (NL; *z* = `r Round_and_format(resultaat$residuals["Negatief","NL"])`) en het Verenigd Koninkrijk (UK; *z* = `r Round_and_format(resultaat$residuals["Negatief","UK"])`) hebben een lager aantal studenten met een negatief BSA dan verwacht; Italië (IT; *z* = `r Round_and_format(resultaat$residuals["Negatief","IT"])`), België (BE; *z* = `r Round_and_format(resultaat$residuals["Negatief","ES"])`) en de Verenigde Staten (US; *z* = `r Round_and_format(resultaat$residuals["Negatief","US"])`) een hoger aantal studenten met negatief BSA dan verwacht. Daarnaast heeft Italië (IT; *z* = `r Round_and_format(resultaat$residuals["Positief","IT"])`) ook een lager aantal studenten met positief BSA dan verwacht.
# <!-- ## /TEKSTBLOK: RapportageChi2.R -->
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
# <!-- ## TEKSTBLOK: UitvoeringFFH.R -->
# De *Fisher-Freeman-Halton exact toets* wordt uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen het land van hoogst genoten vooropleiding en het wel of niet behalen van een positief BSA. Deze toets wordt in plaats van de *Chi-kwadraat toets voor onafhankelijkheid* gebruikt wanneer er in meer dan 20% van de cellen een verwacht aantal observaties van 5 of lager is. Er is een nieuwe dataset `Fisher_BSA_antropologie` ingeladen met daarin een lager aantal observaties.
# <!-- ## /TEKSTBLOK: UitvoeringFFH.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1f.R -->
# Een kruistabel geeft de aantallen observaties weer voor de combinaties van de categorieën van de categorische variabelen `Landen_vooropleiding` en `BSA`. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Fisher_BSA_antropologie$BSA` (positief of negatief BSA) en `Fisher_BSA_antropologie$Landen_vooropleiding` (land van hoogst genoten vooropleiding). 
# <!-- ## /TEKSTBLOK: Data-kruistabel1f.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2f.R -->

# In[ ]:


## Maak een kruistabel
Fisher_BSA_antropologie_kruistabel <- table(Fisher_BSA_antropologie$BSA, Fisher_BSA_antropologie$Landen_vooropleiding)

## Print de kruistabel 
print(Fisher_BSA_antropologie_kruistabel)

## Print een tabel met proporties, tweede argument 2 zorgt ervoor dat de 
## proporties per kolom berekend worden
prop.table(Fisher_BSA_antropologie_kruistabel, 2)


# <!-- ## /OPENBLOK: Data-kruistabel2f.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel3f.R -->
# De kruistabel en bijbehorende tabel met proporties laat zien dat de meerderheid van de studenten een positief BSA ontvangt voor elk land van vooropleiding. Van studenten uit het Nederland (NL) haalt verhoudingsgewijs het grootste deel een positief BSA. Het percentage studenten met een positief BSA is hier `r Round_and_format(100 * prop.table(Fisher_BSA_antropologie_kruistabel, 2)[2,5])`%.
# <!-- ## /TEKSTBLOK: Data-kruistabel3f.R -->

# ## Assumptie groepsgrootte
# 
# <!-- ## TEKSTBLOK: Assumptie0f.R -->
# Toets de assumptie dat niet meer dan 20% van de verwachte aantallen observaties gelijk of kleiner dan vijf is. Bereken het verwachte aantal observaties met het argument `chisq.test()$expected` van de functie `chisq.test()` met als argumenten de variabelen `Fisher_BSA_antropologie$BSA` (positief of negatief BSA) en `Fisher_BSA_antropologie$Landen_vooropleiding` (landen van hoogst genoten vooropleiding).
# <!-- ## /TEKSTBLOK: Assumptie0f.R -->
# 
# <!-- ## OPENBLOK: Assumptie1f.R -->

# In[ ]:


chisq.test(Fisher_BSA_antropologie$BSA, Fisher_BSA_antropologie$Landen_vooropleiding)$expected


# <!-- ## /OPENBLOK: Assumptie1f.R -->
# 
# Drie van de 14 (21,43%) verwachte aantallen observaties zijn kleiner dan vijf. Meer dan 20% van de verwachte aantallen observaties is kleiner of gelijk aan vijf, dus de assumptie van de groepsgroette van de *Chi-kwadraat toets voor onafhankelijkheid* houdt geen stand. De *Fisher-Freeman-Halton toets* moet inderdaad uitgevoerd worden.
# 
# ## Uitvoering
# <!-- ## TEKSTBLOK: Fisher-Freeman-Halton-exact-toets.R-->
# Gebruik de functie `fisher.test()` met als argumenten de variabele `Fisher_BSA_antropologie$BSA` (positief of negatief BSA), de variabele `Fisher_BSA_antropologie$Landen_vooropleiding` (landen van hoogst genoten vooropleiding) en als laatste argument `simulate.p.value = TRUE`. Hierdoor wordt de p-waarde met een simulatie berekend waardoor de rekentijd voor de computer een stuk lager is en de resultaten sneller weergegeven kunnen worden. Gebruik een seed (`set.seed(123)`) om ervoor te zorgen dat de p-waarde reproduceerbaar is. Bij een simulatie kunnen er namelijk kleine verschillen tussen de resultaten zijn bij het herhalen van de simulatie.
# <!-- ## /TEKSTBLOK: Fisher-Freeman-Halton-exact-toets.R-->
# 
# <!-- ## OPENBLOK: Fisher-Freeman-Halton-exact-toets.R-->
# ``` {r fisher toets}
# # Gebruik een seed zodat dezelfde resultaten getoond worden bij het herhalen
# set.seed(123)
# 
# # Voer de Fisher-Freeman-Halton toets uit
# fisher.test(Fisher_BSA_antropologie$BSA, Fisher_BSA_antropologie$Landen_vooropleiding, simulate.p.value = TRUE)
# ```
# <!-- ## /OPENBLOK: Fisher-Freeman-Halton-exact-toets.R-->
# 
# <!-- ## CLOSEDBLOK: Fisher-Freeman-Halton-exact-toets1.R-->
# ``` {r fisher toets p}
# # Gebruik een seed zodat dezelfde resultaten getoond worden bij het herhalen
# set.seed(123)
# 
# # Voer de Fisher-Freeman-Halton toets uit
# fish <- fisher.test(Fisher_BSA_antropologie$BSA, Fisher_BSA_antropologie$Landen_vooropleiding, simulate.p.value = TRUE)$p.value
# ```
# <!-- ## /CLOSEDBLOK: Fisher-Freeman-Halton-exact-toets1.R-->
# 
# <!-- ## TEKSTBLOK: Fisher-Freeman-Halton-exact-toets2.R-->
# * p-waarde is `r Round_and_format(fish)`, de H~0~ kan niet worden verworpen [^8]
# 
# <!-- ## /TEKSTBLOK: Fisher-Freeman-Halton-exact-toets2.R-->
# 
# ## Post-hoc toets: Fisher's exacte toets
# 
# <!-- ## TEKSTBLOK: Fisher-Freeman-Halton-exact-toets post-hoc1.R-->
# Omdat er geen afhankelijkheid is tussen het wel of niet halen van een positief BSA en het land van hoogste vooropleiding, hoeven er geen post-hoc toetsen uitgevoerd te worden. Indien dit wel nodig is, voer deze dan uit met de functie `fisher.multcomp()` met als eerste argument de kruistabel van de dataset en als tweede argument de gebruikte methode om te corrigeren voor meerdere testen, in dit geval `p.method = "bonferroni"`. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans dat er bij toeval een verband wordt ontdekt dat er niet is.[^5]    
# <!-- ## /TEKSTBLOK: Fisher-Freeman-Halton-exact-toets post-hoc1.R -->

# <!-- ## OPENBLOK: Fisher-Freeman-Halton-exact-toets post-hoc2.R -->
# ``` {r fisher toets post hoc, warning=FALSE, message=FALSE}
# library(RVAideMemoire)
# # Maak een kruistabel
# Fisher_BSA_antropologie_kruistabel <- table(Fisher_BSA_antropologie$BSA, Fisher_BSA_antropologie$Landen_vooropleiding)
# # Voer de post-hoc toets uit
# fisher.multcomp(Fisher_BSA_antropologie_kruistabel, p.method = "bonferroni")
# 
# ```
# <!-- ## /OPENBLOK: Fisher-Freeman-Halton-exact-toets post-hoc2.R -->
# 
# <!-- ## TEKSTBLOK: link4.R -->
# De resultaten laten de significantie zien van de [Fisher's exacte toets](13-Chi-kwadraat-toets-en-Fishers-exact-toets-R.html) voor elk mogelijke combinatie van 2x2 tabellen. Geen van de post-hoc toetsen is significant, wat logisch is aangezien de *Fisher-Freeman-Halton exact toets* niet significant was.  De eerste waarde is bijvoorbeeld de p-waarde van deze toets voor de kruistabel bestaande uit de aantallen positief en negatief BSA voor Nederland en Duitsland (NL:GE). De opmerkelijke p-waardes van 1 komen in een aantal gevallen door de Bonferroni correctie die de oorspronkelijke p-waarde met het aantal vergelijkingen (21) vermenigvuldigt. In andere gevallen zijn de verschillen zo klein dat dit leidt tot een p-waarde van 1.
# <!-- ## /TEKSTBLOK: link4.R -->

# ## Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Fisher-Freeman-Halton exact toets* is uitgevoerd om te onderzoeken of er een afhankelijkheid is tussen het land van hoogst genoten vooropleiding en het wel of niet behalen van een positief BSA voor een dataset met een laag aantal observaties. De nulhypothese kan niet verworpen worden (*p* = `r Round_and_format(fish)`), dus er lijkt geen afhankelijkheid te zijn tussen het wel of niet ontvangen van een positief BSA en het land van de hoogst genoten vooropleiding. Het percentage studenten met een positief BSA lijkt niet te verschillen per land van hoogst genoten vooropleiding. 
# 
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->

# [^1]: Van Geloven, N. (20 augustus 2015). *Chi-kwadraat toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Chi-kwadraat_toets).
# [^2]: Van Geloven, N. & Holman, R. (6 mei 2016). *Fisher's exact toets*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Fisher%27s_exact_toets).
# [^3]: Agresti, A. (2003). *Categorical data analysis*. Vol. 482, John Wiley & Sons.
# [^4]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw). [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: De effectmaat *w* wordt voor de *Chi-kwadraat toets voor onafhankelijkheid* berekend door de wortel te nemen van de
# *&chi;^2^*-waarde gedeeld door het totaal aantal observaties, i.e. $\sqrt{ \frac{\chi^2}{N} }$.
# [^7]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^8]: Dit voorbeeld gaat uit van een waarschijnlijkheid van 95% en zodoende een p-waardegrens van 0,05. Dit is naar eigen inzicht aan te passen. Hou hierbij rekening met type I en type II fouten.
# [^9]: De waarde 1,96 is een z-score en correspondeert met het significantieniveau 0,05 voor een tweezijdige toets. Om te corrigeren voor meerdere testen kan een ander significantieniveau gekozen worden wat resulteert in een andere z-score om mee te vergelijken. Bij een significantieniveau van 0,01 is de z-score bijvoorbeeld 2,58. De z-score per significantieniveau is te berekenen met `abs(qnorm(alfa/2))` waarbij `alfa` het gewenste significantieniveau is.
# [^10]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^11]: Een z-score is een maat om aan te geven hoeveel een observatie afwijkt van het gemiddelde. De z-score wordt berekend door het gemiddelde van de observatie af te halen en dit daarna te delen door de standaarddeviatie, i.e. $\frac{X - \mu}{\sigma}$. In feite geeft een z-score aan hoeveel standaarddeviaties de observatie van het gemiddelde afwijkt.
