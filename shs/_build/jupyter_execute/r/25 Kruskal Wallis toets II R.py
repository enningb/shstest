#!/usr/bin/env python
# coding: utf-8
---
title: "Kruskal Wallis toets"
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


source(paste0(here::here(),"/01. Includes/data/25.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik de *Kruskal Wallis toets* om te toetsen of twee of meer ongepaarde groepen van elkaar verschillen op een ordinale[^16] variabele.[^17]<sup>, </sup>[^1] Als de variabele beter als nominaal[^18] beschouwd kan worden, is de *chi-kwadraat toets voor onafhankelijkheid* of de *Fisher-Freeman-Halton exact toets* (bij een laag aantal observaties) een alternatief. Bij deze toetsen wordt echter geen rekening gehouden met de ordening van de categorieën van de ordinale variabele: de variabele wordt behandeld als een nominale variabele.
# 
# # Onderwijscasus
# <div id="casus">
# 
# Bij het interdisciplinaire vak ‘Presentatievaardigheden’ van de faculteit Economie en Bedrijfswetenschappen leren studenten om een overtuigende presentatie te geven over een product. Het vak wordt afgesloten met een individuele presentatie die beoordeeld wordt als onvoldoende, voldoende, goed of uitstekend. Het vak wordt gevolgd door studenten van de masters Economics, Finance, Entrepeneurship en Marketing. De hoofddocent wil graag onderzoeken of er verschillen zijn tussen de beoordelingen van studenten van deze vier masters. Wanneer er verschillen zijn, kan hij in gesprek gaan met studenten van een master die minder goed scoort om te onderzoeken wat de oorzaak hiervan zou kunnen zijn. 
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er zijn geen verschillen tussen (de gemiddelde rangnummers van) de beoordeling van het vak Presentatievaardigheden voor studenten afkomstig van de opleidingen Economics, Finance, Entrepeneurship en Marketing.
# 
# *H~A~*: Er zijn verschillen tussen (de gemiddelde rangnummers van) de beoordeling van het vak Presentatievaardigheden voor studenten afkomstig van de opleidingen Economics, Finance, Entrepeneurship en Marketing.
# 
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de afhankelijke variabele is ordinaal[^16] of continu.[^17] In deze toetspagina staat een casus met een ordinale afhankelijke variabele centraal; een casus met een continue afhankelijke variabele met bijbehorende uitwerking is te vinden in de [Kruskal Wallis toets I](10-Kruskal-Wallis-toets-I-R.html).
# 
# Om de *Kruskal Wallis toets* uit te voeren met een ordinale afhankelijke variabele, moet deze variabele omgezet worden in getallen. Wanneer er vier categorieën zijn, worden ze genummerd van 1 tot en met 4 op basis van de ordening van de variabele. De categorieën onvoldoende, voldoende, goed en uitstekend worden dan omgezet in respectievelijk 1, 2, 3 en 4. Bij de *chi-kwadraat toets voor onafhankelijkheid* en de *Fisher-Freeman_Halton exact toets* wordt dit niet gedaan, maar wordt de ordinale afhankelijke variabele als nominaal[^18] beschouwd. De *Kruskal Wallis toets* maakt een rangschikking van alle observaties van alle groepen samengevoegd en telt vervolgens apart de rangnummers op voor de observaties in alle groepen. Met behulp van de groepsgroottes kan ook het gemiddelde rangnummer van de groepen berekend worden. Het verschil tussen de gemiddelde rangnummers van de groepen bepaalt de significantie van de toets.[^17]
# 
# # Post-hoc toets 
# De *Kruskal Wallis toets* toetst of er een verschil is tussen de groepen op gebied van de afhankelijke variabele. De post-hoc toets wordt daarna gebruikt om te toetsen tussen welke specifieke groepen er een significant verschil is. Gebruik de [Mann-Whitney U toets](23-Mann-Whitney-U-toets-II-R.html) als post-hoc toets.
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout.[^9] Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^3]
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^2] 
# 
# Bij de *Kruskal Wallis toets* wordt eta-squared (*η^2^*) als effectmaat gebruikt.[^10] De effectmaat eta squared (*η^2^*) berekent de proportie van de variantie in de afhankelijke variabele die verklaard wordt door de onafhankelijke variabele. In deze casus berekent het de proportie van de variantie in de beoordelingen van presentaties die verklaard kan worden door de opleiding. Een indicatie om *η^2^* te interpreteren is: rond 0,01 is een klein effect, rond 0,06 is een gemiddeld effect en rond 0,14 is een groot effect.[^11]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Beoordelingen_presentatievaardigheden` ingeladen met daarin de beoordelingen voor het vak Presentatievaardigheden van studenten afkomstig van de opleidingen Economics, Finance, Entrepeneurship en Marketing.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Beoordelingen_presentatievaardigheden)

## Laatste 6 observaties
tail(Beoordelingen_presentatievaardigheden)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-bekijken2.R-->
# De dataset bevat gegevens van studenten van verschillende opleidingen. Gebruik `unique()` om te onderzoeken welke opleidingen er in de data aanwezig zijn. 
# <!-- ## /TEKSTBLOK: Data-bekijken2.R-->
# 
# <!-- ## OPENBLOK: Data-bekijken-2.R -->

# In[ ]:


## Bepaal welke opleidingen er zijn in de dataset
unique(Beoordelingen_presentatievaardigheden$Opleiding)


# <!-- ## /OPENBLOK: Data-bekijken-2.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft het aantal observaties weer voor de combinaties van de categorieën van de variabelen `Opleiding` en `Beoordeling`. In feite laat dit zien welke beoordelingen de studenten van de verschillende opleidingen krijgen. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Beoordelingen_presentatievaardigheden$Opleiding` en de variabele `Beoordelingen_presentatievaardigheden$Beoordeling`. Zet de beoordelingen handmatig op de juiste volgorde, omdat `R` de alfabetische volgorde aanhoudt.
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
Beoordelingen_kruistabel <- table(Beoordelingen_presentatievaardigheden$Beoordeling,
                                  Beoordelingen_presentatievaardigheden$Opleiding)

## Bepaal de volgorde van de beoordelingen
Volgorde <- c("Onvoldoende", "Voldoende", "Goed", "Uitstekend")

## Print de kruistabel 
print(Beoordelingen_kruistabel[Volgorde,])

## Print een tabel met proporties; het tweede argument `2` zorgt ervoor dat de 
## proporties per kolom berekend worden
prop.table(Beoordelingen_kruistabel[Volgorde,], 2)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# De kruistabel en bijbehorende kruistabel met proporties geven informatie over de verdeling van de beoordelingen van studenten. Bij Economics en Finance krijgen de meeste studenten een voldoende als beoordeling. Bij Entrepeneurship worden de presentatievaardigheden van studenten het vaakst als goed beoordeeld en bij Marketing het meest als uitstekend.
# 
# ## De data visualiseren
# Maak een staafdiagram om de verdeling van de beoordelingen aan het begin en eind van het vak visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.R -->

# In[ ]:


## Histogram met ggplot2
library(ggplot2)

ggplot(Beoordelingen_presentatievaardigheden,
  aes(Beoordeling)) +
  geom_bar(color = "grey30",
                 fill = "#0089CF") +
  scale_x_discrete(limits = c("Onvoldoende", "Voldoende", "Goed", "Uitstekend")) +
  facet_wrap(~ Opleiding) +
  ylab("Frequentie") +
  labs(title = "Beoordeling van presentatievaardigheden per opleiding")


# <!-- ## /OPENBLOK: Histogram1.R -->
# 
# Het staafdiagram maakt duidelijk dat bij Economics en Finance de meeste studenten een voldoende halen voor hun presentatievaardigheden. Bij Marketing en Entrepeneurship is de beoordeling met de hoogste frequentie hoger. Bij Marketing ontvangen de meeste studenten goed als beoordeling en bij Entrepeneurship komt de beoordeling uitstekend het meest voor.
# 
# ## Kruskal Wallis toets
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-1.R -->
# Voer de *Kruskal Wallis toets* uit om te onderzoeken of er verschillen zijn tussen de beoordelingen van de presentatievaardigheden van studenten van de opleidingen Economics, Finance, Entrepeneurship en Marketing. Zet eerst de categorische variabele `Beoordeling` om in een numerieke variabele door de categorieën onvoldoende, voldoende, goed en uitstekend om te zetten in respectievelijk 1, 2, 3 en 4. Gebruik de functie `kruskal.test()` met als eerste argument de afhankelijke variabele `Beoordeling_numeriek` en de variabele die de groep definiëert: `Opleiding`. Het tweede argument is het dataframe `Beoordelingen_presentatievaardigheden`. 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-1.R -->
# 
# <!-- ## OPENBLOK: Kruskal-Wallis-test-2.R -->

# In[ ]:


# Zet de categorieën om in getallen
Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Beoordeling == "Onvoldoende"] <- 1
Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Beoordeling == "Voldoende"] <- 2
Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Beoordeling == "Goed"] <- 3
Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Beoordeling == "Uitstekend"] <- 4

# Maak de variabele numeriek
Beoordelingen_presentatievaardigheden$Beoordeling_numeriek <- as.numeric(Beoordelingen_presentatievaardigheden$Beoordeling_numeriek)

# Voer de Kruskal Wallis toets uit
kruskal.test(Beoordeling_numeriek ~ Opleiding, Beoordelingen_presentatievaardigheden)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-2.R -->
# 
# Bereken de effectmaat *&eta;^2^* vervolgens op basis van de *&chi;^2^*-waarde van de *Kruskal-Wallis toets*.
# <!-- ## OPENBLOK: Kruskal-Wallis-test-3.R -->

# In[ ]:


# Sla de teststatistiek op
KW_teststatistiek <- kruskal.test(Beoordeling_numeriek ~ Opleiding, Beoordelingen_presentatievaardigheden)$statistic

# Bereken eta squared
Eta_squared <- KW_teststatistiek / (nrow(Beoordelingen_presentatievaardigheden) - 1)

# Print de effectgrootte
paste("Eta squared is",Eta_squared)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-3.R -->

# <!-- ## CLOSEDBLOK: Kruskal-Wallis-test-4.R -->

# In[ ]:


Ktest <- kruskal.test(Beoordeling_numeriek ~ Opleiding, Beoordelingen_presentatievaardigheden)
vK_DF <- Round_and_format(Ktest$parameter)
vK_Chi2 <- Round_and_format(Ktest$statistic)
vK_P <- Round_and_format(Ktest$p.value)


# <!-- ## /CLOSEDBLOK: Kruskal-Wallis-test-4.R -->
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-5.R -->
# * *df*: het aantal groepen - 1 = `r vK_DF`  
# * *H* = `r vK_Chi2`, *df* = `r vK_DF`, *p* < 0,01, *&eta;^2^* = `r Round_and_format(Eta_squared)`  [^13]  
# * p-waarde < 0,05, dus de H~0~ wordt verworpen[^14]
# * Eta squared is `r Round_and_format(Eta_squared)` wat duidt op een gemiddeld tot groot effect 
# 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-5.R -->

# ## Post-hoc toets: Mann-Whitney U toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test.R -->
# Gebruik de [Mann-Whitney U toets](23-Mann-Whitney-U-toets-II-R.html) als post-hoc toets om te bepalen welke groepen significant verschillen. Gebruik de functie `pairwise.wilcox.test()` met als eerste argument de afhankelijke variabele `Beoordelingen_presentatievaardigheden$Beoordeling_numeriek` en als tweede argument de definitie van de groepen `Beoordelingen_presentatievaardigheden$Opleiding`. Pas de *Bonferroni correctie* toe met `p.adjust.method = "bonferroni"`. Naast de p-waarde worden bij de [Mann-Whitney U toets](23-Mann-Whitney-U-toets-II-R.html) de gemiddelde rangnummers en de effectmaat *r* gerapporteerd. Voor meer informatie, zie de toetspagina van de [Mann-Whitney U toets](23-Mann-Whitney-U-toets-II-R.html).
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test.R -->
# <!-- ## OPENBLOK: Mann-Whitney-U-test.R -->
# ``` {r pairwise wilcox test, warning = FALSE}
# pairwise.wilcox.test(Beoordelingen_presentatievaardigheden$Beoordeling_numeriek, Beoordelingen_presentatievaardigheden$Opleiding, p.adjust.method = "bonferroni")
# ```
# <!-- ## /OPENBLOK: Mann-Whitney-U-test.R -->
# 
# <!-- ## CLOSEDBLOK: Mann-Whitney-U-test1.R -->
# ``` {r pairwise wilcox test closed, warning = FALSE, echo = FALSE}
# posthoc <- pairwise.wilcox.test(Beoordelingen_presentatievaardigheden$Beoordeling_numeriek, Beoordelingen_presentatievaardigheden$Opleiding, p.adjust.method = "bonferroni")$p.value
# 
# N_EC <- sum(Beoordelingen_presentatievaardigheden$Opleiding == "Economics")
# N_FI <- sum(Beoordelingen_presentatievaardigheden$Opleiding == "Finance")
# N_EN <- sum(Beoordelingen_presentatievaardigheden$Opleiding == "Entrepeneurship")
# N_MA <- sum(Beoordelingen_presentatievaardigheden$Opleiding == "Marketing")
# 
# ```
# <!-- ## /CLOSEDBLOK: Mann-Whitney-U-test1.R -->
# 
# De [Mann-Whitney U toets](23-Mann-Whitney-U-toets-II-R.html) gebruikt het gemiddelde rangnummer van twee ongepaarde groepen om de significantie van de toets te bepalen. Met behulp van het gemiddelde rangnummer kan bepaald worden welke groep hogere rangnummers heeft wat een benadering is voor het verschil tussen twee groepen.[^15] In deze casus heeft de opleiding met een hoger rangnummer dus over het algemeen studenten met een hogere beoordeling. Bereken en rapporteer daarom het gemiddelde rangnummer. In de onderstaande code worden de gemiddelde rangnummers voor alle post-hoc toetsen berekend. De resultaten zijn te zien in Tabel 1.
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-test2.R -->

# In[ ]:


# Maak een functie om het gemiddelde rangnummer te berekenen voor een vergelijking van twee groepen
Gemiddeld_rangnummer <- function(Opleiding_1, Opleiding_2){
  
  # Bind alle observaties in een variabele
  Beoordelingen <- c(Opleiding_1, Opleiding_2)
  
  # Maak een variabele die aangeeft in welke groep de observatie zit
  Groepsindicator <- c(rep(1, length(Opleiding_1)), rep(2, length(Opleiding_2)))
  
  # Bereken de rangnummers van alle observaties
  Rangschikkingen <- rank(Beoordelingen)
  
  # Bereken het gemiddelde rangnummer voor beide opleidingen
  Gemiddeld_rangnummer_Opleiding_1 <- mean(Rangschikkingen[Groepsindicator == 1])
  Gemiddeld_rangnummer_Opleiding_2 <- mean(Rangschikkingen[Groepsindicator == 2])
  
  # Retourneer beide gemiddelde rangnummers
  return(list(Groep_1 = Gemiddeld_rangnummer_Opleiding_1, Groep_2 = Gemiddeld_rangnummer_Opleiding_2))
}


# Definieer variabelen die observaties bevatten voor de verschillende opleidingen
Beoordeling_Economics <- Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Opleiding == "Economics"]

Beoordeling_Finance <- Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Opleiding == "Finance"]

Beoordeling_Entrepeneurship <- Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Opleiding == "Entrepeneurship"]

Beoordeling_Marketing <- Beoordelingen_presentatievaardigheden$Beoordeling_numeriek[Beoordelingen_presentatievaardigheden$Opleiding == "Marketing"]

# Bereken de gemiddelde rangnummers voor elke vergelijking
Gem_EC_FI <- Gemiddeld_rangnummer(Beoordeling_Economics, 
                                  Beoordeling_Finance)

Gem_EC_EN <- Gemiddeld_rangnummer(Beoordeling_Economics, 
                                  Beoordeling_Entrepeneurship)

Gem_EC_MA <- Gemiddeld_rangnummer(Beoordeling_Economics, 
                                  Beoordeling_Marketing)

Gem_FI_EN <- Gemiddeld_rangnummer(Beoordeling_Finance, 
                                  Beoordeling_Entrepeneurship)

Gem_FI_MA <- Gemiddeld_rangnummer(Beoordeling_Finance, 
                                  Beoordeling_Marketing)

Gem_EN_MA <- Gemiddeld_rangnummer(Beoordeling_Entrepeneurship, 
                                  Beoordeling_Marketing)


# <!-- ## /OPENBLOK: Mann-Whitney-U-test2.R -->
# 
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test3.R -->
# | Vergelijking | p-waarde     | Gemiddeld rangnummer (links)  | Gemiddeld rangnummer (rechts)     |
# | -------------  | ----------  | ---------- | -------- |
# | EC vs. FI    | 1,00 `r #Round_and_format(posthoc[1,1])` |  `r Round_and_format(Gem_EC_FI[[1]])` | `r Round_and_format(Gem_EC_FI[[2]])` |
# | EC vs. EN    | 0,23 `r #Round_and_format(posthoc[2,1])` |  `r Round_and_format(Gem_EC_EN[[1]])` | `r Round_and_format(Gem_EC_EN[[2]])` |
# | EC vs. MA    | 0,05 `r #Round_and_format(posthoc[3,1])` |  `r Round_and_format(Gem_EC_MA[[1]])` | `r Round_and_format(Gem_EC_MA[[2]])` |
# | FI vs. EN    | 0,03 `r #Round_and_format(posthoc[2,2])` |  `r Round_and_format(Gem_FI_EN[[1]])` | `r Round_and_format(Gem_FI_EN[[2]])` |
# | FI vs. MA    | 0,01 `r #Round_and_format(posthoc[3,2])` |  `r Round_and_format(Gem_FI_MA[[1]])` | `r Round_and_format(Gem_FI_MA[[2]])` |
# | EN vs. MA    | 1,00 `r #Round_and_format(posthoc[3,3])` |  `r Round_and_format(Gem_EN_MA[[1]])` | `r Round_and_format(Gem_EN_MA[[2]])` |
# *Tabel 1. Resultaten post-hoc toetsen voor vergelijking Economics (EC), Finance (FI), Entrepeneurship (EN) en Marketing (MA).*
# 
# Er zijn twee significante verschillen bij de post-hoc toetsen te vinden. Zo is er een significant verschil (*p* = 0,03) tussen Finance (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_EN[[1]])`,  *n* = `r N_FI`) en Entrepeneurship (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_EN[[2]])`,  *n* = `r N_EN`), waarbij het gemiddeld rangnummer hoger is voor Entrepeneurship. Daarnaast is er een significant verschil (*p* = 0,01) tussen Finance (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_MA[[1]])`,  *n* = `r N_FI`) en Marketing (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_MA[[2]])`,  *n* = `r N_MA`), waarbij het gemiddeld rangnummer hoger is voor Marketing.
# 
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test3.R -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Kruskal Wallis toets* is uitgevoerd om te toetsen of er verschillen zijn tussen de studenten van de opleidingen Economics, Finance, Entrepeneurship en Marketing wat betreft hun beoordelingen bij het vak Presentatievaardigheden. Uit de resultaten kan afgelezen worden dat er een significant verschil is tussen de verdelingen van de beoordelingen van de presentatievaardigheden voor de verschillende vooropleidingen, *H* = `r vK_Chi2`, *df* = `r vK_DF` ,*p* < 0,01, *&eta;^2^* = `r Round_and_format(Eta_squared)`. De resultaten ondersteunen de conclusie dat er een verschil is tussen de beoordelingen van de presentatievaardigheden voor de vier opleidingen.
# 
# De [Mann-Whitney U toets](23-Mann-Whitney-U-toets-II-R.html) is uitgevoerd als post-hoc toets om te onderzoeken welke opleidingen van elkaar verschillen qua beoordelingen van de presentatievaardigheden van studenten.  De *Bonferroni correctie* is gebruikt om de Type I fout te voorkomen die gepaard gaat met het veelvuldig toetsen. Er is een significant verschil (*p* = 0,03) gevonden tussen de opleidingen  Finance (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_EN[[1]])`,  *n* = `r N_FI`) en Entrepeneurship (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_EN[[2]])`,  *n* = `r N_EN`), waarbij het gemiddeld rangnummer hoger is voor Entrepeneurship. Daarnaast is er een significant verschil (*p* = 0,01) tussen Finance (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_MA[[1]])`,  *n* = `r N_FI`) en Marketing (Gemiddeld rangnummer = `r Round_and_format(Gem_FI_MA[[2]])`,  *n* = `r N_MA`), waarbij het gemiddeld rangnummer hoger is voor Marketing. De overige vergelijkingen tussen opleidingen leidden niet tot een significant verschil. Een overzicht van de resultaten van de post-hoc toetsen is te vinden in Tabel 1. Al met al lijkt er een verschil te zijn tussen de beoordelingen van de presentatievaardigheden van studenten afkomstig van de opleidingen Economics, Finance, Entrepeneurship en Marketing, waarbij de studenten afkomstig van de opleidingen Entrepeneurship en Marketing hogere beoordelingen lijken te behalen dan de studenten van de opleidingen Finance.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: De toets rangschikt de datapunten van laag naar hoog en geeft elke datapunt een rangnummer. Vervolgens wordt per groep het gemiddelde berekend van de rangnummers. Deze gemiddelden wordt met elkaar vergeleken. Voor meer informatie lees: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^2]: Van Geloven, N. (21 maart 2018). *Kruskal Wallis*. [Wiki Statistiek Academisch Medisch Centrum](https://wikistatistiek.amc.nl/index.php/Kruskal_Wallis). 
# [^3]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^9]: Universiteit van Amsterdam (7 juli 2014). *Kruskal-Wallis Test*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Kruskal-Wallis_Test).
# [^10]: De effectmaat *&eta;^2^* wordt voor de *Kruskal-Wallis toets* berekend door de *&chi;^2^*-waarde te delen door het totaal aantal observaties minus één, i.e. $\frac{\chi^2}{N-1} $.
# [^11]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^13]: De test-statistiek *H* volgt bij benadering de chi-kwadraat verdeling. Onder deze hypothese is *H* chi-kwadraat, vandaar dat dit in de output uitgedrukt wordt in chi-kwadraat.
# [^14]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met Type I en Type II fouten. 
# [^15]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^16]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^17]:  Laerd statistics (2018). *Kruskal-Wallis H Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/kruskal-wallis-h-test-using-spss-statistics.php.
# [^18]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# 
