|                       |                                                                 |
|-----------------------|-----------------------------------------------------------------|
| **Official homepage** | <https://ahc.leeds.ac.uk/languages/staff/1137/dr-serge-sharoff> |
| **Google Scholar:**   | <https://scholar.google.co.uk/citations?user=qcnf4QsAAAAJ>      |
| **Semantic Scholar:** | <https://www.semanticscholar.org/author/S.-Sharoff/2506104>     |

## My research interests

Artificial Intelligence and more specifically Large Language Models,
such as ChatGPT, have recently made a profound impact on how we interact
with the computers by providing the ability to produce new texts in
response to prompts. Fundamental research in this area is at the core of
my expertise, I've been doing this since my own PhD in the 1990s. This
pre-dated LLMs, but the idea of linking [language to
meanings](../publications/1999-interact.pdf) remains the same. One of my
recent papers on the [diversity of texts on the
Web](./publications/2020-LREC-anatomy.pdf) has been cited by some of the
[GPT creators from OpenAI](https://arxiv.org/abs/2212.14578). See also
[my collection of curious cases](./GPT-collection.html) of testing
ChatGPT in a range of scenarios.

My research interests are related to three domains: linguistics,
computer science and cognitive science.

Probably the most interesting bit in my recent research is in digital
curation of corpora from the web, cf. the set of available large corpora
and the procedure described at
<http://corpus.leeds.ac.uk/internet.html>, see [the full
paper](../publications/2006-ijcl-proof.pdf). The current set of
resources includes multi-million word corpora for Chinese, English,
French, German, Italian, Polish, Portuguese, Russian and Spanish.

Web corpora can be curated in terms of domains and [genres](webgenres/),
and also via automatic annotation for their linguistic properties, such
as parts of speech, syntactic relations or named entities. The resources
for developing statistical models are relatively modest for many
languages, so I research methods for bootstraping them from related
languages, for example, from
[Russian](publications/2011-dialog-sharoff-nivre.pdf) to
[Ukrainian](publications/2016-HyTra.pdf).

Another example is [ASSIST](http://ucrel.lancs.ac.uk/projects/assist/),
a joint project with Lancaster University, which is about an automatic
procedure for finding translation equivalent using large comparable
corpora (consisting of texts which are not translations of each other).
See a [series of BUCC workshops](https://comparable.limsi.fr/) and a
[recent book](https://link.springer.com/book/10.1007/978-3-031-31384-4)
on the topic. [Its introduction](publications/2023-bucc-intro.pdf) is
available from my list of [publications](publications/list.html).

My approach in linguistics rests on the assumption that language is the
resource for exchanging meanings. My interests in linguistics stretch
from contrastive semantics (how to study words that are used to mean
things in different ways in different languages) to corpus linguistics
(how to study real uses of words in their contexts) to computational
linguistics (how to dewsign computational models for natural language
understanding and generation). See also the page with my tools for
[corpus collection and processing](../webgenres/)

My interests in [communication studies](communication.html) focus on
social practices of communities of language speakers, which result in
creation and maintenance of meanings in the intersubjective space of
people conducting communication. This is directly relevant to
understanding when and how large language models are likely to fail in
the form of biases and hallucinations, because via pre-training on very
large corpora the LLMs have acquired very good knowledge of linguistic
resources used for communication without understanding the conditions
under which the corresponding texts have been produced.

The most convenient access to the list of my publications is via [Google
Scholar](https://scholar.google.com/citations?user=qcnf4QsAAAAJ&view_op=list_works&sortby=pubdate).

See my formal [CV](cv-formal.pdf) as well as my [academic
genealogy](lineage.html) (the list through my supervisors can be traced
back to Leibniz, Poisson and Gauss).

## PhD projects

I am happy to consider applications from prospective PhD students in the
area of my expertise. The following general topics are preferable:

### Automatic Text Classification for Translation

Setting up a translation project usually involves assessing the amount
of time required for translating a text and selecting the most suitable
translator. Modern approaches in Language Technology can do wonders with
text processing, but it is not clear how helpful they can be in the
translation settings. For example, can they help to determine the genre
of a text, its difficulty or suitability to translators? Similar text
classification tools can be also used for tasks related to learning
foreign languages.

*Background references*:

-   Serge Sharoff. [Genre Annotation for the Web: text-external and
    text-internal perspectives](publications/2021-register.pdf).
    *Register Studies*. 2021
-   Serge Sharoff. [Functional text dimensions for the annotation of Web
    corpora](publications/2018-ftd.pdf). *Corpora*, 13(1):65–95, 2018
-   Yu Yuan and Serge Sharoff. [Sentence Level Human Translation Quality
    Estimation with Attention-based Neural
    Networks](publications/2020-LREC-htqe.pdf). In Proc International
    Conference on Language Resources and Evaluation (LREC'20),
    Marseilles, May 2020

### Language adaptation for improving models of lesser-resourced languages

A translation model needs to be applicable to a large number of
languages, while the training resources or linguistic models are often
better developed only for some languages. Language adaptation can be
designed in a way similar to domain adaptation to improve the models of
lesser-resourced languages by taking into account the resources
available for closely related languages, e.g., from French to Romanian.
This can be applied in a range of training scenarios, such as
Part-Of-Speech tagging, text classification, translation quality
prediction, etc.

*Background references:*

-   Serge Sharoff. [Finding next of kin: Cross-lingual embedding spaces
    for related languages](publications/2019-jnle.pdf). *Journal of
    Natural Language Engineering*, 25, 2019
-   Miguel Rios and Serge Sharoff. [Language adaptation for extending
    post-editing estimates for closely related
    languages](publications/2016-pbml.pdf). *The Prague Bulletin of
    Mathematical Linguistics*, 106:181-192, 2016

### Non-parallel resources for translation

Modern Machine Translation is based on "plagiarising" large amounts of
existing translations, which usually come from institutions such as the
United Nations or the European Parliament. This is not enough for many
language directions or for specific domains, such as biomedicine. What
are productive methods to mine information about translations from
non-parallel texts, such as Wikipedia articles on the same topic or news
wire streams in different languages?

*Background references:*

-   Serge Sharoff. [Know thy corpus! Robust methods for digital curation
    of Web corpora](publications/2020-LREC-anatomy.pdf). In Proc LREC,
    Marseilles, May 2020
-   Maria Kunilovskaya and Serge Sharoff. [Building functionally similar
    corpus resources for translation
    studies](publications/2019-RANLP.pdf). In Proc RANLP, Varna,
    September 2019
-   Pierre Zweigenbaum, Serge Sharoff, and Reinhard Rapp. [A
    multilingual dataset for evaluating parallel sentence extraction
    from comparable corpora](publications/2018-lrec-bucc.pdf) In Proc
    LREC, Miyazaki, Japan, May 2018

I have also prepared a [textbook on Comparable
Corpora](https://link.springer.com/book/10.1007/978-3-031-31384-4)
published in the Synthesis Lecture Series. The [introduction to the
book](publications/2023-bucc-intro.pdf) is available.
