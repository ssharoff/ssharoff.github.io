# In the garden and in the jungle: comparing genres in the BNC and in the Internet

**Serge Sharoff**

The jungle metaphor is quite common in genre studies. The subtitle of
[David Lee's](http://llt.msu.edu/vol5num3/lee/) seminal paper on genre
classification is \`navigating a path through the BNC jungle'. According
to [Adam
Kilgarriff,](http://www.kilgarriff.co.uk/Publications/2001-K-CorpLingWAC.txt)
the BNC is a jungle only when compared to smaller Brown-type corpora,
while it looks more like an English garden when compared to the Web . A
corpus from the web can easily surpass the BNC in size, see 160 million
words of [I EN](http://wackybook.sslmit.unibo.it/pdfs/sharoff.pdf) or 2
billion words of ukWac (<http://wacky.sslmit.unibo.it/>).

However, we know little about the domains and genres of texts in corpora
collected in this way. This webpage lists resources that make I-EN, I-RU
(a web corpus of Russian) and ukWac a bit similar to the BNC.

Below I report two ways of approaching the question of genre
classification. One involves a traditional **typology** of typical genre
labels, as applicable to the Web, for example, texts aimed at
instructing, reporting or entertaining the reader. Another approach
involves designing a **topology** to assess how similar individual texts
are to a prototypical webpage, for example, a typical news item is aimed
at reporting, but some of them also aim at entertaining, so that such
texts are positioned between reporting and entertaining texts.

## Topology for text classification

The topological approach is described in my forthcoming paper:

Serge Sharoff, (2018) Functional Text Dimensions for annotation of Web
corpora. In *Corpora*, **31**:2 [PDF](/publications/2018-ftd.pdf)

The automatic classification model is based on a pre-trained transformer
as hosted on HuggingFace: <https://huggingface.co/ssharoff/genres>.

In the end the Web corpora can be classified to provide data on their
composition:

1.  [BNC](tfhub-bnc.pred.xz). The BNC is NOT a Web corpus. However, it
    is useful to compare the Web corpora to its composition.
2.  [Aranea English](thub-enmaius.genres.xz)
3.  [Aranea Russian](thub-rumaius.genres.xz)
4.  [English TenTen](ententen.pred.genres.xz)

The training resources consist in multi-annotated webpages for Russian
and English (along with translations of some pages into Chinese, French
and German) as described in the following table:

|                 |                |        |         |                                                |
|-----------------|----------------|--------|---------|------------------------------------------------|
| Corpus          | Language       | \#Docs | \#Words | Annotations                                    |
| 5g, part1       | en,de,fr,ru,zh | 113    | 306302  | [5g-p1.tgz](reference/5g-p1.tgz)               |
| 5g, part 2      | en,fr,ru,zh    | 133    | 505468  | [5g-p2.tgz](reference/5g-p2.tgz)               |
| ukWac, random   | en             | 257    | 211549  | [ukwac-sample.tgz](reference/ukwac-sample.tgz) |
| GICR, random    | ru             | 618    | 919972  | [gicr-random.tgz](reference/gicr-random.tgz)   |
| GICR, blogs     | ru             | 285    | 83829   | [gicr-blogs.tgz](reference/gicr-blogs.tgz)     |
| Total           |                | 1406   | 2027120 |                                                |
| All in one-line | en             | 1686   | 2469295 | [file:en.ol.xz](en.ol.xz)                      |
| All in one-line | ru             | 1930   | 2413675 | [file:ru.ol.xz](ru.ol.xz)                      |

## Typology for text classification

The typology and the procedure for automatic annotation of Web texts is
described in:

Serge Sharoff, In the garden and in the jungle: comparing genres in the
BNC and Internet. In [Genres on the
Web](http://www.springer.com/computer/ai/book/978-90-481-9177-2),
Mehler, A., Sharoff., S., Santini, M., (editors) Springer 2010.
[PDF](file:///serge/publications/2010-chp7-genres-web1.pdf)

According to this approach, the texts in I-EN, I-RU and ukWac have been
automatically classified using the following classes:

1.  discussion - all texts expressing positions and discussing a state
    of affairs
2.  information - catalogues, lists (mostly containing incomplete
    sentences)
3.  instruction - how-tos, FAQs, tutorials
4.  propaganda - adverts, political pamphlets
5.  recreation - fiction and popular lore
6.  regulations - laws, small print, rules
7.  reporting - newswires and informative broadcasts, police reports

## Source data

-   English sample: [file:i-en-sample.txt.gz](i-en-sample.txt.gz)
-   Russian sample: [file:i-ru-sample.txt.gz](i-ru-sample.txt.gz)
-   English POS trigrams: [file:i-en.fw](i-en.fw)
-   Russian POS trigrams: [file:i-ru.fw](i-ru.fw)

## Validated samples

-   English BNC: [file:bnc-coded.csv](bnc-coded.csv)
-   English Internet:
    [file:i-en-sample-coded.csv](i-en-sample-coded.csv)
-   Russian Internet:
    [file:i-ru-sample-coded.csv](i-ru-sample-coded.csv)
-   Russian RNC: [file:rrc-x-coded.csv](rrc-x-coded.csv)

## Classified files

-   I-EN: [file:i-en-pred.csv.gz](i-en-pred.csv.gz)
-   ukWac: [file:ukWac-pred.csv.gz](ukWac-pred.csv.gz)
-   I-RU: [file:i-ru-pred.csv.gz](i-ru-pred.csv.gz)

The accuracy of this classification is about 73-84% (see the paper above
for argumentation), so you have one chance in four that a link is not of
the correct type. Let me know if you have ideas on how to improve the
accuracy.

## Legacy classes

I-EN and ukWac files have been also classified using David Lee's BNC
classification (70 genres in total) and the four main genres from the
Brown corpus (press, fiction, nonfiction and misc):

-   I-EN by BNC: [file:i-en-pred-70bnc.csv.gz](i-en-pred-70bnc.csv.gz)
-   I-EN by Brown Corpus:
    [file:i-en-pred-4bc.csv.gz](i-en-pred-4bc.csv.gz)
-   ukWac by BNC:
    [file:ukWac-pred-70bnc.csv.gz](ukWac-pred-70bnc.csv.gz)
-   ukWac by Brown Corpus:
    [file:ukWac-pred-4bc.csv.gz](ukWac-pred-4bc.csv.gz)

The accuracy of this classification has not been validated. Presumably
it is quite low (especially for the 70-genres classification from the
BNC). I made a quick check for the genre distribution for 8310 pages
from [The Guardian](http://guardian.co.uk) website, which is a
newspaper, so it should be classified as 'press' according to the Brown
Corpus, but the genre of feature articles, biographies, reviews can be
different from what is assumed by \`press' in the Brown Corpus (it
corresponds to 'reporting' in the classification used above):

|        |            |
|--------|------------|
| 10.01% | fiction    |
| 29.07% | misc       |
| 16.68% | nonfiction |
| 44.24% | press      |

The following is the distribution of genres assigned to the same set of
8310 pages according to the BNC-trained classifier (only the 10 most
frequent labels are listed):

|        |                                     |
|--------|-------------------------------------|
| 3.14%  | W<sub>newspothersocial</sub>        |
| 3.21%  | W<sub>newspbrdshtnateditorial</sub> |
| 3.29%  | S<sub>speechunscripted</sub>        |
| 3.35%  | W<sub>newspbrdshtnatcommerce</sub>  |
| 3.61%  | W<sub>newspbrdshtnatsports</sub>    |
| 4.16%  | W<sub>fictprose</sub>               |
| 5.57%  | W<sub>poplore</sub>                 |
| 5.93%  | W<sub>newspbrdshtnatarts</sub>      |
| 6.45%  | W<sub>biography</sub>               |
| 8.19%  | W<sub>newspbrdshtnatmisc</sub>      |
| 11.01% | W<sub>misc</sub>                    |

Not all items are treated as coming from newspapers, but many of them
are (in the BNC genre scheme, `brdsht_nat` means \`national
broadsheets', `newsp_other` means either regional or tabloid). Webpages
automatically classified as all forms of `W_newsp` account for 41% of
The Guardian subcorpus in ukWac.

## About

The resources listed on this page have been developed by Serge Sharoff
(Centre for Translation Studies, University of Leeds). Get in touch
[with me](file:///serge/) if you have any comments or suggestions.

***Note: for files from the \`Genres on the Web' colloquium (2007), see
the original [colloquium page](colloquium/)***

***Note: for the description of a Google Research Award project, see
[the project webpage](google.html)***

  

------------------------------------------------------------------------

Serge Sharoff 2015-12-20
