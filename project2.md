---
layout: default
img: rosetta
img_url: http://www.flickr.com/photos/calotype46/6683293633/
caption: Rosetta stone (credit&#59; calotype46)
title: Project 2 | Decoding
active_tab: project
-

<div class="alert alert-info">
  Due in-class Wednesday, April 8th.  
</div>

Decoding:  <span class="text-muted">Project 2</span>
=============================================================

Decoding is process of taking input that looks like this:

*honorables sénateurs , que se est - il passé ici , mardi dernier ?*

...And turning into output that looks like this:

*honourable senators , what happened here on Tuesday ?*


In order to decode we need a probability model over pairs
of English and Foreign sentences. You did most of the work of creating
such a model in [Project 1](project1.html). In this assignment, you
will build the rest of the pieces that you need to generate
translations of new sentences.

## Getting Started

There's no starter code for this project, but there will be places
where you're explicitly allowed to use methods from NLTK.

The final result of your project will be a script named <tt>decode.py</tt>
that takes a list Foreign sentences and generates an English
translation of each.

To get there, you'll need to generate several components:

## Language Model

Define a language model module called LM in its own .py file. Your
module should define one or more language model
classes that support the following operations:
   * load(fname), which loads a saved model from the file
     <tt>fname</tt>.
   * store(fname), which saves the current model to the file <tt>fname</tt>.
   * train(fname), which trains the model on the text in the file
     <tt>fname</tt>.
   * prob(word, context), which returns the probability of seeing the
     word word following the context context.
   * logprob(word, context), which returns the negative log
     probability of seeing the word word following the context context
     (you should feel free to re-use your prob function here!)

At its simplest, the language model can just calculate unigram
probabilities (in which case the prob fucntion will ignore context), without any
smoothing. You may want to get that model working first, then use
subclasses to develop more complicated language models. That way, you
can test the integration of a simple model into your full system
first, and changes to the base behavior of your class(es) will only
have to be made once. Remember: if you find yourself copying and
pasting code between classes, that's probably not a good sign! 

As your language model gets more complicated, and/or as you
train with more data, you'll want a way to save your model
and re-load it. At that point, the load and save functions will make
your life much easier. You can take a look at the <tt>pickle</tt> module for
one way to implement them.

To get full base credit for this part (which will get you to
approximately a B on the project without any performance points), you
should implement at least a bigram model with some flavor of smoothing
or interpolation. There's plenty of room to improve over that,
though. Chen and Goodman have a fantastic [survey](handouts/chen_goodman.pdf) of language model
smoothing methods that you can try, including a description of
Modified Kneser-Ney, which remains a state of the art option for
n-gram language models that is still used today.

## Translation Model

Define a translation model module called TM in its own .py file. Your
module should define one or more 
classes that support the following operations:
   * load(fname), which loads a saved model from the file
     <tt>fname</tt>.
   * store(fname), which saves the current model to the file <tt>fname</tt>.
   * train(alignedSents), which trains on a set of aligned sentences
   * prob(e, f), which returns the probability of the English word (or
     phrase) e being generated as a translation of the Foreign word (or
     phrase) f. 
   * logprob(e, f), which returns the negative log probability of the English word (or
     phrase) e being generated as a translation of the Foreign word (or
     phrase) f. (You should feel free to re-use your prob function here!)

To get word alignments, you can use your code from Project 1 or one of the built-in alignment
models in the nltk.align package, which implements IBM Models 1-3. You
may want to get a simple word-level model based on one of the IBM
alignments working first, then use
subclasses to develop more complicated translation models. That way, you
can test the integration of a simple model into your full system
first, and changes to the base behavior of your class(es) will only
have to be made once. Remember: if you find yourself copying and
pasting code between classes, that's probably not a good sign! 

As your translation model gets more complicated, and/or as you
train with more data, you'll want a way to save your model
and re-load it. At that point, the load and save functions will make
your life much easier. Again, look at the <tt>pickle</tt> module for
one way to implement them.

To get full base credit for this part (which will get you to
approximately a B on the project without any performance points), you
should implement a phrase translation model that considers phrases of
at least length 2 (longer phrases are fine). You're encouraged to make
improvements to this part of your system, though, if they will help
your overall performance!

## Decoder

(To be filled in once we've talked about this in class!)

This project will have a bit of a competitive aspect to it -- part of
your grade will depend on how your output compares to that of other groups.

## Ground Rules

<ul>
<li>
   You must work in a group of 3-4, under these conditions: 
   <ol>
   <li>
   You must post the members of your group on the Project 2 Teams
   piazza post. 
   </li>
   <li>
   Everyone in the group will receive the same grade on the assignment. 
   </li>
  </ol>
</li>
<li> You must turn in four things:
  <ol>
  <li>Your translations of the entire dataset, added to your github
  repository as <tt>translations.txt</tt>
  </li>
  <li> Your trained language and translation models, stored in a
  format that your code can understand, added to your github
  repository as <tt>teamname.lm</tt> and <tt>teamname.tm</tt>, along
  with any other tuned parameters stored in a format your code can
  understand as <tt>teamname.parameters</tt>.
  </li>
  <li> The code for your MT system, following the interface described
  above so that we can run it with your parameters, language model, and translation
  model on new sentences.
  </li>
  <li> A short (max 4 pages) report describing how your system works,
  what preprocessing you did of the text, and how well your system
  worked, added to your github repository as <tt>teamname_report.pdf</tt>.
You should tell us not only about your final 
  algorithm, but also things that you tried that didn't work, experiments that
  you did, or other interesting things that you observed while working on it.
  What did you learn? What did you think about the quality of the translations?
  Do you think that more probable translations are better?
  </li>
  </ol>
</li>
<li>
You do not need any other data than what is provided. You should feel 
   free to use additional codebases and libraries <b>except for those
   expressly intended to decode machine translation models</b>. 
   You must write your
   own decoder. If you would like to base your solution on finite-state
   toolkits or generic solvers for traveling salesman problems or
   integer linear programming, that is fine. 
   But machine translation software including (but not limited to)
   Moses, cdec, Joshua, or phrasal is off-limits. You may of course inspect 
   these systems if you want to understand how they work. But be warned: they are
   generally quite complicated because they provide a great deal of other
   functionality that is not the focus of this assignment.
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
