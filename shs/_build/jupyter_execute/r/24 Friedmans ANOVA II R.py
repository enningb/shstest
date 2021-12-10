#!/usr/bin/env python
# coding: utf-8
---
title: "Friedman's ANOVA"
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


source(paste0(here::here(),"/01. Includes/data/24.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# Gebruik *Friedman's ANOVA* om te toetsen of twee of meer gepaarde groepen van elkaar verschillen op een ordinale[^16] variabele.[^1] Als de variabele beter als nominaal[^18] beschouwd kan worden, is de [multilevel multinomiale logistische regressie](20-Multilevel-multinomiale-logistische-regressie-R.html) een alternatief. Bij deze toets wordt echter geen rekening gehouden met de ordening van de categorieën van de ordinale variabele: de variabele wordt behandeld als een nominale variabele.
# 
# # Onderwijscasus
# <div id="casus">
# 
# De opleidingsdirecteur van de bachelor Geschiedenis van een universiteit merkt dat er tijdens het eerste studiejaar veel studenten zijn die niet alle vakken voldoende afsluiten. Zij wil uitvinden in welke onderwijsperiode dit vooral plaatsvindt om te onderzoeken waardoor de studievertraging veroorzaakt wordt. Op deze universiteit bestaat het eerste jaar uit vier onderwijsperiodes met daarin drie vakken. De opleidingsdirecteur vraagt studieresultaten op van eerstejaars studenten in het vorige collegejaar. Met deze resultaten wil zij onderzoeken of er verschillen zijn tussen de vier onderwijsperiodes wat betreft het aantal vakken dat studenten voldoende afsluiten.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is.
# 
# *H~0~*: Er zijn geen verschillen tussen (de gemiddelde rangnummers van) het aantal voldoendes in onderwijsperiode 1, 2, 3 en 4 voor studenten van de bachelor Geschiedenis.
# 
# *H~A~*: Er zijn wel verschillen tussen (de gemiddelde rangnummers van) het aantal voldoendes in onderwijsperiode 1, 2, 3 en 4 voor studenten van de bachelor Geschiedenis.
# 
# </div>
# 
# # Assumpties
# 
# Het meetniveau van de afhankelijke variabele is ordinaal[^16] of continu.[^1] In deze toetspagina staat een casus met een ordinale afhankelijke variabele centraal; een casus met een continue afhankelijke variabele met bijbehorende uitwerking is te vinden in de [Friedman's ANOVA I](9- Friedmans-ANOVA-I-R.html).
# 
# Om *Friedman's ANOVA* uit te voeren met een ordinale afhankelijke variabele, moet deze variabele in sommige gevallen omgezet worden in getallen. Als een variabele bijvoorbeeld vier categorieën bevat, worden ze genummerd van 1 tot en met 4 op basis van de ordening van de variabele. Een voorbeeld hiervan is de afhankelijke variabele Beoordeling die de categorieën onvoldoende, voldoende, goed en uitstekend bevat. De categorieën onvoldoende, voldoende, goed en uitstekend worden dan omgezet in respectievelijk 1, 2, 3 en 4. Bij de [multilevel multinomiale logistische regressie](20-Multilevel-multinomiale-logistische-regressie-R.html) wordt dit niet gedaan, maar wordt de ordinale afhankelijke variabele als nominaal[^18] beschouwd. 
# 
# *Friedman's ANOVA* maakt voor elke observatie-eenheid een rangschikking van alle observaties. Vervolgens wordt het gemiddelde rangnummer per groep berekend en vergeleken tussen de groepen. In de huidige casus wordt er dus voor elke student een rangschikking gemaakt van het aantal voldoendes in onderwijsperiode 1, 2, 3 en 4 en wordt het gemiddelde rangnummer berekend voor elk van de vier onderwijsperioden. Het verschil tussen de gemiddelde rangnummers van de groepen bepaalt de significantie van de toets.[^1]
# 
# # Post-hoc toets 
# *Friedman's ANOVA* toetst of er een verschil is tussen de groepen op gebied van de afhankelijke variabele. De post-hoc toets wordt daarna gebruikt om te toetsen tussen welke specifieke groepen er een significant verschil is. Gebruik de [Wilcoxon signed rank toets](22-Wilcoxon-signed-rank-toets-II-R.html) als post-hoc toets.
# 
# Gebruik een correctie voor de p-waarden, omdat er meerdere toetsen tegelijkertijd worden gebruikt. Meerdere toetsen tegelijkertijd uitvoeren verhoogt de kans dat een van de nulhypotheses onterecht wordt verworpen en er bij toeval een verband wordt ontdekt dat er niet is (type I fout). In deze toetspagina wordt de *Bonferroni correctie* gebruikt. Deze correctie past de p-waarde aan door de p-waarde te vermenigvuldigen met het aantal uitgevoerde toetsen en verlaagt hiermee de kans op een type I fout. Een andere uitleg hiervan is dat het significantieniveau gedeeld wordt door het aantal toetsen wat leidt tot een lager significantieniveau en dus een strengere toets. Er zijn ook andere opties voor een correctie op de p-waarden.[^5]
# 
# # Effectmaat
# De p-waarde geeft aan of het verschil tussen groepen significant is. De grootte van het verschil of effect is echter ook relevant. Een effectmaat is een gestandaardiseerde maat die de grootte van een effect weergeeft, zodat effecten van verschillende onderzoeken met elkaar vergeleken kunnen worden.[^5] Voor *Friedman's ANOVA* wordt de effectmaat *Kendall's W* vaak gebruikt.[^6]<sup>, </sup>[^7]<sup>, </sup>[^8] Een indicatie om *Kendall's W* te interpreteren is: rond 0,1 is het een klein effect, rond 0,3 is het een gemiddeld effect en rond 0,5 is het een groot effect.[^6]
# 
# # Uitvoering
# <!-- ## TEKSTBLOK: Dataset-inladen.R-->
# Er is een dataset `Voldoendes_Geschiedenis` ingeladen met daarin per student per periode het aantal voldoendes in het eerste jaar van de studenten van de bachelor Geschiedenis.
# <!-- ## /TEKSTBLOK: Dataset-inladen.R-->
# 
# ## De data bekijken
# <!-- ## TEKSTBLOK: Data-bekijken.R -->
# Gebruik `head()` en `tail()` om de structuur van de data te bekijken.
# <!-- ## /TEKSTBLOK: Data-bekijken.R -->
# <!-- ## OPENBLOK: Data-bekijken.R -->

# In[ ]:


## Eerste 6 observaties
head(Voldoendes_Geschiedenis)

## Laatste 6 observaties
tail(Voldoendes_Geschiedenis)


# <!-- ## /OPENBLOK: Data-bekijken.R -->
# 
# <!-- ## TEKSTBLOK: Data-kruistabel1.R -->
# Een kruistabel geeft het aantal observaties weer voor de combinaties van de categorieën van de variabelen `Periode` en `Voldoendes`. In feite laat dit zien hoeveel studenten 0, 1, 2 of 3 voldoendes hebben gehaald in elke onderwijsperiode. Maak de kruistabel met de functie `table()` met als argumenten de variabele `Voldoendes_Geschiedenis$Periode` en de variabele `Voldoendes_Geschiedenis$Voldoendes`.
# <!-- ## /TEKSTBLOK: Data-kruistabel1.R -->
# 
# <!-- ## OPENBLOK: Data-kruistabel2.R -->

# In[ ]:


## Maak een kruistabel
Voldoendes_kruistabel <- table(Voldoendes_Geschiedenis$Periode,
                                  Voldoendes_Geschiedenis$Voldoendes,
                               dnn = c("Periode","Aantal voldoendes"))

## Print de kruistabel 
print(Voldoendes_kruistabel)

## Print een tabel met proporties; het tweede argument `1` zorgt ervoor dat de 
## proporties per rij berekend worden
prop.table(Voldoendes_kruistabel, 1)


# <!-- ## /OPENBLOK: Data-kruistabel2.R -->
# 
# De kruistabel en bijbehorende kruistabel met proporties geven informatie over de verdeling van de beoordelingen van studenten. In periode 1, 2 en 4 haalden de meeste studenten 3 voldoendes, maar in periode 3 haalden de meeste studenten 2 voldoendes. 
# 
# ## De data visualiseren
# Maak een staafdiagram om de verdeling van het aantal voldoendes voor alle onderwijsperioden visueel weer te geven.
# 
# <!-- ## OPENBLOK: Histogram1.R -->

# In[ ]:


## Staafdiagram met ggplot2
library(ggplot2)

ggplot(Voldoendes_Geschiedenis,
  aes(Voldoendes)) +
  geom_bar(color = "grey30",
                 fill = "#0089CF") +
  facet_wrap(~ Periode) +
  ylab("Frequentie") +
  labs(title = "Aantal voldoendes per periode")


# <!-- ## /OPENBLOK: Histogram1.R -->
# *Figuur 1. Staafdiagram met de frequenties van het aantal voldoendes voor onderwijsperiode 1, 2, 3 en 4.*
# 
# Het staafdiagram (Figuur 1) laat zien dat de meeste studenten 3 voldoendes halen in periode 1, 2 en 4 en de meeste studenten 2 voldoendes halen in periode 3. Ook valt op dat in periode 2 en 4 verreweg de meeste studenten 3 voldoendes halen, maar dat dat niet zo is in periode 1.
# 
# ## Friedman's ANOVA
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-1.R -->
# Voer de *Friedman's ANOVA* uit om te onderzoeken of er verschillen zijn tussen het aantal voldoendes in de vier onderwijsperioden in het eerste jaar van studenten van de bachelor Geschiedenis. Gebruik de functie `friedman.test()` met als eerste argument de formule `Voldoendes ~ Periode | Studentnummer` met daarin links van de tilde de afhankelijke variabele `Voldoendes` en rechts van de tilde de onafhankelijke variabele `Periode` en na het sluisteken de variabele `Studentnummer` die de deelnemers[^19] aangeeft. Het tweede argument is de dataset `Voldoendes_Geschiedenis`. 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-1.R -->
# 
# <!-- ## OPENBLOK: Kruskal-Wallis-test-2.R -->

# In[ ]:


friedman.test(Voldoendes ~ Periode | Studentnummer,
              Voldoendes_Geschiedenis)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-2.R -->
# 
# Bereken de effectmaat *Kendall's W* vervolgens op basis van de *&chi;^2^*-waarde van de *Friedman's ANOVA*.
# <!-- ## OPENBLOK: Kruskal-Wallis-test-3.R -->

# In[ ]:


# Sla de Chi-kwadraat waarde op
Chi2 <- friedman.test(Voldoendes ~ Periode | Studentnummer,
                      Voldoendes_Geschiedenis)$statistic

# Sla het aantal deelnemers op
N <- length(unique(Voldoendes_Geschiedenis$Studentnummer))  

# Sla het aantal groepen op
k <- length(unique(Voldoendes_Geschiedenis$Periode))

# Bereken de effectmaat
W <- Chi2 / (N * (k - 1))

# Print de effectmaat
paste("De effectmaat is", W)


# <!-- ## /OPENBLOK: Kruskal-Wallis-test-3.R -->

# <!-- ## CLOSEDBLOK: Kruskal-Wallis-test-4.R -->

# In[ ]:


obj <- friedman.test(Voldoendes ~ Periode | Studentnummer,
              Voldoendes_Geschiedenis)
vChi2 <- Round_and_format(obj$statistic)
vdf <- Round_and_format(obj$parameter)


# <!-- ## /CLOSEDBLOK: Kruskal-Wallis-test-4.R -->
# <!-- ## TEKSTBLOK: Kruskal-Wallis-test-5.R -->
# 
# * *&chi;^2^~`vdf`~* = `r vChi2`, *p* < 0,0001, *W* = `r Round_and_format(W)`
# * De p-waarde is kleiner dan 0,05, dus de H~0~ wordt verworpen.[^14]
# * Er is een significant verschil tussen het aantal voldoendes in de vier onderwijsperioden; het effect van de onderwijsperiode op het aantal voldoendes is klein
# 
# <!-- ## /TEKSTBLOK: Kruskal-Wallis-test-5.R -->

# ## Post-hoc toets: Wilcoxon signed rank toets
# <!-- ## TEKSTBLOK: Mann-Whitney-U-test.R -->
# Gebruik de [Wilcoxon signed rank toets](22-Wilcoxon-signed-rank-toets-II-R.html) als post-hoc toets om te bepalen welke groepen significant verschillen. Gebruik de functie `pairwise.wilcox.test()` met als eerste argument de afhankelijke variabele `Voldoendes_Geschiedenis$Voldoendes`, als tweede argument de onafhankelijke variabele `Voldoendes_Geschiedenis$Periode`, als derde argument `paired = TRUE` om aan te geven dat er gepaarde groepen zijn en als vierde argument `p.adjust.method = "bonferroni"` om aan te geven dat de *Bonferroni correctie* toegepast moet worden. Naast de p-waarde worden bij de [Wilcoxon signed rank toets](22-Wilcoxon-signed-rank-toets-II-R.html) de som van de rangnummers gerapporteerd. Voor meer informatie, zie de toetspagina van de [Wilcoxon signed rank toets](22-Wilcoxon-signed-rank-toets-II-R.html).
# <!-- ## /TEKSTBLOK: Mann-Whitney-U-test.R -->
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-test.R -->
# ``` {r pairwise wilcox test, warning = FALSE}
# pairwise.wilcox.test(Voldoendes_Geschiedenis$Voldoendes, 
#                      Voldoendes_Geschiedenis$Periode, 
#                      paired = TRUE,
#                      p.adjust.method = "bonferroni")
# ```
# <!-- ## /OPENBLOK: Mann-Whitney-U-test.R -->
# 
# <!-- ## CLOSEDBLOK: Mann-Whitney-U-test1.R -->
# ``` {r pairwise wilcox test closed, warning = FALSE, echo = FALSE}
# posthoc <- pairwise.wilcox.test(Voldoendes_Geschiedenis$Voldoendes, 
#                      Voldoendes_Geschiedenis$Periode, 
#                      paired = TRUE,
#                      p.adjust.method = "bonferroni")$p.value
# 
# ```
# <!-- ## /CLOSEDBLOK: Mann-Whitney-U-test1.R -->
# 
# De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) gebruikt de som van positieve en negatieve rangnummers van de verschilscores om de significantie van de toets te bepalen. Deze sommen beschrijven het verschil tussen twee gepaarde groepen waarbij de groep met een hogere som van rangnummers ook hogere waarden op de afhankelijke variabele heeft. In deze casus heeft de periode met hogere rangnummers een hoger aantal voldoendes. Bereken de som van de positieve en negatieve rangnummers voor alle vergelijkingen. In de onderstaande code worden de gemiddelde rangnummers voor alle post-hoc toetsen berekend. De resultaten zijn te zien in Tabel 1.
# 
# <!-- ## OPENBLOK: Mann-Whitney-U-test2.R -->

# In[ ]:


# Definieer een functie die de sommen van de positieve en negatieve rangnummers berekent
Sommen_rangnummers <- function(Groep_1, Groep_2){
  
  # Bereken de verschilscores
  Verschilscores <- Groep_1 - Groep_2
  
  # Rangschik de absolute waarden van de verschilscores
  Rangnummers <- rank(abs(Verschilscores))

  # Maak een vector met daarin de tekens (plus of min) van de verschilscores
  Tekens <- sign(Verschilscores)

  # Bereken de som van de positieve rangnummers
  Som_positief <- sum(Rangnummers[Tekens == 1])

  # Bereken de som van de negatieve rangnummers
  Som_negatief <- sum(Rangnummers[Tekens == -1])
  
  # Retourneer de som van de positieve en negatieve rangnummers
  return(list(Positief = Som_positief, Negatief = Som_negatief))
}

# Definieer de variabelen die het aantal voldoendes bevatten per periode
Voldoendes_Periode_1 <- Voldoendes_Geschiedenis$Voldoendes[Voldoendes_Geschiedenis$Periode == 1]
Voldoendes_Periode_2 <- Voldoendes_Geschiedenis$Voldoendes[Voldoendes_Geschiedenis$Periode == 2]
Voldoendes_Periode_3 <- Voldoendes_Geschiedenis$Voldoendes[Voldoendes_Geschiedenis$Periode == 3]
Voldoendes_Periode_4 <- Voldoendes_Geschiedenis$Voldoendes[Voldoendes_Geschiedenis$Periode == 4]

# Bereken de positieve en negatieve som van rangnummers

## De som van rangnummers per vergelijking
(Som_1_2 <- Sommen_rangnummers(Voldoendes_Periode_1, Voldoendes_Periode_2))
Som_1_3 <- Sommen_rangnummers(Voldoendes_Periode_1, Voldoendes_Periode_3)
Som_1_4 <- Sommen_rangnummers(Voldoendes_Periode_1, Voldoendes_Periode_4)
Som_2_3 <- Sommen_rangnummers(Voldoendes_Periode_2, Voldoendes_Periode_3)
Som_2_4 <- Sommen_rangnummers(Voldoendes_Periode_2, Voldoendes_Periode_4)
Som_3_4 <- Sommen_rangnummers(Voldoendes_Periode_3, Voldoendes_Periode_4)


# <!-- ## /OPENBLOK: Mann-Whitney-U-test2.R -->
# 
# <!-- ## TEKSTBLOK: posthoc6.R -->
# | Vergelijking | p-waarde     |   Som positieve rangnummers        | Som negatieve rangnummers     |
# | -------------  | ----------  | --------- | ---------- | -------- |
# | Periode 1 vs. 2    | 0,496`r #Round_and_format(posthoc[2,1])` |`r Round_and_format(Som_1_2[[1]])` | `r Round_and_format(Som_1_2[[2]])` |
# | Periode 1 vs. 3    | 0,814`r #Round_and_format(posthoc[3,3])` | `r Round_and_format(Som_1_3[[1]])` | `r Round_and_format(Som_1_3[[2]])` |
# | Periode 1 vs. 4    | < 0,001 `r #Round_and_format(posthoc[2,2])` | `r Round_and_format(Som_1_4[[1]])` | `r Round_and_format(Som_1_4[[2]])` |
# | Periode 2 vs. 3    | 0,031`r #Round_and_format(posthoc[3,1])` |  `r Round_and_format(Som_2_3[[1]])` | `r Round_and_format(Som_2_3[[2]])` |
# | Periode 2 vs. 4    | 0,259`r #Round_and_format(posthoc[1,1])` | `r Round_and_format(Som_2_4[[1]])` | `r Round_and_format(Som_2_4[[2]])` |
# | Periode 3 vs. 4    | < 0,0001 `r #Round_and_format(posthoc[3,2])` | `r Round_and_format(Som_3_4[[1]])` | `r Round_and_format(Som_3_4[[2]])` |
# 
# *Tabel 1. Resultaten post-hoc toetsen voor de vergelijking van het aantal voldoendes voor periode 1, 2, 3 en 4.*
# <!-- ## /TEKSTBLOK: posthoc6.R -->

# <!-- ## TEKSTBLOK: posthoc7.R -->
# De significante verschillen op de post-hoc toetsen zijn:
# 
# * Het aantal voldoendes in periode 1 (Som = `r Round_and_format(Som_1_4[[1]])`) verschilt significant van het aantal voldoendes in periode 4 (Som = `r Round_and_format(Som_1_4[[2]])`), *p* < 0,001. De hogere som van rangnummers in periode 4 duidt erop dat het aantal voldoendes hoger is in periode 4 ten opzichte van periode 1.
# * Het aantal voldoendes in periode 2 (Som = `r Round_and_format(Som_2_3[[1]])`) verschilt significant van het aantal voldoendes in periode 3 (Som = `r Round_and_format(Som_2_3[[2]])`), *p* = 0,031. De hogere som van rangnummers in periode 2 duidt erop dat het aantal voldoendes hoger is in periode 2 ten opzichte van periode 3.
# * Het aantal voldoendes in periode 3 (Som = `r Round_and_format(Som_3_4[[1]])`) verschilt significant van het aantal voldoendes in periode 4 (Som = `r Round_and_format(Som_3_4[[2]])`), *p* < 0,0001. De hogere som van rangnummers in periode 4 duidt erop dat het aantal voldoendes hoger is in periode 4 ten opzichte van periode 3.
# 
# <!-- ## /TEKSTBLOK: posthoc7.R -->

# # Rapportage
# <!-- ## TEKSTBLOK: Rapportage.R -->
# De *Friedman's ANOVA* is uitgevoerd om te toetsen of er verschillen zijn tussen het aantal voldoendes in de vier onderwijsperioden van het eerste jaar van de bachelor Geschiedenis. Uit de resultaten kan afgelezen worden dat er een significant verschil is tussen de onderwijsperioden wat betreft het aantal voldoendes, *&chi;^2^~`vdf`~* = `r vChi2`, *p* < 0,0001, *W* = `r Round_and_format(W)`.
# 
# De [Wilcoxon signed rank toets](07-Wilcoxon-signed-rank-toets-R.html) is uitgevoerd als post-hoc toets om te onderzoeken tussen welke perioden er verschillen zijn in het aantal voldoendes dat studenten behalen. De *Bonferroni correctie* is gebruikt om de Type I fout te voorkomen die gepaard gaat met het veelvuldig toetsen. Er is een significant verschil (*p* < 0,001) gevonden tussen periode 1 (Som = `r Round_and_format(Som_1_4[[1]])`) en periode 4 (Som = `r Round_and_format(Som_1_4[[2]])`) waarbij er meer voldoendes zijn gehaald in periode 4. Daarnaast is er een significant verschil (*p* = 0,031) gevonden tussen periode 2 (Som = `r Round_and_format(Som_2_3[[1]])`) en periode 3 (Som = `r Round_and_format(Som_2_3[[2]])`) waarbij er meer voldoendes zijn gehaald in periode 2. Ook is er een significant verschil (*p* < 0,0001) gevonden tussen periode 3 (Som = `r Round_and_format(Som_3_4[[1]])`) en periode 4 (Som = `r Round_and_format(Som_3_4[[2]])`) waarbij er meer voldoendes zijn gehaald in periode 4. De overige vergelijkingen tussen opleidingen leidden niet tot een significant verschil. De resultaten suggereren dat periode 2 en 4 periodes zijn waarin studenten een groot aantal voldoendes halen voor de drie vakken die ze volgen. In periode 1 en 3 lijkt het aantal voldoendes per student wat lager te zijn. Het is daarom handig om in te zoomen op deze onderwijsperioden om de oorzaak van studievertraging te vinden.
# <!-- ## /TEKSTBLOK: Rapportage.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]:  Laerd statistics (2018). *Friedman Test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/friedman-test-using-spss-statistics.php.
# [^5]: Field, A., Miles, J., & Field, Z. (2012). *Discovering statistics using R*. London: Sage publications.
# [^6]: University of Sheffield. *Friedman test in SPSS*. [Mathematics and Statistics Help (MASH)](https://www.sheffield.ac.uk/polopoly_fs/1.714575!/file/stcp-marshall-FriedmanS.pdf). Bezocht op 13 maart 2020.
# [^7]: *Kendall's W* wordt berekend door de teststatistiek van *Friedman's ANOVA* (dit is de *&chi;^2^*) te delen door het aantal deelnemers *N* en het aantal groepen *k* minus één, i.e. $W = \frac{\chi^2}{N(k-1)}$.
# [^8]: Kassambara, A. (2020). *rstatix: Pipe-Friendly Framework for Basic Statistical Tests*. [R package version 0.4.0.](https://CRAN.R-project.org/package=rstatix).
# [^10]: De effectmaat *&eta;^2^* wordt voor de *Kruskal-Wallis toets* berekend door de *&chi;^2^*-waarde te delen door het totaal aantal observaties minus één, i.e. $\frac{\chi^2}{N-1} $.
# [^11]: Allen, P. & Bennett, K. (2012). *SPSS A practical Guide version 20.0*. Cengage Learning Australia Pty Limited.
# [^14]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met Type I en Type II fouten. 
# [^15]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage.
# [^16]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^18]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
