#!/usr/bin/env python
# coding: utf-8
---
title: "Multinomiale logistische regressie"
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


source(paste0(here::here(),"/01. Includes/data/47.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik *multinomiale logistische regressie* om te toetsen of een nominale[^14] afhankelijke variabele met meer dan twee categorieën voorspeld kan worden met twee of meer onafhankelijke variabelen (predictors) en om te toetsen of er een relatie is tussen een predictor en de afhankelijke variabele in aanwezigheid van andere predictors.[^1]

# # Onderwijscasus
# <div id = "casus">
# 
# Na afronding van de opleiding Fysiotherapie is het mogelijk om een hbo-master te volgen, een wo-master te volgen en direct aan het werk te gaan. De opleidingsdirecteur wil graag inventariseren welke karakteristieken van studenten bepalend zijn voor het vervolg na de studie om de voorlichtingsactiviteiten binnen de studie beter op de behoeften van studenten af te kunnen stemmen. Zij vraagt daarom te onderzoeken of het gemiddelde cijfer en het wel of niet nominaal afstuderen gerelateerd zijn aan de keuze om na de opleiding een hbo-master te volgen, een wo-master te volgen of direct aan het werk te gaan.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *multinomiale logistische regressie* wordt er een hypothese opgesteld voor het complete model en hypotheses voor de individuele predictors.
# 
# Hypotheses regressiemodel:
# 
# *H~0~*: Geen enkele predictor van de predictors Gemiddeld_cijfer en Nominaal is gerelateerd aan de afhankelijke variabele vervolg na opleiding ($\beta_{1,1} = \beta_{1,2} = \beta_{2,1} = \beta_{2,2} = 0$).
# 
# *H~A~*: Ten minste een van de predictors Gemiddeld_cijfer en Nominaal  is gerelateerd aan de afhankelijke variabele vervolg na opleiding (Ten minste één $\beta_{i,j} \neq 0, i = 1, 2, j = 1, 2$).
# 
# Hypotheses individuele predictors (met als voorbeeld de predictor Gemiddeld_cijfer voor het volgen van een hbo master versus direct aan het werk gaan):
# 
# *H~0~*: De predictor Gemiddeld_cijfer heeft geen voorspellende waarde voor de kans op het volgen van een hbo master na de opleiding ten opzichte van direct aan het werk gaan na de opleiding in aanwezigheid van de andere predictor Nominaal ($\beta = 0$).
# 
# *H~A~*: De predictor Gemiddeld_cijfer heeft voorspellende waarde voor de kans op het volgen van een hbo master na de opleiding ten opzichte van direct aan het werk gaan na de opleiding in aanwezigheid van de andere predictor Nominaal ($\beta \neq 0$).
# 
# </div>
# 
# # Multinomiale logistische regressie
# 
# Het doel van *multinomiale logistische regressie* is het voorspellen van een nominale[^14] afhankelijke variabele (met meer dan twee categorieën) op basis van meerdere onafhankelijke variabelen, ook wel predictors genoemd.[^1] Bij [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) wordt het voorspellen van een afhankelijke variabele gedaan met behulp van een regressievergelijking waarin de afhankelijke variabele een lineaire combinatie is van de predictors, i.e. 
# 
# $$ y_i = \beta_0 + \beta_1 * x_{1i} + \beta_2 * x_{2i} + e_i$$
# 
# met $y_i$ als afhankelijke variabele, $\beta_0$ als intercept, $x_{1i}$ en $x_{2i}$ als predictors, $\beta_{1}$ en $\beta_{2}$ als regressiecoefficiënten van predictors, $e_i$ als residu of error en $i$ als indicator van de deelnemer[^19] uit de steekproef. De intercept $\beta_0$ geeft de waarde van de afhankelijke variabele weer als alle predictors gelijk aan nul zijn. De regressiecoefficiënten $\beta_1$ en $\beta_2$ geven de relatie tussen de afhankelijke variabele en de predictor weer. De residu of error $e_i$ is het verschil tussen de geobserveerde waarde van de afhankelijke variabele en de voorspelde waarde op basis van het regressiemodel.[^21] 
# 
# Bij [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) wordt een continue afhankelijke variabele voorspeld op basis van een aantal predictors. Daarnaast is er [logistische regressie](41-Logistische-regressie-R.html) waarbij de afhankelijke variabele binair is. Bij [logistische regressie](41-Logistische-regressie-R.html) wordt de kans op een van beide mogelijkheden van de binaire variabele voorspeld. Als de afhankelijke variabele Uitval in het eerste studiejaar bestaat uit de mogelijkheden Uitval en Geen Uitval, dan kan met [logistische regressie](41-Logistische-regressie-R.html) de kans op het uitvallen van de student voorspeld worden. Voor meer informatie, zie de bijbehorende [toetspagina](41-Logistische-regressie-R.html).
# 
# Ook als de afhankelijke variabele categorisch is en meer dan twee mogelijkheden bevat, is het mogelijk een vorm van regressie uit te voeren. De gebruikte techniek hangt dan echter af van het meetniveau van de afhankelijke variabele. Als het meetniveau ordinaal[^14] is, is [ordinale logistische regressie](53-Ordinale-logistische-regressie-R.html) de juiste techniek. Een voorbeeld van een ordinale afhankelijke variabele is de beoordeling van een opdracht met als mogelijkheden onvoldoende, voldoende en goed. Als het meetniveau nominaal[^14] is, dan is *multinomiale logistische regressie* de juiste techniek. Bij *multinomiale logistische regressie* wordt een nominale afhankelijke variabele met meer dan twee mogelijkheden voorspeld op basis van een aantal predictors. Om dit te doen, moet er een referentiecategorie gekozen worden. Voor elke mogelijkheid van de nominale afhankelijke variabele wordt dan de kans voorspeld ten opzichte van de referentiecategorie. In de huidige casus werkt dit als volgt bij een keuze voor direct aan het werk gaan na de opleiding als referentiecategorie. Met het regressiemodel wordt zowel de kans op het volgen van een hbo master ten opzichte van direct aan het werk gaan voorspeld als de kans op het volgen van een wo master ten opzichte van direct aan het werk gaan. In feite wordt er voor beide kansen een aparte regressievergelijking opgesteld met eigen regressiecoëfficiënten. Het regressiemodel van de huidige casus is dus op te schrijven met de volgende twee vergelijkingen
# 
# $$ \log(\frac{P_{i,WO \ master }}{P_{i,werk }})  = \beta_{0,1} + \beta_{1,1} * Nominaal_{i} + \beta_{2,1} * Gemiddeld Cijfer_{i} + e_{i,1}$$
# 
# $$ \log(\frac{P_{i,hbo \ master }}{P_{i,werk }}) = \beta_{0,2} + \beta_{1,2} * Nominaal_{i} + \beta_{2,2} * Gemiddeld Cijfer_{i} + e_{i,2}$$
# 
# waarbij $P_{i,WO \ master }$ de kans op het volgen van een wo master is (en waarbij de andere kansen op vergelijkbare wijze zijn weergegeven),  $\beta_{0,1}$ als intercept van de eerste vergelijking, $Nominaal_{i}$ en $GemiddeldCijfer_{i}$ als predictors, $\beta_{1,1}$ en $\beta_{2,2}$ als regressiecoefficiënten van de predictors van de eerste vergelijking, $e_{i,1}$ als residu of error van de eerste vergelijking en $i$ als indicator van de deelnemer uit de steekproef. Dezelfde notatie geldt ook voor de tweede vergelijking. Bij *multinomiale logistische regressie* is het aantal vergelijkingen gelijk aan het aantal mogelijkheden van de nominale afhankelijke variabele minus één (de referentiecategorie).[^20]
# 
# Bij *multinomiale logistische regressie* wordt eerst getoetst of alle vergelijkingen met de predictors toegevoegd samen voor een betere voorspelling zorgen dan alle vergelijkingen met alleen een intercept. Als dit het geval is, dan worden de individuele predictors getoetst op hun significantie. Het is dus mogelijk dat een predictor in de ene vergelijking wel significant is en in een andere vergelijking niet. Het is ook mogelijk dat een of meerdere vergelijking helemaal geen significante predictors bevatten. De vergelijkingen moeten daarom apart van elkaar geïnterpreteerd worden om de resultaten goed te duiden.
# 
# In onderstaande sectie wordt in meer details aan de hand van een aantal wiskundige formules uitgelegd hoe *multinomiale logistische regressie* werkt. Zonder deze paragraaf te lezen is de toetspagina ook goed te begrijpen. De geïnteresseerde lezer kan hier wat meer begrip op doen over de achtergrond van *multinomiale logistische regressie*.
# 
# ## De achtergrond van multinomiale logistische regressie
# 
# Bij *multinomiale logistische regressie* wordt de kans op een van de mogelijkheden van de nominale afhankelijke variabele ten opzichte van de referentiecategorie voorspeld op basis van de predictors. In zekere zin is het regressiemodel een combinatie van meerdere [logistische regressie](41-Logistische-regressie-R.html)-vergelijkingen, waarbij het aantal vergelijkingen gelijk is aan het aantal categorieën van de nominale afhankelijke variabele minus één (de referentiecategorie). De vergelijkingen voor deze casus zijn al opgesteld in de vorige paragraaf en luiden
# 
# $$ \log(\frac{P_{i,WO \ master }}{P_{i,werk }})  = \beta_{0,1} + \beta_{1,1} * Nominaal_{i} + \beta_{2,1} * Gemiddeld Cijfer_{i} + e_{i,1}$$
# 
# $$ \log(\frac{P_{i,hbo \ master }}{P_{i,werk }}) = \beta_{0,2} + \beta_{1,2} * Nominaal_{i} + \beta_{2,2} * Gemiddeld Cijfer_{i} + e_{i,2}$$
# waarbij $P_{i,WO \ master }$ de kans op het volgen van een wo master is (en waarbij de andere kansen op vergelijkbare wijze zijn weergegeven),  $\beta_{0,1}$ als intercept van de eerste vergelijking, $Nominaal_{i}$ en $GemiddeldCijfer_{i}$ als predictors, $\beta_{1,1}$ en $\beta_{2,2}$ als regressiecoefficiënten van de predictors van de eerste vergelijking, $e_{i,1}$ als residu of error van de eerste vergelijking en $i$ als indicator van de deelnemer uit de steekproef. [^20]
# 
# De regressievergelijking geeft niet direct een voorspelling van de kans op de mogelijkheid van de nominale afhankelijke variabele, maar een voorspelling van de logaritme van de kans op de mogelijkheid gedeeld door de kans op de referentiecategorie. De kans op de mogelijkheid is getransformeerd met behulp van een logit-transformatie. Bij [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) is er een directe lineaire relatie tussen de afhankelijke variabele en de predictors. Bij *multinomiale logistische regressie* is er een lineaire relatie tussen de logit van de mogelijkheid en de predictors. De interesse gaat echter uit naar de kans op een bepaalde mogelijkheid van de nominale afhankelijke variabele en niet naar de logit. Er is dus geen directe lineaire relatie tussen de kans op een mogelijkheid en de predictors. De logit transformatie is als het ware de intermediair die zorgt voor de lineaire relatie en wordt daarom ook wel een link-functie genoemd.
# 
# Op basis van de logits is het wel mogelijk om de kansen op de verschillende mogelijkheden van de nominale afhankelijke variabele uit te rekenen. Voor een algemene *multinomiale logistische regressie* met twee predictoren is de formule voor de mogelijkheden 
# 
# $$ P(Y_i = j) = \pi_{ij} = \frac{\exp( [\beta_{0j} + \beta_{1j} * x_{1i} + \beta_{2j} * x_{2i}])}{1 + \sum_{k \neq j^*} \exp( [\beta_{0k} + \beta_{1k} * x_{1i} + \beta_{2k} * x_{2i}])} $$
# 
# en voor de referentiecategorie
# $$ P(Y_i = j^*) = \pi_{ij^*} = \frac{1}{1 + \sum_{k \neq j^*} \exp( [\beta_{0k} + \beta_{1k} * x_{1i} + \beta_{2k} * x_{2i}])} $$
# 
# waarbij $j$ de categorie/mogelijkheid van de nominale afhankelijke variabele aangeeft, $j^*$ de referentiecategorie aangeeft en $\pi_{ij}$ de kans voor deelnemer $i$ op mogelijkheid $j$ aangeeft.
# 
# Voor de huidige casus is de vergelijking voor de mogelijkheid wo master
# 
# $$  \pi_{i, wo \ master} = \frac{\exp( \beta_{0,1} + \beta_{1,1} * Nom_{i} + \beta_{2,1} * GemCijfer_{i})}{1 + \exp( \beta_{0,1} + \beta_{1,1} * Nom_{i} + \beta_{2,1} * Gem Cijfer_{i}) + \exp(\beta_{0,2} + \beta_{1,2} * Nom_{i} + \beta_{2,2} * GemCijfer_{i})}, $$
# 
# de vergelijking voor de mogelijkheid hbo master
# 
# $$  \pi_{i, hbo \ master} = \frac{\exp( \beta_{0,2} + \beta_{1,2} * Nom_{i} + \beta_{2,2} * GemCijfer_{i})}{1 + \exp( \beta_{0,1} + \beta_{1,1} * Nom_{i} + \beta_{2,1} * Gem Cijfer_{i}) + \exp(\beta_{0,2} + \beta_{1,2} * Nom_{i} + \beta_{2,2} * GemCijfer_{i})} $$
# 
# en de vergelijking voor de referentiecategorie 
# 
# $$  \pi_{i, Werk} = \frac{1}{1 + \exp( \beta_{0,1} + \beta_{1,1} * Nom_{i} + \beta_{2,1} * Gem Cijfer_{i}) + \exp(\beta_{0,2} + \beta_{1,2} * Nom_{i} + \beta_{2,2} * GemCijfer_{i})}. $$
# 
# Merk hierbij op dat de referentiecategorie gekozen wordt door de onderzoeker en dat de vergelijkingen dus veranderen bij de keuze voor een andere referentiecategorie.[^20]
# 
# Op basis van de vergelijkingen van de *multinomiale logistische regressie* wordt er een kans berekend voor alle mogelijkheden van de nominale afhankelijke variabele. Hoewel de techniek van *multinomiale logistische regressie* bedoeld is om de significantie van het model en de individuele regressiecoëfficiënten te toetsen, kunnen deze kansen ook gebruikt worden om een voorspelling of classificatie te maken van de categorie van de nominale afhankelijke variabele waar de student in terecht zal komen. De classificatie kan bijvoorbeeld de categorie met de hoogste voorspelde kans zijn. Op deze manier kan *multinomiale logistische regressie* gebruikt worden om studenten te classificeren.

# ## Maximum likelihood
# 
# Bij *multipele lineaire regressie* worden de regressiecoëfficiënten bepaald door de som van de gekwadrateerde residuën zo klein mogelijk te maken. Deze methode heet *ordinary least squares* (OLS) en zorgt ervoor dat de voorspellingen van het regressiemodel zo dichtbij als mogelijk zitten bij de echte observaties. Voor meer informatie, zie de [toetspagina](28-Multipele-lineaire-regressie-R.html). Bij *multinomiale logistische regressie* wordt ook geprobeerd om de voorspellingen van het regressiemodel zo dichtbij de observaties te krijgen als mogelijk, maar er wordt een andere methode gebruikt. Deze methode heet *maximum likelihood* schatting en heeft als gevolg dat er ook andere statistische toetsen gebruikt worden. Om modellen te vergelijken wordt bij *multinomiale logistische regressie* de *likelihood ratio toets* gebruikt in plaats van de F-toets. Om regressiecoëfficiënten te toetsen, wordt de *Wald toets* gebruikt in plaats van de t-toets.[^2]<sup>,</sup>[^20]

# ## Likelihood ratio toets voor significantie regressiemodel
# 
# Bij *maximum likelihood* schatting laat de likelihood van het model zien hoe dichtbij de voorspellingen van het model bij de observaties zitten. De likelihood is hoger voor een model waarin de voorspellingen dichterbij de observaties zitten. Op basis van de likelihood wordt het gehele regressiemodel statistisch getoetst en kunnen (geneste) modellen onderling vergeleken worden.
# 
# De eerste vraag bij *multinomiale logistische regressie* is of het model betere voorspellingen geeft dan een model zonder predictors. Daarom wordt het voorgestelde model vergeleken met een interceptmodel, een model waarin er geen predictors zijn en dus alleen de intercept gebruikt wordt om voorspellingen te maken. De verwachting is dat het voorgestelde model betere voorspellingen genereert en dus een hogere likelihood heeft. De significantie van dit verschil wordt getoetst met een *likelihood ratio* toets. De getoetste nulhypothese is dat de regressiecoëfficiënten van alle predictors gelijk aan nul zijn, wat wil zeggen dat de predictors niet zorgen voor betere voorspellingen. De getoetste alternatieve hypothese is dat minimaal een van de regressiecoëfficiënten van de predictors niet gelijk aan nul is, wat wil zeggen dat het model betere voorspellingen genereert. Als het verschil tussen beide modellen significant is, kunnen de individuele predictors getoetst worden. Als de toename niet significant is, is de analyse afgelopen en is de conclusie dat het voorgestelde model niet in staat is om de afhankelijke variabele beter te voorspellen dan een model zonder predictors.[^2]<sup>,</sup>[^20]
# 
# De *likelihood ratio* toets kan ook gebruikt worden om verschillende regressiemodellen onderling te vergelijken. Hierbij wordt getoetst of er een verschil is tussen de likelihood (de kwaliteit van het model) van beide modellen. Er kan bijvoorbeeld in eerste instantie een model met twee predictors getoetst worden om vervolgens te toetsen of de voorspellingen van het regressiemodel nog beter worden met twee extra predictors. Het verschil in likelihood tussen het model met twee en vier predictors wordt dan getoetst met een chi-kwadraat toets. Hierbij is de nulhypothese dat de extra toegevoegde predictors een regressiecoëfficiënt van nul hebben en de alternatieve hypothese dat minimaal een van de regressiecoëfficiënten van de extra predictors niet gelijk aan nul is. Een eis voor deze toets is dat beide modellen genest zijn. Bij geneste modellen is het ene model te schrijven als een versie van het andere model na het verwijderen van een aantal predictors. In deze casus zou er een model opgesteld kunnen worden waarin alleen de variabele Nominaal een predictor is van Vervolg en een model waarin de de variabelen Nominaal en Gemiddeld_cijfer predictors zijn van Vervolg. Dit zijn geneste modellen, omdat het eerste model (alleen Nominaal als predictor) een versie is van het tweede model na het verwijderen van de predictors Gemiddeld_cijfer. Het model waarbij de predictors verwijderd zijn, wordt als het ware gereduceerd. Daarom wordt dit het gereduceerde model genoemd. Het model waar de predictors niet verwijderd zijn, wordt het uitgebreide model genoemd. Om modellen met een *likelihood ratio* te vergelijken, moeten ze dus genest zijn. In andere woorden, het verschil tussen beide regressiemodellen moet dus toe te wijzen zijn aan het toevoegen of verwijderen van een of meerdere predictors.[^2]<sup>,</sup>[^20]
# 
# Bij *multinomiale logistische regressie* is de effectmaat gebaseerd op een vergelijking van de likelihood van het voorgestelde model ten opzichte van de likelihood van het interceptmodel. Een veelgebruikte versie hiervan is Nagelkerke's $R^2$ ($R_N^2$) welke waardes aanneemt tussen 0 en 1. Let op dat Nagelkerke's $R^2$ niet geïnterpreteerd kan worden als verklaarde variantie (zoals $R^2$ bij *multipele lineaire regressie*). Er kan dus niet gezegd worden dat een bepaald percentage van de variantie verklaard wordt door het model. Daarom wordt er een algemenere term gebruikt om Nagelkerke's $R^2$ te duiden. De juiste term hiervoor is de verklaarde variatie of model fit.[^2]
# 
# ## Individuele predictors toetsen en interpreteren met de Wald toets
# 
# Als de *likelihood ratio* toets aantoont dat het regressiemodel betere voorspellingen geeft dan het interceptmodel, kunnen de predictors getoetst worden. De regressiecoefficiënten van de predictors en de intercept worden getoetst met een *Wald toets* waarbij de nulhypothese is dat de coefficiënt gelijk aan nul is ($\beta = 0$) en de (tweezijdige) alternatieve hypothese dat de coefficiënt niet gelijk aan nul is ($\beta \neq 0$). Er kan ook een eenzijdige alternatieve hypothese opgesteld worden, bijvoorbeeld als er de verwachting is dat de coefficiënt positief of negatief is. De *Wald-toets* toont in feite aan of er wel of geen relatie is tussen de predictor en afhankelijke variabele in de aanwezigheid van de andere predictoren van het regressiemodel. Bij de *Wald-toets* is de gebruikte toetsstatistiek de z-score.[^2]
# 
# De regressiecoëfficiënten bij *multinomiale logistische regressie* worden geïnterpreteerd in termen van odds ratios. Odds is een Engelse term en is een variant van kans, namelijk de kans op een gebeurtenis gedeeld door 1 minus de kans op een gebeurtenis ($\frac{\pi}{1 - \pi}$). Bij een kans van  2/3 is de odds $\frac{2/3}{1 - 2/3} = \frac{2/3}{1/3} = 2$. Bij het opgooien van een muntje is de kans op zowel kop als munt 0,5. De odds van zowel kop of munt zijn dus $\frac{1/2}{1 - 1/2} = \frac{1/2}{1/2} = 1$. De odds kan echter ook uitgedrukt worden als een ratio van de kansen van twee gebeurtenissen, namelijk de kans op de ene gebeurtenis gedeeld door de kans op de andere gebeurtenis. In de huidige casus is er de odds van de mogelijkheden van de nominale afhankelijke variabele ten opzichte van de referentiecategorie, bijvoorbeeld de odds van het volgen van een hbo master ten opzichte van direct aan het werk gaan. 
# 
# Een odds ratio is een ratio van twee odds. In de huidige casus wordt onderzocht of nominaal afstuderen gerelateerd is aan het vervolg na de opleiding. Stel dat de odds op voor een hbo master ten opzichte van direct aan het werk gaan 1/3 is voor nominaal afgestudeerden en 1/6 is voor niet nominaal afgestudeerden. Dan is de odds ratio voor de variabele Nominaal $\frac{1/3}{1/6} = 2$. De odds dat nominaal afgestudeerden een hbo master volgen ten opzichte van direct aan het werk gaan is dus twee keer zo hoog als de odds dat niet nominaal afgestudeerden een hbo master volgen ten opzichte van direct aan het werk gaan. Dit is de manier om de odds ratio te interpreteren.[^2]
# 
# Regressiecoëfficiënten zijn gelijk aan de logaritme van de odds ratio van de bijbehorende predictor. De odds ratio zelf wordt berekend door de exponent te nemen van de regressiecoëfficiënt. Let bij het interpreteren van odds ratios op dat de betekenis verschillend is voor continue en categorische predictors. In beide gevallen geldt echter dat een toename van één eenheid van de predictor resulteert in een odds die vermenigvuldigd wordt met de exponent van de regressiecoëfficiënt $\exp(\beta)$. De odds zijn dus $\exp(\beta)$ keer zo hoog na een toename van één eenheid van de predictor. Een voorbeeld van de interpretatie van regressiecoëfficiënten is handig voor de huidige casus. Voor elke predictor is een fictieve waarde van de regressiecoëfficiënt gemaakt die geïnterpreteerd wordt. De intercept wordt bij *multinomiale logistische regressie* meestal niet geïnterpreteerd.[^2]
# 
# * Nominaal; hbo master vs. werk ($\beta_{1,1} = 0,405$): De regressiecoefficiënt van de variabele Nominaal is gelijk aan 0,405. De odds ratio van deze predictor is dus $exp(0,405) = 1,5$. De variabele Nominaal is zo opgesteld dat het nominaal afgestudeerden vergelijkt ten opzichte van niet nominaal afgestudeerden als referentiecategorie. Als de overige predictors gelijkblijven is de odds van het volgen van een hbo master ten opzichte van direct aan het werk gaan voor nominaal afgestudeerden 1,5 keer zo hoog als de odds voor niet nominaal afgestudeerden. In een regressiemodel worden categorische variabelen omgezet in binaire variabelen met de waarden 0 en 1, omdat dat nodig is om het model te fitten. De variabele Nominaal zou bijvoorbeeld gecodeerd kunnen worden met een 1 voor nominaal afstuderen en een 0 voor niet nominaal afstuderen. Let goed op hoe de categorieën gecodeerd zijn, i.e. welke categorie de waarde 1 en 0 hebben. Dit bepaalt namelijk de interpretatie.
# * Gemiddeld_cijfer; hbo master vs. werk ($\beta = 0,182$): De coëfficient van de variabele Gemiddeld_cijfer is gelijk aan 0,182. De odds ratio van deze predictor is dus $exp(0,182) = 1,2$. Als de overige predictors gelijkblijven is de odds van het volgen van een hbo master ten opzichte van direct aan het werk gaan 1,2 keer zo hoog bij een toename van het gemiddeld cijfer met één punt.
# * Nominaal; wo master vs. werk ($\beta = -0,693$): De regressiecoefficiënt van de variabele Nominaal is gelijk aan -0,693. De odds ratio van deze predictor is dus $exp(-0,693) = 0,5$. De variabele Nominaal is zo opgesteld dat het nominaal afgestudeerden vergelijkt ten opzichte van niet nominaal afgestudeerden als referentiecategorie. Als de overige predictors gelijkblijven is de odds van het volgen van een wo master ten opzichte van direct aan het werk gaan voor nominaal afgestudeerden 0,5 keer zo hoog als de odds voor niet nominaal afgestudeerden. De odds van het volgen van een wo master ten opzichte van direct aan het werk gaan voor nominaal afgestudeerden is dus eigenlijk 2 (1 / 0,5 = 2) keer zo laag als de odds voor niet nominaal afgestudeerden. Let opnieuw goed op hoe de categorieën gecodeerd zijn, i.e. welke categorie de waarde 1 en 0 hebben. Dit bepaalt namelijk de interpretatie.
# * Gemiddeld_cijfer; wo master vs. werk ($\beta = -0,105$): De coëfficient van de variabele Gemiddeld_cijfer is gelijk aan -0,105. De odds ratio van deze predictor is dus $exp(-0,105) = 0,9$. Als de overige predictors gelijkblijven is de odds van het volgen van een wo master ten opzichte van direct aan het werk gaan 0,9 keer zo hoog bij een toename van Gemiddeld_cijfer met één punt. De odds van het volgen van een wo master ten opzichte van direct aan het werk gaan is dus eigenlijk 1.11 (1 / 0,9) keer zo laag bij een toename van één punt in het gemiddelde cijfer.

# ## Predictors vergelijkingen door standaardisatie
# 
# Op basis van de regressievergelijking en de Wald-toetsen kan bepaald worden of predictors gerelateerd zijn aan de afhankelijke variabele en wat de invloed van een verandering van de predictor is op de afhankelijke variabele. Een andere relevante vraag is welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. Op basis van de regressiecoëfficienten kan dit niet bepaald worden, omdat de schaal van de predictors verschilt. Het gemiddelde cijfer varieert tussen de 1 en 10 (waarschijnlijk zijn de meeste waarden hoger dan 5,5) terwijl de variabele Nominaal gelijk is aan een 1 of een 0. 
# 
# Standaardiseer de predictors om de predictors onderling te kunnen vergelijken. Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$. Als het regressiemodel opnieuw geschat wordt met gestandaardiseerde variabelen, kunnen de coëfficiënten onderling vergeleken worden op basis van hun grootte. Een grotere (absolute waarde van de) coëfficient betekent een sterkere relatie met de afhankelijke variabele. De coëfficiënt is nu te interpreteren in termen van standaardafwijkingen. Een toename van één eenheid van de predictor staat voor een toename van een standaardafwijking van deze predictor. Deze toename van één standaardafwijking resulteert in een verandering van de odds die gelijk is aan de exponent van de bijbehorende (gestandaardiseerde) regressiecoëfficiënt.[^2]<sup>,</sup>[^11] De predictor met de hoogste absolute waarde van de regressiecoëfficiënt is het sterkst gerelateerd aan de afhankelijke variabele.
# 
# ## Voorspellen op basis van het regressiemodel
# 
# Een regressiemodel maakt het mogelijk om een afhankelijke variabele te voorspellen op basis van een aantal predictors. Als van een student bekend is wat zijn gemiddelde cijfer is en of hij wel of niet nominaal is afgestudeerd, kan een voorspelling gemaakt worden van de kans dat de student een hbo master gaat volgen ten opzichte van direct aan het werk gaan en de kans dat de student een wo master gaat volgen ten opzichte van direct aan het werk gaan. Voor alle deelnemers in de steekproef kunnen deze voorspellingen gemaakt worden. De regressievergelijking maakt het echter ook mogelijk om voor nieuwe deelnemers voorspellingen te maken, waar bijvoorbeeld ook *machine learning* technieken voor gebruikt kunnen worden. Dit wordt een out-of-sample voorspelling genoemd omdat de nieuwe deelnemer niet in de steekproef zit waarop het regressiemodel wordt geschat. Als de opleidingsdirecteur een jaar later het vervolg van de nieuwe afgestudeerde studenten van de opleiding Fysiotherapie wilt voorspellen, kan hij de regressievergelijking van het jaar ervoor gebruiken. Een out-of-sample voorspelling geeft vaak een goede indicatie van de kwaliteit van het regressiemodel, omdat de nieuwe deelnemer niet gebruikt zijn om het model te schatten. Als het doel is om het regressiemodel te gebruiken voor het voorspellen van nieuwe deelnemers, dan is de kwaliteit van de out-of-sample voorspellingen van belang.[^2]
# 
# Bij *multinomiale logistische regressie* wordt de logaritme van de odds op een gebeurtenis ten opzichte van een referentiecategorie voorspeld. In de huidige casus gaat het om de odds op het volgen van een hbo master versus direct aan het werk gaan na afronding van de studie en de odds op het volgen van een wo master versus direct aan het werk gaan na afronding van de studie. Deze odds kunnen echter ook omgezet worden in de kans op een bepaalde gebeurtenis. In de huidige casus gaat het dan om de kans op het volgen van een hbo master, de kans op het volgen van een wo master en de kans op direct aan het werk gaan. Een kans kan waarden aannemen tussen 0 en 1. De geobserveerde waarde is echter een categorie, in de huidige casus de categorie hbo master, wo master of direct aan het werk. Het voorspellen van een categorische variabele wordt classificatie genoemd en is ook mogelijk met *multinomiale logistische regressie*. Voor elke categorie van de afhankelijke variabele is een kans voorspeld en de categorie met de hoogste voorspelde kans is dan het meest waarschijnlijk. Met het regressiemodel kan er geclassificeerd worden door de categorie met de hoogste voorspelde kans toe te wijzen aan die deelnemer. Als een deelnemer een kans van 0,2 heeft om een wo master te volgen, een kans van 0,3 om een hbo master te volgen en een kans van 0,5 om direct aan het werk te gaan, dan is de juiste classificatie dat de deelnemer direct aan het werk gaat.[^12]
# 
# Op basis van de classificaties en de geobserveerde waarden kan een classificatietabel gemaakt worden. Hierin worden de geobserveerde waarden voor de variabele uitval uitgezet tegenover de geclassificeerde waarden. Een voorbeeld van een classificatietabel voor de huidige casus is te zien in Tabel 1. In de cel linksboven is te zien dat er 30 studenten zijn waarvoor voorspeld is dat ze een hbo master gaan volgen en die dat ook daadwerkelijk zijn gaan doen. Voor de wo master zijn er 60 studenten waarvoor dit voorspeld is en die dit ook daadwerkelijk zijn gaan doen. Voor direct aan het werk gaan zijn dit 100 studenten. Deze cellen vormen samen een schuine lijn van linksboven naar rechtsonder in de tabel, deze lijn wordt de diagonaal genoemd. Alle cellen op de diagonaal bevatten de deelnemers die correct geclassificeerd zijn. De overige cellen liggen niet op de diagonaal en bevatten de deelnemers die incorrect geclassificeerd zijn. Zo bevat de cel linksonder 20 studenten waarvoor voorspeld is dat ze een hbo master gaan volgen, maar die in werkelijkheid direct aan het werk zijn gegaan. 
# 
# Op basis van de classificatietabel kan berekend worden welk percentage van de deelnemers correct geclassificeerd is. Dit wordt de accuraatheid genoemd en is te berekenen door het aantal correct geclassificeerde deelnemers te delen door het totaal aantal deelnemers. In de huidige casus is de accuraatheid $\frac{30 + 60 + 100}{370} = 0,514$, dus 51,4% van de deelnemers is correct geclassificeerd.[^12]
# 
# ||                      | Voorspelling    | |
# |-------------| -------------------- | -------------| ------------| ------------| 
# ||                            | Hbo master | wo master | Werk |
# |**Observaties**| Hbo master  | **30**         | 10        | 80  |
# |               | wo master   | 10         | **60**        | 20  |
# |               | Werk        | 20         | 40        | **100** |
# 
# *Tabel 1. Classificatietabel van de observaties en classificaties van het vervolg van afgestudeerden na de bacheloropleiding Fysiotherapie.*
# 
# # Uitleg assumpties
# 
# Om een valide resultaat te vinden met *multinomiale logistische regressie*, dient er aan een aantal assumpties voldaan te worden.[^1]<sup>,</sup>[^2] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Outliers
# 
# Voordat gestart kan worden met *multinomiale logistische regressie*, moet de data gescreend worden op de aanwezigheid van outliers. Outliers (uitbijters) zijn observaties die sterk afwijken van de overige observaties. Univariate outliers zijn observaties die afwijken voor één specifieke variabele, zoals een student die twintig jaar over zijn studie heeft gedaan. Multivariate outliers zijn observaties die afwijken door de combinatie van meerdere variabelen, zoals een persoon van 18 jaar met een inkomen van €100.000,-. De leeftijd van 18 jaar is geen outlier op zichzelf en een inkomen van €100.000,- is dat ook niet. Echter, de combinatie van beide zorgt ervoor dat de observatie vrij onwaarschijnlijk is.[^9]
# 
# Na het vinden van een outlier is de volgende stap om een goede oplossing voor te outlier te bedenken. Het is van belang hier goed over na te denken en niet zomaar een outlier te verwijderen met als enige argument dat het een outlier is. In het algemeen kan er onderscheid gemaakt worden tussen onmogelijke en onwaarschijnlijke outliers.[^3] Een onmogelijke outlier is een observatie die technisch gezien niet kan kloppen, bijvoorbeeld een leeftijd van 1000 jaar, een negatief salaris of een man die zwanger is. Bij deze outliers is het een optie om de waarde te vervangen als er een overduidelijke fout bij het invoeren van de data is gemaakt. Een andere optie is de waarde te verwijderen. Een onwaarschijnlijke outlier is een observatie die technisch gezien wel kan, maar heel erg afwijkt van de overige observaties. De rijksten der aarde zijn in de stad of het dorp waar zij wonen qua vermogen waarschijnlijk een outlier. Maar het zijn bestaande personen dus het verwijderen van de observatie zou hier foutief zijn. Opties in deze situatie zijn om te overwegen de variabele(n) te transformeren, de outlier gewoon mee te nemen in de analyse of de analyse met en zonder de outlier uit te voeren en beide te rapporteren. Ook is het niet verboden om de outlier toch te verwijderen, maar het is in dat geval wel van belang dit transparant te rapporteren en op een goede wijze te beargumenteren.[^3]
# 
# Bij *multinomiale logistische regressie* zijn er vier nuttige methoden om outliers te vinden.[^9]
# 
# ### Boxplots en standaardiseren
# 
# Begin voor de analyse met het screenen van de variabelen in de dataset op de aanwezigheid van univariate outliers. Voor continue variabelen bestaat deze screening uit het visualiseren van de variabele met een boxplot en het standaardiseren[^4] van de variabele. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. In dat geval wijkt de observatie namelijk meer dan drie standaardafwijkingen af van het gemiddelde van de variabele. Gebruik zowel de boxplot als de standaardisering om outliers te vinden voor continue variabelen.[^3]
# 
# Bij categorische variabelen hebben boxplots en standaardisatie geen zin, omdat het geen variabelen met een continue schaal zijn. Bij categorische variabelen is het nuttig om een overzicht te maken van de bestaande categorieën en bijbehorende aantallen observaties en is het nuttig om te onderzoeken of elke observatie slechts in één categorie past. Doe dit met behulp van tabellen.
# 
# ### Gestandaardiseerde residuën
# 
# De residuën van een logistisch regressiemodel zijn de verschillen tussen de observaties van de afhankelijke variabele en de voorspelde kans. Bij *multinomiale logistische regressie* zijn er echter meer dan twee mogelijkheden voor de afhankelijke variabele en worden er meerdere kansen berekend. Er wordt daarom gebruik gemaakt van de odds ten opzichte van een referentiecategorie. Het is daarom ingewikkeld om de residuën te berekenen en vervolgens de gestandaardiseerde residuën te onderzoeken.
# 
# Een oplossing hiervoor is het uitvoeren van een [logistische regressie](41-Logistische-regressie-R.html) voor elke combinatie van twee mogelijkheden en voor elke combinatie de gestandaardiseerde residuën te onderzoeken. In de huidige casus zijn er die combinaties: hbo master versus werk, wo master versus werk en hbo master versus wo master. Voer voor elke combinatie een logistisch regressiemodel uit en onderzoek de gestandaardiseerde residuën. Als er een groot verschil is tussen observatie en voorspelling, zou dat kunnen wijzen op een univariate outlier. Bekijk met een grafiek of er outliers zijn. Als het gestandaardiseerde residu een score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. Op deze manier kunnen outliers bij het regressiemodel kunnen worden geïdentificeerd.[^9]
# 
# ### Mahalanobis afstand
# 
# Multivariate outliers zijn deelnemers met een combinatie van observaties op verschillende variabelen die erg afwijken van de overige deelnemers. Deze multivariate outliers kunnen geïdentificeerd worden met de Mahalanobis afstand. De Mahalanobis afstand is een maat die aangeeft in hoeverre de observaties van een deelnemer voor alle predictors afwijken van de gemiddeldes van de predictors. Het is een maat voor een afstand tussen twee punten als meerdere variabelen worden gebruikt. Bereken de Mahalanobis afstand voor elke deelnemer en vergelijk deze met de criteriumwaarde. De criteriumwaarde wordt bepaald op basis van de chi-kwadraat score bij een aantal vrijheidsgraden dat gelijk is aan het aantal predictors en een significantieniveau van 0,001 (of een zelf gekozen significantieniveau). In de code wordt toegelicht hoe de criteriumwaarde bepaald kan worden.[^9]
# 
# ### Cook's afstand
# 
# De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van de andere deelnemers wat betreft de waardes van de predictorvariabelen. Een andere manier om multivariate outliers te vinden is te bepalen hoeveel invloed een deelnemer heeft op de schattingen van het regressiemodel. Als de uitkomsten van het regressiemodel sterk veranderen als een bepaalde deelnemer weggelaten wordt uit de dataset, dan is deze deelnemer invloedrijk. Met behulp van Cook's afstand worden invloedrijke deelnemers ontdekt. Als Cook's afstand groter dan 1 is, wordt de deelnemer beschouwd als invloedrijk.
# 
# Hoewel de Mahalanobis afstand en Cook's afstand beide multivariate outliers identificeren, verschillen ze in het soort outlier waarop de focus ligt. Bij de Mahalanobis afstand worden afwijkende datapunten gevonden en bij Cook's distance invloedrijke datapunten. Het is echter niet zo dat een afwijkend datapunt ook tegelijkertijd invloedrijk is en dat een invloedrijk datapunt ook afwijkt. Een afwijkend datapunt kan ondanks zijn afwijking van de de overige datapunten toch op een juiste manier voorspeld worden. En een invloedrijk datapunt hoeft niet per se sterk af te wijken van de overige datapunten wat betreft de waardes voor de predictorvariabelen. Houdt hier rekening mee bij het bepalen hoe om te gaan met de gevonden outlier(s).[^9]
# 
# Cook's afstand wordt berekend op basis van de residuën van het regressiemodel. Bij *multinomiale logistische regressie* zijn er meer dan twee mogelijkheden voor de afhankelijke variabele en worden er meerdere kansen berekend. Er wordt daarom gebruik gemaakt van de odds ten opzichte van een referentiecategorie. Het is daarom ingewikkeld om de residuën te berekenen en vervolgens de gestandaardiseerde residuën te onderzoeken. Een oplossing hiervoor is het uitvoeren van een [logistische regressie](41-Logistische-regressie-R.html) voor elke combinatie van twee mogelijkheden en voor elke combinatie de Cook's afstanden te berekenen. In de huidige casus zijn er die combinaties: hbo master versus werk, wo master versus werk en hbo master versus wo master. Voer voor elke combinatie een logistisch regressiemodel uit en onderzoek de Cook's afstanden. Als Cook's afstand groter dan 1 is, wordt de deelnemer beschouwd als invloedrijk en zou er een outlier kunnen zijn.
# 
# ## Lineariteit: Box-Tidwell
# 
# Bij *multinomiale logistische regressie* is de regressievergelijking zo opgesteld dat er een lineaire relatie is tussen elke predictor en de logit van de mogelijkheden van de afhankelijke variabele ten opzichte van de referentiecategorie. Een lineaire relatie houdt in dat de toename of afname van de (logit van de) afhankelijke variabele als gevolg van de toename van de predictor constant is. In tegenstelling tot [multipele lineaire regressie](28-Multipele-lineaire-regressie-R.html) kan bij *multinomiale logistische regressie* geen grafiek gemaakt worden om een lineaire relatie te onderzoeken. In plaats daarvan is er een statistische toets om te onderzoeken of er een lineaire relatie is tussen de predictor en de logit van de afhankelijke variabele. Bij deze *Box-Tidwell test* wordt er voor elke continue predictor een extra term toegevoegd die bestaat uit het product van de predictor en de logaritme van de predictor. Voor de predictor Gemiddeld_cijfer zou dit dus betekenen dat er een extra variabele wordt (Gemiddeld_cijfer * ln[Gemiddeld_cijfer]). Voeg deze interactietermen voor alle continue predictors toe en toets of de regressiecoëfficiënten van deze interactietermen significant zijn. Als dit zo is, dan is er voor die predictor niet voldaan aan de assumptie van lineariteit. Een oplossing hiervoor is het transformeren[^5] van de variabele.[^6]
# 
# ## Multicollineariteit
# 
# Multicollineariteit houdt in dat er een hoge correlatie tussen twee of meerdere predictors is. Er is perfecte multicollineariteit als één predictor een lineaire combinatie is van een of meerdere andere predictors. In andere woorden, de predictor is precies te berekenen op basis van andere predictor(s). In dat geval kan de regressievergelijking niet wiskundig bepaald worden en werkt *multinomiale logistische regressie* niet. Dit komt zeer weinig voor en is vaak makkelijk op te lossen door goed naar de variabelen die het veroorzaken te kijken en een variabele te transformeren of te verwijderen.[^9]
# 
# Bij een hoog niveau van multicollineariteit kan de regressievergelijking wel geschat worden, maar zijn de uitkomsten minder betrouwbaar. De standaardfouten van de regressiecoëfficiënten worden groter bij meer multicollineariteit en dit levert bij hoge multicollineariteit problemen op. Ook is het lastig om te ontdekken wat per predictor de bijdrage is aan de voorspellingen van de afhankelijke variabele, omdat bepaalde predictors sterk gecorreleerd zijn en overlappen in het deel van de variantie dat ze verklaren.[^9] 
# 
# Multicollineariteit wordt getoetst met de Variance Inflation Factor (VIF) die meet hoe sterk elke predictor gecorreleerd is met de andere predictors. Als de VIF van een predictor hoger dan 10 is, is er multicollineariteit voor die predictor.[^9]<sup>,</sup>[^7] Multicollineariteit kan opgelost worden door een van de predictors die het veroorzaakt te verwijderen uit het model. Een andere optie is een principale componenten analyse (PCA) uitvoeren op de predictoren zodat er een onderliggende variabele gecreëerd wordt (zie Field[^9] voor meer informatie).
# 
# ## Observaties per variabele
# 
# Bij *multinomiale logistische regressie* is de afhankelijke variabele nominaal wat betekent dat de variabele meer dan twee mogelijkheden heeft. Dit kan een probleem opleveren als er categorische predictors zijn. Voor elke categorie van een categorische predictor moeten er observaties zijn voor alle mogelijkheden van de afhankelijke variabele. Deze assumptie kan onderzocht worden door een kruistabel te maken voor de combinatie van elke categorische predictor en de afhankelijke variabele. Een voorbeeld van een dergelijke kruistabel is te zien in Tabel 2 voor de afhankelijke variabele Vervolg en predictor Nominaal. In deze kruistabel is te zien dat er binnen de categorie Niet-nominaal van de predictor Nominaal nul deelnemers zijn die een hbo master zijn gaan doen. Deze categorie bevat dus een lege cel en voldoet niet aan de assumptie.[^2]<sup>,</sup>[^6]
# 
# ||                      | Nominaal    | |
# |-------------| -------------------- | -------------| ------------| 
# |                |             | Nominaal | Niet-nominaal|
# |**Vervolg**     | Hbo master  | 50       | 0          |
# |                | wo master   | 40       | 200        |
# |                | Werk        | 80       | 160        |
# 
# *Tabel 2. Kruistabel van de observaties voor de afhankelijke variabele Vervolg en predictor Nominaal waarbij voor de categorie niet-nominaal niet alle waarden van de afhankelijke variabele aanwezig zijn.*
# 
# Daarnaast is het met een nominale afhankelijke variabele mogelijk dat er een categorische predictor is die perfect de waarde van de afhankelijke variabele voorspelt. Een voorbeeld hiervan is te zien in Tabel 3, opnieuw voor de afhankelijke variabele Vervolg en predictor Nominaal. De categorie Nominaal  bevat alleen studenten die een hbo master zijn gaan doen en de categorie Niet-nominaal alleen studenten die een wo master zijn gaan doen of direct aan het werk zijn gegaan. De predictor Nominaal voorspelt dus perfect of een student wel of niet een hbo master gaat doen. Dit fenomeen wordt *complete separation* genoemd en komt af en toe voor als er heel veel predictors aanwezig zijn en weinig observaties. Als dit gebeurt, dan werkt de *maximum likelihood* methode niet.[^6]
# 
# ||                      | Nominaal    | |
# |-------------| -------------------- | -------------| ------------| 
# |                |             | Nominaal | Niet-nominaal|
# |**Vervolg**     | Hbo master  | 50       | 0          |
# |                | wo master   | 0        | 200        |
# |                | Werk        | 0        | 200        |
# 
# *Tabel 3. Kruistabel van de observaties voor de afhankelijke variabele Vervolg en predictor Nominaal waarbij er sprake is van complete separation.*
# 
# Het gevolg van de assumptie voor observaties per variabele zijn dat er extreem hoge regressiecoëfficiënten en standaardfouten worden gevonden of dat de *maximum likelihood* methode niet werkt. Toets daarom deze assumptie door voor elke categorische predictor een kruistabel te maken met de afhankelijke variabele en onderzoek of er lege cellen zijn en of er *complete separation* plaatsvindt. Als er niet aan deze assumptie voldaan is, dan zijn er meerdere oplossingen mogelijk. De categorie die problemen geeft bij de categorische predictor kan verwijderd worden of worden samengevoegd met een andere categorie. Daarnaast kan de hele predictor verwijderd worden. Ten slotte is meer data verzamelen ook een optie als dit mogelijk is.[^6]
# 
# ## Overdispersie
# 
# Bij *multinomiale logistische regressie* wordt aangenomen dat de residuën niet gecorreleerd zijn. Dit is in principe het geval als alle deelnemers willekeurig in de steekproef zijn opgenomen. Als deelnemers meerdere keren gemeten zijn of gematcht zijn met andere deelnemers, dan is hier geen sprake van en zijn er waarschijnlijk gecorreleerde residuën. *multinomiale logistische regressie* is dan niet de juiste analysemethode, maar *multilevel multinomiale logistische regressie* kan hiervoor wel gebruikt worden. Bij *multinomiale logistische regressie* wordt daarom getoetst of er overdispersie is. Overdispersie betekent dat de variantie in de voorspelde kansen groter is dan op basis van het model wordt verwacht. Het gevolg is dat de standaardfouten te laag zijn en er een hogere kans is op type I fouten (onterecht verwerpen van de nulhypothese) bij het toetsen van de significantie van regressiecoëfficiënten, de significantie van het hele model en de significantie van het vergelijken van verschillende modellen onderling met de *likelihood ratio toets*. [^20]<sup>,</sup>[^6]
# 
# De dispersieparameter geeft aan of er sprake is van overdispersie. De dispersieparameter hoort in de buurt van 1 te zitten. Als de parameter hoger dan 2 is, is er sprake van overdispersie. De gevolgen van overdispersie voor het toetsen van regressiecoëfficiënten kunnen verholpen worden door de standaardfouten van de regressiecoëfficiënten te herschalen op basis van de overdispersie. Bij het toetsen van het gehele model of het vergelijken van modellen onderling worden de waarden van de chi-kwadraat toetsstatistiek gedeeld door de dispersieparameter en wordt de p-waarde berekend op basis van de herschaalde toetsstatistiek. Het onderzoeken van de dispersieparameter en het corrigeren in het geval van overdispersie worden toegelicht bij het toetsen van de assumpties in deze toetspagina.[^20]
# 
# Er kan ook sprake zijn van onderdispersie: de situatie waarin de variantie in voorspelde kansen kleiner is dan op basis van het model wordt verwacht. Dit leidt tot meer conservatieve toetsen en een erg lage kans op type I fouten. Deze situatie is minder erg dan overdispersie en er wordt in dit geval meestal geen correctie uitgevoerd. Dezelfde correctie als bij overdispersie kan echter wel uitgevoerd worden en zorgt er in dit geval voor dat de significantietoetsen minder conservatief worden.[^20]<sup>,</sup>[^6]
# 
# # Toetsing assumpties
# 
# Voer *multinomiale logistische regressie* uit om te onderzoeken of het vervolg na de bachelor Fysiotherapie (hbo master, wo master of direct aan het werk) te voorspellen is op basis van het wel of niet nominaal afstuderen en het gemiddelde cijfer van de bachelor van de studenten. Start met het toetsen van de assumpties en voer vervolgens de *multinomiale logistische regressie* uit als hieraan voldaan is.
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Voer eerst de *multinomiale logistische regressie* uit omdat deze nodig is voor het toetsen van assumpties en sla het resultaat op. Interpreteer de resultaten pas na het toetsen van de assumpties. Gebruik de functie `mblogit()` van het package `mclogit` met als eerste argument de regressievergelijking `Vervolg ~  Nominaal + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Vervolg` en rechts de twee onafhankelijke variabelen `Nominaal` en `Gemiddeld_cijfer`. Het tweede argument is de dataset `Fysiotherapie_Vervolg`.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


library(mclogit)

Regressiemodel <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                          Fysiotherapie_Vervolg)


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# ## Outliers
# 
# ### Boxplots en standaardiseren
# 
# <!-- ## TEKSTBLOK: Outlier1.R -->
# Onderzoek of er univariate outliers zijn met behulp van boxplots en gestandaardiseerde scores voor continue variabelen en tabellen voor categorische variabelen. Begin met de boxplot voor de variabele `Gemiddeld_cijfer`.
# <!-- ## /TEKSTBLOK: Outlier1.R -->
# 
# <!-- ## OPENBLOK: Outlier2.R -->

# In[ ]:


# Maak een boxplot van de continue variabelen in de dataset
boxplot(Fysiotherapie_Vervolg[,"Gemiddeld_cijfer"])


# <!-- ## /OPENBLOK: Outlier2.R -->
# 
# Voor de gemiddelde cijfers zijn er geen onmogelijke scores en zijn er geen grote afwijkingen. Op basis van de gestandaardiseerde scores kan onderzocht worden of er toch nog een outlier is. Onderzoek de gestandaardiseerde scores door een functie te schrijven die het aantal observaties per variabele telt met een gestandaardiseerde score hoger dan 3 of lager dan -3. Pas deze functie vervolgens toe op de gemiddelde cijfers.
# 
# <!-- ## OPENBLOK: Outlier3.R -->

# In[ ]:


# Maak een functie om het aantal observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3 te tellen
Outlier_standaardiseren <- function(variabele){
  # Standaardiseer de variabele met de scale functie
  Z_score <- scale(variabele)
  # Tel het aantal observaties met een absolute score hoger dan 3
  Aantal_outliers <- sum(abs(Z_score) > 3)
  # Retourneer dit aantal
  return(Aantal_outliers)
}

# Tel voor de continue variabelen het aantal observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3
Outlier_standaardiseren(Fysiotherapie_Vervolg$Gemiddeld_cijfer)


# <!-- ## /OPENBLOK: Outlier3.R -->

# Er zijn nul observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3. Er zijn in deze stap voor de continue variabelen geen outliers gevonden.
# 
# Nominaal en Vervolg zijn de categorische variabele in deze dataset. Maak een tabel met de frequenties voor alle categoriëen van deze variabelen om te onderzoeken of hier afwijkende waardes zijn.
# 
# <!-- ## OPENBLOK: Outlier4.R -->

# In[ ]:


table(Fysiotherapie_Vervolg$Nominaal)
table(Fysiotherapie_Vervolg$Vervolg)


# <!-- ## /OPENBLOK: Outlier4.R -->
# 
# Voor alle drie de categorische variabelen zijn er geen categorieën met opmerkelijke waarden. Er zijn hier dus ook geen outliers.
# 
# ### Gestandaardiseerde residuën
# 
# <!-- ## TEKSTBLOK: Outlier5.R -->
# Onderzoek of er outliers zijn met behulp van de gestandaardiseerde residuën. Voer een [logistische regressie](41-Logistische-regressie-R.html) uit voor elke combinatie van twee mogelijkheden en onderzoek voor elke combinatie de gestandaardiseerde residuën. Maak eerst aparte datasets voor elke combinatie van twee mogelijkheden. Gebruik daarna om de logistische regressie uit te voeren de functie `glm()` met als eerste argument de regressievergelijking `Vervolg ~ Nominaal + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Vervolg` en rechts de twee onafhankelijke variabelen `Nominaal` en `Gemiddeld_cijfer`. Het tweede argument is de dataset (bijvoorbeeld `Fysiotherapie_Uitval_Niet_nominaal`) en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden. Bereken vervolgens de gestandaardiseerde residuën met de functie `rstandard()`, maak een plot en tel het aantal gestandaardiseerde residuën met een waarde hoger dan 3 of lager dan -3.
# <!-- ## /TEKSTBLOK: Outlier5.R -->
# 
# <!-- ## OPENBLOK: Outlier6.R -->

# In[ ]:


## Maak datasets voor beide logistische regressievergelijkingen
Fysiotherapie_WO_master_hbo_master <- Fysiotherapie_Vervolg[Fysiotherapie_Vervolg$Vervolg != "werk",]
Fysiotherapie_WO_master_werk <- Fysiotherapie_Vervolg[Fysiotherapie_Vervolg$Vervolg != "hbo master",]
Fysiotherapie_hbo_master_werk <- Fysiotherapie_Vervolg[Fysiotherapie_Vervolg$Vervolg != "WO master",]

## Voer de logistische regressiemodellen uit
Regressiemodel_WO_master_hbo_master <- glm(Vervolg ~ Nominaal + Gemiddeld_cijfer,
                                           data = Fysiotherapie_WO_master_hbo_master,
                                           family = "binomial")
Regressiemodel_WO_master_werk <- glm(Vervolg ~ Nominaal + Gemiddeld_cijfer,
                                     data = Fysiotherapie_WO_master_werk,
                                     family = "binomial")
Regressiemodel_hbo_master_werk <- glm(Vervolg ~ Nominaal + Gemiddeld_cijfer,
                                      data = Fysiotherapie_hbo_master_werk,
                                      family = "binomial")


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd_WO_master_hbo_master <- rstandard(Regressiemodel_WO_master_hbo_master)
Residu_gestandaardiseerd_WO_master_werk <- rstandard(Regressiemodel_WO_master_werk)
Residu_gestandaardiseerd_hbo_master_werk <- rstandard(Regressiemodel_hbo_master_werk)

# Plot de gestandaardiseerde residuën
plot(Residu_gestandaardiseerd_WO_master_hbo_master, 
     xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")
plot(Residu_gestandaardiseerd_WO_master_werk, 
     xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")
plot(Residu_gestandaardiseerd_hbo_master_werk, 
     xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")

# Tel het aantal gestandaardiseerde residuën met een absolute waarde groter dan 3
sum(abs(Residu_gestandaardiseerd_WO_master_hbo_master > 3))
sum(abs(Residu_gestandaardiseerd_WO_master_werk > 3))
sum(abs(Residu_gestandaardiseerd_hbo_master_werk > 3))


# <!-- ## /OPENBLOK: Outlier6.R -->
# 
# Er zijn geen gestandaardiseerde residuën met een score hoger dan 3 of lager dan -3 wat er op wijst dat er geen outliers in de data zijn.
# 
# ### Mahalanobis distance
# 
# <!-- ## TEKSTBLOK: Outlier7.R -->
# Onderzoek of er multivariate outliers zijn met behulp van de Mahalanobis distance met behulp van de functie `mahalanobis()`. De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van het gemiddelde van alle deelnemers voor alle predictors samen. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabele Nominaal om in een numerieke variabele met de waarde 1 voor Nominaal en 0 voor Niet nominaal. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd.
# 
# Neem vervolgens een subset van de dataset met alleen de predictors en gebruik deze voor de Mahalanobis afstand. Gebruik de functie `mahalanobis()` met als argumenten de dataset `Subset`, de gemiddeldes van elke kolom berekend met `colMeans(Subset)` en de covariantiematrix van de dataset berekend met `cov(Subset)`.
# 
# Bereken daarna de criteriumwaarde op basis van het gewenste significantieniveau en het aantal predictors. Plot de Mahalanobis afstanden en tel het aantal deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde. Het gehanteerde significantieniveau is 0,001.
# <!-- ## /TEKSTBLOK: Outlier7.R -->
# 
# <!-- ## OPENBLOK: Outlier8.R -->

# In[ ]:


# Zet Nominaal om in een numerieke variabele met een 1 voor een vrouw en 0 voor een man
Fysiotherapie_Vervolg$Nominaal_dummy <- as.numeric(Fysiotherapie_Vervolg$Nominaal == "Nominaal")

# Maak een subset van de dataset met alle predictors
Subset <- Fysiotherapie_Vervolg[,c("Nominaal_dummy",
                                    "Gemiddeld_cijfer"
                                    )]

# Bereken de Mahalanobis afstand voor elke deelnemer 
Mahalanobis_afstanden <- mahalanobis(Subset,
                                     colMeans(Subset),
                                     cov(Subset))

# Bepaal de criteriumwaarde voor de Mahalanobis afstand met de functie qchisq() met als eerste argument 1 - het significantieniveau en als tweede argument het aantal predictors. In deze casus is het significantieniveau voor de Mahalanobis afstand 0.001 en het aantal predictors berekend met ncol(Subset).
(Criteriumwaarde <- qchisq(1 - 0.001, ncol(Subset)))

# Plot de Mahalanobis afstanden
plot(Mahalanobis_afstanden, xlab = "Volgorde", ylab = "Mahalanobis afstanden")

# Tel het aantal Mahalanobis afstanden groter dan de criteriumwaarde
sum(Mahalanobis_afstanden > Criteriumwaarde)


# <!-- ## /OPENBLOK: Outlier8.R -->
# 
# <!-- ## TEKSTBLOK: Outlier9.R -->
# Er zijn geen deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde van `r Round_and_format(Criteriumwaarde)`, dus er lijken geen multivariate outliers te zijn op basis van de Mahalanobis afstand.
# <!-- ## /TEKSTBLOK: Outlier9.R -->
# 
# ### Cook's afstand
# 
# <!-- ## TEKSTBLOK: Outlier10.R -->
# Onderzoek of er outliers zijn met behulp van de gestandaardiseerde residuën. Voer een [logistische regressie](41-Logistische-regressie-R.html) uit voor elke combinatie van twee mogelijkheden en onderzoek voor elke combinatie de Cook's afstanden. Maak eerst aparte datasets voor elke combinatie van twee mogelijkheden. Gebruik daarna om de logistische regressie uit te voeren de functie `glm()` met als eerste argument de regressievergelijking `Vervolg ~ Nominaal + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Vervolg` en rechts de twee onafhankelijke variabelen `Nominaal` en `Gemiddeld_cijfer`. Het tweede argument is de dataset (bijvoorbeeld `Fysiotherapie_Uitval_Niet_nominaal`) en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden. Bereken vervolgens de Cook's afstanden met de functie `cooks.distance()`, maak een plot en tel het aantal Cook's afstanden dat groter is dan de criteriumwaarde van 1.
# <!-- ## /TEKSTBLOK: Outlier10.R -->
# 
# <!-- ## OPENBLOK: Outlier11.R -->

# In[ ]:


## Maak datasets voor beide logistische regressievergelijkingen
Fysiotherapie_WO_master_hbo_master <- Fysiotherapie_Vervolg[Fysiotherapie_Vervolg$Vervolg != "werk",]
Fysiotherapie_WO_master_werk <- Fysiotherapie_Vervolg[Fysiotherapie_Vervolg$Vervolg != "hbo master",]
Fysiotherapie_hbo_master_werk <- Fysiotherapie_Vervolg[Fysiotherapie_Vervolg$Vervolg != "WO master",]

## Voer de logistische regressiemodellen uit
Regressiemodel_WO_master_hbo_master <- glm(Vervolg ~ Nominaal + Gemiddeld_cijfer,
                                           data = Fysiotherapie_WO_master_hbo_master,
                                           family = "binomial")
Regressiemodel_WO_master_werk <- glm(Vervolg ~ Nominaal + Gemiddeld_cijfer,
                                     data = Fysiotherapie_WO_master_werk,
                                     family = "binomial")
Regressiemodel_hbo_master_werk <- glm(Vervolg ~ Nominaal + Gemiddeld_cijfer,
                                      data = Fysiotherapie_hbo_master_werk,
                                      family = "binomial")

# Bepaal Cook's afstand voor elke deelnemer
Cooks_afstand_WO_master_hbo_master <- cooks.distance(Regressiemodel_WO_master_hbo_master)
Cooks_afstand_WO_master_werk <- cooks.distance(Regressiemodel_WO_master_werk)
Cooks_afstand_hbo_master_werk <- cooks.distance(Regressiemodel_hbo_master_werk)

# Plot Cook's afstanden
plot(Cooks_afstand_WO_master_hbo_master, 
     xlab = "Volgorde", ylab = "Cook's afstanden")
plot(Cooks_afstand_WO_master_werk, 
     xlab = "Volgorde", ylab = "Cook's afstanden")
plot(Cooks_afstand_hbo_master_werk, 
     xlab = "Volgorde", ylab = "Cook's afstanden")

# Tel het aantal Cook's afstanden groter dan de criteriumwaarde van 1
sum(abs(Cooks_afstand_WO_master_hbo_master > 1))
sum(abs(Cooks_afstand_WO_master_werk > 1))
sum(abs(Cooks_afstand_hbo_master_werk > 1))


# <!-- ## /OPENBLOK: Outlier11.R -->
# 
# Er zijn geen deelnemers met een Cook's afstand groter dan de criteriumwaarde van 1. Er lijken dus geen invloedrijke datapunten of multivariate outliers te zijn.
# 
# ## Lineariteit: Box-Tidwell
# 
# Voer de *Box-Tidwell test* uit om te onderzoeken of er een lineaire relatie is tussen de continue predictors en de logit van de afhankelijke variabele. Maak eerst voor elke continue predictor een nieuwe variabele aan die bestaat uit het product van de predictor met de logaritme (`log()`) van de predictor. Voeg daarna deze nieuwe interactietermen toe aan de regressievergelijking en voer de *multinomiale logistische regressie* uit. Gebruik de functie `mblogit()` van het package `mclogit` met als eerste argument de regressievergelijking `Vervolg ~ Nominaal + Gemiddeld_cijfer + Gemiddeld_cijfer_log` met links van de tilde de afhankelijke variabele `Vervolg` en rechts de twee onafhankelijke variabelen `Nominaal` en `Gemiddeld_cijfer` en de interactietermen `Gemiddeld_cijfer_log`. Het tweede argument is de dataset `Fysiotherapie_Vervolg`.
# 
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


# Maak de interactievariabele aan voor de continue predictor Gemiddeld_cijfer
Fysiotherapie_Vervolg$Gemiddeld_cijfer_log <- Fysiotherapie_Vervolg$Gemiddeld_cijfer * log(Fysiotherapie_Vervolg$Gemiddeld_cijfer)

library(mclogit)

# Voeg deze interactievariabelen toe aan het regressiemodel en toets het regressiemodel
Regressiemodel_Box_Tidwell <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer + Gemiddeld_cijfer_log,
                                      Fysiotherapie_Vervolg)

# Bekijk de significantie van de regressiecoëfficiënten
summary(Regressiemodel_Box_Tidwell)


# <!-- ## /OPENBLOK: AssLineariteit1.R -->
# 
# <!-- ## CLOSEDBLOK: AssLineariteit2.R -->

# In[ ]:


# Maak de interactievariabelen aan voor de continue predictor Gemiddeld_cijfer
Fysiotherapie_Vervolg$Gemiddeld_cijfer_log <- Fysiotherapie_Vervolg$Gemiddeld_cijfer * log(Fysiotherapie_Vervolg$Gemiddeld_cijfer)

library(mclogit)

# Voeg deze interactievariabelen toe aan het regressiemodel en toets het regressiemodel
Regressiemodel_Box_Tidwell <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer + Gemiddeld_cijfer_log,
                                      Fysiotherapie_Vervolg)

# Bekijk de significantie van de regressiecoëfficiënten
BT <- summary(Regressiemodel_Box_Tidwell)$coefficients


# <!-- ## /CLOSEDBLOK: AssLineariteit2.R -->
# 
# De interactieterm van de predictor Gemiddeld_cijfer is voor zowel de vergelijking tussen hbo master en werk (*z* = `r Round_and_format(BT[7,3])`, *p* = `r Round_and_format(BT[7,4])`) als de vergelijking tussen wo master en werk (*z* = `r Round_and_format(BT[8,3])`, *p* = `r Round_and_format(BT[8,4])`) niet significant.[^8] Er is dus voldaan aan de assumptie van lineariteit.
# 
# ## Multicollineariteit
# 
# <!-- ## TEKSTBLOK: AssMulticollineariteit1.R -->
# Onderzoek of er sprake is van multicollineariteit met behulp van Variance Inflation Factors (VIFs). Bereken de VIFs voor elke predictor met de functie `VIF()` van het package `DescTools` waarbij de functie als argument `Multicollineariteit` (het object van het regressiemodel) heeft. De functie `VIF()` werkt niet op het object van de *multinomiale logistische regressie* van het package `mclogit`. Voer daarom een regressiemodel uit met een zelfverzonnen afhankelijke variabele en de predictors van de *multinomiale logistische regressie*. Gebruik de functie `lm()` met als eerste argument de vergelijking `log(Gemiddeld_cijfer) ~ Nominaal + Gemiddeld_cijfer` met links van het tilde de zelfverzonnen afhankelijke variabele `log(Gemiddeld_cijfer)` en rechts de predictors `Nominaal` en `Gemiddeld_cijfer`. Het tweede argument is de dataset `Fysiotherapie_Vervolg`. De afhankelijke variabele is hier zelfverzonnen omdat de VIF niet afhankelijk is van deze variabele. De afhankelijke variabele kan dus ook op een andere manier gemaakt worden.
# <!-- ## /TEKSTBLOK: AssMulticollineariteit1.R -->
# 
# <!-- ## OPENBLOK: AssMulticollineariteit2.R -->

# In[ ]:


library(DescTools)

Multicollineariteit <- lm(log(Gemiddeld_cijfer) ~ Nominaal + Gemiddeld_cijfer,
                           Fysiotherapie_Vervolg)

# Bereken de VIF voor de predictors Cijfers_P1, Cijfers_P2 en Cijfers_P3
VIF(Multicollineariteit)


# <!-- ## /OPENBLOK: AssMulticollineariteit2.R -->
# 
# Geen enkele van de VIFs is hoger dan 10, dus er is voldaan aan de assumptie van multicollineariteit.
# 
# ## Observaties per variabele
# 
# Onderzoek met behulp van kruistabellen de assumptie over observaties per variabele. Maak voor elke categorische predictor een kruistabel met de afhankelijke variabele en onderzoek of voor elk niveau van de categorische predictors beide waarden van de afhankelijke variabele aanwezig zijn.
# 
# <!-- ## OPENBLOK: ObsperVar1.R -->

# In[ ]:


# Maak de kruistabel voor de predictor Nominaal
with(Fysiotherapie_Vervolg,
     table(Nominaal,
           Vervolg))


# <!-- ## /OPENBLOK: ObsperVar1.R -->
# 
# Voor alle categorieën van beide predictors zijn er studenten die een hbo master gaan volgen, een wo master gaan volgen en direct aan het werk gaan. Dus alle waarden van de afhankelijke variabele zijn aanwezig in alle categorieën. Er is dus ook geen sprake van *complete separation* dus er is aan deze assumptie voldaan.
# 
# ## Overdispersie
# 
# <!-- ## TEKSTBLOK: Dispersie1.R -->
# Bereken de dispersieparameter om te bepalen of er sprake is van overdispersie. Voer eerst de *multinomiale logistische regressie* uit omdat deze nodig is voor het toetsen van assumpties en sla het resultaat op. Interpreteer de resultaten pas na het toetsen van de assumpties. Gebruik de functie `mblogit()` van het package `mclogit` met als eerste argument de regressievergelijking `Vervolg ~  Nominaal + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Vervolg` en rechts de twee onafhankelijke variabelen `Nominaal` en `Gemiddeld_cijfer`. Het tweede argument is de dataset `Fysiotherapie_Vervolg`. Bereken daarna de dispersieparameter met de functie `dispersion()` met als argumenten het object van het regressiemodel `Dispersie` en `method = "Pearson"` om de dispersie te berekenen op basis van de chi-kwadraat toetsstatistiek die ook voor de significantie van het gehele model gebruikt wordt.
# <!-- ## /TEKSTBLOK: Dispersie1.R -->
# 
# <!-- ## OPENBLOK: Dispersie2.R -->

# In[ ]:


# Fit het regressiemodel
library(mclogit)

Dispersie <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                     Fysiotherapie_Vervolg)

dispersion(Dispersie, method = "Pearson")


# <!-- ## /OPENBLOK: Dispersie2.R -->
# 
# <!-- ## CLOSEDBLOK: Dispersie3.R -->

# In[ ]:


# Fit het regressiemodel
library(mclogit)

Dispersie <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                          Fysiotherapie_Vervolg)

Disp <- dispersion(Dispersie, method = "Pearson")


# <!-- ## /CLOSEDBLOK: Dispersie3.R -->
# 
# <!-- ## TEKSTBLOK: Dispersie4.R -->
# Er is sprake van een onderdispersie, aangezien de dispersieparameter (`r Round_and_format(Disp)`) kleiner dan 1 is. Het verschil met 1 is echter niet zeer klein en bij onderdispersie wordt er in het algemeen geen correctie uitgevoerd. Voor de *multinomiale logistische regressie* in deze casus wordt daarom geen correctie uitgevoerd vanwege onderdispersie.
# <!-- ## /TEKSTBLOK: Dispersie4.R -->
# 
# # Uitvoering
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Als alle assumpties zijn getoetst en aan alle assumpties is voldaan, kan de *multinomiale logistische regressie* uitgevoerd worden. Gebruik de functie `mblogit()` van het package `mclogit` met als eerste argument de regressievergelijking `Vervolg ~  Nominaal + Gemiddeld_cijfer` met links van de tilde de afhankelijke variabele `Vervolg` en rechts de twee onafhankelijke variabelen `Nominaal` en `Gemiddeld_cijfer`. Het tweede argument is de dataset `Fysiotherapie_Vervolg`. 
# 
# Voer daarna de *likelihood ratio toets* uit met behulp van de functie `lrtest()` van het package `lmtest` met als argument het object van het regressiemodel (`Regressiemodel`). Sla het model op en presenteer vervolgens een overzicht van de resultaten met de functie `summary()`. Bepaal de 95%-betrouwbaarheidsintervallen van de regressiecoëfficiënten met de functie `confint()`. Bereken ten slotte de Nagelkerke $R^2$ met behulp van de functie `r2_nagelkerke()` van het package `performance`.
# 
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


library(mclogit)

# Voer de multipele lineaire regressie uit
Regressiemodel <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                          Fysiotherapie_Vervolg)

# Voer de likelihood ratio toets uit
library(lmtest)
lrtest(Regressiemodel)

# Presenteer de resultaten
summary(Regressiemodel)

# Presenteer de 95%-betrouwbaarheidsintervallen
confint(Regressiemodel)

# Bereken de odds ratio van alle regressiecoëfficiënten door de exponent te nemen
exp(coef(Regressiemodel))

# Bepaal de Nagelkerke R2
library(performance)
r2_nagelkerke(Regressiemodel)


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# <!-- ## CLOSEDBLOK: Uitvoering3.R -->

# In[ ]:


# Voer de multipele lineaire regressie uit
Regressiemodel <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                          Fysiotherapie_Vervolg)

# Voer de likelihood ratio toets uit
LR_test <- lrtest(Regressiemodel)

# Presenteer de resultaten
Reg <- summary(Regressiemodel)#$coefficients
R2 <- r2_nagelkerke(Regressiemodel)
CI <- confint(Regressiemodel)


# <!-- ## /CLOSEDBLOK: Uitvoering3.R -->
# 
# ## Significantie regressiemodel
# 
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# Bepaal als eerste stap de significantie van het regressiemodel met behulp van de *likelihood ratio toets*. De *likelihood ratio toets* voor het regressiemodel laat een significant verschil zien tussen het voorgestelde model en een model met alleen een intercept, *&chi;^2^* = `r Round_and_format(LR_test$Chisq[2])`, *df* = `r -1 * LR_test$Df[2]`, *p* < 0,0001, $R^2_N$ = `r Round_and_format(100 * R2)`.[^8] De nulhypothese dat geen enkele predictor van de predictors Nominaal en  Gemiddeld_cijfer gerelateerd is aan de afhankelijke variabele Vervolg kan verworpen worden. De Nagelkerke $R^2$ is `r Round_and_format(100*R2)`. Omdat de *likelihood ratio toets* voor het gehele model significant is, kunnen de coëfficiënten geinterpreteerd worden.
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# 
# ## Significantie en interpretatie coëfficiënten
# 
# <!-- ## TEKSTBLOK: Coefficienten1.R -->
# Voor de intercept en de regressiecoëfficiënten van de predictors zijn de geschatte coëfficiënt (`Estimate`), de standaardfout van de geschatte coëfficiënt (`Std. Error`) en de z-statistiek (`z value`) en p-waarde (`Pr(>|z|)`) van de *Wald toets* voor de regressiecoëfficiënt weergegeven:
# 
# * Nominaal; hbo master vs. werk: de geschatte waarde voor de regressiecoëfficiënt van de variabele Nominaal voor de vergelijking tussen hbo master en werk is `r Round_and_format(Reg$coefficients[3,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[3,3])`, *p* = 0,007).[^8] De hoofdcategorie van de variabele Nominaal is `Nominaal`, aangezien de variabele in de resultaten weergegeven is als `NominaalNominaal`. Dit betekent dat de referentiecategorie `Niet nominaal` is. Als de overige predictors gelijkblijven is de odds van het volgen van een hbo master versus direct aan het werk gaan voor nominaal afgestudeerden `r Round_and_format(exp(Reg$coefficients[3,1]))` keer zo hoog als de odds van het volgen van een hbo master versus direct aan het werk gaan voor niet nominaal afgestudeerden.
# * Nominaal; wo master vs. werk: de geschatte waarde voor de regressiecoëfficiënt van de variabele Nominaal voor de vergelijking tussen wo master en werk is `r Round_and_format(Reg$coefficients[4,1])` en is niet significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[4,3])`, *p* = `r Round_and_format(Reg$coefficients[4,4])`).[^8] De hoofdcategorie van de variabele Nominaal is `Nominaal`, aangezien de variabele in de resultaten weergegeven is als `NominaalNominaal`. Dit betekent dat de referentiecategorie `Niet nominaal` is. De odds ratio hoeft niet geïnterpreteerd te worden, omdat de regressiecoëfficiënt niet significant verschillend van nul is. Er is dus geen relatie tussen het wel of niet nominaal afstuderen en het volgen voor een wo master versus direct aan het werk gaan.
# * Gemiddeld_cijfer; hbo master vs. werk: de geschatte waarde voor de regressiecoëfficiënt van de variabele Gemiddeld_cijfer is `r Round_and_format(Reg$coefficients[5,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[5,3])`, *p* < 0,0001).[^8] De odds ratio van deze predictor is `r Round_and_format(exp(Reg$coefficients[5,1]))`. Als de overige predictors gelijkblijven is de odds van het volgen van een hbo master versus direct aan het werk gaan `r Round_and_format(exp(Reg$coefficients[5,1]))` keer zo hoog bij een toename van het gemiddelde cijfer met één punt.  
# * Gemiddeld_cijfer; wo master vs. werk: de geschatte waarde voor de regressiecoëfficiënt van de variabele Gemiddeld_cijfer is `r Round_and_format(Reg$coefficients[6,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[6,3])`, *p* < 0,0001).[^8] De odds ratio van deze predictor is `r Round_and_format(exp(Reg$coefficients[6,1]))`. Als de overige predictors gelijkblijven is de odds van het volgen van een wo master versus direct aan het werk gaan `r Round_and_format(exp(Reg$coefficients[6,1]))` keer zo hoog bij een toename van het gemiddelde cijfer met één punt.  
# 
# <!-- ## /TEKSTBLOK: Coefficienten1.R -->
# 
# ## Sterkte van de relatie tussen de predictor en afhankelijke variabele
# 
# <!-- ## TEKSTBLOK: CoefficientenStd1.R -->
# De regressiecoëfficiënten van de predictors Nominaal en Gemiddeld_cijfer zijn significant verschillend van nul voor de keuze tussen het volgen van een hbo master versus direct aan het werk gaan. Voor de keuze tussen het volgen van een wo master en direct aan het werk gaan is alleen de predictor Gemiddeld_cijfer significant. In ieder geval dragen beide predictors bij aan het voorspellen van de variabele Vervolg in het algemeen. Met behulp van de gestandaardiseerde regressiecoëfficiënten kan bepaald worden welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. 
# 
# Standaardiseer alle predictors met de functie `scale()` met als argument de predictor. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabele `Nominaal` om in een numerieke variabele met de waarde 1 voor Nominaal en 0 voor Niet nominaal. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd. Voer nu de *multinomiale logistische regressie* uit met de gestandaardiseerde predictors en bekijk de regressiecoëfficiënten. Deze regressiecoëfficiënten zijn nu gestandaardiseerd.
# <!-- ## /TEKSTBLOK: CoefficientenStd1.R -->
# 
# <!-- ## OPENBLOK: CoefficientenStd2.R -->

# In[ ]:


# Zet de variabele Nominaal om in een numerieke variabele met een 1 voor Nominaal en 0 voor Niet nominaal
Fysiotherapie_Vervolg$Nominaal_dummy <- as.numeric(Fysiotherapie_Vervolg$Nominaal == "Nominaal")

# Standaardiseer de predictors
Fysiotherapie_Vervolg$Nominaal_dummy_stand <- scale(Fysiotherapie_Vervolg$Nominaal_dummy)
Fysiotherapie_Vervolg$Gemiddeld_cijfer_stand <- scale(Fysiotherapie_Vervolg$Gemiddeld_cijfer)

# Stel het regressiemodel op
library(mclogit)
Regressiemodel_gestandaardiseerd <- mblogit(Vervolg ~  Nominaal_dummy_stand + Gemiddeld_cijfer_stand,
                                            Fysiotherapie_Vervolg)

# Laat de gestandaardiseerde coefficienten zien
coefficients(Regressiemodel_gestandaardiseerd)

# Laat de gestandaardiseerde odds ratios zien
exp(coefficients(Regressiemodel_gestandaardiseerd))


# <!-- ## /OPENBLOK: CoefficientenStd2.R -->
# 
# <!-- ## CLOSEDBLOK: CoefficientenStd3.R -->

# In[ ]:


Coefficienten_std <- coefficients(Regressiemodel_gestandaardiseerd)


# <!-- ## /CLOSEDBLOK: CoefficientenStd3.R -->
# 
# <!-- ## TEKSTBLOK: CoefficientenStd4.R -->
# Voor de vergelijking hbo master versus werk is de gestandaardiseerde regressiecoëfficiënt is `r Round_and_format(Coefficienten_std[3])` voor de predictor Nominaal en `r Round_and_format(Coefficienten_std[5])` voor de predictor Gemiddeld_cijfer. Voor de vergelijking wo master versus werk is de gestandaardiseerde regressiecoëfficiënt is `r Round_and_format(Coefficienten_std[4])` voor de predictor Nominaal en `r Round_and_format(Coefficienten_std[5])` voor de predictor Gemiddeld_cijfer. Voor beide vergelijkingen heeft de predictor Gemiddeld_cijfer dus meer invloed op het vervolg dan de predictor Nominaal. De invloed van Gemiddeld_cijfer is het sterkst bij de vergelijking wo master versus werk. De gestandaardiseerde odds ratio van de predictor Gemiddeld_cijfer laat zien dat een toename van één standaardafwijking in het gemiddelde cijfer van een student resulteert in een `r Round_and_format(exp(Coefficienten_std[5]))` zo hoge odds dat de student een wo master gaat volgen ten opzichte van direct aan het werk gaan, als de overige predictors gelijk blijven.
# <!-- ## /TEKSTBLOK: CoefficientenStd4.R -->
# 
# # Uitvoering likelihood ratio toets voor vergelijking twee regressiemodellen
# 
# De *likelihood ratio toets* wordt bij *multinomiale logistische regressie* gebruikt om de significantie van het gehele regressiemodel te toetsen ten opzichte van het interceptmodel. Deze *likelihood ratio toets* kan ook gebruikt worden om te toetsen of twee geneste regressiemodellen onderling verschillen qua model fit. Hoewel deze vergelijking in de casus niet voorbijkomt, wordt deze toch geïllustreerd. Vergelijk hiervoor een model met de predictor Nominaal met een model met de predictors Nominaal en Gemiddeld_cijfer.
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken1.R -->
# Voer de *likelihood ratio toets* uit met de functie `lrtest()` van het package `lmtest` met als argumenten de modelobjecten van de resultaten van de twee regressiemodellen die worden vergeleken (`Model_1` en `Model_2`). Voer eerst de *multinomiale logistische regressie* uit voor beide modellen en vergelijk ze daarna. Bereken ten slotte de Nagelkerke $R^2$ met de functie `r2_nagelkerke(Model_1)` van het package `performance` met als argument het modelobject waarvan de verklaarde variatie berekend moet worden.
# <!-- ## /TEKSTBLOK: ModellenVergelijken1.R -->
# 
# <!-- ## OPENBLOK: ModellenVergelijken2.R -->

# In[ ]:


library(mclogit)

# Stel het regressiemodel op met Nominaal als predictor
Model_1 <- mblogit(Vervolg ~  Nominaal,
                   Fysiotherapie_Vervolg)

# Stel het regressiemodel op met alle predictors
Model_2 <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                   Fysiotherapie_Vervolg)

# Voer de likelihood ratio toets uit
library(lmtest)
lrtest(Model_1, Model_2)

# Bereken de verklaarde variatie (%) van model 1
library(performance)
100*r2_nagelkerke(Model_1)

# Bereken de verklaarde variatie (%) van model 2
100*r2_nagelkerke(Model_2)


# <!-- ## /OPENBLOK: ModellenVergelijken2.R -->
# 
# <!-- ## CLOSEDBLOK: ModellenVergelijken3.R -->

# In[ ]:


library(mclogit)

# Stel het regressiemodel op met Nominaal als predictor
Model_1 <- mblogit(Vervolg ~  Nominaal,
                   Fysiotherapie_Vervolg)

# Stel het regressiemodel op met alle predictors
Model_2 <- mblogit(Vervolg ~  Nominaal + Gemiddeld_cijfer,
                   Fysiotherapie_Vervolg)

# Voer de likelihood ratio toets uit
library(lmtest)
Vergelijking <- lrtest(Model_1, Model_2)

# Bereken de verklaarde variatie (%) van model 1
library(performance)
R2_model1 <- 100*r2_nagelkerke(Model_1)

# Bereken de verklaarde variatie (%) van model 2
R2_model2 <- 100*r2_nagelkerke(Model_2)


# <!-- ## /CLOSEDBLOK: ModellenVergelijken3.R -->
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken4.R -->
# De *likelihood ratio toets* toont aan dat er een significant verschil is in de model fit tussen beide modellen, *&chi;^2^* = `r Round_and_format(Vergelijking$Chisq[2])`, *df* = `r -1 * Vergelijking$Df[2]`, *p* < 0,0001.[^8] Het regressiemodel met predictor Nominaal verklaart slechts `r Round_and_format(R2_model1)`% van de variatie in Vervolg en het regressiemodel met predictoren Nominaal en Gemiddeld_cijfer verklaart `r Round_and_format(R2_model2)`% van de variatie. Het verschil in verklaarde variatie is `r Round_and_format(R2_model2 - R2_model1)`%. Het model met Nominaal en Gemiddeld_cijfer als predictors heeft dus een significant betere model fit dan het model met alleen Nominaal als predictor.
# <!-- ## /TEKSTBLOK: ModellenVergelijken4.R -->
# 
# # Voorspellen en classificeren
# 
# Op basis van het regressiemodel kan voor iedere student de kans op het volgen van een hbo master, een wo master en het direct aan het werk gaan voorspeld worden. De voorspelde kans kan direct vergeleken worden met de observaties om te onderzoeken hoe goed het model voorspeld. Daarnaast is het ook mogelijk om de studenten te classificeren in de categorieën hbo master, wo master en werk op basis van de voorspelde kans. Met behulp van de classificaties kan een classificatietabel gemaakt worden waarmee de kwaliteit van de voorspelkracht van het model beoordeeld kan worden.
# 
# Bepaal eerst de voorspelde kansen met de functie `predict()` met als argumenten het object van het regressie model `Regressiemodel` en `type = response` om aan te geven dat de voorspelde kans bepaald moet worden. Classificeer daarna de studenten op basis van de mogelijkheid met de hoogste voorspelde kans. Maak daarna een tabel met de frequenties per mogelijkheid van de classificaties en maak een classificatietabel voor de classificaties en observaties van de studenten Fysiotherapie. Bereken op basis van de classificatietabel de accuraatheid van de classificaties.

# In[ ]:


# Bepaal de voorspelde kansen
Voorspelde_kans <- predict(Regressiemodel,
                           type = "response")

# Classificeer de studenten op basis van de hoogste voorspelde kans
Classificaties <- c()
for (i in 1:nrow(Voorspelde_kans)) {
  Vervolg_opties <- colnames(Voorspelde_kans)
  Classificaties[i] <- Vervolg_opties[Voorspelde_kans[i,] == max(Voorspelde_kans[i,])]
}

# Tabelleer de frequenties per categorie van de classificaties
table(Classificaties)

# Maak een classificatietabel, gebruik de functie factor en het argument levels om aan te geven
# welke categorieën er moeten worden weergegeven
Tabel <- table(Classificaties = factor(Classificaties, levels = c("werk", "hbo master", "WO master")),
               Observaties = Fysiotherapie_Vervolg$Vervolg)
print(Tabel)

# Bereken de accuraatheid
Accuraatheid <- (Tabel["werk","werk"] + Tabel["hbo master","hbo master"] + Tabel["WO master","WO master"]) / sum(Tabel)

Accuraatheid


# De classificatietabel laat zien dat de meerderheid van de studenten correct geclassificeerd is, maar ook dat er veel verkeerde classificaties zijn. Ook valt het op dat er geen enkele student geclassificeerd is met de mogelijkheid hbo master. De accuraatheid van de classificaties van het regressiemodel is `r Round_and_format(100*Accuraatheid)`%.

# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage1.R -->
# Een *multinomiale logistische regressie* is uitgevoerd om te onderzoeken of het vervolg na de bachelor Fysiotherapie (hbo master, wo master of direct aan het werk) gerelateerd is aan het wel of niet nominaal afstuderen en het gemiddelde cijfer van de bachelor van de studenten. Uit het toetsen van de assumpties van *multinomiale logistische regressie* bleek dat er aan alle assumpties is voldaan. De resultaten van de *multinomiale logistische regressie* zijn te vinden in Tabel 4. 
# 
# De *likelihood ratio toets* voor het regressiemodel laat zien dat het opgestelde regressiemodel minimaal één coëfficiënt heeft die significant verschilt van nul, *&chi;^2^* = `r Round_and_format(LR_test$Chisq[2])`, *df* = `r -1 * LR_test$Df[2]`, *p* < 0,0001, $R^2_N$ = `r Round_and_format(100 * R2)`. Voor de vergelijking tussen de mogelijkheden hbo master en direct aan het werk gaan zijn zowel het gemiddelde cijfer (*&beta;* = `r Round_and_format(Reg$coefficients[5,1])`, *z* = `r Round_and_format(Reg$coefficients[5,3])`, *p* < 0,0001) als (*&beta;* = `r Round_and_format(Reg$coefficients[3,1])`, *z* = `r Round_and_format(Reg$coefficients[3,3])`, *p* = 0,007) significante predictors. Voor de vergelijking tussen de mogelijkheden wo master en direct aan het werk gaan is het gemiddelde cijfer (*&beta;* = `r Round_and_format(Reg$coefficients[6,1])`, *z* = `r Round_and_format(Reg$coefficients[6,3])`, *p* < 0,0001) wel een significante predictor, maar het wel of niet nominaal afstuderen (*&beta;* = `r Round_and_format(Reg$coefficients[4,1])`, *z* = `r Round_and_format(Reg$coefficients[4,3])`, *p* = `r Round_and_format(Reg$coefficients[4,4])`) geen significante predictor. De gestandaardiseerde coëfficiënten laten zien dat het gemiddelde cijfer tijdens de bachelor het sterkst gerelateerd is aan het vervolg na de opleiding Fysiotherapie. Om in te schatten welke studenten in aanmerking komen voor een hbo master zijn het wel of niet nominaal afstuderen en het gemiddelde cijfer relevant, maar voor een wo master is alleen het gemiddelde cijfer in de bachelor relevant.
# <!-- ## /TEKSTBLOK: Rapportage1.R -->
# 
# <!-- ## TEKSTBLOK: Rapportage2.R -->
# |                           | Coëfficiënt   | Standaard- fout | z | p-waarde | 95%-betrouwbaar- heidsinterval | Gestandaardiseerde coëfficiënt  | Odds ratio |
# | ------------------------- | ---------| ---------| ---------| ---------| ---------| ---------| ---------| 
# | Intercept; hbo master vs. werk         | `r Round_and_format(Reg$coefficients[1,1])` |  `r Round_and_format(Reg$coefficients[1,2])` |  `r Round_and_format(Reg$coefficients[1,3])` |  < 0,0001*  |  `r Round_and_format(CI[1,1])` - `r Round_and_format(CI[1,2])`  | - | - |
# | Intercept; wo master vs. werk         | `r Round_and_format(Reg$coefficients[2,1])` |  `r Round_and_format(Reg$coefficients[2,2])` |  `r Round_and_format(Reg$coefficients[2,3])` |  < 0,0001*  |  `r Round_and_format(CI[2,1])` - `r Round_and_format(CI[2,2])`  | - | - |
# | Nominaal (Nominaal); hbo master vs. werk | `r Round_and_format(Reg$coefficients[3,1])` |  `r Round_and_format(Reg$coefficients[3,2])` |  `r Round_and_format(Reg$coefficients[3,3])` |   0,007* |  `r Round_and_format(CI[3,1])` - `r Round_and_format(CI[3,2])` | `r Round_and_format(Coefficienten_std[3])`| `r Round_and_format(exp(Reg$coefficients[3,1]))` |
# | Nominaal (Nominaal); wo master vs. werk | `r Round_and_format(Reg$coefficients[4,1])` |  `r Round_and_format(Reg$coefficients[4,2])` |  `r Round_and_format(Reg$coefficients[4,3])` |  `r Round_and_format(Reg$coefficients[4,4])` |  `r Round_and_format(CI[4,1])` - `r Round_and_format(CI[4,2])` | `r Round_and_format(Coefficienten_std[4])`| `r Round_and_format(exp(Reg$coefficients[4,1]))` |
# | Gemiddeld_cijfer; hbo master vs. werk       | `r Round_and_format(Reg$coefficients[5,1])` |  `r Round_and_format(Reg$coefficients[5,2])` |  `r Round_and_format(Reg$coefficients[5,3])` |  < 0,0001* |  `r Round_and_format(CI[5,1])` - `r Round_and_format(CI[5,2])` | `r Round_and_format(Coefficienten_std[5])`| `r Round_and_format(exp(Reg$coefficients[5,1]))` |
# | Gemiddeld_cijfer; wo master vs. werk       | `r Round_and_format(Reg$coefficients[6,1])` |  `r Round_and_format(Reg$coefficients[6,2])` |  `r Round_and_format(Reg$coefficients[6,3])` |  < 0,0001* |  `r Round_and_format(CI[6,1])` - `r Round_and_format(CI[6,2])` | `r Round_and_format(Coefficienten_std[6])`| `r Round_and_format(exp(Reg$coefficients[6,1]))` |
# 
# *Tabel 4. Regressiecoëfficiënten en bijbehorende standaardfouten, z-statistieken, p-waardes, 95%-betrouwbaarheidsintervallen, gestandaardiseerde coëfficiënten en odds ratios.*
# <!-- ## /TEKSTBLOK: Rapportage2.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Multinomial Logistic Regression using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/multinomial-logistic-regression-using-spss-statistics.php
# [^2]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 760-813.
# [^3]: Universiteit van Amsterdam (13 augustus 2016). *Outliers*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).  
# [^4]: Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$.
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 443-446.
# [^7]: Stat 501. *12.4 - Detecting Multicollinearity Using Variance Inflation Factors*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/12/12.4).
# [^8]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^9]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^11]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 338-341.
# [^12]: James, G., Witten, D., Hastie, T. & Tibshirani, R. (2013). *Introduction to Statistical Learning with applications in R*. Springer. Pagina 127-174.
# [^13]: Een ordinale variabele is een categorische variabele waarbij de categorieën geordend kunnen worden. Een voorbeeld is de variabele beoordeling met de categorieën Onvoldoende, Voldoende, Goed en Uitstekend.
# [^14]: Een nominale variabele is een categorische variabele waarbij de categorieën niet geordend kunnen worden. Een voorbeeld is de variabele windstreek (noord, oost, zuid, west) en geslacht (man of vrouw).
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^20]: Stat 504. *8.2 - Baseline-Category Logit Model*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat504/node/173/).
# [^21]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
