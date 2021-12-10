#!/usr/bin/env python
# coding: utf-8
---
title: "Logistische regressie"
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


set.seed(12345)
source(paste0(here::here(),"/01. Includes/data/41.R"))


# <!-- ## /OPENBLOK: Data-aanmaken.R -->
# 
# # Toepassing
# 
# Gebruik *logistische regressie* om te toetsen of een binaire afhankelijke variabele voorspeld kan worden met twee of meer onafhankelijke variabelen (predictors) en om te toetsen of er een relatie is tussen een predictor en de afhankelijke variabele in aanwezigheid van andere predictors.[^1]

# # Onderwijscasus
# <div id = "casus">
# 
# Vanuit het tutoraat van de opleiding Elektrotechniek van een hogeschool wil de studieloopbaanbegeleider meer persoonsgerichte begeleiding aanbieden om studenten te helpen nominaal af te studeren. Op basis van achtergrondkenmerken van de student en resultaten in het eerste studiejaar wil hij een inschatting maken van de kans dat iemand uitvalt in het eerste studiejaar. De variabelen waarvan hij vermoedt dat er een relatie is met uitval zijn geslacht, gemiddeld eindexamencijfer middelbare school, wel of geen vooropleiding in het mbo en de leeftijd van een student aan het begin van het eerste studiejaar. De studieloopbaanbegeleider zou graag op basis van data uit willen zoeken welke van deze variabelen echt gerelateerd zijn aan uitval. Deze informatie kan hij gebruiken om studenten waar de kans op uitval groter is al vroeg in het vizier te krijgen en de juiste begeleiding aan te bieden.
# 
# Dit onderzoek vertaalt zich in de volgende combinatie van hypothesen, waarbij de nulhypothese zo geformuleerd is dat er geen effect of verschil is en de alternatieve hypothese zo geformuleerd is dat er wel een effect of verschil is. Bij *logistische regressie* wordt er een hypothese opgesteld voor het complete model en hypotheses voor de individuele predictors.
# 
# Hypotheses regressiemodel:
# 
# *H~0~*: Geen enkele predictor van de predictors geslacht, gemiddeld eindexamencijfer middelbare school, wel of geen vooropleiding in het mbo en leeftijd is gerelateerd aan de afhankelijke variabele uitval in het eerste jaar ($\beta_1 = \beta_2 = \beta_3 = \beta_4 = 0$).
# 
# *H~A~*: Ten minste een van de predictors geslacht, gemiddeld eindexamencijfer middelbare school, wel of geen vooropleiding in het mbo en leeftijd is gerelateerd aan de afhankelijke variabele uitval in het eerste jaar (Ten minste één $\beta_i \neq 0, i = 1, 2, 3, 4$).
# 
# Hypotheses individuele predictors (met als voorbeeld de predictor gemiddeld eindexamencijfer middelbare school):
# 
# *H~0~*: Het gemiddeld eindexamencijfer middelbare school heeft geen voorspellende waarde voor wel of niet uitvallen in het eerste jaar in aanwezigheid van de andere predictoren geslacht en eindexamencijfer Wiskunde ($\beta = 0$).
# 
# *H~A~*: Het gemiddeld eindexamencijfer middelbare school heeft voorspellende waarde voor wel of niet uitvallen in het eerste jaar in aanwezigheid van de andere predictoren geslacht en eindexamencijfer Wiskunde ($\beta \neq 0$).
# 
# </div>
# 
# # Logistische regressie
# 
# Het doel van *logistische regressie* is het voorspellen van een binaire afhankelijke variabele op basis van meerdere onafhankelijke variabelen, ook wel predictors genoemd.[^1] Bij *multipele lineaire regressie* wordt het voorspellen van een afhankelijke variabele gedaan met behulp van een regressievergelijking waarin de afhankelijke variabele een lineaire combinatie is van de predictors, i.e. 
# 
# $$ y_i = \beta_0 + \beta_1 * x_{1i} + \beta_2 * x_{2i} + e_i$$
# 
# met $y_i$ als afhankelijke variabele, $\beta_0$ als intercept, $x_{1i}$ en $x_{2i}$ als predictors, $\beta_{1}$ en $\beta_{2}$ als regressiecoefficiënten van predictors, $e_i$ als residu of error en $i$ als indicator van de deelnemer[^19] uit de steekproef. De intercept $\beta_0$ geeft de waarde van de afhankelijke variabele weer als alle predictors gelijk aan nul zijn. De regressiecoefficiënten $\beta_1$ en $\beta_2$ geven de relatie tussen de afhankelijke variabele en de predictor weer. De residu of error $e_i$ is het verschil tussen de geobserveerde waarde van de afhankelijke variabele en de voorspelde waarde op basis van het regressiemodel. 
# 
# Bij *logistische regressie* is de afhankelijke variabele echter binair en heeft dus twee mogelijkheden. Daarom wordt de regressievergelijking zo aangepast dat de kans op een van beide mogelijkheden voorspeld wordt. In deze casus wordt bijvoorbeeld de kans voorspeld dat een student uitvalt in het eerste jaar van de bachelor Elektrotechniek. In onderstaande paragraaf wordt in meer details aan de hand van een aantal wiskundige formules uitgelegd hoe *logistische regressie* werkt. Zonder deze paragraaf te lezen is de toetspagina ook goed te begrijpen. De geïnteresseerde lezer kan
# hier wat meer begrip op doen over de achtergrond van *logistische regressie*.
# 
# ## De achtergrond van logistische regressie
# 
# Bij logistische regressie wordt de kans op een van beide mogelijkheden van de binaire afhankelijke variabele voorspeld op basis van de predictors. In deze casus gaat het bijvoorbeeld om de kans op uitval van een student Elektrotechniek in het eerste studiejaar. Voor een algemene logistische regressievergelijking is dit wiskundig te schrijven als
# 
# $$ P(Y_i = 1) = \pi = \frac{1}{1 + \exp( - [\beta_0 + \beta_1 * x_{1i} + \beta_2 * x_{2i}])}$$
# wat inhoudt dat de kans dat de afhankelijke variabele voor persoon $i$ ($Y_i$) gelijk is aan 1 ($P(Y_i =1)$) gemodelleerd is als een (op het oog wat ingewikkelde) functie van de predictors $x_{1i}$ en $x_{2i}$. Deze kans wordt ook wel met het symbool $\pi$ aangegeven. 
# 
# Om de regressievergelijking duidelijker in beeld te hebben, kan bovenstaande vergelijking omgeschreven worden naar
# 
# $$ \ln(\frac{\pi}{1 - \pi})  = \beta_0 + \beta_1 * x_{1i} + \beta_2 * x_{2i}$$
# waarin $\pi$ dus de kans is. Het omzetten van de kans $\pi$ naar $\ln(\frac{\pi}{1 - \pi})$ wordt de logit transformatie of simpelweg de logit genoemd. Dit laat zien wat er bij *logistische regressie* gebeurt. Met behulp van de regressievergelijking wordt de logit van de kans $\pi$ voorspeld en daarna wordt de logit van $\pi$ omgezet in de kans $\pi$ zelf. Op deze manier is het mogelijk om een regressievergelijking te gebruiken om de kans op een bepaalde uitkomst te bepalen. De logit transformatie wordt in de context van regressiemodellen ook wel een link-functie genoemd.[^10]
# 
# De residuën van het regressiemodel zijn de verschillen tussen de geobserveerde categorie en de voorspelde kans voor die categorie. Als de afhankelijke variabele Uitval zo gecodeerd is dat het de waarde 1 heeft bij uitval en de waarde 0 bij geen uitval, dan voorspelt het regressiemodel de kans op uitval. Een voorspelde kans van 0,82 voor een student die daadwerkelijk uitval, levert een residu op van 1 - 0,82 = 0,18.
# 
# ## Maximum likelihood
# 
# Bij *multipele lineaire regressie* worden de regressiecoëfficiënten bepaald door de som van de gekwadrateerde residuën zo klein mogelijk te maken. Deze methode heet *ordinary least squares* (OLS) en zorgt ervoor dat de voorspellingen van het regressiemodel zo dichtbij als mogelijk zitten bij de echte observaties. Voor meer informatie, zie de [toetspagina](28-Multipele-lineaire-regressie-R.html). Bij *logistische regressie* wordt ook geprobeerd om de voorspellingen van het regressiemodel zo dichtbij de observaties te krijgen als mogelijk, maar er wordt een andere methode[^20] gebruikt. Deze methode heet *maximum likelihood* schatting en heeft als gevolg dat er ook andere statistische toetsen gebruikt worden. Om modellen te vergelijken wordt bij *logistische regressie* de *likelihood ratio toets* gebruikt in plaats van de F-toets. Om regressiecoëfficiënten te toetsen, wordt de *Wald toets* gebruikt in plaats van de t-toets.[^2]<sup>,</sup>[^10]

# ## Likelihood ratio toets voor significantie regressiemodel
# 
# Bij *maximum likelihood* schatting laat de likelihood van het model zien hoe dichtbij de voorspellingen van het model bij de observaties zitten. De likelihood is hoger voor een model waarin de voorspellingen dichterbij de observaties zitten. Op basis van de likelihood wordt het gehele regressiemodel statistisch getoetst en kunnen (geneste) modellen onderling vergeleken worden.
# 
# De eerste vraag bij *logistische regressie* is of het model betere voorspellingen geeft dan een model zonder predictors. Daarom wordt het voorgestelde model vergeleken met een interceptmodel, een model waarin er geen predictors zijn en dus alleen de intercept gebruikt wordt om voorspellingen te maken. De verwachting is dat het voorgestelde model betere voorspellingen genereert en dus een hogere likelihood heeft. De significantie van dit verschil wordt getoetst met een *likelihood ratio* toets. De getoetste nulhypothese is dat de regressiecoëfficiënten van alle predictors gelijk aan nul zijn, wat wil zeggen dat de predictors niet zorgen voor betere voorspellingen. De getoetste alternatieve hypothese is dat minimaal een van de regressiecoëfficiënten van de predictors niet gelijk aan nul is, wat wil zeggen dat het model betere voorspellingen genereert. Als het verschil tussen beide modellen significant is, kunnen de individuele predictors getoetst worden. Als de toename niet significant is, is de analyse afgelopen en is de conclusie dat het voorgestelde model niet in staat is om de afhankelijke variabele beter te voorspellen dan een model zonder predictors.[^2]<sup>,</sup>[^10]
# 
# De *likelihood ratio* toets kan ook gebruikt worden om verschillende regressiemodellen onderling te vergelijken. Hierbij wordt getoetst of er een verschil is tussen de likelihood (de kwaliteit van het model) van beide modellen. Er kan bijvoorbeeld in eerste instantie een model met twee predictors getoetst worden om vervolgens te toetsen of de voorspellingen van het regressiemodel nog beter worden met twee extra predictors. Het verschil in likelihood tussen het model met twee en vier predictors wordt dan getoetst met een chi-kwadraat toets. Hierbij is de nulhypothese dat de extra toegevoegde predictors een regressiecoëfficiënt van nul hebben en de alternatieve hypothese dat minimaal een van de regressiecoëfficiënten van de extra predictors niet gelijk aan nul is. Een eis voor deze toets is dat beide modellen genest zijn. Bij geneste modellen is het ene model te schrijven als een versie van het andere model na het verwijderen van een aantal predictors. In deze casus zou er een model opgesteld kunnen worden waarin alleen de variabelen Eindexamencijfer en Vooropleiding predictors zijn van uitval en een model waarin de de variabelen Geslacht, Eindexamencijfer, Vooropleiding en Leeftijd predictors zijn van uitval. Dit zijn geneste modellen, omdat het eerste model (alleen Eindexamencijfer en Vooropleiding als predictor) een versie is van het tweede model na het verwijderen van de predictors Geslacht en Leeftijd. Het model waarbij de predictors verwijderd zijn, wordt als het ware gereduceerd. Daarom wordt dit het gereduceerde model genoemd. Het model waar de predictors niet verwijderd zijn, wordt het uitgebreide model genoemd. Om modellen met een *likelihood ratio* te vergelijken, moeten ze dus genest zijn. In andere woorden, het verschil tussen beide regressiemodellen moet dus toe te wijzen zijn aan het toevoegen of verwijderen van een of meerdere predictors.[^2]<sup>,</sup>[^10]
# 
# Bij *logistische regressie* is de effectmaat gebaseerd op een vergelijking van de likelihood van het voorgestelde model ten opzichte van de likelihood van het interceptmodel. Een veelgebruikte versie hiervan is Nagelkerke's $R^2$ ($R_N^2$) welke waardes aanneemt tussen 0 en 1. Nagelkerke's $R^2$ is een maat die aangeeft hoe goed een model is. Let op dat Nagelkerke's $R^2$ niet geïnterpreteerd kan worden als verklaarde variantie (zoals $R^2$ bij *multipele lineaire regressie*). Een juiste interpretatie is de verklaarde variatie of model fit.[^2]
# 
# ## Individuele predictors toetsen en interpreteren met de Wald toets
# 
# Als de *likelihood ratio* toets aantoont dat het regressiemodel betere voorspellingen geeft dan het interceptmodel, kunnen de predictors getoetst worden. De regressiecoefficiënten van de predictors en de intercept worden getoetst met een *Wald toets* waarbij de nulhypothese is dat de coefficiënt gelijk aan nul is ($\beta = 0$) en de (tweezijdige) alternatieve hypothese dat de coefficiënt niet gelijk aan nul is ($\beta \neq 0$). Er kan ook een eenzijdige alternatieve hypothese opgesteld worden, bijvoorbeeld als er de verwachting is dat de coefficiënt positief of negatief is. De *Wald-toets* toont in feite aan of er wel of geen relatie is tussen de predictor en afhankelijke variabele in de aanwezigheid van de andere predictoren van het regressiemodel. Bij de *Wald-toets* is de gebruikte toetsstatistiek de z-score.[^2]
# 
# De regressiecoëfficiënten bij *logistische regressie* worden geïnterpreteerd in termen van odds ratios. Odds is een Engelse term en is een variant van kans, namelijk de kans op een gebeurtenis gedeeld door 1 minus de kans op een gebeurtenis ($\frac{\pi}{1 - \pi}$). Bij een kans van  2/3 is de odds $\frac{2/3}{1 - 2/3} = \frac{2/3}{1/3} = 2$. Bij het opgooien van een muntje is de kans op zowel kop als munt 0,5. De odds van zowel kop of munt zijn dus $\frac{1/2}{1 - 1/2} = \frac{1/2}{1/2} = 1$. Een odds ratio is een ratio van twee odds. In de huidige casus wordt onderzocht of geslacht gerelateerd is aan uitval. Stel dat de odds op uitval 1/2 is voor mannen en 1/4 is voor vrouwen. Dan is de odds ratio voor de variabele Geslacht $\frac{1/2}{1/4} = 2$. De odds dat mannen uitvallen is dus twee keer zo hoog als de odds dat vrouwen uitvallen. Dit is de manier om de odds ratio te interpreteren.[^2]
# 
# Regressiecoëfficiënten zijn gelijk aan de logaritme van de odds ratio van de bijbehorende predictor. De odds ratio zelf wordt berekend door de exponent te nemen van de regressiecoëfficiënt. Let bij het interpreteren van odds ratios op dat de betekenis verschillend is voor continue en categorische predictors. In beide gevallen geldt echter dat een toename van één eenheid van de predictor resulteert in een odds die vermenigvuldigd wordt met de exponent van de regressiecoëfficiënt $\exp(\beta)$. De odds zijn dus $\exp(\beta)$ keer zo hoog na een toename van één eenheid van de predictor. Een voorbeeld van de interpretatie van regressiecoëfficiënten is handig voor de huidige casus. Voor elke predictor is een verzonnen waarde van de regressiecoëfficiënt gemaakt die geïnterpreteerd wordt. De intercept wordt bij *logistische regressie* meestal niet geïnterpreteerd.[^2]
# 
# * Geslacht ($\beta = 0,405$): De regressiecoefficiënt van de variabele Geslacht is gelijk aan 0,405. De odds ratio van deze predictor is dus $exp(0,405) = 1,5$. De variabele Geslacht is zo opgesteld dat het mannen vergelijkt ten opzichte van vrouwen als referentiecategorie. Als de overige predictors gelijkblijven is de odds van uitval voor mannen 1,5 keer zo hoog als de odds van uitval van vrouwen. In een regressiemodel worden categorische variabelen omgezet in binaire variabelen met de waarden 0 en 1, omdat dat nodig is om het model te fitten. De variabele Geslacht zou bijvoorbeeld gecodeerd kunnen worden met een 1 voor mannen en een 0 voor vrouwen. Let goed op hoe de categorieën gecodeerd zijn, i.e. welke categorie de waarde 1 en 0 hebben. Dit bepaalt namelijk de interpretatie.
# * Eindexamencijfer ($\beta = 0,182$): De coëfficient van de variabele Eindexamencijfer is gelijk aan 0,182. De odds ratio van deze predictor is dus $exp(0,182) = 1,2$. Als de overige predictors gelijkblijven is de odds van uitval 1,2 keer zo hoog bij een toename van het gemiddeld eindexamencijfer met één punt.
# * Vooropleiding ($\beta = -0,693$): De regressiecoefficiënt van de variabele Vooropleiding is gelijk aan -0,693. De odds ratio van deze predictor is dus $exp(-0,693) = 0,5$. De variabele Vooropleiding is zo opgesteld dat het de vooropleiding mbo vergelijkt ten opzichte van de vooropleiding havo als referentiecategorie. Als de overige predictors gelijkblijven is de odds van uitval voor studenten met de vooropleiding mbo 0,5 keer zo hoog als de odds van uitval voor studenten met havo als vooropleiding. De odds van uitval voor studenten met een mbo vooropleiding is dus eigenlijk 2 (1 / 0,5 = 2) keer zo laag als de odds van uitval voor studenten met een havo vooropleiding. In een regressiemodel worden categorische variabelen omgezet in binaire variabelen met de waarden 0 en 1, omdat dat nodig is om het model te fitten. De variabele Vooropleiding zou bijvoorbeeld gecodeerd kunnen worden met een 1 voor mbo en een 0 voor havo. Let goed op hoe de categorieën gecodeerd zijn, i.e. welke categorie de waarde 1 en 0 hebben. Dit bepaalt namelijk de interpretatie.
# * Leeftijd ($\beta = -0,105$): De coëfficient van de variabele Leeftijd is gelijk aan -0,105. De odds ratio van deze predictor is dus $exp(-0,105) = 0,9$. Als de overige predictors gelijkblijven is de odds van uitval 0,9 keer zo hoog bij een toename van Leeftijd met één jaar. De odds van uitval is dus eigenlijk 1.11 (1 / 0,9) keer zo laag bij een toename van één jaar in leeftijd.

# ## Predictors vergelijkingen door standaardisatie
# 
# Op basis van de regressievergelijking en de Wald-toetsen kan bepaald worden of predictors gerelateerd zijn aan de afhankelijke variabele en wat de invloed van een verandering van de predictor is op de afhankelijke variabele. Een andere relevante vraag is welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. Op basis van de regressiecoëfficienten kan dit niet bepaald worden, omdat de schaal van de predictors verschilt. Het gemiddeld eindexamencijfer varieert tussen de 1 en 10 (waarschijnlijk zijn de meeste waarden hoger dan 5,5) terwijl de variabele Geslacht gelijk is aan een 1 of een 0. 
# 
# Standaardiseer de predictors om de predictors onderling te kunnen vergelijken. Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$. Als het regressiemodel opnieuw geschat wordt met gestandaardiseerde variabelen, kunnen de coëfficiënten onderling vergeleken worden op basis van hun grootte. Een grotere (absolute waarde van de) coëfficient betekent een sterkere relatie met de afhankelijke variabele. De coëfficiënt is nu te interpreteren in termen van standaardafwijkingen. Een toename van één eenheid van de predictor staat voor een toename van een standaardafwijking van deze predictor. Deze toename van één standaardafwijking resulteert in een verandering van de odds die gelijk is aan de exponent van de bijbehorende (gestandaardiseerde) regressiecoëfficiënt.[^2]<sup>,</sup>[^11] De predictor met de hoogste absolute waarde van de regressiecoëfficiënt is het sterkst gerelateerd aan de afhankelijke variabele.
# 
# ## Voorspellen op basis van het regressiemodel
# 
# Een regressiemodel maakt het mogelijk om een afhankelijke variabele te voorspellen op basis van een aantal predictors. Als van een student bekend is wat zijn geslacht, gemiddeld eindexamencijfer, vooropleiding en leeftijd is, kan een voorspelling gemaakt worden van de kans dat die student uitvalt in het eerste studiejaar. Voor alle deelnemers in de steekproef is er een voorspelling. De regressievergelijking maakt het echter ook mogelijk om voor nieuwe deelnemers een voorspelling te maken. Dit wordt een out-of-sample voorspelling genoemd omdat de nieuwe deelnemer niet in de steekproef zit waarop het regressiemodel wordt geschat. Als de studieloopbaanbegeleider een jaar later uitval wil voorspellen van de nieuwe studenten, kan hij de regressievergelijking van het jaar ervoor gebruiken. Een out-of-sample voorspelling geeft vaak een goede indicatie van de kwaliteit van het regressiemodel, omdat de nieuwe deelnemer niet gebruikt zijn om het model te schatten. Als het doel is om het regressiemodel te gebruiken voor het voorspellen van nieuwe deelnemers, dan is de kwaliteit van de out-of-sample voorspellingen van belang.[^2]
# 
# Bij *logistische regressie* wordt de kans op een gebeurtenis voorspeld, in de huidige casus is dat de kans op uitval in het eerste studiejaar. Een kans kan waarden aannemen tussen 0 en 1. De geobserveerde waarden zijn echter binair: wel of geen uitval, dus een 0 of een 1 numeriek gezien. Het voorspellen van een categorische variabele wordt classificatie genoemd en is ook mogelijk met een logistisch regressiemodel. Met behulp van een grenswaarde kunnen de studenten geclassificeerd worden in de categorieën uitval en geen uitval op basis van hun voorspelde kans. Meestal wordt de grenswaarde 0,5 gebruikt om deelnemers te classificeren. Alle deelnemers met een voorspelde kans hoger dan 0,5 ($\pi > 0,5$) worden toegewezen aan de categorie met numerieke waarde 1; de deelnemers met een voorspelde kans van 0,5 of lager ($\pi \leq 0,5$) de waarde 0. Studenten met een voorspelde kans hoger dan 0,5 worden dan in de categorie uitval geclassificeerd en studenten met een voorspelde kans gelijk of lager dan 0,5 in de categorie geen uitval. Er kan natuurlijk ook een andere grenswaarde gebruikt worden om te classificeren op basis van de voorspelde kansen.[^12]
# 
# Op basis van de classificaties en de geobserveerde waarden kan een classificatietabel gemaakt worden. Hierin worden de geobserveerde waarden voor de variabele uitval uitgezet tegenover de geclassificeerde waarden. Een voorbeeld van een classificatietabel voor de huidige casus is te zien in Tabel 1. In de cel linksboven is te zien dat er 40 studenten zijn waarvoor uitval voorspeld is en die ook daadwerkelijk uitgevallen zijn, dit zijn de ware positieven. De cel rechtsonder bevat 150 studenten waarvoor geen uitval is voorspeld en die ook daadwerkelijk niet uitgevallen zijn, dit zijn de ware negatieven. Beide cellen bevatten dus alle studenten die correct geclassificeerd zijn. De cel rechtsboven bevat de studenten die wel uitgevallen zijn, maar waarvoor geen uitval was voorspeld. Dit zijn de vals negatieven aangezien ze als geen uitval (negatief) zijn voorspeld, maar uiteindelijk wel uitgevallen zijn. Ten slotte bevat de cel linksonder de studenten die niet uitgevallen zijn, maar waarvoor wel uitval was voorspeld. Dit zijn de vals positieven aangezien ze als uitval (positief) zijn voorspeld, maar uiteindelijk niet uitgevallen zijn.[^12]
# 
# ||                      | Voorspelling    |
# |-------------| -------------------- | -------------| ------------| 
# ||                            | Uitval | geen uitval|
# |**Observaties**| Uitval      | 40 (ware positieven)    | 10 (valse negatieven)         |
# |               | Geen uitval | 50 (valse positieven)   | 150 (ware negatieven)        |
# 
# *Tabel 1. Classificatietabel van de observaties en classificaties van de uitval van studenten in het eerste jaar van de bachelor Elektrotechniek.*
# 
# Op basis van de classificatiematrix kunnen allerlei maten worden berekend die de kwaliteit van de classificatie aangeven. Bekende maten zijn de accuraatheid, de sensitiviteit en de specificiteit:
# 
# * Accuraatheid: de proportie observaties die correct geclassificeerd is. Te bereken door het aantal ware positieven en ware negatieven te delen door het totaal aantal observaties. In Tabel 1 is de accuraatheid $\frac{40 + 150}{40 + 10 + 50 +150} = 0,76$.
# * Sensitiviteit: de proportie positieven die correct geclassificeerd is. Te berekenen door het aantal ware positieven te delen door het totaal aantal positieven. In Tabel 1 is de sensitiviteit $\frac{40}{40 + 10} = 0,80$ .
# * Specificiteit: de proportie negatieven die correct geclassificeerd is. Te berekenen door het aantal ware negatieven te delen door het totaal aantal negatieven. In Tabel 1 is de specificiteit $\frac{150}{150 + 50} = 0,75$.
# 
# De waarden van de classificatietabel hangen af van de grenswaarde die gebruikt wordt om met de voorspelde kansen te classificeren. Het aanpassen van de grenswaarde zorgt dus voor veranderingen in de sensitiviteit en specificiteit. Als een logistisch regressiemodel gebruikt wordt om te classificeren, kan de grenswaarde dus gebruikt worden om een gewenste sensitiviteit en specificiteit te krijgen. Als de studieloopbaanbegeleider het belangrijk vind om alle studenten die dreigen uit te vallen in zicht te krijgen, is het belangrijk dat uitval goed voorspeld wordt en er dus een hoge sensitiviteit is. Als hij meer waarde hecht aan het correct voorspellen van studenten die niet uitvallen, dan is de specificiteit belangrijker.[^12]
# 
# Er is een maat die de kwaliteit van de classificaties weergeeft onafhankelijk van de grenswaarde die gekozen is. Deze maat heet de Area Under the Curve (AUC) die gebaseerd is op de ROC-curve[^21]. Een AUC van 0,5 betekent dat de classificaties niet beter zijn dan een willekeurige keuze voor de ene of de andere optie. Een AUC 1 betekent dat de classificatie perfect is. Op deze manier kan de kwaliteit van de classificaties voor verschillende modellen vergeleken worden onafhankelijk van de gekozen grenswaarde.[^12]
# 
# # Uitleg assumpties
# 
# Om een valide resultaat te vinden met *logistische regressie*, dient er aan een aantal assumpties voldaan te worden.[^1]<sup>,</sup>[^2] In deze sectie worden de assumpties allen toegelicht en worden de opties bij het niet voldoen aan de assumptie weergegeven. Verderop in de toetspagina worden de assumpties getoetst met de dataset van de onderwijscasus.
# 
# ## Outliers
# 
# Voordat gestart kan worden met *logistische regressie*, moet de data gescreend worden op de aanwezigheid van outliers. Outliers (uitbijters) zijn observaties die sterk afwijken van de overige observaties. Univariate outliers zijn observaties die afwijken voor één specifieke variabele, zoals een student die twintig jaar over zijn studie heeft gedaan. Multivariate outliers zijn observaties die afwijken door de combinatie van meerdere variabelen, zoals een persoon van 18 jaar met een inkomen van €100.000,-. De leeftijd van 18 jaar is geen outlier op zichzelf en een inkomen van €100.000,- is dat ook niet. Echter, de combinatie van beide zorgt ervoor dat de observatie vrij onwaarschijnlijk is.[^9]
# 
# Na het vinden van een outlier is de volgende stap om een goede oplossing voor te outlier te bedenken. Het is van belang hier goed over na te denken en niet zomaar een outlier te verwijderen met als enige argument dat het een outlier is. In het algemeen kan er onderscheid gemaakt worden tussen onmogelijke en onwaarschijnlijke outliers.[^3] Een onmogelijke outlier is een observatie die technisch gezien niet kan kloppen, bijvoorbeeld een leeftijd van 1000 jaar, een negatief salaris of een man die zwanger is. Bij deze outliers is het een optie om de waarde te vervangen als er een overduidelijke fout bij het invoeren van de data is gemaakt. Een andere optie is de waarde te verwijderen. Een onwaarschijnlijke outlier is een observatie die technisch gezien wel kan, maar heel erg afwijkt van de overige observaties. De rijksten der aarde zijn in de stad of het dorp waar zij wonen qua vermogen waarschijnlijk een outlier. Maar het zijn bestaande personen dus het verwijderen van de observatie zou hier foutief zijn. Opties in deze situatie zijn om te overwegen de variabele(n) te transformeren, de outlier gewoon mee te nemen in de analyse of de analyse met en zonder de outlier uit te voeren en beide te rapporteren. Ook is het niet verboden om de outlier toch te verwijderen, maar het is in dat geval wel van belang dit transparant te rapporteren en op een goede wijze te beargumenteren.[^3]
# 
# Bij *logistische regressie* zijn er vier nuttige methoden om outliers te vinden.[^9]
# 
# ### Boxplots en standaardiseren
# 
# Begin voor de analyse met het screenen van de variabelen in de dataset op de aanwezigheid van univariate outliers. Voor continue variabelen bestaat deze screening uit het visualiseren van de variabele met een boxplot en het standaardiseren[^4] van de variabele. Als een observatie een gestandaardiseerde score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. In dat geval wijkt de observatie namelijk meer dan drie standaardafwijkingen af van het gemiddelde van de variabele. Gebruik zowel de boxplot als de standaardisering om outliers te vinden voor continue variabelen.[^3]
# 
# Bij categorische variabelen hebben boxplots en standaardisatie geen zin, omdat het geen variabelen met een continue schaal zijn. Bij categorische variabelen is het nuttig om een overzicht te maken van de bestaande categorieën en bijbehorende aantallen observaties en is het nuttig om te onderzoeken of elke observatie slechts in één categorie past. Doe dit met behulp van tabellen.
# 
# ### Gestandaardiseerde residuën
# 
# De residuën van een logistisch regressiemodel zijn de verschillen tussen de observaties van de afhankelijke variabele en de voorspelde kans. Als er een groot verschil is tussen observatie en voorspelling, zou dat kunnen wijzen op een univariate outlier. Standaardiseer daarom de residuën en onderzoek met een grafiek of er outliers zijn. Als een gestandaardiseerde residu een score van groter dan 3 of kleiner dan -3 heeft, wordt deze beschouwd als een outlier. Op deze manier kunnen outliers bij het regressiemodel kunnen worden geïdentificeerd.[^9]
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
# ## Lineariteit: Box-Tidwell
# 
# Bij *logistische regressie* is de regressievergelijking zo opgesteld dat er een lineaire relatie is tussen elke predictor en de logit van de afhankelijke variabele. Een lineaire relatie houdt in dat de toename of afname van de (logit van de) afhankelijke variabele als gevolg van de toename van de predictor constant is. In tegenstelling tot *multipele lineaire regressie* kan bij *logistische regressie* geen grafiek gemaakt worden om een lineaire relatie te onderzoeken, omdat de afhankelijke variabele binair is. In plaats daarvan is er een statistische toets om te onderzoeken of er een lineaire relatie is tussen de predictor en de logit van de afhankelijke variabele. Bij deze *Box-Tidwell test* wordt er voor elke continue predictor een extra term toegevoegd die bestaat uit het product van de predictor en de logaritme van de predictor. Voor de predictor leeftijd zou dit dus betekenen dat er een extra variabele wordt (Leeftijd * ln[Leeftijd]). Voeg deze interactietermen voor alle continue predictors toe en toets of de regressiecoëfficiënten van deze interactietermen significant zijn. Als dit zo is, dan is er voor die predictor niet voldaan aan de assumptie van lineariteit. Een oplossing hiervoor is het transformeren[^5] van de variabele.[^6]
# 
# ## Multicollineariteit
# 
# Multicollineariteit houdt in dat er een hoge correlatie tussen twee of meerdere predictors is. Er is perfecte multicollineariteit als één predictor een lineaire combinatie is van een of meerdere andere predictors. In andere woorden, de predictor is precies te berekenen op basis van andere predictor(s). In dat geval kan de regressievergelijking niet wiskundig bepaald worden en werkt *logistische regressie* niet. Dit komt zeer weinig voor en is vaak makkelijk op te lossen door goed naar de variabelen die het veroorzaken te kijken en een variabele te transformeren of te verwijderen.[^9]
# 
# Bij een hoog niveau van multicollineariteit kan de regressievergelijking wel geschat worden, maar zijn de uitkomsten minder betrouwbaar. De standaardfouten van de regressiecoëfficiënten worden groter bij meer multicollineariteit en dit levert bij hoge multicollineariteit problemen op. Ook is het lastig om te ontdekken wat per predictor de bijdrage is aan de voorspellingen van de afhankelijke variabele, omdat bepaalde predictors sterk gecorreleerd zijn en overlappen in het deel van de variantie dat ze verklaren.[^9] 
# 
# Multicollineariteit wordt getoetst met de Variance Inflation Factor (VIF) die meet hoe sterk elke predictor gecorreleerd is met de andere predictors. Als de VIF van een predictor hoger dan 10 is, is er multicollineariteit voor die predictor.[^9]<sup>,</sup>[^7] Multicollineariteit kan opgelost worden door een van de predictors die het veroorzaakt te verwijderen uit het model. Een andere optie is een principale componenten analyse (PCA) uitvoeren op de predictoren zodat er een onderliggende variabele gecreëerd wordt (zie Field[^9] voor meer informatie).
# 
# ## Observaties per variabele
# 
# Bij *logistische regressie* is de afhankelijke variabele binair wat betekent dat de variabele twee mogelijkheden heeft. Dit kan een probleem opleveren als er categorische predictors zijn. Voor elke categorie van een categorische predictor moeten er observaties zijn voor beide mogelijkheden van de afhankelijke variabele. Deze assumptie kan onderzocht worden door een kruistabel te maken voor de combinatie van elke categorische predictor en de afhankelijke variabele. Een voorbeeld van een dergelijke kruistabel is te zien in Tabel 2 voor de afhankelijke variabele uitval en predictor vooropleiding. In deze kruistabel is te zien dat er binnen de categorie `mbo` van de predictor vooropleiding nul deelnemers zijn die uitvallen. Deze categorie bevat dus een lege cel en voldoet niet aan de assumptie.[^2]<sup>,</sup>[^6]
# 
# ||                      | Vooropleiding    |
# |-------------| -------------------- | -------------| ------------| 
# ||                            | mbo | havo|
# |**Uitval**     | Uitval      | 0     | 40         |
# |               | Geen uitval | 50    | 160        |
# 
# *Tabel 2. Kruistabel van de observaties voor de afhankelijke variabele Uitval en predictor Vooropleiding waarbij voor de categorie mbo niet alle waarden van de afhankelijke variabele aanwezig zijn.*
# 
# Daarnaast is het met een binaire afhankelijke variabele mogelijk dat er een categorische predictor is die perfect de waarde van de afhankelijke variabele voorspelt. Een voorbeeld hiervan is te zien in Tabel 3, wederom voor de afhankelijke variabele uitval en predictor vooropleiding. De categorie `mbo` bevat alleen studenten die uitgevallen zijn en de categorie `havo` alleen studenten die niet uitgevallen zijn. De predictor vooropleiding voorspelt dus perfect of een student wel of niet gaat uitvallen. Dit fenomeen wordt *complete separation* genoemd en komt af en toe voor als er heel veel predictors aanwezig zijn en weinig observaties. Als dit gebeurt, dan werkt de *maximum likelihood* methode niet.[^6]
# 
# ||                      | Vooropleiding    |
# |-------------| -------------------- | -------------| ------------| 
# ||                            | mbo | havo|
# |**Uitval**     | Uitval      | 50     | 0          |
# |               | Geen uitval | 0      | 200        |
# 
# *Tabel 3. Kruistabel van de observaties voor de afhankelijke variabele Uitval en predictor Vooropleiding waarbij er sprake is van complete separation.*
# 
# Het gevolg van de assumptie voor observaties per variabele zijn dat er extreem hoge regressiecoëfficiënten en standaardfouten worden gevonden of dat de *maximum likelihood* methode niet werkt. Toets daarom deze assumptie door voor elke categorische predictor een kruistabel te maken met de afhankelijke variabele en onderzoek of er lege cellen zijn en of er *complete separation* plaatsvindt. Als er niet aan deze assumptie voldaan is, dan zijn er meerdere oplossingen mogelijk. De categorie die problemen geeft bij de categorische predictor kan verwijderd worden of worden samengevoegd met een andere categorie. Daarnaast kan de hele predictor verwijderd worden. Ten slotte is meer data verzamelen ook een optie als dit mogelijk is.[^6]
# 
# ## Overdispersie
# 
# Bij *logistische regressie* wordt aangenomen dat de residuën niet gecorreleerd zijn. Dit is in principe het geval als alle deelnemers willekeurig in de steekproef zijn opgenomen. Als deelnemers meerdere keren gemeten zijn of gematcht zijn met andere deelnemers, dan is hier geen sprake van en zijn er waarschijnlijk gecorreleerde residuën. *Logistische regressie* is dan niet de juiste analysemethoden, maar *multilevel logistische regressie* kan hiervoor wel gebruikt worden. Bij *logistische regressie* wordt daarom getoetst of er overdispersie is. Overdispersie betekent dat de variantie in de voorspelde kansen groter is dan op basis van het model wordt verwacht. Het gevolg is dat de standaardfouten te laag zijn en er een hogere kans is op type I fouten (onterecht verwerpen van de nulhypothese) bij het toetsen van de significantie van regressiecoëfficiënten.[^2]<sup>,</sup>[^6]
# 
# De dispersieparameter geeft aan of er sprake is van overdispersie. De dispersieparameter hoort in de buurt van 1 te zitten. Als de parameter hoger dan 2 is, is er sprake van overdispersie. De gevolgen van overdispersie kunnen verholpen worden door de standaardfouten van de regressiecoëfficiënten te herschalen op basis van de overdispersie. Het onderzoeken van de dispersieparameter en het corrigeren in het geval van overdispersie worden toegelicht bij het toetsen van de assumpties in deze toetspagina.[^2]
# 
# Er kan ook sprake zijn van onderdispersie: de situatie waarin de variantie in voorspelde kansen kleiner is dan op basis van het model wordt verwacht. Dit leidt tot meer conservatieve toetsen voor de regressiecoëfficiënten en een erg lage kans op type I fouten. Deze situatie is minder erg dan overdispersie en er wordt in dit geval meestal geen correctie uitgevoerd. Dezelfde correctie als bij overdispersie kan echter wel uitgevoerd worden en zorgt er in dit geval voor dat de significantietoetsen minder conservatief worden.[^2]<sup>,</sup>[^6]
# 
# # Toetsing assumpties
# 
# Voer *logistische regressie* uit om te onderzoeken of de uitval in het eerste jaar van de bachelor Elektrotechniek te voorspellen is op basis van het geslacht, gemiddeld eindexamencijfer, de vooropleiding en de leeftijd van studenten. Start met het toetsen van de assumpties en voer vervolgens de *logistische regressie* uit als hieraan voldaan is.
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Voer eerst de *logistische regressie* uit omdat deze nodig is voor het toetsen van assumpties en sla het resultaat op. Interpreteer de resultaten pas na het toetsen van de assumpties. Gebruik de functie `glm()` met als eerste argument de regressievergelijking `Uitval ~ Leeftijd + Geslacht + Vooropleiding + Eindexamencijfer` met links van de tilde de afhankelijke variabele `Uitval` en rechts de vier onafhankelijke variabelen `Geslacht`, `Eindexamencijfer`, `Vooropleiding` en `Leeftijd`. Het tweede argument is de dataset `Uitval_Elektrotechniek` en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden.
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


Regressiemodel <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd,
    data = Uitval_Elektrotechniek,
    family = "binomial")


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# ## Outliers
# 
# ### Boxplots en standaardiseren
# 
# <!-- ## TEKSTBLOK: Outlier1.R -->
# Onderzoek of er univariate outliers zijn met behulp van boxplots en gestandaardiseerde scores voor continue variabelen en tabellen voor categorische variabelen. Begin met de boxplot voor de variabelen `Leeftijd` en `Eindexamencijfer`.
# <!-- ## /TEKSTBLOK: Outlier1.R -->
# 
# <!-- ## OPENBLOK: Outlier2.R -->

# In[ ]:


# Maak een boxplot van de continue variabelen in de dataset
boxplot(Uitval_Elektrotechniek[,c("Leeftijd", 
                                  "Eindexamencijfer")],
        names = c("Leeftijd",
                  "Eindexamencijfer"))


# <!-- ## /OPENBLOK: Outlier2.R -->
# 
# Voor beide variabelen zijn er geen onmogelijke scores en zijn er geen grote afwijkingen. Op basis van de gestandaardiseerde scores kan onderzocht worden of er toch nog een outlier is. Onderzoek de gestandaardiseerde scores door een functie te schrijven die het aantal observaties per variabele telt met een gestandaardiseerde score hoger dan 3 of lager dan -3. Pas deze functie vervolgens toe op de drie continue variabelen in de dataset.
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
Outlier_standaardiseren(Uitval_Elektrotechniek$Eindexamencijfer)
Outlier_standaardiseren(Uitval_Elektrotechniek$Leeftijd)


# <!-- ## /OPENBLOK: Outlier3.R -->

# Beide variabelen hebben nul observaties met een gestandaardiseerde score hoger dan 3 of lager dan -3. Er zijn in deze stap voor de continue variabelen geen outliers gevonden.
# 
# Geslacht, Vooropleiding en Uitval zijn de categorische variabelen in deze dataset. Maak een tabel met de frequenties voor alle categoriëen van deze variabelen om te onderzoeken of hier afwijkende waardes zijn.
# 
# <!-- ## OPENBLOK: Outlier4.R -->

# In[ ]:


table(Uitval_Elektrotechniek$Uitval)
table(Uitval_Elektrotechniek$Geslacht)
table(Uitval_Elektrotechniek$Vooropleiding)


# <!-- ## /OPENBLOK: Outlier4.R -->
# 
# Voor alle drie de categorische variabelen zijn er geen categorieën met opmerkelijke waarden. Er zijn hier dus ook geen outliers.
# 
# ### Gestandaardiseerde residuën
# 
# <!-- ## TEKSTBLOK: Outlier5.R -->
# Onderzoek of er outliers zijn met behulp van de gestandaardiseerde residuën van het regressiemodel. Vind eerst de residuën met de functie `rstandard` met als argument `Regressiemodel` (het object van het regressiemodel). Maak vervolgens een plot en tel het aantal gestandaardiseerde residuën met een waarde hoger dan 3 of lager dan -3.
# <!-- ## /TEKSTBLOK: Outlier5.R -->
# 
# <!-- ## OPENBLOK: Outlier6.R -->

# In[ ]:


# Sla de gestandaardiseerde residuën op
Residu_gestandaardiseerd <- rstandard(Regressiemodel)

# Plot de gestandaardiseerde residuën
plot(Residu_gestandaardiseerd, xlab = "Volgorde", ylab = "Gestandaardiseerde residuën")

# Tel het aantal gestandaardiseerde residuën met een absolute waarde groter dan 3
sum(abs(Residu_gestandaardiseerd > 3))


# <!-- ## /OPENBLOK: Outlier6.R -->
# 
# Er zijn geen gestandaardiseerde residuën met een score hoger dan 3 of lager dan -3 wat er op wijst dat er geen outliers in de data zijn.
# 
# ### Mahalanobis distance
# 
# <!-- ## TEKSTBLOK: Outlier7.R -->
# Onderzoek of er multivariate outliers zijn met behulp van de Mahalanobis distance met behulp van de functie `mahalanobis()`. De Mahalanobis afstand geeft aan in hoeverre een deelnemer afwijkt van het gemiddelde van alle deelnemers voor alle predictors samen. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabelen Geslacht en Vooropleiding om in een numerieke variabele met respectievelijk de waarde 1 voor vrouwen en 0 voor mannen en 1 voor mbo en 0 voor havo. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd.
# 
# Neem vervolgens een subset van de dataset met alleen de predictors en gebruik deze voor de Mahalanobis afstand. Gebruik de functie `mahalanobis()` met als argumenten de dataset `Subset`, de gemiddeldes van elke kolom berekend met `colMeans(Subset)` en de covariantiematrix van de dataset berekend met `cov(Subset)`.
# 
# Bereken daarna de criteriumwaarde op basis van het gewenste significantieniveau en het aantal predictors. Plot de Mahalanobis afstanden en tel het aantal deelnemers met een Mahalanobis afstand groter dan de criteriumwaarde. Het gehanteerde significantieniveau is 0,001.
# <!-- ## /TEKSTBLOK: Outlier7.R -->
# 
# <!-- ## OPENBLOK: Outlier8.R -->

# In[ ]:


# Zet Geslacht om in een numerieke variabele met een 1 voor een vrouw en 0 voor een man
Uitval_Elektrotechniek$Geslacht_dummy <- as.numeric(Uitval_Elektrotechniek$Geslacht == "Vrouw")
Uitval_Elektrotechniek$Vooropleiding_dummy <- as.numeric(Uitval_Elektrotechniek$Vooropleiding == "havo")

# Maak een subset van de dataset met alle predictors
Subset <- Uitval_Elektrotechniek[,c("Geslacht_dummy",
                                    "Eindexamencijfer",
                                    "Vooropleiding_dummy",
                                    "Leeftijd"
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
# Onderzoek of er multivariate outliers zijn met behulp van Cook's afstand. Cook's afstand geeft aan hoeveel invloed het weglaten van een deelnemer heeft op de uitkomsten van het regressiemodel. Gebruik hiervoor de functie `cooks.distance` met als argument  `Regressiemodel` (het object van het regressiemodel). Plot de Cook's afstanden daarna en tel het aantal Cook's afstanden dat groter is dan de criteriumwaarde van 1.
# <!-- ## /TEKSTBLOK: Outlier10.R -->
# 
# <!-- ## OPENBLOK: Outlier11.R -->

# In[ ]:


# Bepaal Cook's afstand voor elke deelnemer
Cooks_afstand <-  cooks.distance(Regressiemodel)

# Plot Cook's afstanden
plot(Cooks_afstand, xlab = "Volgorde", ylab = "Cook's afstanden")

# Tel het aantal Cook's afstanden groter dan de criteriumwaarde van 1
sum(Cooks_afstand > 1)


# <!-- ## /OPENBLOK: Outlier11.R -->
# 
# Er zijn geen deelnemers met een Cook's afstand groter dan de criteriumwaarde van 1. Er lijken dus geen invloedrijke datapunten of multivariate outliers te zijn.
# 
# ## Lineariteit: Box-Tidwell
# 
# Voer de *Box-Tidwell test* uit om te onderzoeken of er een lineaire relatie is tussen de continue predictors en de logit van de afhankelijke variabele. Maak eerst voor elke continue predictor een nieuwe variabele aan die bestaat uit het product van de predictor met de logaritme (`log()`) van de predictor. Voeg daarna deze nieuwe interactietermen toe aan de regressievergelijking en voer de *logistische regressie* uit. Gebruik de functie `glm()` met als eerste argument de regressievergelijking `Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd + Leeftijd_log_leeftijd + Eindexamencijfer_log_eindexamencijfer` met links van de tilde de afhankelijke variabele `Uitval` en rechts de vier onafhankelijke variabelen `Geslacht`, `Eindexamencijfer`, `Vooropleiding` en `Leeftijd` en de interactietermen `Leeftijd_log_leeftijd` en `Eindexamencijfer_log_eindexamencijfer`. Het tweede argument is de dataset `Uitval_Elektrotechniek` en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden.
# 
# <!-- ## OPENBLOK: AssLineariteit1.R -->

# In[ ]:


# Maak de interactievariabelen aan voor de continue predictors Leeftijd en Eindexamencijfer
Uitval_Elektrotechniek$Leeftijd_log_leeftijd <- Uitval_Elektrotechniek$Leeftijd * log(Uitval_Elektrotechniek$Leeftijd)
Uitval_Elektrotechniek$Eindexamencijfer_log_eindexamencijfer <- Uitval_Elektrotechniek$Eindexamencijfer * log(Uitval_Elektrotechniek$Eindexamencijfer)

# Voeg deze interactievariabelen toe aan het regressiemodel en toets het regressiemodel
Regressiemodel_Box_Tidwell <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd + Leeftijd_log_leeftijd + Eindexamencijfer_log_eindexamencijfer,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Bekijk de significantie van de regressiecoëfficiënten
summary(Regressiemodel_Box_Tidwell)


# <!-- ## /OPENBLOK: AssLineariteit1.R -->
# 
# <!-- ## CLOSEDBLOK: AssLineariteit2.R -->

# In[ ]:


# Maak de interactievariabelen aan voor de continue predictors Leeftijd en Eindexamencijfer
Uitval_Elektrotechniek$Leeftijd_log_leeftijd <- Uitval_Elektrotechniek$Leeftijd * log(Uitval_Elektrotechniek$Leeftijd)
Uitval_Elektrotechniek$Eindexamencijfer_log_eindexamencijfer <- Uitval_Elektrotechniek$Eindexamencijfer * log(Uitval_Elektrotechniek$Eindexamencijfer)

# Voeg deze interactievariabelen toe aan het regressiemodel en toets het
Regressiemodel_Box_Tidwell <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd + Leeftijd_log_leeftijd + Eindexamencijfer_log_eindexamencijfer,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Bekijk de significantie van de regressiecoëfficiënten
BT <- summary(Regressiemodel_Box_Tidwell)


# <!-- ## /CLOSEDBLOK: AssLineariteit2.R -->
# 
# Zowel de predictor Leeftijd (*z* = `r Round_and_format(BT$coefficients[6,3])`, *p* = `r Round_and_format(BT$coefficients[6,4])`) als de predictor Eindexamencijfer (*z* = `r Round_and_format(BT$coefficients[7,3])`, *p* = `r Round_and_format(BT$coefficients[7,4])`) heeft geen significante interactieterm.[^8] Er is dus voldaan aan de assumptie van lineariteit.
# 
# ## Multicollineariteit
# 
# <!-- ## TEKSTBLOK: AssMulticollineariteit1.R -->
# Onderzoek of er sprake is van multicollineariteit met behulp van Variance Inflation Factors (VIFs). Bereken de VIFs voor elke predictor met de functie `VIF()` van het package `DescTools` waarbij de functie als argument `Regressiemodel` (het object van het regressiemodel) heeft.
# <!-- ## /TEKSTBLOK: AssMulticollineariteit1.R -->
# 
# <!-- ## OPENBLOK: AssMulticollineariteit2.R -->

# In[ ]:


library(DescTools)

# Bereken de VIF voor elke predictor
VIF(Regressiemodel)


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


# Maak de kruistabel voor de predictor Geslacht
with(Uitval_Elektrotechniek,
     table(Geslacht,
           Uitval))

# Maak de kruistabel voor de predictor Vooropleiding
with(Uitval_Elektrotechniek,
     table(Vooropleiding,
           Uitval))


# <!-- ## /OPENBLOK: ObsperVar1.R -->
# 
# Voor alle categorieën van beide predictors zijn er studenten die wel en niet uitvallen. Dus beide waarden van de afhankelijke variabele zijn aanwezig in alle categorieën. Er is dus ook geen sprake van *complete separation* dus er is aan deze assumptie voldaan.
# 
# ## Overdispersie
# 
# <!-- ## TEKSTBLOK: Dispersie1.R -->
# Bereken de dispersieparameter om te bepalen of er sprake is van overdispersie. Voer hiervoor de *logistische regressie* uit met behulp van de functie `glm()` met als derde argument `family = "quasibinomial"` die ervoor zorgt dat de resultaten gecorrigeerd worden voor de dispersie. Het eerste argument is de regressievergelijking `Uitval ~ Geslacht + Eindexamencijfer +  Vooropleiding + Leeftijd` met links van de tilde de afhankelijke variabele `Uitval` en rechts de vier onafhankelijke variabelen `Geslacht`, `Eindexamencijfer`, `Vooropleiding` en `Leeftijd`. Het tweede argument is de dataset `Uitval_Elektrotechniek`.
# <!-- ## /TEKSTBLOK: Dispersie1.R -->
# 
# <!-- ## OPENBLOK: Dispersie2.R -->

# In[ ]:


# Fit het regressiemodel
Regressiemodel_dispersie <- glm(Uitval ~ Geslacht + Eindexamencijfer +  Vooropleiding + Leeftijd,
    data = Uitval_Elektrotechniek,
    family = "quasibinomial")

# Print de waarde van de dispersieparameter
summary(Regressiemodel_dispersie)$dispersion


# <!-- ## /OPENBLOK: Dispersie2.R -->
# 
# Er is sprake van onderdispersie, aangezien de dispersieparameter (`r Round_and_format(summary(Regressiemodel_dispersie)$dispersion)`) kleiner dan 1 is. Het verschil met 1 is echter niet zo groot en bij onderdispersie wordt er in het algemeen geen correctie uitgevoerd. Voor de *logistische regressie* in deze casus wordt daarom geen correctie uitgevoerd vanwege onderdispersie.

# # Uitvoering
# 
# <!-- ## TEKSTBLOK: Uitvoering1.R -->
# Als alle assumpties zijn getoetst en aan alle assumpties is voldaan, kan de *logistische regressie* uitgevoerd worden. Gebruik de functie `glm()` met als eerste argument de regressievergelijking `Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd` met links van de tilde de afhankelijke variabele `Uitval` en rechts de vier onafhankelijke variabelen `Geslacht`, `Eindexamencijfer`, `Vooropleiding` en `Leeftijd`. Het tweede argument is de dataset `Uitval_Elektrotechniek` en het derde argument `family = "binomial"` geeft aan dat er een *logistische regressie* uitgevoerd moet worden. Voer daarna de *likelihood ratio toets* uit met behulp van de functie `lrtest()` van het package `lmtest` met als argument het object van het regressiemodel (`Regressiemodel`). Sla het model op en presenteer vervolgens een overzicht van de resultaten met de functie `summary()`. Bepaal de 95%-betrouwbaarheidsintervallen van de regressiecoëfficiënten met de functie `confint()`. Bereken ten slotte de Nagelkerke $R^2$ met behulp van de functie `Nagelkerke()` van het package `fmsb`.
# 
# <!-- ## /TEKSTBLOK: Uitvoering1.R -->
# 
# <!-- ## OPENBLOK: Uitvoering2.R -->

# In[ ]:


# Voer de multipele lineaire regressie uit
Regressiemodel <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd,
    data = Uitval_Elektrotechniek,
    family = "binomial")

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
library(fmsb)
NagelkerkeR2(Regressiemodel)


# <!-- ## /OPENBLOK: Uitvoering2.R -->
# 
# <!-- ## CLOSEDBLOK: Uitvoering3.R -->

# In[ ]:


# Voer de multipele lineaire regressie uit
Regressiemodel <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Voer de likelihood ratio toets uit
LR_test <- lrtest(Regressiemodel)

# Presenteer de resultaten
Reg <- summary(Regressiemodel)
F_toets <- Reg$fstatistic
R2 <- NagelkerkeR2(Regressiemodel)[[2]]
CI <- confint(Regressiemodel)


# <!-- ## /CLOSEDBLOK: Uitvoering3.R -->
# 
# ## Significantie regressiemodel
# 
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# Bepaal als eerste stap de significantie van het regressiemodel met behulp van de *likelihood ratio toets*. De *likelihood ratio toets* voor het regressiemodel laat een significant verschil zien tussen het voorgestelde model en een model met alleen een intercept, *&chi;^2^* = `r Round_and_format(LR_test$Chisq[2])`, *df* = `r -1 * LR_test$Df[2]`, *p* < 0,0001, $R^2_N$ = `r Round_and_format(100 * R2)`.[^8] De nulhypothese dat geen enkele predictor van de predictors Geslacht, Eindexamencijfer, Leeftijd en Vooropleiding is gerelateerd aan de afhankelijke variabele Uitval kan verworpen worden. De Nagelkerke $R^2$ is `r Round_and_format(100*R2)`. Omdat de *likelihood ratio toets* voor het gehele model significant is, kunnen de coëfficiënten geinterpreteerd worden.
# <!-- ## TEKSTBLOK: Ftoets1.R -->
# 
# ## Significantie en interpretatie coëfficiënten
# 
# <!-- ## TEKSTBLOK: Coefficienten1.R -->
# Voor de intercept en de regressiecoëfficiënten van de predictors zijn de geschatte coëfficiënt (`Estimate`), de standaardfout van de geschatte coëfficiënt (`Std. Error`) en de z-statistiek (`z value`) en p-waarde (`Pr(>|z|)`) van de *Wald toets* voor de regressiecoëfficiënt weergegeven:
# 
# * Geslacht: de geschatte waarde voor de regressiecoëfficiënt van de variabele Geslacht is `r Round_and_format(Reg$coefficients[2,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[2,3])`, *p* < 0,001).[^8] De hoofdcategorie van de variabele Geslacht is `Vrouw`, aangezien de variabele in de resultaten weergegeven is als `GeslachtVrouw`. Dit betekent dat de referentiecategorie `Man` is. Als de overige predictors gelijkblijven is de odds van uitval voor vrouwen `r Round_and_format(exp(Reg$coefficients[2,1]))` keer zo hoog als de odds van uitval voor mannen.
# * Eindexamencijfer: de geschatte waarde voor de regressiecoëfficiënt van de variabele Eindexamencijfer_Wiskunde is `r Round_and_format(Reg$coefficients[3,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[3,3])`, *p* < 0,0001).[^8] De odds ratio van deze predictor is `r Round_and_format(exp(Reg$coefficients[3,1]))`. Als de overige predictors gelijkblijven is de odds van uitval `r Round_and_format(exp(Reg$coefficients[3,1]))` keer zo hoog bij een toename van het gemiddeld eindexamencijfer met één punt.  De odds van uitval is dus eigenlijk `r Round_and_format(1 / exp(Reg$coefficients[3,1]))` (1 / `r Round_and_format(exp(Reg$coefficients[3,1]))`) keer zo laag bij een toename van het gemiddeld eindexamencijfer met één punt.
# * Vooropleiding: de geschatte waarde voor de regressiecoëfficiënt van de variabele Vooropleiding is `r Round_and_format(Reg$coefficients[4,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[4,3])`, *p* = `r Round_and_format(Reg$coefficients[4,4])`).[^8] Aangezien deze coëfficiënt niet significant is, hoeft hij niet geïnterpreteerd te worden.
# * Leeftijd: de geschatte waarde voor de regressiecoëfficiënt van de variabele Leeftijd is `r Round_and_format(Reg$coefficients[5,1])` en is significant verschillend van 0 (*z* = `r Round_and_format(Reg$coefficients[5,3])`, *p* < 0,0001).[^8] De odds ratio van deze predictor is `r Round_and_format(exp(Reg$coefficients[5,1]))`. Als de overige predictors gelijkblijven is de odds van uitval `r Round_and_format(exp(Reg$coefficients[5,1]))` keer zo hoog bij een toename van leeftijd met één jaar.
# 
# <!-- ## /TEKSTBLOK: Coefficienten1.R -->
# 
# ## Sterkte van de relatie tussen de predictor en afhankelijke variabele
# 
# <!-- ## TEKSTBLOK: CoefficientenStd1.R -->
# De regressiecoëfficiënten van de predictors Eindexamencijfer_Wiskunde en Aantal_Hoorcolleges zijn significant verschillend van nul en dragen dus bij aan het voorspellen van het eindcijfer Methoden & Statistiek. Met behulp van de gestandaardiseerde regressiecoëfficiënten kan bepaald worden welke predictor het sterkst gerelateerd is aan de afhankelijke variabele. 
# 
# Standaardiseer alle predictors met de functie `scale()` met als argument de predictor. Een voorwaarde voor de functie is dat alle variabelen numeriek zijn. Zet daarom eerst de variabelen `Geslacht` en `Vooropleiding` om in een numerieke variabele. Het omzetten van een categorische variabele in een of meer numerieke variabele heet dummycoderen; de variabelen worden vaak dummies genoemd. Gebruik vervolgens de gestandaardiseerde om de *logistische regressie* uit te voeren met de functie `glm()` op dezelfde manier als eerder is gedaan.
# <!-- ## /TEKSTBLOK: CoefficientenStd1.R -->
# 
# <!-- ## OPENBLOK: CoefficientenStd2.R -->

# In[ ]:


# Zet de variabelen om in een numerieke variabele met een 1 voor een man en 0 voor een vrouw
Uitval_Elektrotechniek$Geslacht_dummy <- as.numeric(Uitval_Elektrotechniek$Geslacht == "Vrouw")
Uitval_Elektrotechniek$Vooropleiding_dummy <- as.numeric(Uitval_Elektrotechniek$Vooropleiding == "havo")

# Standaardiseer de predictors
Uitval_Elektrotechniek$Geslacht_dummy_stand <- scale(Uitval_Elektrotechniek$Geslacht_dummy)
Uitval_Elektrotechniek$Vooropleiding_dummy_stand <- scale(Uitval_Elektrotechniek$Vooropleiding_dummy)
Uitval_Elektrotechniek$Leeftijd_stand <- scale(Uitval_Elektrotechniek$Leeftijd)
Uitval_Elektrotechniek$Eindexamencijfer_stand <- scale(Uitval_Elektrotechniek$Eindexamencijfer)

# Stel het regressiemodel op met Geslacht als numerieke variabele
Regressiemodel_gestandaardiseerd <- glm(Uitval ~ Geslacht_dummy_stand + Eindexamencijfer_stand +  Vooropleiding_dummy_stand + Leeftijd_stand,
    data = Uitval_Elektrotechniek,
    family = "binomial")

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
# De gestandaardiseerde regressiecoëfficiënt is `r Round_and_format(Coefficienten_std[3])` voor de predictor Geslacht, `r Round_and_format(Coefficienten_std[2])` voor de predictor Eindexamencijfer, `r Round_and_format(Coefficienten_std[4])` voor de predictor Vooropleiding en `r Round_and_format(Coefficienten_std[5])` voor de predictor Leeftijd. De leeftijd van een student heeft dus de meeste invloed op uitval. De invloed van Geslacht en Eindexamencijfer is ongeveer even groot. De gestandaardiseerde odds ratio van de predictor Leeftijd laat zien dat een toename van één standaardafwijking in de leeftijd van een student resulteert in een `r Round_and_format(exp(Coefficienten_std[5]))` zo hoge odds dat de student uitvalt, als de overige predictors gelijk blijven.
# <!-- ## /TEKSTBLOK: CoefficientenStd4.R -->
# 
# # Uitvoering likelihood ratio toets voor vergelijking twee regressiemodellen
# 
# De *likelihood ratio toets* wordt bij *logistische regressie* gebruikt om de significantie van het gehele regressiemodel te toetsen ten opzichte van het interceptmodel. Deze *likelihood ratio toets* kan ook gebruikt worden om te toetsen of twee geneste regressiemodellen onderling verschillen qua model fit. Hoewel deze vergelijking in de casus niet voorbijkomt, wordt deze toch geïllustreerd. Vergelijk hiervoor een model met de predictoren Eindexamencijfer en Vooropleiding met een model met de predictors Geslacht, Eindexamencijfer, Vooropleiding en Leeftijd.
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken1.R -->
# Voer de *likelihood ratio toets* uit met de functie `lrtest()` van het package `lmtest` met als argumenten de modelobjecten van de resultaten van de twee regressiemodellen die worden vergeleken (`Model_1` en `Model_2`). Voer eerst de *logistische regressie* uit voor beide modellen en vergelijk ze daarna. Bereken ten slotte de Nagelkerke $R^2$ met de functie `NagelkerkeR2(Model_1)$R2` met als argument het modelobject waarvan de verklaarde variatie berekend moet worden.
# <!-- ## /TEKSTBLOK: ModellenVergelijken1.R -->
# 
# <!-- ## OPENBLOK: ModellenVergelijken2.R -->

# In[ ]:


# Stel het regressiemodel op met Vooropleiding en Eindexamencijfer als predictor
Model_1 <- glm(Uitval ~ Eindexamencijfer + Vooropleiding,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Stel het regressiemodel op met alle predictors
Model_2 <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Voer de likelihood ratio toets uit
library(lmtest)
lrtest(Model_1, Model_2)

# Bereken de verklaarde variatie (%) van model 1
library(fmsb)
100*NagelkerkeR2(Model_1)$R2

# Bereken de verklaarde variatie (%) van model 2
100*NagelkerkeR2(Model_2)$R2


# <!-- ## /OPENBLOK: ModellenVergelijken2.R -->
# 
# <!-- ## CLOSEDBLOK: ModellenVergelijken3.R -->

# In[ ]:


# Stel het regressiemodel op met Vooropleiding en Eindexamencijfer als predictor
Model_1 <- glm(Uitval ~ Eindexamencijfer + Vooropleiding,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Stel het regressiemodel op met alle predictors
Model_2 <- glm(Uitval ~ Geslacht + Eindexamencijfer + Vooropleiding + Leeftijd,
    data = Uitval_Elektrotechniek,
    family = "binomial")

# Voer de likelihood ratio toets uit
library(lmtest)
Vergelijking <- lrtest(Model_1, Model_2)

# Bereken verklaarde variantie (%) van model 1
library(fmsb)
R2_model1 <- 100*NagelkerkeR2(Model_1)$R2

# Bereken verklaarde variantie (%) van model 2
R2_model2 <- 100*NagelkerkeR2(Model_2)$R2


# <!-- ## /CLOSEDBLOK: ModellenVergelijken3.R -->
# 
# <!-- ## TEKSTBLOK: ModellenVergelijken4.R -->
# De *likelihood ratio toets* toont aan dat er een significant verschil is in de model fit tussen beide modellen, *&chi;^2^* = `r Round_and_format(Vergelijking$Chisq[2])`, *df* = `r -1 * Vergelijking$Df[2]`, *p* < 0,0001.[^8] Het regressiemodel met predictors Vooropleiding en Eindexamencijfer verklaart slechts `r Round_and_format(R2_model1)`% van de variatie in uitval en het regressiemodel met vier predictoren verklaart `r Round_and_format(R2_model2)`% van de variatie. Het verschil in verklaarde variatie is `r Round_and_format(R2_model2 - R2_model1)`%. Het model met het Geslacht, Eindexamencijfer, Vooropleiding en Leeftijd als predictors heeft dus een significant betere model fit dan het model met alleen Vooropleiding en Eindexamencijfer als predictors.
# <!-- ## /TEKSTBLOK: ModellenVergelijken4.R -->
# 
# # Voorspellen en classificeren
# 
# Op basis van het logistisch regressiemodel kan voor iedere student de kans op uitval voorspeld worden. De voorspelde kans kan direct vergeleken worden met de observaties om te onderzoeken hoe goed het model voorspeld. Daarnaast is het ook mogelijk om de studenten te classificeren in de categorieën Uitval en Geen uitval op basis van de voorspelde kans. Met behulp van de classificaties kan een classificatietabel gemaakt worden waarmee de kwaliteit van de voorspelkracht van het model beoordeeld kan worden.
# 
# Bepaal eerst de voorspelde kansen met de functie `predict()` met als argumenten het object van het regressie model `Regressiemodel` en `type = response` om aan te geven dat de voorspelde kans bepaald moet worden. Classificeer daarna de studenten op basis van de voorspelde kans met de functie `ifelse()` met als eerste argument de conditie die gecheckt wordt `Voorspelde_kans > 0.5`, als tweede argument de classificatie als de student aan de conditie voldoet (`"Uitval"`) en als derde argument de classificatie als de student niet aan de conditie voldoet (`"Geen uitval"`). De conditie stelt dat de voorspelde kans groter dan 0,5 moet zijn. In dat geval is Uitval de classificatie voor die student. Als de kans 0,5 of kleiner is, dan is Geen uitval de classificatie voor die student. Maak daarna een classificatietabel voor de classificaties en observaties van de studenten Elektrotechniek. Bereken op basis van de classificatietabel de accuraatheid, sensitiviteit en specificiteit van de classificaties. Bereken ten slotte de Area Under the Curve (AUC) van het logistisch regressiemodel met behulp van de functie `roc()$auc` van het package `pROC` met als argumenten de observaties `Uitval_Elektrotechniek$Uitval_dummy` en de voorspelde kansen `Voorspelde_kans`.

# In[ ]:


# Bepaal de voorspelde kansen
Voorspelde_kans <- predict(Regressiemodel,
                           type = "response")

# Classificeer de studenten op basis van de voorspelde kans
Classificaties <- ifelse(Voorspelde_kans > 0.5,
                         "Uitval",
                         "Geen uitval")

# Maak een classificatietabel
Tabel <- table(Classificaties = Classificaties,
      Observaties = Uitval_Elektrotechniek$Uitval)
print(Tabel)

# Bereken de accuraatheid
Accuraatheid <- (Tabel["Uitval","Uitval"] + Tabel["Geen uitval","Geen uitval"]) / sum(Tabel)
Accuraatheid

# Bereken de sensitiviteit
Sensitiviteit <- Tabel["Uitval","Uitval"] / (Tabel["Uitval","Uitval"] + Tabel["Geen uitval","Uitval"])
Sensitiviteit

# Bereken de specificiteit
Specificiteit <- Tabel["Geen uitval","Geen uitval"] / (Tabel["Geen uitval","Geen uitval"] + Tabel["Uitval","Geen uitval"])
Specificiteit

# Maak een numerieke versie van de variabele Uitval met een 1 voor Uitval en een 0 voor Geen uitval
Uitval_Elektrotechniek$Uitval_dummy <- as.numeric(Uitval_Elektrotechniek$Uitval == "Uitval")

# Bereken de Area Under the Curve (AUC)
library(pROC)
roc(Uitval_Elektrotechniek$Uitval_dummy,
    Voorspelde_kans)$auc


# In[ ]:


# Bepaal de voorspelde kansen
Voorspelde_kans <- predict(Regressiemodel,
                           type = "response")

# Classificeer de studenten op basis van de voorspelde kans
Classificaties <- ifelse(Voorspelde_kans > 0.5,
                         "Uitval",
                         "Geen uitval")

# Maak een classificatietabel
Tabel <- table(Classificaties = Classificaties,
      Observaties = Uitval_Elektrotechniek$Uitval)

# Bereken accuraatheid
Accuraatheid <- (Tabel["Uitval","Uitval"] + Tabel["Geen uitval","Geen uitval"]) / sum(Tabel)

# Bereken sensitiviteit
Sensitiviteit <- Tabel["Uitval","Uitval"] / (Tabel["Uitval","Uitval"] + Tabel["Geen uitval","Uitval"])

# Bereken specificiteit
Specificiteit <- Tabel["Geen uitval","Geen uitval"] / (Tabel["Geen uitval","Geen uitval"] + Tabel["Uitval","Geen uitval"])

# Bereken de Area Under the Curve (AUC)
library(pROC)
AUC <- roc(Uitval_Elektrotechniek$Uitval_dummy,
    Voorspelde_kans)$auc


# De classificatietabel laat zien dat de meeste studenten correct geclassificeerd zijn. De sensitiviteit is `r Round_and_format(Sensitiviteit)`, dus van de studenten die daadwerkelijk uitvallen is `r Round_and_format_0decimals(100 * Sensitiviteit)`% correct geclassificeerd. De specificiteit is `r Round_and_format(Specificiteit)`, dus van de studenten die niet uitvallen is `r Round_and_format_0decimals(100 * Specificiteit)`% correct geclassificeerd. Dit laat zien dat het model er beter in is om het niet uitvallen van studenten te classificeren dan het uitvallen van studenten. De Area Under the Curve van het logistisch regressiemodel is `r Round_and_format(AUC)`.
# 
# # Rapportage
# 
# <!-- ## TEKSTBLOK: Rapportage1.R -->
# Een *logistische regressie* is uitgevoerd om te onderzoeken of de vooropleiding, de leeftijd, het geslacht en het gemiddeld eindexamencijfer van studenten die starten met de bachelor Elektrotechniek gerelateerd is aan het wel of niet uitvallen in het eerste jaar van deze opleiding. Uit het toetsen van de assumpties van *logistische regressie* bleek dat er aan alle assumpties is voldaan. De resultaten van de *logistische regressie* zijn te vinden in Tabel 1. 
# 
# De *likelihood ratio toets* voor het regressiemodel laat zien dat het opgestelde regressiemodel minimaal één coëfficiënt heeft die significant verschilt van nul, *&chi;^2^* = `r Round_and_format(LR_test$Chisq[2])`, *df* = `r -1 * LR_test$Df[2]`, *p* < 0,0001, $R^2_N$ = `r Round_and_format(100 * R2)`. Het gemiddeld eindexamencijfer (*&beta;* = `r Round_and_format(Reg$coefficients[3,1])`, *z* = `r Round_and_format(Reg$coefficients[3,3])`, *p* < 0,0001), de leeftijd (*&beta;* = `r Round_and_format(Reg$coefficients[5,1])`, *z* = `r Round_and_format(Reg$coefficients[5,3])`, *p* < 0,0001) en het geslacht (*&beta;* = `r Round_and_format(Reg$coefficients[2,1])`, *z* = `r Round_and_format(Reg$coefficients[2,3])`, *p* < 0,0001) zijn significante predictors van het eindcijfer voor het vak, maar de vooropleiding van de student is dit niet (*&beta;* = `r Round_and_format(Reg$coefficients[4,1])`, *z* = `r Round_and_format(Reg$coefficients[4,3])`, *p* = `r Round_and_format(Reg$coefficients[4,4])`). De gestandaardiseerde coëfficiënten laten zien dat de leeftijd van de student het sterkst gerelateerd is aan de kans op uitval. Om in te schatten of een student extra ondersteuning kan krijgen omdat de kans op uitval hoger is, kan de studieloopbaanbegeleider dus rekening houden met het geslacht, de leeftijd en het gemiddeld eindexamencijfer van studenten, maar hoeft hij geen rekening te houden met de vooropleiding.
# <!-- ## /TEKSTBLOK: Rapportage1.R -->
# 
# <!-- ## TEKSTBLOK: Rapportage2.R -->
# |                           | Coëfficiënt   | Standaard- fout | z | p-waarde | 95%-betrouwbaar- heidsinterval | Gestandaardiseerde coëfficiënt  | Odds ratio |
# | ------------------------- | ---------| ---------| ---------| ---------| ---------| ---------| ---------| 
# | Intercept                 | `r Round_and_format(Reg$coefficients[1,1])` |  `r Round_and_format(Reg$coefficients[1,2])` |  `r Round_and_format(Reg$coefficients[1,3])` |  < 0,0001*  |  `r Round_and_format(CI[1,1])` - `r Round_and_format(CI[1,2])`  | - | - |
# | Geslacht (Vrouw) | `r Round_and_format(Reg$coefficients[2,1])` |  `r Round_and_format(Reg$coefficients[2,2])` |  `r Round_and_format(Reg$coefficients[2,3])` |  < 0,01* |  `r Round_and_format(CI[2,1])` - `r Round_and_format(CI[2,2])` | `r Round_and_format(Coefficienten_std[2])`| `r Round_and_format(exp(Reg$coefficients[2,1]))` |
# | Eindexamencijfer       | `r Round_and_format(Reg$coefficients[3,1])` |  `r Round_and_format(Reg$coefficients[3,2])` |  `r Round_and_format(Reg$coefficients[3,3])` |  < 0,0001* |  `r Round_and_format(CI[3,1])` - `r Round_and_format(CI[3,2])` | `r Round_and_format(Coefficienten_std[3])`| `r Round_and_format(exp(Reg$coefficients[3,1]))` |
# | Vooropleiding (mbo)       | `r Round_and_format(Reg$coefficients[4,1])` |  `r Round_and_format(Reg$coefficients[4,2])` |  `r Round_and_format(Reg$coefficients[4,3])` |  < 0,0001* |  `r Round_and_format(CI[4,1])` - `r Round_and_format(CI[4,2])` | `r Round_and_format(Coefficienten_std[4])`| `r Round_and_format(exp(Reg$coefficients[4,1]))` |
# | Leeftijd          | `r Round_and_format(Reg$coefficients[5,1])`0 |  `r Round_and_format(Reg$coefficients[5,2])` |  `r Round_and_format(Reg$coefficients[5,3])` |  `r Round_and_format(Reg$coefficients[5,4])` |  `r Round_and_format(CI[5,1])` - `r Round_and_format(CI[5,2])`  | `r Round_and_format(Coefficienten_std[5])`| `r Round_and_format(exp(Reg$coefficients[5,1]))` |
# *Tabel 1. Regressiecoëfficiënten en bijbehorende standaardfouten, z-statistieken, p-waardes, 95%-betrouwbaarheidsintervallen, gestandaardiseerde coëfficiënten en odds ratios.*
# <!-- ## /TEKSTBLOK: Rapportage2.R -->
# 
# <!-- ## CLOSEDBLOK: Footer.R -->

# In[ ]:





# <!-- ## /CLOSEDBLOK: Footer.R -->
# 
# [^1]: Laerd Statistics (2018). *Binomial Logistic Regression using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/binomial-logistic-regression-using-spss-statistics.php
# [^2]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 760-813.
# [^3]: Universiteit van Amsterdam (13 augustus 2016). *Outliers*. [UvA Wiki Methodologiewinkel](https://wiki.uva.nl/methodologiewinkel/index.php/Outliers).  
# [^4]: Standaardiseren houdt in dat de variabelen getransformeerd worden zodat ze een gemiddelde van 0 hebben en een standaardafwijking van 1. Dit wordt gedaan door voor alle observaties van een variabele eerst het gemiddelde af te trekken en daarna te delen door de standaardafwijking, i.e. $\frac{x_i - \mu}{\sigma}$.
# [^5]: Er zijn verschillende opties om variabelen te transformeren, zoals de logaritme, wortel of inverse (1 gedeeld door de variabele) nemen van de variabele. Zie *Discovering statistics using IBM SPSS statistics* van Field (2013) pagina 201-210 voor meer informatie over welke transformaties wanneer gebruikt kunnen worden.
# [^6]: Tabachnick, B.G. & Fidell, L.S. (2013). *Using multivariate statistics*. Sixth Edition, Pearson. Pagina 443-446.
# [^7]: Stat 501. *12.4 - Detecting Multicollinearity Using Variance Inflation Factors*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/12/12.4).
# [^8]: In dit voorbeeld wordt uitgegaan van een waarschijnlijkheid van 95% c.q. een p-waardegrens van 0,05. De grens is naar eigen inzicht aan te passen; houd hierbij rekening met type I en type II fouten.
# [^9]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 293-356.
# [^10]: Stat 501. *15.1 - Logistic Regression*. [PennState Eberly College of Science](https://online.stat.psu.edu/stat501/lesson/15/15.1). 
# [^11]: Field, A. (2013). *Discovering statistics using IBM SPSS statistics*. Sage. Pagina 338-341.
# [^12]: James, G., Witten, D., Hastie, T. & Tibshirani, R. (2013). *Introduction to Statistical Learning with applications in R*. Springer. Pagina 127-174.
# [^19]: Met een deelnemer wordt het object bedoeld dat geobserveerd wordt, bijvoorbeeld een student, een inwoner van Nederland, een opleiding of een organisatie. Met een observatie wordt de waarde bedoeld die de deelnemer heeft voor een bepaalde variabele. Een deelnemer heeft dus meestal een observatie voor meerdere variabelen.
# [^20]: De reden hiervoor is wiskundig van aard.
# [^21]: Een Receiver Operating Characteristic curve (ROC-curve) is een grafiek met op de x-as 1 minus de specificiteit en op de y-as de sensitiviteit van een classificatiemodel. De ROC-curve is de lijn met daarop punten voor alle combinaties van de sensitiviteit en 1 minus de specificiteit voor verschillende criteriumwaarden op basis waarvan geclassificeerd wordt. Het oppervlak onder de curve (Area Under the Curve; AUC) laat zien hoe goed het model in staat is te classificeren onafhankelijk van de criteriumwaarde die gebruikt wordt. 
