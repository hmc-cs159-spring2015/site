---
layout: default
img: rosetta
img_url: http://www.flickr.com/photos/calotype46/6683293633/
caption: Rosetta stone (credit&#59; calotype46)
title: Project 3 | Evaluation
active_tab: projects
---

<div class="alert alert-info">
This project is due Wednesday April 29th, in class.
</div>

Evaluation:  <span class="text-muted">Project 3</span>
=============================================================

Machine translation systems are typically evaluated through relative
ranking. For instance, given the following German sentences:

*Die Prager Börse stürzt gegen Geschäftsschluss ins Minus.*

*Nach dem steilen Abfall am Morgen konnte die Prager Börse die Verluste korrigieren.*

...One machine translation system produces this output:

*The Prague stock exchange throws into the minus against closing time.*

*After the steep drop in the morning the Prague stock exchange could correct the losses.*

...And a second machine translation system produces this output:

*The Prague stock exchange risks geschäftsschluss against the down.*

*After the steilen waste on the stock market Prague, was aez almost half of the normal tagesgeschäfts.*

A plausible ranking of the translation systems would place the first
system higher than the second. While neither translation is perfect, the 
first one is clearly easier to understand and conveys more of the original
meaning. *Your challenge is to write a program that ranks the systems in 
the same order that a human evaluator would.*

There is great need to evaluate translation systems: to 
decide whether to purchase one system or another, or to assess incremental
changes to a system --- since, as you saw in the first two assignments,
there are many choices in the design of a system that naturally lead to
different translations. Ideally such comparisons between systems should be 
done by humans, but human rankings are slow and costly to obtain, making 
them less feasible when comparisons are must be done frequently or between 
large numbers of systems. Furthermore, as you saw in class, it is possible
to use machine learning techniques to directly optimize machine translation 
towards an objective function. If we could devise a function that 
correctly ranked systems, we could, in principle achieve better translation
through optimization. Hence automatic evaluation is a topic of intense study.
 
## Getting Started

In your team's repository, we have provided you with a very simple
evaluation program written in Python. There is also a directory containing
a development dataset and a test dataset. Each dataset consists of 
a human translation and many machine translations of some German documents.
The evaluator compares each machine translation to a human 
*reference translation* sentence by sentence, computing how many words 
they have in common. It then ranks the machine translation systems according 
to the percentage of words that also appear in the reference. Note that while we
collect statistics for each sentence, and the best system on each sentence
will vary, the final ranking is at the system level.
Run the evaluator on the development data using this command:

<tt>evaluate.py -r dev/reference -s dev/source dev/system* &gt; hyp.dev</tt>

This runs the evaluation and stores the final ranking in 
<tt>output</tt>. You can see the rank order of the systems simply by looking
at the file &mdash; the first line is the best system, the second is second
best, and so on. To calculate the correlation between this ranking and a 
human ranking of the same set of systems, run the command:

<tt>grade.py --ref answer_key.dev --hyp hyp.dev -v </tt>

This command computes 
<a href="http://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient">Spearman's rank correlation coefficient</a>
(rho) between the automatic ranking
and a human ranking of the systems (see Section 4 of 
<a href="http://aclweb.org/anthology-new/W/W11/W11-2103.pdf">this paper</a> for an explanation
of how the human rankings were obtained). A rho of 1 means that the rankings
are identical; a rank of zero means that they are uncorrelated; and a negative
rank means that they are inversely correlated.

You should also rank the test data, for which we did not provide human
rankings. To do this, run the command:

<tt>evaluate.py -r test/reference -s test/source test/system* &gt; test_output.txt</tt>

You can confirm that the output is a valid ranking of the test data 
using the check command:

<tt>sanityCheck test_output.txt</tt>

Your ranking should be a total ordering of the systems &mdash; ties are not allowed.

## The Challenge

Improving the evaluation algorithm should cause rho
to increase. Your task for this assignment is to <b>obtain a
Spearman's rank correlation coefficient that is as high as possible on the 
test data.</b> Whoever obtains the highest rho will receive the most 
points. 

The first thing you should do to improve over the default system is to implement the 
well-known <a href="http://aclweb.org/anthology-new/P/P02/P02-1040.pdf">BLEU</a>
metric for $$N=4$$ with uniform weights $$w_n=\frac{1}{4}$$. Be sure
to implement the modified precision and brevity penalty as described
in the paper. Generate your rankings of the test systems using just
BLEU and store that ranking in a new file <tt>test\_bleu.txt</tt>.

Implementing basic BLEU will be enough to get a B on the project. The
rest of the project points will depend on how much you can improve
your correlation with the human judgments on the test systems. You may find it useful to experiment with BLEU's parameters,
or to retokenize the data in some way. However, there are many, many 
alternatives to BLEU &mdash; the topic of evaluation is so popular that
Yorick Wilks, a well-known researcher, once remarked that  
*more has been written about machine translation evaluation than about
machine translation itself*. Some of the techniques people have tried
may result in stronger correlation with human judgement, including:

<ul>
  <li><a href="http://aclweb.org/anthology-new/W/W11/W11-2105.pdf">Incorporating recall statistics into the metric.</a></li>
  <li><a href="http://aclweb.org/anthology-new/W/W07/W07-0734.pdf">Stemming the words, or counting synonyms as matches.</a></li>
  <li><a href="http://aclweb.org/anthology-new/W/W11/W11-2112.pdf">Analyzing predicate-argument structure and distributional semantics of the translations</a>.</li>
  <li><a href="http://aclweb.org/anthology-new/W/W11/W11-2106.pdf">Combining many of these features with machine learning techniques</a> (you could train on the development data).</li>
  <li><a href="http://aclweb.org/anthology-new/W/W11/W11-2113.pdf">Combining only simple features with machine learning</a>.</li>
</ul>

But the sky's the limit! There are many, many ways to automatically evaluate
machine translation systems, and you can try anything you want as long as you follow the ground rules:

## Ground Rules

<ul>
<li>
   You must work in a group of 4, under these conditions: 
   <ol>
   <li>
   Sign up for groups in class on April 15.
   </li>
   <li>
   Everyone in the group will receive the same grade on the assignment. 
   </li>
  </ol>
</li>
<li> You must turn in three things:
  <ol>
  <li>Your rankings of the test set systems, added to your github repository as
  <tt>test\_bleu.txt</tt> and (if you made improvements) <tt>test\_final.txt</tt>. </li>
  <li> The code for your ranking algorithm system, which should work
  with the same command-line arguments as the given code. Your code
  should be clear enough that we can reproduce your results on the
  test set. 
  </li>
  <li> A short (2-4 pages) report describing how your system works,
  what preprocessing you did of the text, and how well your system
  worked (in terms of performance on the development set), added to your github repository as <tt>teamname_report.pdf</tt>.
You should tell us not only about your final algorithm, but also things that you tried that didn't work, experiments that
  you did, or other interesting things that you observed while working
  on it. What was your best correlation score on the development set?
  What did you learn? What aspects of good translations were you good
  at identifying? What aspects of a good or bad translation does your
  system still not handle well?
  </li>
  </ol>
  </li>
  <li>
  You should be prepared to talk about your system and results on the
  last day of class, but you do not need to prepare slides for a
  formal presentation. 
  </li>
<li>
You do not need any other data than what is provided. You should feel 
   free to use additional codebases and libraries <b>except for those
   expressly intended to evaluate machine translation systems</b>. 
   You must implement BLEU and any extensions you choose yourself. 
   If you aren't sure whether 
   something is permitted, ask me.
</li>
</ul>
If you have any questions or you're confused about anything,
<a href="https://piazza.com/class/i4ugmh3p8hx459">just ask</a>.

*Credits: This assignment is adapted from one originally developed by 
[Philipp Koehn](http://homepages.inf.ed.ac.uk/pkoehn/)
and later modified by [John DeNero](http://www.denero.org/). It
incorporates some ideas from
[Chris Dyer](http://www.cs.cmu.edu/~cdyer) and [Chris Callison-Burch](http://www.cis.upenn.edu/~ccb/).*
