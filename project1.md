---
layout: default
img: rosetta
img_url: http://www.flickr.com/photos/calotype46/6683293633/
caption: Rosetta stone (credit&#59; calotype46)
title: Project 1 | Alignment
active_tab: project
---

<div class="alert alert-info">
  Due in-class Wednesday, February 25.
</div>

Alignment <span class="text-muted">Project 1</span>
=============================================================

Aligning words is a key task in machine translation. We start with
a large _parallel corpus_ of aligned sentences. For example, we might
have the following sentence pair from the proceedings of the bilingual 
Canadian parliament:

*le droit de permis passe donc de $ 25 à $ 500*.

*we see the licence fee going up from $ 25 to $ 500*.

Getting documents aligned at the _sentence_ level like this is
relatively easy: we can use paragraph boundaries and cues
like the length and order of each sentence. But to learn a translation
model we need alignments at the _word_ level. That's where you come
in. **Your task is to write a program that aligns words 
automatically.** For example, given the sentence above, your program
would ideally output these pairs:

*le -- the,
droit -- fee,
permis -- license,
passe -- going,
passe -- up,
donc -- from,
$ -- $,
25 -- 25,
à -- to,
$ -- $,
50 -- 50*

Your program can leave words unaligned (e.g. *we* and *see*) or 
multiply aligned (e.g. *passe* aligned to *going up*). It will be
faced with difficult choices. Suppose it sees this sentence pair:

*I want to make it clear that we have to let this issue come to a vote today*.

*il est donc essentiel que cette question fasse le objet de un vote aujourd' hui .*

Your program must make a choice about how to align the words of the non-literal
translations *I want to make it clear* and *il est donc essentiel*. Even
experienced bilinguals will disagree on examples like this. So word alignment
does not capture every nuance, but it is still very useful.

Getting Started
---------------
One team will work on each of the five extension choices listed under
"Options." We'll sign up for these groups in class, and the group
members will be added to this page. 

You must have git and python 3 on your system to run the assignment.
Once you've confirmed this, go to your fork's GitHub page, copy the clone URL on the right-hand side of the screen (we'll call this <fork-url>). run this command:

    git clone https://github.com/hmc-cs159-spring2015/aligner-<option>.git

where "\<option\>" is the name of the option team that you want to
join. (This page will be updated when the group code forks are available).

In your code directory you will find a python program called
`align`, which contains a complete but very simple alignment algorithm.
For every word, it computes the set of sentences that the word appears in. 
Intuititvely, word pairs that appear in similar sets of sentences are likely
to be translations. Our aligner first computes the similarity of these sets  with
[Dice's coefficient](http://en.wikipedia.org/wiki/Dice's_coefficient/). Given
sets $$X$$ and $$Y$$, Dice's coefficient is:

<p>$$\delta(X,Y) = \frac{2 \times |X \cap Y|}{|X| + |Y|}$$</p>

For any two sets $$X$$ and $$Y$$, $$\delta(X,Y)$$ will be a number between
0 and 1. The baseline aligner will align any word pair with a 
coefficient over 0.5. Run it on 1000 sentences:

    python align --train 1000 --accuracy

This compares the alignments against human-produced alignments, computing 
[alignment error rate](http://aclweb.org/anthology-new/P/P00/P00-1056.pdf), 
which balances precision and recall. It will also show you the comparison 
in a grid. Look at the terrible output of this heuristic method -- it's 
better than chance, but not any good. Try training on 10,000 sentences:

    python align -n 10000 | python score-alignments 

Performance should improve, but only slightly! Try changing the
threshold for alignment. How does this affect alignment error rate?

The Challenge
-------------

Your task is to _improve the
alignment error rate as much as possible_. It shouldn't be hard: you've 
probably noticed that thresholding a Dice coefficient is a bad idea because 
alignments don't compete against one another. A good way to correct this is 
with a probabilistic model like IBM Model 1. It forces all of the English 
words in a sentence to compete as the explanation for each foreign word.

Formally, IBM Model 1 is a probabilistic model that generates each word of 
the foreign sentence $${\bf f}$$ independently, conditioned on some word 
in the English sentence $${\bf e}$$. Given $${\bf f}$$, the joint probability of 
an alignment $${\bf a}$$ and translation $${\bf e}$$ factors across words: 
$$P({\bf f}, {\bf a} | {\bf e}) = \prod_i P(a_i = j | |{\bf e}|) \times P(f_i | e_j)$$. In 
Model 1, we fix $$P(a_i = j | |{\bf e}|)$$ to be uniform 
(i.e. equal to $$\frac{1}{|{\bf e}|}$$), so this probability
depends only on the word translation parameters $$P(f | e)$$. But where do
thes parameters come from? You will first learn them from the data using
expectation maximization (EM), and then use them to align. EM attempts to
maximize the *observed* data likelihood $$P({\bf e}|{\bf f})$$, which does not contain
alignments. To do this, we marginalize over the alignment variable:

<p>$$P({\bf e}|{\bf f}) = \prod_i \sum_j P(a_i = j | |{\bf e}|)$$</p>

This problem can't be solved in closed form, but we can iteratively
hill-climb on the likelihood by first fixing some parameters, computing
expectations under those parameters, and maximizing the likelihood as
treating expected counts as observed. To compute the iterative update, for 
every pair of an English word type $$e$$ and a French word type $$f$$, 
count up the expected number of times $$f$$ aligns to 
$$e$$ and normalize over values of $$e$$. That will give you a new
estimate of the translation probabilities $$P (f |e)$$, which leads 
to new expectations, and so on. For more detail, read 
[this note](http://www.cs.jhu.edu/~alopez/papers/model1-note.pdf). We
recommend developing on a small data set (1000 sentences) with a few 
iterations of EM. When you see improvements on this small set, try it out on
the complete data.

Developing a Model 1 aligner will be enough to eearn a passing grade. But alignment isn't a solved problem, and the goal of
this assignment isn't for you to just implement a well-known algorithm. To 
get full credit you **must** experiment with at least one additional
model of your choice and present your findings. One team will work on
each of the options described below.

Options
-

* Team Diagonal (Josh, Ben, and Erin): Implement
  [a model that prefers to align words close to the diagonal](http://aclweb.org/anthology/N/N13/N13-1073.pdf).
* Team HMM (Hayden, Mai, Maury, Shannon): Implement an
  [HMM alignment model](http://aclweb.org/anthology-new/C/C96/C96-2141.pdf).
* Team Combination (Hannah, Tasman, Mechana): Train a French-English model and an English-French model and [combine their predictions](http://aclweb.org/anthology-new/N/N06/N06-1014.pdf).
* Team Supervised Discriminative (Sisi, Emily, Michael): Train a [supervised discriminative alignment model](http://aclweb.org/anthology-new/P/P06/P06-1009.pdf) on the annotated development set.
* Team Unsupervised Discriminative (Coline, Emma, James): Train an [unsupervised discriminative alignment model](http://aclweb.org/anthology-new/P/P11/P11-1042.pdf).
 
If you get your extension working and want to try other things, you're
welcome to, as long as you follow the ground rules:

Ground Rules
------------

* You must work with a group, and only one group can work on each
  extension. We will start group sign-ups in class on Wednesday,
  February 11.
* Everyone in the group will receive the same grade on the assignment.
* Your group grade will be based on the quality and content of your
  final presentation, as well as on a review of the code that you submit.
* You are encouraged to post early (and often!) on Piazza sharing your
current progress on the development set. Some points will be awarded
based on how well your final alignment system completes its task.
* You may only use data or code resources other than the ones we
  provide _with advance permission_. We will ask you to make 
  your resources available to everyone. If you have a cool idea 
  using the Berkeley parser, or a French-English dictionary, that's 
  great. But we want everyone to have access to the same resources, 
  so we'll ask you to share the parses. This kind of 
  constrained data condition is common in real-world evaluations of AI 
  systems, to make evaluations fair. A few things are off-limits:
  Giza++, the Berkeley Aligner, or anything else that
  already does the alignment for you. You must write your
  own code.
* If you want to do system combination, you can join
  forces with your classmates for the "best system" points. Each group
  will still be expected to give their own presentation.


Presentations
-
Presentations will take place on the day that the project is due, and
all group members will be expected to participate. You will have 15
minutes total (12 minutes + 3 minutes for questions) to present. Your
presentation should match the format of a research talk, and should include:
1. The motivation for your extension. What limitations of IBM Model 1
   does it attempt to improve on?
2. A clear, mathematical description of your algorithm. You don't have
   to go into detail on proofs, but your audience should be able to
   understand the important parts of your approach.
3. A quantitative summary of how well your approach worked.
4. An qualitative analysis of the approach, and comments on what you
   think would be the biggest next step to improve the alignments you generated.


If you have any questions or you're confused about anything, just ask.

*Credits: This assignment is adapted from one originally developed by 
[Philipp Koehn](http://homepages.inf.ed.ac.uk/pkoehn/)
and later modified by [John DeNero](http://www.denero.org/). It
incorporates some ideas from
[Chris Dyer](http://www.cs.cmu.edu/~cdyer) and [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/).*
