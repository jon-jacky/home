
Commonplace Book: a book into which notable extracts from other works
are copied for personal use.

Begun November 2016.
Successor to <http://jon-jacky.github.io/home/links.html>, Spring 2001 -- July 2017

11 Apr 2019

- <https://news.ycombinator.com/item?id=1476059>, comments by *dasht* on
  GNU HURD: Altered visions and lost promise:
  "I was one of the hacker employees of the FSF back in the early days
  of the HURD project.  ...  The original vision for the GNU system ...
  was to - sure - grow a unix clone, but then to build a user space
  that much more closely resembled that of lisp machines.
  Emacs (with its lisp extensibility) was taken to be a paradigm
  for how interactive programs might work. ...

  Interactive programs should be uniformly customizable, extensible,
  and self-documenting - roughly in the manner of Emacs.
  That sounds like a trite thing. After all, the programs we wound up with
  have all three traits. ...
  I mean something more specific but hard to convey concisely. Most of
  (our present programs are) not written as extension packages,
  which betrays an architectural weakness in contrast to emacs.
  (Their) interaction model and customization model is awkward and ad hoc,
  compared to emacs. (Their) on-line documentation ... is not designed
  in a way such that its enhancement is a natural part of writing extensions.
  ... the architectural approach (emacs) takes is vastly more sane than
  what the interactive programs we wound up with use. ...
  (These) observations apply (to Gimp), to the Open Office suite,
  to Gnome, to Firefox, and more.
  We have a big, barely maintainable heap of discordant and vaguely
  conceived functionality.

  On a more mundane level, even the command line got horked.  ...
  (we wanted) a shell much more like the much-loved shell on the Tops-20
  operating system. The (shell) was supposed to be gradually refined
  so that those standard "*--help*" messages could be automagically
  used by the shell to intelligently prompt for arguments to a program.

  I guess I should add that a lisp - most of us that I knew assumed Scheme -
  would figure prominently as the main extension language (rather than Emacs lisp).
  Why a lisp? Well, it had a proven track record and that was our aesthetic
  -- I'll leave it at that."

- <https://www.recurse.com/blog/11-exploring-emacs>, Exploring Emacs:
  "Emacs makes it easy to see the code behind its commands. ...
  For instance, if you want to see how a particular command-key sequence works,
  type *C-h k* and then the key sequence into the modeline prompt.

  If you're curious how *C-h k* itself works, type *C-h k C-h k*.
  According to the *Help* buffer that appears, *C-h k* corresponds to the
  Emacs Lisp function *describe-key* defined in *help.el*.
  Move your cursor onto the *help.el* text in the *Help* buffer and press enter.
  Youre now looking at the Emacs Lisp source for *describe-key*. ..."

- <https://news.ycombinator.com/item?id=5729291>, comments by *brudgers* on
  How to Learn Emacs: A Hand-drawn One-pager for Beginners:
  (That how-to describes some command-key sequences or keyboard shortcuts,
  for example *C-p* moves the cursor to the previous line.)
  "The power of Emacs is being command driven. The command for moving to previous line is:
  *previous-line*.  The mini-buffer is where one enters commands. The command
  for switching focus to the mini-buffer is: *M-x*.  Tell the new user
  what is really going on. To move to the previous line:
  a) enter the command <M-x> to switch focus to the mini-buffer
  b) enter the command <previous-line> to move the coursor
  c) after entering the command, focus will return from the mini-buffer to the invoking buffer.
  ...  what tutorials are teaching is not the language of Emacs (commands and eLisp),
  but the language of Emacs users (shortcuts) ...
  the starting point for everything is <M-x *command*>."

31 Mar 2019

- *The Autobiography of Malcolm X* as told to Alex Haley, pages 174-176, 183
  (no link):
  "It had really begun, back in the Charlestown Prison, when Bimbi made me
  feel envy for his stock of knowledge. ... But any book I picked up had few
  sentences which didn't contain one to nearly all of the words that might
  have been in Chinese. ... I saw that the best thing I could do was get hold
  of a dictionary.  ... that moved me to request a dictionary along with some
  tablets and pencils from the Norfolk Prison Colony school

  ... I didn't know *which* words I needed to learn.  Finally, just to start
  some kind of activity, I began copying.  In my slow, painstaking, ragged
  handwriting, I copied into that tablet everything printed on that first page ...
  I believe it took me a day.  ...  Then, aloud, I read back to myself, everything
  I'd written on the  tablet.  Over and over, aloud, to myself ...
  I woke up the next morning, thinking about those words -- immensely proud
  to realize not only that I had written so much at one time, but I'd written words
  that I never knew were in the world.  Moreover ... I could remember what many
  of these words meant. ...

  I was so fascinated that I went on -- I copied the dictionary's next page.
  ... With every succeedeing page, I also learned of people and places and events
  from history.  ... Finally the dictionary's A section had filled a whole tablet --
  and I went on into the B's.  That was the way I started copying what eventually
  became the entire dictionary. ... during the rest of my time in prison I would
  guess I wrote a million words.

  ... as my word-base broadened, I could for the first time pick up a book and
  read and now begin to understand what the book was saying.  Anyone who has
  read a great deal can imagine the new world that opened. ... from then until
  I left that prison, in every free moment I had, if I was not reading in the
  library, I was reading on my bunk. ... months passed without my even thinking
  about being imprisoned.  In fact, up to then, I had never been so truly free
  in my life.

  ... No university would ask any student to devour literature as I did when
  this new world opened up to me. ...
  I don't think anyone got more out of going to
  prison than I did.  In fact, prison enabled me to study far more
  intensively than I would have if my life had gone differently and I
  had attended some college. ... Where else but in a prison could I have
  attacked my ignorance by being able to study intensely sometimes as much
  as fifteen hours a day?"

  (Compare to Anthony Burgess and John McPhee below on reading the dictionary.)

20 Mar 2019

- *But Beautiful: A Book About Jazz* by Geoff Dyer, pages 184-186, 188-189,
  192-193, 194-197, 197-198 (no link):
  personal, imaginative retellings of incidents from
  the lives of musicians: Lester Young, Thelonious Monk and others.
  From the much different omniscient Afterword:

  "... From the beginning (jazz) developed through the shared participation
  of a community of audiences and performers ... every time (a musician)
  picks up his horn, he cannot avoid commenting, automatically and implicitly
  ... on the tradition that has laid the music at his feet.  ...
  Ideally, a new version of an
  old song is virtually a recomposition and this labile relation between
  composition and improvisation is one of the sources of jazz's ability to
  constantly replenish itself. ...

  There are two apparently contradictory ways in which the antecedent's voice
  makes itself heard.
  Some musical personalities are so strong .. that they colonize
  a whole area of expression, and others can encroach on it only at the
  price of surrendering their individuality. ... It is now almost impossible
  for a trumpeter to play a ballad with a Harmon mute and not sound as if
  he is imitating Miles Davis.  Alternatively, there are
  rare instances of musicians assimilating their predominant influences to
  such an extent that they seem at times, as Harold Bloom has said of some
  poets, to "achieve a style that captures and oddly retains priority over
  their precursors ... and one can believe for startled moments, that they
  are being *imitated by their ancestors*." ... Lester Young frequently sounds
  as if he is indebted to those like Stan Getz who in fact owe their sound
  entirely to him.   At times early Keith Jarrett makes us wonder if
  Bill Evans does not sound too much like Jarrett.

  ... hand in hand with jazz's capacity to absorb its surrounding
  history goes its capacity to raise to the level of genius those who would
  otherwise have lacked a medium to express themselves. ... In what other
  art form could a man like Art Pepper have achieved the beauty he did?"

  Anyone who becomes interested in jazz is struck very early on by
  the high casualty rate among its practitioners. ... Virtually all
  black musicians were subject to racial discrimination and abuse. ...
  While (some) who dominated jazz in the 1930s ended up as alcoholics,
  the generation of musicians who forged the bebop revolution in the 1940s
  and consolidated its development in the 1950s fell victim to a virtual
  epidemic of heroin addiction.  Drug addiction led directly (in the cases
  of (some)) and indirectly (in the cases of (others)) to jail.  The routes
  to the psychiatric wards of hospitals, while a good deal more tortuous,
  was just as well trodden. ... (These) -- so many of the leading figures
  of the 1940s and 1950s suffered some kind of breakdown that it is only
  a slight exagerration of perspective to say that Bellevue has an almost
  equal claim to Birdland as being the home of modern jazz.

  Students of literature routinely find the early deaths of Shelley and Keats
  ... as fulfilling the doomed caveat of the Romantic agony. ...
  the suggestion is that premature death is a condition of creativity ...
  For jazz musicians of the bebop era making it into middle age begins to
  seem like a dream of longevity.  John Coltrane died at forty, Charlie
  Parker at thirty-four ... In a few cases their talent was so prodigious
  that at the time of their deaths some musicians had already produced an
  important body of work -- but even this consolidated achievement painfully
  emphasizes how much might have been accomplished in the years to come.
  Clifford Brown had already established himself as one of the greatest
  trumpeters of all time when he was killed in a car crash at age twenty-five
  ... when you consider that if Miles Davis had died at a similar age we would
  have nothing beyond *The Birth of the Cool*, some sense of the scale of the
  loss appears.

  If at first it seems melodromatic to suggest that there is something
  iherently dangerous in the form, a little consideration is likely
  leave us wondering how it could be otherwise.
  ... from the 1940s onward jazz advanced with the power and ferocity of a
  fire sweeping through a forest.   How could an art form have developed so
  rapidly and at such a pitch of excitement without exacting a huge human toll?
  If jazz has a vital connection with "the universal struggle of modern man"
  how could the men who create it not bear the scars of that struggle?"

18 Mar 2019

- <https://news.ycombinator.com/item?id=19416485> - comments on
  *The Unix-Haters Handbook* -  "I think (this book) still has
  a valuable lesson that many, particularly young CS students,
  would benefit from: Unix is not the perfect fundamental model for computing.
  C is not the gospel. Their prevalence today is as much a historic and economic accident
  as a rational consequence of their objective merits. Both are social artifacts,
  not manifestations of fundamental truths."

  "... I still miss my Lisp Machine. It's not that Unix is really that bad,
  it's that it has a certain model of computer use which has crowded out
  the more ambitious visions which were still alive in the 70s and 80s."

  BUT --

  <https://news.ycombinator.com/item?id=19407811> - comments on
  fragmentation and dead ends in Lisp projects -
  "... as an aside lisp also has a reputation, unfounded or not,
  for encouraging people to develop a bespoke private universe
  that's hard for other people to get a handle on."

10 Mar 2019

- <http://www.cheng.staff.shef.ac.uk/morality/morality.pdf> -
  Mathematics, Morally by Eugenia Cheng - "... The key characteristic
  about proof is not its infallibility, not its ability to convince
  but its *transferrability*. Proof is the best medium for
  communicating my argument to X in a way which will not be in danger
  of ambiguity, misunderstanding, or defeat. Proof is the pivot for
  getting from one person to another, but some translation is needed
  on both sides.

  So when I read an article, I always hope that the author will have
  included a reason and not just a proof, in case I can convince
  myself of the result without having to go to all the trouble of
  reading the fiddly proof. When this does happen, the benefits are
  very great. But is it always possible? ..."

10 Mar 2019

- Ghosts and Psychic Dreams: The Dizzying Fiction of Anthony Burgess, by
  Margaret Drabble, *TLS*, Feb 22 2018, p. 3 (no link): "... Burgess suffered
  from ... an excessive love of words and language ... he cheerfully recommends
  "ransacking the dictionary" when in need of an inspirational boost.  Rejecting
  a critic who praised Shakespeare's dying delerium in his novel *Nothing Like the
  Sun* (1964) as "wrting of the highest order', he confesses, "Not quite so, really.
  I had taught myself the trick of contriving a satisfactory coda
  by what, in music, is termed aleatory means: I flicked through the dictionary
  and took whatever words leapt from the page.  I did this again at the end of my
  Napoleon novel: the effect is surrealistic, oceanic, and easily achieved".  This is
  a very odd mode of composition.  Laura Sage nailed it in a review ... "Better the
  collective unwisdom of the verbal stew, he would say, than any tyrannous signature".
  ..."

10 Mar 2019

- <https://news.ycombinator.com/item?id=19344872> - Comment on The Emacs
  Package Developer's Handbook - "... the highly imperative Logo-like
  model of coding is, though kind of clunky at times, also extremely
  intuitive and straightforward. Your programs often work the same way
  you work: go to the other buffer, search forward for a regexp, kill
  the line, go back to the beginning, and so on, just like “editor
  macros.” So there’s no funky abstraction frameworks with models and
  controllers and whatnot, just buffers with cursors basically."

28 Feb 2019

- <https://news.ycombinator.com/item?id=19263295> - Comments on
  *Hypercard Users Guide* (1987) - "Hypercard was a thrust in the
  direction of the Engelbart/Kay/Papert vision of personal computing,
  one where there wasn't so much of a division between "programmers"
  and "users" ... This vision of computing has fallen out of fashion
  ...  We have, instead, allowed our personal
  media to become arcane devices of dubiously "necessary"
  complexity. You can see this in any cafe where a web developer is
  using a teletype emulator to create a UI, or when someone cannot
  take the logical "next step" in processing some information in their
  spreadsheets (like retrieving data easily) because the system is not
  set up to allow them to explore that possibility without first
  learning a full fledged programming language top to bottom. ...  you
  "do Hypercard" in Hypercard itself, and that the home stack is
  itself an explorable example of how the whole system works. ..."

  "What was great about the later versions of Hypercard is how they
  fit holistically within OS8/9 (operating system) ... What really
  should have happened next is that many of the basic applications
  should have themselves been implemented in "a hypercard". For
  example, imagine a Finder that let you peek under the hood to see
  all of its scripts and, after some kind of "unlocking" allowed you
  to change it. You get access to a lot of the power of the OS's API
  for free at that point ... The switch to Unix also meant a switch to
  an older, more complicated, less intuitive bundle of methods for
  system scripting. Useful UI metaphors go away at that level and are
  replaced with bad and outdated metaphors, like the teletype.
  ... personal computing operating systems seem to have regressed from
  the contructionist perspective. ... you cannot have a "modern
  hypercard" without having a different kind of operating system,
  which itself might require a different hardware architecture."

- <https://news.ycombinator.com/item?id=19239776> - Comments on "Why 80s
  BASIC still matters" - "BASIC made it easy to learn incrementally,
  one line at a time. Syntax and block issues in Python require too
  much up-front training, in my opinion." ...

  "... I know from teaching kids that LINE NUMBERS make more sense to
  them. ..."

  "... I understood 8-bit BASICs ... because I could spatially follow the
  flow of a program written with GOTO: knowing the line number told me
  roughly where in the code it would land. But code that used labels
  and indirection(arrays, pointers, that kind of thing) was beyond me
  for quite a while ... Modern languages pack in tons of indirection
  because that's where the power tools are - but an introductory
  environment might benefit from cutting down on that."

  "... BASIC worked without any planning whatsoever. You don't need to
  declare variables, or even arrays if you only use subscripts
  1-10. Strings handled automatically.  So it was really fun to play
  with. You could make your new computer do something rather quickly,
  and refine it over time.  Line numbers were needed on the old 8-bit
  systems that didn't have full screen text editors with copy/paste
  built in. It's how you told BASIC where to put new lines in the program. ..."

20 Feb 2019

- <https://www.nytimes.com/2019/02/13/magazine/women-coding-computer-programming.html> - The Secret History of Women in Coding - features Mary Ellen
  Wilkes, who worked on the LINC laboratory minicomputer in the 1960s and
  wrote these papers about it:

  <http://www.digibarn.com/stories/linc/documents/LINC-Mary-Allen-Wilkes/Conversational-Access-CACM-1970.pdf> - Conversational Access to a 2048-word Machine, 
  Comm. of the Association for Computing Machinery 13, 7, pp. 407–14, July 1970.
  "LAP6 is an online system running on a 2048 word LINC which provides
  full facilities for text editing, automatic filing and file
  maintenance, and program preparation and assembly. ... The small
  memory has had surprisingly little effect on the functional
  specification of the system ... and perhaps operated with a positive
  effect on the criterion of simplicity. Compromises were, of course,
  necessary, but we also found that operating features which may seem
  highly desirable, for example, to a professional in the computer
  field, can be so much excess baggage in an on-line applications
  environment. ..."

  <http://www.digibarn.com/stories/linc/documents/LINC-Mary-Allen-Wilkes/Scroll-Editing-Proc.-IEEE.pdf> - Scroll Editing: an on-line algorithm for manipulating long character strings, 
  IEEE Trans. on Computers 19, 11, pp. 1009–15, November 1970.
  Describes the ingenious virtual memory scheme: "An algorithm that
  runs on a 2048-word LINC provides efficient on-line editing of
  character strings virtually unlimited in length. Fixed-address LINC
  tape holds the character sequence in the manner of a scroll. Edited
  characters are spliced directly in or out of the scroll as it moves
  across a display scope under the viewer's control. A 512-character
  "playground" created at the splice point provides sufficient ease to
  permit changing the scroll contents dynamically..."

17 Feb 2019

- *Out of Sheer Rage: Wrestling with D. H. Lawrence* by Geoff Dyer, pages 90,
  137-138, 149, 152-153, 229, 231-232 (no link):
  "All the work of (Lawrence's) maturity was built on his
  relationship with Frieda. 'Fidelity to oneself means fidelity single and
  unchanging, to one other one.'  His adult life begins with the unalterable
  fact of his marriage. ...

  Films and books urge us to think that there will come certain moments in our
  lives when, if we can make some grand, once-in-a-lifetime gesture ...
  then we will be liberated, free.  Moments --
  crises -- like these are crucial to the cinema or theatre where psychological
  turmoil has to be externalized and compressed.  Dramatically speaking what
  happens after moments like these is unimportant even though the drama continues
  afterwards, with the consequences of these sudden lurches beyond the
  quotidian. ... Unless, like Thelma and Louise, you plunge off the side of a
  canyon, there is no escaping the everyday.  What Lawrence's life demonstrates
  so powerfully is that it actually takes a daily effort to be free.  To be free
  is not the result of a moment's decisive action but a project to be constantly
  renewed.  More than anything else, freedom requires tenaciousness.  There are
  intervals of repose but there will never come a state of definitive rest where
  you can give up because you have turned freedom into a permanent condition.
  Freedom is always precarious. ...

  What is surprising is to find that the parts of the correspondence of a great
  writer I most like are those which would be edited out if any kind of selection
  were made, i.e. those having nothing to do with his genius and everything to
  do with his ordinariness, with the ordinariness he claimed to loathe. The fact
  that Lawrence wrote *Lady Chatterly's Lover* means next to nothing to me; what
  matters is that he paid his way, settled his debts, made nice jam and
  marmalade, and put up shelves.

  You see I've decided to butch it out, to go in the opposite direction
  to that suggested by yoga and meditation.  The yoga-meditation-zen path leads
  to peace with the world and oneness with the infinite.  Petty annoyances fade
  into insignificance, the ego dissolves, and you are left in state of unruffled
  serenity and calm.  Or so I gather.  It's never worked for me.  Faced with the
  thousands of petty annoyances and grievances encountered in the course of a
  week ... (I'm) shaking my fist at the world.  I won't let even the smallest
  grievance escape me.  I'm going to seize on the most insignificant
  inconvenience, annoyance, hindrance, set-back, disappointment and am going
  to focus all my rage, anger, bitterness, and frustration on it. ...

  ... the alternatives to giving in and giving up are never as simple as they
  seem.  Believe me, I know.  I've devoted more of my life to thoughts of
  giving up than anyone else I can think of.  Nietzsche wrote that the thought
  of suicide had gotten him through many a bad night, and thinking of giving
  up is probably the one thing that's kept me going.  I think about it on a daily
  basis but always come up with the problem of what to do when I've given up.
  Give up one thing and you're immediately obliged to do something else.  The
  only way to give up totally is to kill yourself but that one act requires an
  assertion of will equal to the total amount that would be expended in the rest
  of a normal lifetime.  Killing yourself is not giving up, it's more like a
  catastrophic fast-forwarding. ...

  And there you have it.  One way or another we all have to write our studies
  of D. H. Lawrence.  Even if they will never be published, even if we will
  never complete them, even if all we are left with after years and years of
  effort is an unfinished, unfinishable record of how we failed to live up to
  our own earlier ambitions, still we all have to try to make some progress with
  our books about D. H. Lawrence.  The world over, from Taos to Taormina, from
  the places we have visited to countries we will never set foot in, the best
  we can do is to try to make some progress with our studies of D. H. Lawrence."

17 Feb 2019

- <https://github.com/hundredrabbits/Orca> - Live Programming Environment -
  via <https://news.ycombinator.com/item?id=19118951> - "What is it?
  What does it do? Why would I use it?"
  "This isn't really that kind of piece of software. It's a work of art ...
  open it up and play around and you might find something worthy of delight."
  "Think cellular automatons combined with PD/MaxMSP. ...
  There are nodes to generate data (counters, timers, etc.), nodes that have
  state and nodes that are sinks (OSC and MIDI). ... It's fun."

  "Orca is just one piece of the world that this guy has been building at
  <https://wiki.xxiivv.com/#home>
  He's got a suite of tools: Left, Dotgrid, Ronin, Marabu (text, graphics,
  super-graphics, audio).
  Then a logging/personal wiki setup that I think is fascinating: Nataniev,
  Horaire, Oscean. Which goes all the way down to his own database formats and
  time format.
  The philosophy and aesthetic of his work is awesome in the completeness of
  associated art and the connection between the build-up of his own software
  ecosystem."

14 Feb 2019

- <http://sunnyday.mit.edu/16.355/syllabus-355-2017.html> - *System Engineering
  of Software-Intensive Systems* - course at MIT by safety expert
  Nancy Leveson: "Note that the class is a system engineering of software class,
  not a standard software engineering class and as such will not provide basic
  training in programming or in specific approaches or tools for developing
  software. ... Instead of a textbook, required reading will consist of a
  carefully selected set of historically important and foundational papers
  as well as some more current ones. Some papers will be technical while others
  will be opinions or essays. The literature is vast, and papers have been
  selected for their historical relevance in the development of the field or
  for their ability to help you critique the assumptions underlying current
  software/system engineering dogma.  ... There will be no programming
  assignments. ...  most assignments will involve evaluation and interpretation
  rather than practice in applying particular techniques or tools. ..."

  <http://sunnyday.mit.edu/16.355/> Readings and class notes

14 Feb 2019

- <http://www.1-9-9-1.com/> - *1991 - A server-side web framework written in Forth*
  "The year is 1991. The World Wide Web has just seen public release.
  *1991* looks to ease your interactions with the new web using cutting edge
  programming techniques in Forth (well, Gforth). ...

  'You're using Gforth, which came out in 1992. Also, it's 2017.'
  Okay. But Fredric Jameson establishes that in postmodernism we have experienced
  a weakening sense of historicity such that what is, what was, and what will
  be all exist as presents in time. 1970, 1991, 1992, and 2017 all happen
  simultaneously. Hence developers working on new projects while still coding
  in decades-old text editors. They write the future in the past and are made
  present in so doing."

  via <https://news.ycombinator.com/item?id=19146767> -
  "A microframework in a scant 480 lines of code, plus a postmodern manifesto ..."

 9 Feb 2019

- <http://jazz-quotes.com/> - "... I've begun collecting quotes from different books
  I have and from across the internet. ..."  For example:

  <http://jazz-quotes.com/artist/miles-davis/>  Miles Davis:

  "... you can't play everything at once!"

  "Sometimes you have to play a long time to be able to play like yourself."

  <http://jazz-quotes.com/artist/thelonious-monk/>  Thelonious Monk:

  "Just because you're not a drummer doesn't mean you don't have to keep time."

 9 Feb 2019

- <https://news.ycombinator.com/item?id=19122578> comment by Ron Garret on
  <https://kirit.com/Build%20me%20a%20LISP>  "... An S-expression is a
  *serialization* of a (single) cons cell, whose elements might be other cells.
  ... The fact that S-expressions represent cons cells and NOT vectors is crucially
  important. It is the feature from which Lisp derives much of its power.

  It is possible to make a Lisp-like language where the surface syntax
  represents vectors instead of cons cells. In fact, this makes a useful
  exercise.
  If you undertake this exercise you will come to know the answer to the
  question: why has this idea (a vector-based Lisp) not gained
  more wide-spread adoption?

  ... S-expressions are not a data type, they are a serialization of cons cells,
  i.e. they are a *mapping* between cons cells and strings, and this mapping
  has a very particular feature from which much of Lisp's power is derived,
  which is that it compresses a linked list of cons cells into this:
  *(1 2 3 4)* instead of this *(1 . (2 . (3 . (4 . nil))))*

  ... What this (linked) article is describing is similar in
  spirit to Lisp, but it's not Lisp. It's a different (toy) language at a
  completely different point in the design space."

 4 Feb 2019

- *How to Write a Thesis* by Umberto Eco, pages x, xxvi, 5-7, 9-10,
  110-111, 125, 142-144, 145, 149-150, 221 (no link). From the forward
  by Francesco Erspamer: "Umberto Eco takes us back to the original
  purpose of theses and dissertations ... They are not a test or exam,
  nor should they be.  They are not meant to show that the student did
  his or her homework.  Rather, they prove that students can *make*
  something out of their education."

  Eco: "... I became aware that many times over the course of my
  readings, I had attributed to others ideas that they had merely
  inspired me to look for; and many other times I remained convinced
  that an idea was mine until, after revisiting some books read many
  years before, I discovered that the idea, or its core, had come to
  me from a certain author. ... research is a mysterious adventure
  that inspires passion and holds many surprises.  Not just an
  individual but also an entire culture participates, as ideas
  sometimes travel freely, migrate, disappear, and reappear.  In this
  sense, ideas are similar to jokes that become better as each person
  tells them.

  As we shall see, the rigor of a thesis is more important that its
  scope.  One can even collect soccer trading cards with rigor
  ... There will always be a difference between his collection and the
  Louvre, but it is better to build a serious trading card collection
  ... than to create a cursory art collection.

  Writing a thesis requires a student to organize ideas and data, to
  work methodically, and to build an "object" that in principle will
  serve others.  ... If a student works rigorously, no topic is truly
  foolish, and the student can draw useful conclusions even from a
  remote or peripheral topic.

  In 1957 the great contemporary Italian critic Gianfranco Contini
  published a survey ... Had the survey been a thesis, it would have
  earned a failing grade ... Contini dedicated entire chapters to
  so-called "minor" authors and relegated certain "major" authors to
  mentions in short footnotes or omitted them altogether.  The
  committee would have attributed these choices to carelessness or
  ignorance.  Naturally, since Contini is a scholar of recognized
  historical knowledge and critical acumen, readers understood that
  the omissions and disproportions were intentional, and the absence
  of a particular author was a more eloquent expression of Contini's
  disfavor than a hostile review.  But if a student in his twenties
  plays the same trick, who guarantees that there is shrewdness behind
  his silence?  Do the omissions replace criticism that the student
  has written elsewhere, or that he *would be capable* of writing?

  The purpose of this fictitious introduction (fictitous, because you
  will rewrite it many times ...) is to allow you to give your ideas a
  primary direction that will not change ... If you cannot write the
  introduction, it means that you do not yet have clear ideas on how
  to begin. ... And it is precisely on the basis of this suspicion
  that you must write your introduction, as if it were a review of the
  already completed work. ... The goal of a good final introduction is
  to so satisfy and enlighten the reader that he does not need to read
  any further.  This is a paradox, but often a good introduction
  ... provides a reviewer with the right ideas, and prompts him to
  speak about the book as the author wished.

  Photocopies are indispensable instruments. ... But a set of
  photocopies can become an alibi.  A student makes hundreds of pages
  of photocopies and takes them home, and the manual labor he
  exercises in doing so gives him the impression that he possesses the
  work.  Owning the photocopies exempts the student from actually
  reading them.  This sort of vertigo of accumulation, a neocapitalism
  of information, happens to many.  Defend yourself from this trap: as
  soon as you have the photocopy, read and annotate it immediately.
  ... do not photocopy something new until you *own* (that is, before
  you have read and annotated) the previous set of photocopies.  There
  are many things that I *do not know* because I photocopied a text
  and then relaxed as if I had read it.

  ... *the best ideas may not come from the major authors.* This is
  academic humility: the knowledge that anyone can teach us something.
  ... The point is that we must listen with respect to anyone, without
  this exempting us from pronouncing our value judgments; or from the
  knowledge that the author's opinion is very different from ours, and
  that he is ideologically very distant from us.  But even the
  sternest opponent can suggest some ideas to us. ... I learned
  ... that if I wanted to do research, as a matter of principle I
  should not exclude any source.  This is what I call academic
  humility. ...

  ... it is a common belief that a popular work, where the topic is
  explained so that anyone can understand it, requires less skill than
  a specialized scientific report ... This is not completely
  true. ... usually works that do not explain the terms they use
  ... reveal authors who are more insecure than those who make every
  reference and every step explicit.  If you read the great scientists
  or the great critics, you will see that ... they are quite clear and
  are not ashamed of explaining things well.

  *You are not e. e. cummings.* ... he did all the things that an
  avant-garde poet can and should do.  But you are not an avant-garde
  poet.  Not even if your thesis is on avant-garde poetry. ... the
  language of the thesis is a *metalanguage*, that is, a language that
  speaks of other languages. ... From Dante to Eliot and from Eliot to
  Sanguineti, when an avant-garde poet wanted to talk about their
  poetry, they wrote in clear prose.  ... Are you a poet?  Then do not
  pursue a university degree.

  ... writing a thesis is like cooking a pig: nothing goes to waste.

25 Jan 2019

- <https://github.com/ktye/iv> - APL interpreter and stream processor - 
  "Next tasks: ... learn APL ... The author has never used APL ..."
  via <https://news.ycombinator.com/item?id=18997977> -
  "Of course it takes less time and effort to write an APL interpreter
  than it does to actually learn APL."

 9-14 Jan 2019

- *Clear and Simple as the Truth: Writing Classical Prose* by
   Francis-Noel Thomas and Mark Turner, pages 3 - 6, 13 - 14, 63, 81 -
   87 (no link): "The teaching of writing in America is almost
   entirely controlled by the view that teaching writing is teaching
   verbal skills ... Our answer is that writing is an intellectual
   activity, not a bundle of skills. ... any attempt to teach writing
   by teaching writing skills detached from underlying conceptual
   issues is doomed.

   But it is possible to learn to write by learning a style of
   writing.  We think conceptual stands are the basis of writing since
   they define styles. ... verbal artifacts -- like plumage -- help
   identify a style.  Nevertheless, in general, a style cannot be
   defined, analyzed, or learned as a matter of verbal choices.

   Writing is defined conceptually and leads to skills. ... But in no
   case is the activity constituted by the skills.  Great painters are
   often less skillful than mediocre painters; it is their concept of
   painting, not their skills, that defines their activity ...
   Intellectual activities generate skills, but skills do not generate
   intellectual activities.  The relationship is not symmetric.

   A style is defined by its conceptual stand on truth, presentation,
   writer, reader, thought, language, and their relationships.
   Classic style ... adopts the stance that its purpose is
   presentation; its motive, disinterested truth.  Successful
   presentation consists of aligning language with truth, and the test
   of this alignment is clarity and simplicity.  The idea that
   presentation is successful when language is aligned with truth
   implies that truth can be known; truth needs no argument but only
   accurate presentation; the reader is competent to recognize truth;
   the symmetry between writer and reader allows the presentation to
   follow the model of conversation; a natural language is sufficient
   to express truth; and the writer knows the truth before he puts it
   into language.

   ... Once adapted, the classic stand offers a general style of
   presentation suitable to any subject whatever. ... The style does
   not limit the writer's subject matter or efface his individuality,
   but the writer's individuality will be expressed principally by his
   knowledge of his subject.

   ... We coach our readers in the conceptual stand that might turn
   them into classical writers, and contrast the classic stand with
   some others: reflexive, practical, plain, contemplative, romantic,
   prophetic, oratorical."

   "Classic style is focused and assured.  Its virtues ... are its
   vices.  It declines to acknowledge ambiguities, unessential
   qualifications, doubts, or other styles ... writing in this style
   requires no commitment to a set of beliefs, only a willingness to
   adopt a role for a limited time and a specific purpose.  The role
   is severely limited because ... The human condition does not, in
   general, allow the degree of autonomy and certainty that the
   classic writer pretends to have.  ... The insousiance required to
   ignore what everyone knows and to carry the reader along in this
   style cannot be maintained for very long, and the masters of the
   style always know its limits.  The classic distance is a sprint."

   "Abstractions can be clear and exact.  From the classic viewpoint,
   the distinction between abstract and concrete has no consequence.
   ... What matters is not the ontological category of the subject but
   rather the style in which it is conceived. ... in classic style,
   the human soul can be conceived as clearly and exactly as the tree
   in front of your face. ..."

   "Classical style is not practical style.  In the model scene behind
   the practical style, the reader has a problem to solve ... a job to
   do. ... in this scene, writing is an instrument for delivering
   information with the maximum efficiency and in such a way as to
   place the smallest possible burden on the reader ...  The best
   known teachers of practical style are Strunk and White, in their
   ubiquitous *Elements of Style*.  The best teachers of practical
   style are Joseph Williams and Gregory Colomb, in Williams's *Style:
   Toward Clarity and Grace* ... (that book) is missing only one thing: namely,
   an explicit acknowledgment of its fundamental stand, and
   acknowledgment that its fundamental stand is one of many
   alternatives. ... In the model scene of practical style, readers
   and writers hold standard job slots in existing institutions.
   ... practical style serves the purpose of keeping the information
   flowing efficiently through institutions. ...  There is a surface
   mark of practical style ... (it) permits skimming ... you can
   simply glance through and extract what you want.  If you try to
   skim classic writing in this way, you run the risk of missing
   indispensable nuances or refinements. ..."


 4 Jan 2019

- <https://news.ycombinator.com/item?id=14852625> - comments on the book *Thinking Forth* - 
  "For me the biggest influences underemphasized in other sources are
  to be alert for relentless simplification, for 'mechanical
  sympathy', for ways changing your problem could make it much simpler
  to solve -- and that there's an agility in using a simpler
  programming system like a Forth which you grok and can change as you
  need to, which can sometimes outweigh the leverage of a big one that
  comes with lots of stuff already done for you. These are useful
  points of view even with Forth being almost never the most practical
  tool now. ..."

  Also <https://news.ycombinator.com/item?id=12713797> "... Good Forth
  programmers appear to solve hard problems by ruthlessly stripping
  away everything irrelevant from the problem to end up with an easy
  one. ..."

22 Dec 2018

- <https://smallstep.com/blog/everything-pki.html> - Everything you
  should know about certificates and PKI but are too afraid to ask -
  "Certificates and PKI (Public Key Infrastructure) are built on public
  key cryptography ... which uses key pairs. A key pair consists of a
  public key that can be distributed and shared with the world, and a
  corresponding private key that should be kept confidential by the
  owner.  There are two things you can do with a key pair: 1. You can
  encrypt some data with the public key. The only way to decrypt that
  data is with the corresponding private key.  2. You can sign some
  data with the private key. Anyone who knows the corresponding public
  key can verify the signature, proving which private key produced it.
  ... Verifying (my) signature is good evidence you’re talking to
  me. This effectively allows computers to see who they’re talking to
  across a network.

  Public key cryptography is a magical gift from mathematics to
  computer science.

  What if you don’t already know my public key? That’s what
  certificates are for.  ... A certificate is a data structure that
  contains a public key and a name. The data structure is then
  signed. The signature binds the public key to the name. The entity
  that signs a certificate is called the issuer (or certificate
  authority) and the entity named in the certificate is called the
  subject.  ... if you know (the issuer’s) public key you can
  authenticate (the certificate) by verifying the signature. ... Thus,
  certificates let you use (your) trust (of the issuer), and knowledge
  of an issuer’s public key, to learn another entity’s public key. ..."

- <https://robertheaton.com/2014/03/27/how-does-https-actually-work/> -
  "HTTPS takes the well-known and understood HTTP protocol, and simply
  layers an SSL encryption layer on top of it.  The SSL layer has 2
  main purposes: 1. Verifying that you are talking directly to the
  server that you think you are talking to 2. Ensuring that only the
  server can read what you send it and only you can read what it sends
  back. (When) contact has been established, the server has to prove
  its identity to the client. This is achieved using its SSL
  certificate.  The client checks that it either implicitly trusts the
  certificate, or that it is verified and trusted by one of several
  Certificate Authorities (CAs) that it also implicitly trusts.
  Much more about this shortly. ...

  ... certificates are completely open and public, so any attacker
  could grab Microsoft’s certificate, intercept a client’s request to
  Microsoft.com and present the legitimate certificate to it. The
  client would accept this and happily begin the handshake. However,
  when the client encrypts the key that will be used for actual data
  encryption, it will do so using the real Microsoft’s public key from
  this real certificate. Since the attacker doesn’t have Microsoft’s
  private key in order to decrypt it, they are now stuck. ...

  Order is maintained as long as the attacker doesn’t control a
  trusted certificate’s private key. If the client is somehow tricked
  into trusting a certificate and public key whose private key is
  controlled by an attacker, trouble begins.

  Can my company monitor my HTTPS traffic over their network?  If you
  are also using a machine controlled by your company, then
  yes. Remember that at the root of every chain of trust lies an
  implicitly trusted CA, and that a list of these authorities is
  stored in your browser. Your company could use their access to your
  machine to add their own self-signed certificate to this list of
  CAs. They could then intercept all of your HTTPS requests,
  presenting certificates claiming to represent the appropriate
  website, signed by their fake-CA and therefore unquestioningly
  trusted by your browser. Since you would be encrypting all of your
  HTTPS requests using their dodgy certificate’s public key, they
  could use the corresponding private key to decrypt and inspect (even
  modify) your request, and then send it onto it’s intended
  location. ... Incidentally, this is also how you use a proxy to
  inspect and modify the otherwise inaccessible HTTPS requests made by
  an iPhone app (link)."

- <https://robertheaton.com/2018/11/28/https-in-the-real-world/> -
  "... Desperately holding these attackers at bay are nothing more than
  the raw power of HTTPS and a handful of trusted Certificate
  Authorities (CAs) run by incorruptible treefolk who live in the
  mountains. ... We’ll see how PKI addresses the facts that 1) your
  own private key might not stay private; 2) your Certificate
  Authority’s private key might not stay private; and 3) Certificate
  Authorities are not actually staffed exclusively by incorruptible
  treefolk who live in the mountains. ..."

14 Dec 2018

- <https://humane.computer/in-conversation-with-aza-raskin/> - Interview
  about Archy <https://github.com/DanielFeichtinger/Archy>, also at
  11-19 Oct below. "You can think of applications as walled cities —
  they have to develop all of their own infrastructure. ... it’s the
  application as a framework which is broken. You want to tear it
  apart and just have functionality that you can use anywhere."
  "There were no files, because the best label for a file is the file
  itself, the content of it. Everything was in one long, conceptual
  document ... what you want is to have all of your content and work
  projects stored spatially. ... a full-on zooming user-interface
  (ZUI), ...no matter where you are you can zoom out and grab your
  bearings, and zoom in ad infinitum, a much better way of doing
  folders and taxonomies."  Hmnn ...  ".. any bit of text can refer to any
  other bit of text, and you can run any command and do any
  functionality from anywhere, that you could open up your tools and
  it was all coded in the same environment, that you were making in,
  very Smalltalk or Alan Kay-like, and so your tools themselves can be
  modified in real-time to modify themselves if need be."

- <https://www.fugue.co/blog/2015-11-11-guide-to-emacs.html> - Recreates
  Archy-like philosophy and workflow in emacs, including some
  customizations: "Ace Jump Mode ... works a bit like Jef Raskin's
  Leap feature from days gone by."  Explicitly references Archy's
  predecessor, the Canon Cat (see 11-19 Oct below).

 6 Dec 2018

- <https://www.newyorker.com/magazine/2018/12/10/the-friendship-that-made-google-huge>  - Profile of Jeff Dean and Sanjay Ghemawat, 
  the pair programming team that created MapReduce, TensorFlow, and
  much more.  Story by James Somers, whose style here recalls John
  McPhee.  Somers is a programmer himself, and a prolific writer with
  a bountiful web site: <http://jsomers.net/>

27 Nov 2018

- <https://news.ycombinator.com/item?id=18525800> - comment on Lisp
  Machine Inc. K-machine by jolmg - "In any case, looking at Lisp OSes
  vs Unix OSes, there is a design dichotomy where both options have
  great advantages. Anyone correct me if I'm wrong, but I understand
  Lisp OSes chose to have the whole OS work in a single high-level
  language, which allows a very natural coupling between programs,
  basically destroying the distiction between whole programs and
  program functions. On the other hand, Unix OSes chose to have a very
  unassuming framework for programs that would best support a great
  diversity of programming languages so that they could best
  interoperate despite the fact that they could work via very
  different semantics. This structure, as we all know, consists around
  the semantics of files which could be thought of as global
  variables, plain text arguments as very unassumming (untyped and
  with no predefined arity) function call arguments, standard input,
  output, and error as lazily-evaluated function arguments, and
  environment variables which could be thought as dynamically-scoped
  variables."

- <https://www.gocomics.com/nancy/2018/04/09> - Nancy - Contemporary take
  on the ancient comic strip by a new cartoonist:
  <https://www.vulture.com/2018/11/new-nancy-cartoonist-olivia-jaimes.html>

23 Nov 2018

- <http://www.jfsowa.com/computer/memo125.htm> - Memo 125 by John
  F. Sowa, on IBM's proposed but unbuilt Future System of the 1970s -
  "The external interface of an operating system is not something
  tangible like a pay stub, but rather a set of interfaces that form
  the innermost level of other programs. ... such as editors,
  compilers, and query facilities. ... The design of these (other
  programs) may be called the *secondary architecture* to distinguish
  it from the heart of the operating system, which constitutes the
  *primary architecture*.  The primary architecture of an operating
  system comprises the following seven areas: Resource allocation,
  process creation, (etc.) ... These seven items form a closed
  list. ... they are interdependent and cannot be designed by isolated
  groups working in far-flung locations, nor even by different
  departments working on separate floors of the same building.  By
  contrast, the secondary architecture is an open-ended list ...  Once
  the primary architecture is firm, the secondary facilities can be
  designed and implemented by groups at opposite ends of the earth
  with a low level of intercommunication."

  "(The proposed OS), in its present state, has guidelines for the
  human factors of using displays, but it lacks a primary architecture
  that determines what kinds of operations are possible. ...  the
  slogan "display-oriented" is dangerous because it focuses on an
  external device, whose support is part of the secondary
  architecture, and overlooks the question of what properties the
  primary architecture must have to support a truly interactive
  system. ... (such as) an on-line symbol table, dynamic resource allocation,
  and a modifiable run-time environment.  ... if it doesn't (have
  those properties), it can never be more than a batch system with
  displays attached."

20 Nov 2018

- <http://homepages.cs.ncl.ac.uk/brian.randell/NATO/> - The NATO
  Software Engineering Conferences - "In the fall of 1968 and again
  the in fall of 1969, NATO hosted a conference devoted to the subject
  of software engineering. ... The motivation for these conferences
  was that the computer industry at large was having a great deal of
  trouble in producing large and complex software systems. ... the
  conference reports have gained a certain amount of classical
  aura. ... I felt that the time had come to make them widely
  available, if for no other reason than to let the current generation
  know what the state of the art was in the late 1960's."  PDFs of
  both reports, a new introduction, a memoir by an original
  participant/editor, and photos.

12 Nov 2018

- *Draft No. 4: John McPhee On the Writing Process* (2017), pages
   19-20, 158-160, 162 (no link): "It doesn't matter that something
   you've done before worked out well.  Your last piece is never going
   to write your next one for you.  Square 1 does not become Square 2,
   just Square 1 squared and cubed."

   "You can build a structure in a such a way that it causes people to
   to want to keep turning pages.  A compelling structure in
   nonfiction can have an attracting effect analogous to a story line
   in fiction."

   "If your prose seems stillborn and you completely lack confidence,
   you might be a writer.  ... if you tell people "you just love to
   write," you may be delusional. ...  First drafts are slow and
   develop clumsily ... That four-to-one ratio in writing time --
   first draft versus all the other drafts combined -- has for me been
   consistent in projects of any length ... The hardest part comes
   first, getting something -- anything -- out in front of
   me. ... With that, you have achieved a sort of nucleus ... you may
   be actually writing only two or three hours a day, but your mind
   ... is working on it twenty-four hours a day ... but only if some
   sort of draft or earlier version aleady exists.  Until it exists,
   writing has not really begun."

   "You draw a box around not only around any word that does not seem
   quite right but also around words that fulfill their assignment but
   seem to present an opportunity.  ... If there's a box around
   "sensitive" ... try "susceptible".  Why "susceptible?  Because you
   looked up "sensitive" in the dictionary and it said "highly
   susceptible."  With dictionaries, I spend a great deal more time
   looking up words I know than words I have never heard of -- at
   least ninety-nine to one.  The dictionary definitions of words you
   are trying to replace are far more likely to help out than a
   scattershot wad from a thesaurus."

10 Nov 2018

- <https://www.metafilter.com/177575/Violin-Sonatas-etc> - Links to more
  than fifty performances of sonatas for violin, viola, cello, and
  double bass, listed in chronological order from Mozart to Philip
  Glass.  With even more links from commenters, including some earlier
  baroque pieces.

27 Oct 2018

- <http://thequietus.com/articles/25409-richard-thompson-interview-favourite-albums?page=4> - 
  Thompson talks about 13 favorite records including ... Moby Grape
  !?  "They were the most interesting band that came out of the San
  Francisco scene in the late 60s. They seemed less out of it, more
  focused, and less noodly than some of the others. It's a record that
  gets forgotten a bit, this one, but it's full of fantastic songs and
  really well played, with a great guitarist in Jerry Miller. ..."

- <https://jjon.github.io/Old-GooglePlus-Posts/> - Recommendations from
  an eclectic musician, with links to recordings etc.  No-nonsense
  list he recently rescued from the discontinued
  <https://plus.google.com/u/0/collection/0T0sDB>

22 Oct 2018

- <https://news.ycombinator.com/item?id=18267445> - An immersive
  programming experience - "I've found a good way to approach
  Smalltalk systems like Pharo and Squeak is to remember they're
  *whole systems*, not just languages with a bolted-on IDE.  I like to
  think of each running instance as more akin to a Unix virtual
  machine than anything else. ..." "... The globals dictionary and
  class variables etc are roughly analogous to the filesystem. ..."
  Much discussion of using an image-based rather than file-based system.

- <https://news.ycombinator.com/item?id=18274235> - Hardware Interrupts - 
  "... interrupts are a pretty old concept as far as i know. I'm
  curious if there is anything that would replace them?"  Many
  suggestions, including "You could get rid of interrupts if you take
  a completely different approach to CPU architecture. ... something
  that is driven by data. ... On every cycle, the CPU would look at
  any new data that has arrived and process it accordingly. In this
  view, key-presses or timer ticks would just be like any other data
  flowing through the system."

19 Oct 2018

- <http://calculusmadeeasy.org/> - *Calculus Made Easy* by Silvanus
  P. Thompson (1910) - "The text is based on the PDF version from
  Project Gutenberg converted to html by hand." That is,
  <http://www.gutenberg.org/ebooks/33283>

- <https://news.ycombinator.com/item?id=18256690> - (Common Lisp is) A
  language designed for modifying programs while they
  run. ... Consider the Common Lisp generic function
  UPDATE-INSTANCE-FOR-REDEFINED-CLASS. It's in the language
  standard. ... You don't want to have to stop the program and rebuild
  it just because you redefined a class. ... telling the Lisp new
  definitions as it runs is the standard way that you normally work."

- <https://news.ycombinator.com/item?id=18228740> - "Is there a modern
  “power on to basic” computer, for kids to learn on?"  Over 300 responses.

- <https://news.ycombinator.com/item?id=18236396> - "What's your
  favorite elegant/beautiful algorithm?"  Over 400 responses.

11-19 Oct 2018

- <https://www.exolymph.news/2017/07/27/alternate-computer-universes/> -
  "The Macintosh began as a variant on the dedicated word processor
  ... The normal way to program it is by writing code directly into
  your text document and highlighting it — upon which the language
  will be identified, it will be compiled, and the code will become a
  clickable button that when clicked is executed. In other words, it’s
  a system optimized for ‘literate programming’."
  Article reprinted at <https://medium.com/@enkiv2/alternate-computer-universes-jef-raskins-macintosh-1a3f19b9110a.>  

- <http://www.canoncat.net/cat/Cat%20Work%20Processor.pdf> - "The user
  interface was based on a simple text editor in which all data was
  seen as a long stream of text broken into pages, which could also be
  broken into documents. ... the disk was simply an image of the
  memory ... the Cat had no concept of files.  ... This feature
  allowed users to transfer their entire Cat environment ... by just
  taking their disk from one Cat and inserting it into another ..."
  <https://news.ycombinator.com/item?id=6978587> - "There's something
  elegant about its lack of silos: all of your (textual) data is in
  one space that you leap around with the aid of dedicated search
  forwards/backwards keys, reprogramming or extending the system
  itself is likewise a keystroke away."  Details at
  <https://ia600206.us.archive.org/30/items/TechnicalDocumentationForTheCanonCatEditorSep88/Technical_Documentation_for_the_Canon_Cat_Editor_Sep88.pdf>
  via <https://archive.org/details/jefraskin>

  <https://en.wikipedia.org/wiki/Archy> and
  <https://github.com/DanielFeichtinger/Archy> "All content in Archy is
  persistent. This eliminates the need for, and the concept of, saving
  a document after editing it. ... Command names can be inserted and
  executed at any place in the interface ... Since a command can be
  used anywhere, applications are obsolete as the core of the
  interface's design. Installing a new package of commands provides a
  functionality ... not restricted to ... a single application
  ... (they) can be used system-wide ..."
  <https://news.ycombinator.com/item?id=6978587> "... my main work tool
  is pretty much a copy of the Cat on modern hardware ... the (editor)
  I'm using now is Archy ... It's pretty much a copy of the Canon Cat,
  rewritten in python."

 9 Oct 2018

- <http://antirez.com/news/74> - Fascinating little programs - "Why is
  it so great to hack a small piece of code? ... It can be totally
  understood, dominated. You can use smartness since little code is
  the only place of the world where coding smartness will pay off,
  since in large projects obviousness is far better in the long
  run. However I believe there is more than that, and is that small
  programs can be perfect. ... maybe there is still something to
  preserve from the ancient times where software could be perfect, the
  feeling that what you are creating has a structure and is not just a
  pile of code that works."  See also his <http://antirez.com/news/108>
  Writing an editor in less than 1000 lines of code

 7 Oct 2018

- <http://studyhall.xyz/blog/libraries-coworking-jackdenton> - Writer
  reports on working at four NYC public library branches. "If I told
  you that Poets House is a bad place to write a poem, would you
  believe me?"  Great photos, interesting page design and typography on
  this and linked pages.

 6 Oct 2018

- *Uncommon People: The Rise and Fall of the Rock Stars*, David
  Hepworth (2017), pages 2, 69, 280, 281 (no link): "Rock stars were
  the product of an age when music was hard to access and was
  treasured accordingly. ... This was in the days when any records,
  but particularly imported American blues records, were such objects
  of desire that enthusiasts would ofen embark on inconvenient
  cross-town trips involving changing buses to visit somebody's house
  where there was rumored to be a copy of some particular gem; once
  there, they would play both sides again and again, staring
  hypnotized at the spinning labels until both sight and sound had
  been seared into memory. ... (The rock star) made his name in the
  vanished world of records you could hold in your hand. ... which we
  had secured by using all our available cash in one particular week,
  a record that would, for a while at least, be the most precious
  thing we owned.  ... We now live in a world of unlimited supply and
  exhausted demand.  Music can be every bit as good now as it used to
  be.  However, it can never be as precious as it used to be.  It
  doesn't have our undivided attention any longer. ... Now that we
  have easy access to everything, the individual atoms that make up
  that everything are less significant in themselves.  The same
  applies to the people associated with those atoms.  That's why we
  don't have rock stars anymore."

 5 Oct 2018

- <http://obsolescence.wixsite.com/obsolescence/pidp-11> - "The PiDP-11
  is a modern replica of the PDP-11/70.  Introduced in 1975, the 11/70
  was top of the line in the famed PDP-11 range, and the very last
  system with a proper front panel. ..."  Comments in
  <https://news.ycombinator.com/item?id=18124861> "It just goes to say
  that current systems lack something.  We cannot always put the finger on
  what it is and backtrack to where we think times were better. Using
  these machines is the closest real thing to going back in
  time. ... We cannot bring them back today and use them as primary
  systems because we don't have the context that need those
  machines. They are doomed to be played a little and to be sent back
  to attic." Another commenter responds "The exercise of traveling
  back in time is often not as much as to use the machines for actual
  work, but to experience them as tools to learn about the context
  where they existed ... to (re)learn the lessons others learned
  before us that we can still benefit from."

 1 Oct 2018

- <https://news.ycombinator.com/item?id=12250857> - "... Are there any
  other noteworthy, older computer technologies that are in some ways
  superior to current technologies?"  Several long responses,
  describing some different systems than the recent thread on historic
  OS: <https://news.ycombinator.com/item?id=10114460>

- <https://github.com/terkelg/awesome-creative-coding> - "Creative
  coding is a different discipline than programming systems. The goal
  is to create something expressive instead of something functional."
  via <https://github.com/sindresorhus/awesome>

30 Sep 2018

- *The Art of Fiction* by John Gardner (1983), Ch 6 Technique, p.
  127 (no link) - "Writing an exercise, the beginning writer is doing
  exactly what the professional does most of the time.  Much of what
  goes into a real story or novel goes in not because the writer
  desperately wants it there but because he needs it: The scene
  justifies some later action, shows some basis of motivation, or
  reveals some aspect of character without which the projected climax
  of the action would not seem credible. ..."  According to the book,
  this is the one way in which creative writing is like programming.
  In every other way it is completely different.

29 Sep 2018

- <https://solar.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website/> - "The new blog is designed to radically reduce the energy use
  associated with accessing our content. ... Thanks to a low-tech web
  design, we managed to decrease the average page size of the blog by
  a factor of five compared to the old design – all while making the
  website visually more attractive (and mobile-friendly). Secondly,
  our new website runs 100% on solar power, not just in words, but in
  reality: it has its own energy storage and will go off-line during
  longer periods of cloudy weather. ..."  Lots of details about DIY
  solar panels + batteries + tiny server computer + page design.  Interesting
  graphic design too.  via
  <https://news.ycombinator.com/item?id=18075143>

24 Sep 2018

- <https://mprove.de/diplom/gui/Kay75.pdf> - "Personal Computing by Alan
  Kay" (1975) - Early explanations of the Alto computer and Smalltalk
  language, including motivation and rationale, with descriptons of
  programs written by adults and especially children. "The 'pocket universe' (a
  metaphor we like) needs an epistemology if not a
  metaphysics. ... The basic principle of recursive design is: make
  the *parts* have the same power and capabilities as the
  *whole*. ... It is interesting to note that none of the *parts* of
  most programming languages, 'data structures', 'functions', and
  'control structures', have the same power as the *whole*, instead
  they are *dilutions* of the idea of the computer."

  Via <https://news.ycombinator.com/item?id=18044785> - "What happened
  to this future?  I miss it."

19 Sep 2018

- <http://doc.cat-v.org/plan_9/misc/ubiquitous_fileserver/ubiquitous_fileserver.pdf> - "The Ubiquitous File Server in Plan 9 ... 
  the design of a given component, whether device driver, system
  service or application, often begins by designing a suitable name
  space, at a level of abstraction above that of (say) the API for any
  particular programming language. In other words, in Plan 9, the name
  space provides the focus for design.  We look at a reasonable
  collection of examples ... network interfaces: Plan 9 does not
  provide special ‘socket’ system calls to access networks. Instead,
  devices, interfaces, protocols and services are all represented by
  file trees, conventionally collected together under /net. (Details
  follow) ... (Other examples include) domain name service ...  connection
  service ... mail boxes ... authentication ... window managment ...
  storage formats ... The exposing of data interfaces through the name
  space has a further advantage. ... ordinary system commands can
  operate on it, including *ls*, *cmp*, and *cp*.  ... The server is
  often tested using shell commands or shell scripts ..." Also, any
  server can be used *ad lib* just by typing *echo* or *cat* commands at
  the shell prompt.  This 18-page paper is the most thorough explanation of
  Plan 9 I have seen.

- <http://doc.cat-v.org/plan_9/misc/dead_OSes_still_matter/login.pdf> -
  "Why Some Dead OSes Still Matter - Plan 9 does not have an
  equivalent to the *ioctl()* system call, which cannot be isued
  across a network owing to the reliance on a local pointer to pass
  data.  Instead most servers by convention serve a file named *ctl*
  at the top of their hierarchy, which allows clients to control not
  only I/O but the general behavior of the servers."

  Comments in <https://news.ycombinator.com/item?id=10114460> including
  a roll call of other historic OS, links.

- <http://doc.cat-v.org/bell_labs/the_hideous_name/the_hideous_name.pdf> - "The Hideous Name - 
  ... the UNIX file system contains objects that are not ordinary
  files.  Simply by having ordinary file names, though, these objects
  have ordinary file properties such as protection. ... standard
  software can provide services for them that would otherwise require
  special handling. ... When machines are connected together, their
  name spaces may be joined to facilitate the sharing of files.  If
  the name spaces have the same clean structure, that structure can be
  extended simply to describe the larger space."

16 Sep 2018

- <https://arxiv.org/abs/1809.01639> - Making Better Sense of Quantum
  Mechanics by N. David Mermin - "It once made sense to exclude the
  scientist from scientific explanations of the physical world. This
  warded off superstitious, animistic, or religious explanations. But
  ... today it makes sense to insist that the scientist should not be
  excluded from a philosophical understanding of the nature of
  scientific explanation. ... the historic exclusion of the user,
  while it may have helped get science off the ground, is today
  responsible not only for the confusion at the foundations of quantum
  mechanics, but also for a broader misunderstanding of the nature of
  science in general."  In addition to this argument, much of the
  value here is in the review of the opinions of many physicists and
  others, expressed in their own words (via quotations).  But this
  paper didn't resolve any quantum mysteries for me.

15 Sep 2018

- <https://github.com/arwn/9front-paper/blob/master/paper.pdf> - Using
  9front - "Why would anyone want to use 9front? Well chances are you
  don't. On the strange off-chance that you do end up using it you'll
  be greated with confused looks and open arms by the community, or
  rather, lack of community. ... After booting your 9front machine you
  should be greeted with a drab looking gray screen. Congratulations,
  You've made a terrible decision."

  See also <http://fqa.9front.org/>

- <http://blog.fogus.me/2011/05/03/the-german-school-of-lisp-2/> -
  "*Fluchtpunkt* Lisps skirt the vanishing point between theory,
  practicality, and art. ... (examples include *T* and *Pico Lisp*)
  ...  Fluchtpunkt Lisps are Focused: Uncompromising in their vision,
  Spartan: Devoid of the seemingly unnecessary comforts found in many
  modern languages, Controversial: Not always by design, but often
  because of their design, Fun.

12 Sep 2018

- <https://news.ycombinator.com/item?id=11796650> - Harvey OS – A Fresh
  Take on Plan 9 - "Unix wrinkles: there are so many, but just
  consider the sockets interface. Sockets completely break the Unix
  model of named entities that you can open and close and read and
  write. Sockets don't have names and are not visible in the file
  system. It's a long list of what they got wrong and that's why, in
  1978, other mechanisms were proposed (if you're willing to dig you
  can find the RFC and you'll see ideas like /dev/tcp/hostname and so
  on). But to our dismay (I was there at the time) the current BSD
  socket interface won. Many of us were disappointed by that decision
  but it was the fastest way to get network support into Unix."

  See also <https://github.com/Harvey-OS/harvey>

11 Sep 2018

- <https://morepypy.blogspot.com/2018/09/the-first-15-years-of-pypy.html> - 
  "Originally ... it was more meant as a kind of executable
  explanation of how Python works ...  But pretty soon there were
  then also plans for how the virtual machine (VM) could be
  bootstrapped to be runnable ..." "The use of RPython for other
  languages complicated the PyPy narrative a lot, and in a way we
  never managed to recover the simplicity of the original project
  description "PyPy is Python in Python". Because now it's something
  like "we have this somewhat strange language, a subset of Python,
  that's called RPython, and it's good to write interpreters in. And
  if you do that, we'll give you a JIT for almost free. And also, we
  used that language to write a Python implementation, called
  PyPy.". It just doesn't roll off the tongue as nicely."

  The original vision of a pedagogical Python in Python has recently been
  realized by others in *Byterun* and *Tailbiter*:
  <http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html> and
  <https://codewords.recurse.com/issues/seven/dragon-taming-with-tailbiter-a-bytecode-compiler>

 9 Sep 2018

- <https://www.theatlantic.com/entertainment/archive/2018/07/a-writers-fixation-on-sound/565904/> - R. O. Kwon on Writing *The Incendiaries* - "I worked for 10 years
  on my first book. ... I couldn’t feel done with my novel until I
  could pick it up, read a line, and not desperately want to change
  all the words.  ...  I spent two whole years just reworking the
  first 20 pages over and over again. By the end, I had the most
  reworked, totally inert pages I’ve ever seen in my life. It was just
  going nowhere. ... (Lauren Groff suggested) The idea is to get
  through early drafts as quickly as possible. ... I wrote whole
  drafts by hand. Then I wrote using a program that acts just like a
  typewriter: You can backspace once, but can’t cut and paste full
  paragraphs, and can only move forward. Then, in Word, I wrote a
  draft in which, every time I finished a paragraph, I turned the font
  white so I couldn’t see it and mess with it anymore. ... There’s no
  reason to do all that careful line-edit work when I’m still making
  basic character and structural changes. ... As I continue, and start
  to focus more on sound ... I do a lot of reading out loud to help me
  determine whether the sound is working. ... When I’m finding joy in
  a paragraph, there’s really no sentence where I’m getting bored."
  "I keep a giant, running document of bits and pieces from books I
  love. ... When I feel confused and lost ... I just go back to the
  document and start reading.  ... I think there’s never been a time
  when that hasn’t sparked something in me, and given me an idea or a
  thought that can bring me back to my own writing ..."

- <https://www.metafilter.com/176413/Time-for-some-classical-music> -
  Eclectic suggestions by many ordinary music lovers, with links,
  responding to these recommendations from nineteen composers,
  musicians, and critics:
  <https://www.nytimes.com/2018/09/06/arts/music/5-minutes-that-will-make-you-love-classical-music.html>
  Also,
  <https://ask.metafilter.com/326239/Please-recommend-me-many-requiems-music-books-movies-anything>

 5 Sep 2018

- <https://news.ycombinator.com/item?id=17910632>, comments on
  <https://tinyletter.com/jamesbowman/letters/upduino-a-9-99-fpga> -
  "Can someone explain why someone would choose an FPGA over a
  standard microprocessor? What advantages could this UPDuino have
  over an Arduino? Also, how do ASIC's figure into this comparison?"
  and, "How does one go about developing on an FPGA ...?"  Many
  detailed answers, also many suggestions for FPGA projects.  Also,
  "Can this run a RISC-V core? ... Yes, it can:"
  <https://github.com/grahamedgecombe/icicle> and
  <https://github.com/cliffordwolf/picorv32>

31 Aug 2018

- <https://dl.acm.org/citation.cfm?id=806447> - "Z - The 95% Program
  Editor (1981) ... Z is the production editor in the Yale Computer
  Science Department ... developed using the Yale BLISS programming
  (language) environment for TOPS-20 (operating system for
  DECSystem-20)".  Provides much functionality similar to the Emacs of
  that era, but with a completely different command language and
  internals, and most significantly, "Rather than develop our own
  specialized macro or programming language to support user
  extensions, we felt it way better not to provide the feature at
  all."  This paper tells how to implement many features for editing
  programs in several languages that "would seem to require the
  existence of a parse tree", but instead use only "a simple
  table-driven lexer (that) takes a line of text and divides it into
  (a few) categories" and "by making a very simple assumption about
  how a programmer formats his program."

29 Aug 2018

- <https://github.com/darklife/darkriscv> - "Open source RISC-V
  implemented from scratch in one night! ... the code is very compact,
  with around two hundred lines of Verilog ... my target is the
  ultra-low-cost Xilinx Spartan-6 family of FPGAs ... the performance
  of 75MIPS is good enough for me."  Via
  <https://news.ycombinator.com/item?id=17852876> "... a very incomplete
  implementation. ... The fact that this is RISCV is somewhat of a red
  herring as you could do a similar thing with a restricted subset of
  MIPS or ARM or even x86 ..." BUT author answers: "although 25% of
  RV32I instruction set is missing in my implementation, there is no
  side effect, ... since the gcc
  generates by default exactly the implemented subset and nothing
  more. I think this is a very important advantage in the RISCV
  architecture when compared with others and I dont think the gcc will
  have the same benevolent behaviour in the case of ARM or x86."

27 Aug 2018

- <http://stevelosh.com/blog/2018/08/a-road-to-common-lisp/> - "I want
  you to realize that Common Lisp is a stable, large, practical,
  extensible, ugly language."  Via
  <https://news.ycombinator.com/item?id=17852194>  "This is a
  godsend. Probably the best introductory article on Lisp to date."

26 Aug 2018

- <https://arxiv.org/abs/1807.08416> - Some Fundamental Theorems in
  Mathematics by Oliver Knill - Linked PDF is a survey of modern math
  in 133 pages, in the form of the "fundamental" theorem in each of
  135 areas, all in the first 62 pages!  Followed by a rationale and
  an explanation of "fundamental", by thirteen two-page lecture
  summaries on key topics, by Twitter math: forty-two 140-character
  statements of theorems with proof summaries, and more. "Teaching a
  course called “Math from a historical perspective” at the Harvard
  extension school led me to write up the present document. ... I’m
  reporting on many of these theorems as a tourist and not as a
  local."

 8 Aug 2018

- <https://twobithistory.org/2018/08/05/where-vim-came-from.html> - "Vim
  is only the latest iteration of a piece of software—call it the "wq
  text editor”—that has been continuously developed and improved since
  the dawn of the Unix epoch."  History of *qed*, *ed*, *ex*, *vi*, *vim* and
  other editors, with links to more detailed histories of several.
  More articles at <https://twobithistory.org/timeline.html> "This is a
  blog about computer history intended primarily for computer people."

 7 Aug 2018

- <https://believermag.com/broken-time/> - Broken Time: “Nardis” and the
  Curious History of a Jazz Obsession - "Though superb versions of
  “Nardis” have been recorded by everyone ... no one embodied its
  melodic potential more than Bill Evans. ..." much about Evans, some
  about Ralph Towner and Richard Beirach, bits about Miles Davis and
  several more. Via <https://www.metafilter.com/175776/Broken-Time>
  which also links to <https://www.jmeshel.com/124-bill-evans-nardis/>
  with 19 different recordings by Bill Evans, and also via
  <https://news.ycombinator.com/item?id=17684477> with links to more
  performances by Evans, Towner, and guitarist Antoine Boyer.
  Evans talks about music between playing with the trio at this house
  concert in Helsinki in 1970: <https://www.youtube.com/watch?v=C0AcvMBPuZI>

 3 Aug 2018

- <https://www.mnot.net/blog/2018/07/31/read_rfc> - How to Read an RFC -
  "Requests for Comments (RFCs) are how we specify many protocols on
  the Internet. These documents are alternatively treated as holy
  texts ... then shunned as irrelevant because they can’t be
  understood. ... with some insight into how they’re constructed and
  published, it’s a bit easier to understand what you’re looking
  at. ... I currently co-chair the IETF HTTP and QUIC Working Groups,
  and am a member of the Internet Architecture Board."  In addition to
  the sites linked in this article, <https://pretty-rfc.herokuapp.com>
  provides the RFCs in a more navigable HTML format.

31 Jul 2018

- <https://news.ycombinator.com/item?id=17607095> - "Where can
  one learn about the history of the internet ... ?"  Many links, for
  example <http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf>
  summarized here:
  <https://blog.acolyer.org/2015/01/22/the-design-philosophy-of-the-darpa-internet-protocols/>
  Several posts recommend this:
  <https://www.coursera.org/learn/internet-history>

- <https://news.ycombinator.com/item?id=17642846> - Hello World on z/OS - Comments 
  on this article about a novice trying to program a
  mainframe, by many others with more experience:
  <https://medium.com/@bellmar/hello-world-on-z-os-a0ef31c1e87f> "And
  yes, ... I am an IBMer, working in a z/OS product that's over 40
  years old" "z/OS, TSO, JCL and the rest are different to what most
  people are used to but this is where modern IT started, where
  virtualisation, high availability and serious backward compatibility
  were invented."

24 Jul 2018

- <http://exofrills.org/> - "xo - the text editor without frills ...
  designed to just provide the features that you need to program
  effectively and nothing else. It is ridiculously lightweight and
  only relies on Python 3, *urwid*, and *pygments*. Less than 850
  lines of code in a single file! ... If you ask for more features *I
  will probably say no!*  Just fork xo yourself."
  <https://github.com/scopatz/xo>

16 Jul 2018

- <https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1012.html> -
  "Roughly speaking, there are two ways in which people try to reason
  about programs; I shall distinguish them as “the postulational
  method” and “the operational method”. ... The tragedy of today's
  world of programming is that, to the extent that it reasons about
  programs at all, it does so almost exclusively operationally. ..."
  Don't miss the version in Dijkstra's handwriting at
  <https://www.cs.utexas.edu/~EWD/ewd10xx/EWD1012.PDF> See also
  <https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1073.html>
  (or .pdf) for some short examples of mathematics in the form he
  advocates.  See
  <https://www.cs.utexas.edu/~EWD/transcriptions/EWD13xx/EWD1300.html>
  for a lengthy rationale for this form.  Much much more at
  <https://www.cs.utexas.edu/~EWD/welcome.html>

- <http://www.ams.org/notices/201201/rtx120100031p.pdf> - A Revolution
  in Mathematics? by Frank Quinn.  Similar argument to EWD1012 above,
  but from a mathematician, not a computer scientist. "The physical
  sciences all went through 'revolutions': wrenching transitions in
  which methods changed radically and became much more powerful.  It
  is not widely realized, but there was a similar transition in
  mathematics between about 1890 and 1930. ... The strangest
  difference is that the scientific revolutions were highly visible,
  while the significance of the mathematical event is essentially
  unrecognized. ..."

 6 Jul 2018

- <https://basicengine.org/> - "The BASIC Engine is a very low-cost
  single-board home computer ... can be built at home ... for under 10
  Euros in parts. ... Check the one-hour silent video below to see how
  to build a BASIC Engine using a soldering iron, a heat gun,
  tweezers, solder wire and side cutters, without fancy tools, mad
  soldering skills and with only a minimal amount of patience." also
  <https://basicengine.org/history.html> - "The VS23S010D-L ... is a
  static RAM chip ... (that) comes with a video controller. ... It
  comes with 128 kB, some or all of which can be used as a frame
  buffer ... has a "block move" feature, more commonly known as a
  blitter. It allows you to copy sections of video memory ... provides
  a dramatic performance boost in ... text screen scrolling and
  rendering of tiled backgrounds."  Also
  <https://github.com/uli/basicengine-firmware> "The software is a
  heavily modified version of Toyoshiki Tiny BASIC
  <https://github.com/Tamakichi/ttbasic_arduino/tree/ttbasic_arduino_ps2_ntsc>
  " via <https://www.metafilter.com/175123/62984-bytes-free.> Recently
  noticed at <https://news.ycombinator.com/item?id=17674944> "drive
  tiny, minimal CPUs to do amazing things at the edge of their
  specifications cause it's cool and fun"  "That is software
  defined broadcast television. Mind. Blown." Compare to Uzebox, 24
  May below.

- <http://www.garbled.net/tmp/bringup.pdf> - "Bringup is Hard
  ... Bringup is the initial stage of a new port of an Operating
  System to a new hardware platform.  Often, bringup is one of the
  most difficult things to learn how to do in OS programming. ..."
  Related:
  <https://utcc.utoronto.ca/~cks/space/blog/linux/LinuxBootOverview> - "A
  broad overview of how modern Linux systems boot ..."  Much more
  at <https://news.ycombinator.com/item?id=17340033>

- <https://rushter.com/blog/python-virtualenv/> - "... quick overview of
  internals behind popular virtual environments, e.g., virtualenv,
  virtualenvwrapper, conda, pipenv."

- <https://www.partiallyapplied.com/blog/church/> - "Exploring Church
  Numerals with Python ... representing natural numbers as lambda
  calculus terms."  Also
  <https://eli.thegreenplace.net/2016/some-notes-on-the-y-combinator/> -
  "... the Y combinator isn't something unique to the Lisp family of
  languages, here's a Python implementation. ..."

27 Jun 2018

- <http://www.aholme.co.uk/6502/Main.htm> - "Here, with full source
  code, is a cycle-accurate 6502 microprocessor core in Verilog HDL,
  which was automatically generated from a transistor-level netlist
  ...  The core runs 10 times faster than a real 6502 and occupies
  only 8% of the flops and 7% of the LUTs in the Xilinx xc3s500e FPGA
  on a Spartan 3E Starter Kit. ... The 6502 has been studied and
  reverse-engineered more than any other microprocessor ..." (reviews
  history, with some links).  via
  <https://news.ycombinator.com/item?id=17399967> with more links about
  6502 and other 8-bit processors.

- <https://leanpub.com/insidethepythonvirtualmachine/read> - "Inside The
  Python Virtual Machine".  Long and detailed with lots of examples in
  C and Python byte code.  Finishes with an explanation of generators
  and how they are implemented.

- <https://github.com/dylanaraps/pure-bash-bible> - "... methods of
  doing various tasks using only built-in bash features ... remove
  unneeded dependencies from your scripts ... make them that little
  bit faster."  Also <https://dmytrish.net/blog/en/bash-tcp> - "bash can
  connect to TCP/UDP servers on its own, without using nc/telnet
  ... (by using) /dev/tcp/HOST/PORT" ... (example follows)

25 Jun 2018

- <http://recodeproject.com/> - "...a community-driven effort to
  preserve computer art by translating it into a modern programming
  language (Processing). ... "Computer Graphics and Art" was a
  quarterly magazine published between 1976 and 1978. We are using PDF
  copies of the entire run of the magazine as our starting point for
  the project."

- <https://monoskop.org/images/b/b3/Dwyer_Terence_Composing_with_Tape_Recorders_Musique_Concrete_for_Beginners.pdf> - 
  Oxford University Press, 1971.  PDF includes the entire 44 page
  book. via <https://news.ycombinator.com/item?id=17338092>

- <https://github.com/pervognsen/bitwise/> - "Bitwise is an educational
  project where we create the software/hardware stack for a computer
  from scratch. ... can be done much more simply and quickly than
  people realize if we strongly favor simplicity over marginal gains
  in feature completeness or performance. ... The first major project
  will be the C-like systems language compiler. ... On the hardware
  side of things, we will be designing a computer from scratch that
  can be synthesized and deployed on a real FPGA. This will include a
  RISC-V CPU ..."

14 Jun 2018

- <https://bootstrapping.miraheze.org/wiki/Main_Page> - "This wiki is
  about bootstrapping. Building up compilers and interpreters and
  tools from nothing."  Also
  <https://speakerdeck.com/nineties/creating-a-language-using-only-assembly-language.> "Let's play with limitations ..." 
  Both via <https://news.ycombinator.com/item?id=17290573> - "The
  problem with this kind of site ... is that it could take years to
  review each item."

12 Jun 2018

- <https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/> -
  What is code? by Paul Ford, much-praised 38,000 word essay with web
  animations etc. comprises entire June 11, 2015 issue of Bloomberg
  Business Week.  Also
  <https://medium.com/interactive-mind/so-you-don-t-have-time-to-read-what-is-code-1da0e4529896>
  "Here are some main takeaways, and then a full outline is below."
  <https://news.ycombinator.com/item?id=17259483> - reviewed on HN three
  years later - "I don't think this really achieves what it sets out
  to do ... This seems more like "What is tech culture?" for people
  who are already a part of tech culture."
  <https://www.theframeworkproject.com/interviews/paul-ford> - author
  interview - "... should everyone learn to code? Everyone should seek
  to empower themselves to understand more about the world that
  they're in. Coding is not communicated as a path to that. It's
  communicated as a way to riches or a socioeconomic ladder."
  "... once things scale and lots and lots of human beings get
  involved, the fundamental crappy parts of human culture sort of
  start to permeate back through. Twitter's a great example. You
  couldn't have a more annoying bunch of do-gooders trying to create
  Twitter, and then the platform they create ends up having enormous
  issues ..."  "The tweets don't add up to a corpus. I miss
  that. ... When I was writing every day or blogging or doing weird
  code stuff, I could point back to months before when I had just not
  known something and now I knew something new and I created something
  new. And I don't feel that the platforms that we have today
  encourage people to create at that level."
  <http://gawker.com/what-is-code-a-q-a-with-writer-and-programmer-paul-fo-1710884170> - another author interview - "... of course it’s too much. ... We
  just live in this bizarre land of plenty, and technology is just one
  of those things we have way too much of."

- <https://rushter.com/blog/python-gil-thread-scheduling/> - Python's
  GIL implemented in pure Python - "I was trying to understand all the
  details of the GIL ... from the CPython's source code.  So here is a
  simplified algorithm of the thread scheduling that is taken from
  CPython 3.7 and rewritten from C to pure Python. ... Basically, the
  job of the GIL is to pause the while loop for all threads except for
  a thread that currently owns the GIL."

11 Jun 2018

- <https://publicdomainreview.org/collections/ernst-haeckels-jellyfish/>
  Many beautiful pictures and links to more of his work.  More Haeckel
  drawings at 2 Nov 2017 below.

- <http://www.pong-story.com/LAWN_TENNIS.pdf> - Atari Pong Circuit
  Analysis - Awesomely detailed, 106 pages. "Atari’s Arcade Pong PCB
  contained 66 IC’s. ... It was simply hard wired TTL logic and
  predates microprocessor and software controlled video games ... the
  game has also been emulated in software to play on computers. ... in
  most cases it is a poor facsimile of the real thing."  via
  <https://news.ycombinator.com/item?id=17200163> "... an insanely
  clever masterpiece of digital design. ... It’s mindbendingly
  brilliant."  Compare to Uzebox with 2 ICs, 24 May 2018 below.

 3 Jun 2018

- <https://web.archive.org/web/20110723033542/http%3A//www.burlingtontelecom.net/~ashawley/gnu/emacs/doc/emacs-1978.html>
  An Introduction to the Emacs Editor by Eugene Ciccarelli, AI Memo
  No. 447, January 1978, Artificial Intelligence Laboratory,
  Massachusetts Institute of Technology (not the same as Richard
  Stallman's 1979 AI Memo 519 on Emacs,
  <https://ia601004.us.archive.org/32/items/MITAIMemo519/MIT-AIMemo519.pdf>).
  "This memo is aimed at users unfamiliar not only with the Emacs
  editor, but also with the ITS operating system. ...  Emacs runs on
  the ITS machines, AI, ML, MC, and DM.  For people coming from an
  Arpanet TIP, the host numbers are: 134 (AI), 198 (ML), 236 (MC), and
  70 (DM).  If you don't have a regular username there, ... (use) the
  WHOIS program: :WHOIS XYZ.  If WHOIS didn't find any regular user
  XYZ, you can use that name.  :LOGIN XYZ.  You are now talking to
  DDT, the top-level, monitor program ..."

 2 Jun 2018

- <https://news.ycombinator.com/item?id=17194456> - comments on 'A few
  words on Doug Engelbart' by Bret Victor: "The failure to replicate
  Engelbart's vision of collaborative UI plagues me ... we can't even
  achieve the level of integration they had back in the 60s. ..."
  Much discussion of why Engelbart's prototype from fifty years ago --
  and his larger project to 'augment human intellect' -- remain
  mostly unrealized: "... Engelbart's system was a completely shared
  space in which everyone lived and was trusted, then of course our
  systems are inelegant by comparison. ..."

 1 Jun 2018

- <http://obsolescence.wixsite.com/obsolescence/how-to-use-the-pidp-8> -
  Obsolescence Guaranteed - "The PiDP-8/I is a modern replica of the
  1968 PDP-8/I computer. ... behind the blinking lights sits a
  Raspberry Pi, running a modified version of SimH ... the idea was to
  illustrate how utterly unique the PDP-8 was in the evolution of
  computing. ... it was pretty much *the* prototype of a personal
  computer."

- <http://computermuseum.informatik.uni-stuttgart.de/cm003_en.html> -
  Computermuseum der Fakultat Informatik - photos and descriptions of
  scores of calculators, computers, peripherals, and associated test
  instruments from the 1950s - 1980s. "not all pages have been
  translated yet", use the deutsch page to see those pictures.  Uses
  typewriter font throughout - for that historical flavor?

- <http://www.cap-lore.com/CapTheory/> - "Capability Theory by Sound
  Bytes ... This is a collection of insights for designing capability
  based systems. ... "  Many many links on capabilities and operating
  systems research crammed into a no-frills single page.

- <https://github.com/nebulet/nebulet> - "Nebulet is a microkernel that
  executes WebAssembly modules instead of ELF binaries. Furthermore,
  it does so in ring 0 and in the same address space as the kernel,
  instead of in ring 3." Also <http://lsneff.me/why-nebulet/> "Operating
  system design has been somewhat stagnant since, well, ever.
  ... Nebulet lets us try ideas that have been left dormant again."
  via <https://news.ycombinator.com/item?id=17187384>

31 May 2018

- <http://www.bldgblog.com/2018/05/journey-of-a-single-line/> -
  "... Wacław Szpakowski was a trained architect who dedicated an
  inordinate amount of his own free time to hand-drawing elaborate
  mazes and patterns using only a single line. ..."  Several beautiful
  and striking examples on this page, many more here:
  <http://miguelabreugallery.com/exhibitions/grounding-vision-waclaw-szpakowski/>
  (click images link in upper right corner)

24 May 2018

- <http://uzebox.org/wiki/index.php?title=Main_Page> - Uzebox -
  "retro-minimalist homebrew game console. ... video sync generation,
  tile rendering and music mixing is done realtime by a background
  task ... easy and fun to assemble and program ... contains only two
  chips: an ATmega644 and an AD725 RGB-to-NTSC converter." Links to
  <http://uzebox.org/files/wiki/uzebox_how_it_works_v10.pdf>, 21 pages:
  "... ATMega644 ... 20Mhz ... 64K of flash and 4K of RAM. ... I
  couldn't get around insane cycle-counting for the kernel ...  Each
  and every (scan)line, including the sync code must take exactly 1820 clock
  cycles. ..."

22 May 2018

- <https://www.metafilter.com/174248/A-plethora-of-Sun-Ras-four-decades-of-baffling-dazzling-mystical-jazz>
  Long annotated discography and links to performances at YouTube and
  Bandcamp.  Defies description or summarization.

- <http://www.ubuweb.com/> UbuWeb.  "All avant-garde.  All the time."
  One of many many pages is <http://www.ubu.com/emr/> Electronic Music
  Resources: "We've taken the filing cabinet as our model, rather
  than the museum, and our focus is on historical and rare material
  rather than recent developments."  Interesting austere page design.

21 May 2018

- <https://www.pocketputer.com/> Pocket Puter - via
  <https://news.ycombinator.com/item?id=17114515>, "I want to create the
  information piece to make it possible for homeless individuals and
  others at risk of homelessness to use minimal tech, like a
  smartphone or tablet, to start addressing some of their problems. As
  one element of that, I explicitly want to support the ability to
  earn an online income, even with very minimal tech. ... I was able
  to earn money online while homeless and eventually get off the
  street."

- <https://tools.ietf.org/html/rfc1>, RFC1: Host Software by Steve
  Crocker, 7 Apr 1969.  "The software for the ARPA Network exists
  partly in the IMPs and partly in the respective HOSTs.  BB&N has
  specified the software of the IMPs and it is the responsibility of
  the HOST groups to agree on HOST software. ... I present here some
  of the tentative agreements reached and some of the open questions
  encountered."

20 May 2018

- <http://kakoune.org/why-kakoune/why-kakoune.html> - " ... in insert
  mode most keys insert their character in the buffer ... but in
  normal (default) mode, keys have a different effect (move, copy,
  paste, undo, open ...) ... non-modal text editors are extremely
  biased towards insertion. ... at the expense of making most other
  operations suboptimal ... vi basic grammar is verb followed by
  object ...  Kakoune’s grammar is object followed by verb ... you
  always see the current object (the selection) before you apply
  your change ...  vi treats moving around and selecting an object as
  two different things. Kakoune unifies that, moving is selecting. w
  does not just go to the next word, it selects from current position
  to the next word. ..."

18 May 2018

- <https://www.scottaaronson.com/blog/?p=524> - "Timeline of computer
  science ... I somehow got roped into creating a timeline of “150
  major events in computer science history" ... I’m including my
  current draft list of 152 events below ... From the data, it would
  appear that the level of intellectual excitement in computer science
  peaked in the 1960s, and has steadily declined ever since, except
  for a bump in the 1990s coinciding with the Internet boom.  ..."

- <http://blog.thelifeofkenneth.com/2017/11/creating-autonomous-system-for-fun-and.html>
  "...  start thinking about the Internet ...  as a very large mesh of
  independent connected organizations instead of an abstract cloud
  ... Almost no one needs to consider the Internet at this
  level. ... you can probably pay someone else to provide it and don't
  need to sit down and learn how BGP works and what an Autonomous
  System is. But let's ignore that for one second, and talk about how
  to become your own ISP. ..."

- <http://www.donationcoder.com/forum/index.php?topic=45547> - "The Acme
  editor on Debian on Windows ... Windows 10 has got support for being
  used as a host system for Linux applications ... this is the least
  inconvenient way to use Acme on Windows.  What we need is both an X
  server ... and a Linux distribution running on the Windows NT
  subsystem. ...  Here's how to install it. ... Try something new?
  Dive into history? Show off your weirdness to your friends? Do nerdy
  things with nerdy software? Acme has it."

14 May 2018

- <http://www.tnhh.net/posts/bked-gui-as-tui.html> - "BKED (pronounced
  buh-ked, e as in kept) was the de-facto text editor in Vietnam in
  the 80s-90s. ... BKED runs on MS-DOS and looks just like Microsft
  Editor aka edit.com, except for it displays and allows the user to
  input text in Vietnamese. ... it is a full-blown GUI that runs in
  Hercules/CGA/EGA/VGA graphics .... It draws every single pixel in
  its GUI with no acceleration ... It had to do it very quickly and
  economically – computers in Vietnam at the time were all old
  secondhand ones imported from the US recycling centers and
  such. ... it could also do quite sophisticated mathematical formulas
  and chart drawing. ... the editor was used to typeset the whole
  suite of national textbooks on every subject in the 90s."  Several
  screenshots in the article demonstrate the features.

13 May 2018

- <https://bertfreudenberg.github.io/Smalltalk78/> - Smalltalk78 desktop
  running in the browser.  Looks very accurate but not clear how to
  work it on a mouse-less Macbook with a touchpad.  Via
  <https://github.com/bertfreudenberg/Smalltalk78> "...  a Virtual
  Machine written in JavaScript to run a Smalltalk-78 snapshot in the
  web browser. To learn more, please read our paper ... (at)
  <http://freudenbergs.de/bert/publications/Ingalls-2014-Smalltalk78.pdf>"

10 May 2018

- <https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda>
  Hyperlinks_in_Terminal_Emulators.md, "Hyperlinks (a.k.a. HTML-like
  anchors) in terminal emulators. Most of the terminal emulators
  auto-detect when a URL appears onscreen and allow to conveniently
  open them. ... It was, however, not possible until now for arbitrary
  text to point to URLs, just as on webpages. ..."

- <https://github.com/junegunn/fzf> - A command-line fuzzy finder -
  "It's an interactive Unix filter for command-line that can be used
  with any list; files, command history, processes, hostnames,
  bookmarks, git commits, etc. ..."  See also
  <https://github.com/bling/fzf.el>, "an Emacs front-end for fzf".

 9 May 2018

- <https://www.metafilter.com/174029/Sextets-septets-octets-nonets>
  "Stepping beyond the more familiar three-, four- and five-piece
  line-ups, there is a wealth of classical music out there composed
  for slightly bigger bands. ... a small selection of which can be
  found via the links within..."  Also links to:
  <https://www.metafilter.com/166863/Piano-violin-and-cello>
  <https://www.metafilter.com/163338/String-Quartets>
  <https://www.metafilter.com/170478/Piano-Quintets>

- <https://news.ycombinator.com/item?id=17028491> - "Emacs. It's the
  "best of both worlds" combination of text-based interfaces and
  GUIs. It supports software that can be interactive, and yet also as
  interoperable as CLI applications ...", cites
  <https://ambrevar.bitbucket.io/emacs-everywhere/> - "... any
  structure, interface element and even code can be passed around and
  combined between the different interfaces to various programs."  Via
  <https://news.ycombinator.com/item?id=17026490>, comments on
  <https://ambrevar.bitbucket.io/emacs-eshell/>

30 Apr 2018

- <https://ericphanson.com/posts/2016/the-traveling-salesman-and-10-lines-of-python/>
  Traveling Salesman solved by simulated annealing.  The ten lines of
  Python include two lines to draw a graph of the route.  Demonstrates
  matplotlib, numpy, random, math, and several comprehension and
  slicing idioms.  Nice page design: "This site created with the Tufte
  theme for Jekyll."

- <https://www.pagetable.com/?p=774> - "Microsoft BASIC for 6502
  Original Source Code [1978] ... currently the oldest publicly
  available piece of source written by Bill Gates. ... developed on a
  PDP-10, using the MACRO-10 assembler. A set of macros developed by
  Paul Allen allowed MACRO-10 to understand and translate 6502
  assembly, albeit in a modified format to fit the syntax of macros.
  ... with all original comments, documentation and easter eggs ...
  6955 lines."  Via <https://news.ycombinator.com/item?id=16938934>,
  "What are some examples of beautiful x86 assembly code?"

26 Apr 2018

- <https://www.popsci.com/quantum-computer-photos> - "Yale University
  applied physicists Robert Schoelkopf and Michel Devoret pioneered a
  way to stabilize (qubits). By building qubits out of superconductors
  ... As a look inside their lab reveals, it takes a huge
  operation—and a very cold fridge."  Impressive photos of cryogenics
  and microwave electronics.

- <https://www.gnu.org/software/guix/blog/2018/guix-on-android/> - Not
  really practical but provides a description of how Android is
  configured on top of the Linux kernel, with a photo of terminal
  running on a tiny phone.  "Android's root filesystem is actually the
  initramfs so any modification to its content will be lost after a
  reboot."

25 Apr 2018

- <https://jeffreykegler.github.io/personal/timeline_v3> - "Parsing: a
  timeline", actually a short but dense review article from Panini in
  4th BCE then skipping to the early 20th century and on through 2012.
  Extensive bibliography with links.  Samples: "1991 ... On the
  written record, the discontent with LALR and yacc is hard to
  find. ...  But, by 1991, a movement away from LALR has already
  begun. Parsing practice falls back on recursive descent ..."  "2004:
  ... PEG takes the old joke that "the code is the documentation" one
  step further -- with PEG it is often the case that nothing documents
  the grammar, not even the code."

16 Apr 2018

- <http://www.vulture.com/article/100-most-influential-pages-comic-book-history.html> - "We have set out to trace the evolution of American comics by
  looking at 100 pages that altered the course of the field’s
  history." From 1929 to 2014.

- <https://www.theverge.com/2018/4/16/17233946/olpcs-100-laptop-education-where-is-it-now>
  "... the XO-1: a toylike green-and-white laptop with rounded edges,
  a swiveling “neck” instead of a standard hinge ...  Its screen
  folded into the keyboard to create a tablet ... Ear-like antennas
  flipped up to extend its Wi-Fi range ... hundreds of color
  permutations, so kids could tell their laptops apart. And a
  dustproof one-piece rubber keyboard made it easy to print any key
  layout." (Many large photos with the article show all this.)

  Comments at <https://news.ycombinator.com/item?id=16849374> - "... the
  OLPC has *tremendous* industrial design, which nothing else I've
  ever seen matches." "... there still isn't a laptop that I've seen
  that is a durable as the XO. ... It came with a complete repair
  manual and you could use standard tools to take it apart and put it
  back together ..." "The OLPC organization seriously tried to make
  Alan Kay's Dynabook real ... they got in way over their heads ..."

  Earlier at <https://news.ycombinator.com/item?id=13258261> -
  "... meant to come with ... a "View Source" button to let you
  inspect and edit the code to all your apps; UI making it easy to set
  up ad hoc networks to share/collaborate with anyone around you ..."

  See also <http://laptop.org/8.2.0/manual/> - "There are no files,
  folders, or applications. ... Activities include an application,
  data, and history of the interaction that can be used to
  resume. ... Everything is saved automatically ... A Journal is used
  for accessing data. ... Some Activities allow users to work and learn
  cooperatively. For example ... to collaboratively create a document.

15 Apr 2018

- <http://nymag.com/selectall/2018/04/an-apology-for-the-internet-from-the-people-who-built-it.html>  - "To understand what went wrong — how the Silicon Valley dream of
  building a networked utopia turned into a globalized strip-mall
  casino overrun by pop-up ads and cyberbullies and Vladimir Putin — we
  spoke to more than a dozen architects of our digital present."

- <https://www.metafilter.com/173509/Take-me-for-a-walk-in-the-morning-dew-my-honey> - "Morning Dew is a post-nuclear protest song, written in 1961 by
  Canadian Bonnie Dobson ... the power of the song is evidenced by
  the vast number of covers over the years."  History,
  recollections, links to many versions.

10 Apr 2018

- <https://github.com/adamisntdead/QuSimPy> - "a toy multi-qubit quantum
  computer simulator, written in 150 lines of python", uses numpy and
  functools reduce, nice concise examples of complex matrices
  etc. <https://news.ycombinator.com/item?id=16797193> - "... to
  simulate a basic quantum computer, all you need is the following: A
  product state vector, ... A set of common quantum logic gates, which
  are matrices you multiply against the product state vector ... The
  measurement logic, where you calculate how the product state
  collapses ... This project is an implementation of those three
  things in Python. There is nothing special about the above
  mathematical constructs save that they match the observed semantics
  of a quantum system." ... "Quantum Computation and Quantum
  Information, a.k.a "Mike and Ike" is the authoritative textbook
  ... very readable and beginner friendly. It's well worth reading the
  introduction to QC in the first twelve pages and skimming the first
  sixty."

 7 Apr 2018

- <https://news.ycombinator.com/item?id=16775768> - "Raspberry Pi
  microSD card performance comparison" "I've tested the (several RPi
  rivals) and all of these boards are leagues beyond the Pi in terms
  of I/O performance (both networking and local storage). The problem
  is ...  these boards ... have a much worse initial onboarding
  experience (grabbing a disk image, flashing the card or onboard
  memory, first boot, then figuring out where to go next) than what
  you get with the Pi and it's handy, well-written tutorials."  That
  is the only reason that the Raspberry Pi maintains its position of
  where it is. It isn't a great computer, it is a great ecosystem.
  ... "... would just be happy if my rpi would not randomly corrupt
  the memory card for no reason all the time. ..."  Many comments on
  reliability (or not) of various brands/kinds of SD cards, and how
  to boot from server as alternative to SD cards etc.

 6 Apr 2018

- <https://news.ycombinator.com/item?id=16775744> - "Ask HN: How to
  self-learn electronics?"  Many many detailed responses with advice
  on books, videos, equipment, and methods.

- <https://news.ycombinator.com/item?id=16773824> - comments on NixOS
  18.03 Released.  "It makes all packages immutable by giving them
  their own directory identified by a hash that is derived from ALL of
  that package's dependencies. ... all changes you make to your system
  are non-destructive. ... you can always roll back to a previous OS
  state ... If you want to reproduce your system, you can copy the
  whole content and "checkout" the relevant revision on the new
  system. ..."

 5 Apr 2018

- <http://cs107e.github.io/> - "CS107e Spring 2018 ... third course in
  Stanford’s introductory programming sequence. ... bare metal
  programming on the Raspberry Pi. ... uses no operating system and
  few external libraries." ... resource page links to Raspberry Pi
  Bare Metal Forum at
  <https://www.raspberrypi.org/forums/viewforum.php?f=72.>   Possibly
  pertinent: <https://web.stanford.edu/class/cs140e/> - "CS140e (Winter
  2018) An Experimental Course on Operating Systems ... students
  implement a simple, clean operating system (virtual memory,
  processes, file system) on a Raspberry Pi 3 in the Rust programming
  language".  Comments: <https://news.ycombinator.com/item?id=16134618>
  See also 18 Jan 2018.

- <http://seenaburns.com/2018/04/04/writing-to-the-framebuffer/>
  "... /dev/fb0 acts like any other memory device in /dev and we can
  write to it like a file. ...", several examples using cat and simple
  C programs.  <https://news.ycombinator.com/item?id=16755552> "Keep in
  mind that /dev/fb, on a modern system, isn't an actual framebuffer
  on your GPU. It's a land of make-believe, mostly supported to get
  the kernel console ("fbcon") working. ... there's compatibility code
  which sets up a user-space buffer in the KMS subsystem [0] which is
  swapped to when fbcon happens through a large chain of strange
  events that are hard to describe. ..."   See also 31 Jan 2018.

 2 Apr 2018

- <https://github.com/vygr/ChrysaLisp> - "Parallel OS, with GUI,
  Terminal, OO Assembler, Class libraries, C-Script compiler, Lisp
  interpreter and more...  Runs on OSX or Linux for x64 ... Will move
  to bare metal eventually ...  What we deserve is a modern version of
  what Taos did ..." (author is "Inventor of the Taos OS")

31 Mar 2018

- <https://www.moma.org/interactives/exhibitions/2011/AccesstoTools/> -
  "Publications from the Whole Earth Catalog, 1968-1974" with
  nostalgia-inducing content, typography, and design, via
  <https://news.ycombinator.com/item?id=16720764> which also links to a
  page by yellowed page scan of the classic Last Whole Earth Catalog:
  <https://archive.org/details/B-001-013-719>

30 Mar 2018

- <https://github.com/ShivamSarodia/ShivyC> - "ShivyC is a hobby C
  compiler written in Python that supports a subset of the C11
  standard ...  has a very limited preprocessor that parses out
  comments and expands #include directives."  Not small, looks like
  thousands of lines.  Comments in
  <https://news.ycombinator.com/item?id=16719648> - "... The parser has
  a somewhat unusual structure ... "exception-oriented programming"
  ... fits that code well."

28 Mar 2018

- <https://www.moma.org/calendar/exhibitions/3863?locale=en> - "Thinking
  Machines: Art and Design in the Computer Age, 1959–1989, The Museum
  of Modern Art." Comments at <https://news.ycombinator.com/item?id=16694759>

- <https://1403.slantedhall.com/> - "1403 Vintage Mono Pro ... typeface
  inspired by the IBM 1403 mainframe line printer from the 1960s"
  via <https://news.ycombinator.com/item?id=16701009> responding to 
  <https://www.ibm.com/plex/> - "IBM Plex™ is our new typeface."

- <https://try-mts.com/why-try-mts/> - "Try MTS. Exploring the Michigan
  Terminal System. ...  an operating system running on IBM System/360
  compatible mainframes dating from the 1960s. ... back in the 60s and
  70s there was an explosion of new operating systems and ideas and
  it's important to get a flavour of what was going on then."

22 Mar 2018

- <http://invislib.blogspot.com/2008/08/t.html> - "The Invisible Library
  ... catalog of books that exist only within other books", including
  "TRAPNEL, X. (Frances Xavier): Bin Ends, Camel Ride to the Tomb,
  Dogs Have No Uncles, Profiles in String  —from Anthony Powell's A
  Dance to the Music of Time"

- <http://www.bachrewrite.com/en/> - "Bach played on electric pianos ...
  the point was the combination of a period-instrument orchestra with
  the sound of the Wurlitzer and Rhodes, which – perversely – should
  now also be treated as historical instruments."  Interesting
  black-and-white page design and photography.

19 Mar 2018

- <https://idea-instructions.com/> - "An ongoing series of nonverbal
  algorithm assembly instructions" - in the style of Ikea
  instructions!

16 Mar 2018

- <https://standardebooks.org/about/> - "The Standard Ebooks project
  differs from those etext projects (Gutenberg, Archive) in that we
  aim to make free public domain ebooks that are carefully typeset,
  cleaned of ancient and irrelevant ephemera, take full advantage of
  modern ereading technology, are formatted according to a detailed
  style guide, and that are each held to a standard of quality and
  internal consistency."

- <https://github.com/thoughtbot/write-yourself-a-roguelike> - "Write
  Yourself A Roguelike: Ruby Edition ... compile the contents of the
  book directory into an EPUB-formatted e-book." (contents are .md
  files)

15 Mar 2018

- <https://news.ycombinator.com/item?id=16591918> - "“Write your own” or
  “Build your own” software projects. ... writings/tutorials/videos
  which describe a specific technology or feature by implementing them
  ..."  Many links to pertinent projects.  Added 16 Mar:
  <https://github.com/tuvtran/project-based-learning> "Curated list of
  project-based tutorials",
  <https://github.com/cweagans/awesome-diy-software> "list inspired by
  this HN post" (above), apparently mostly just links from that post.

- <http://nsl.com/> - "no stinking loops ..." APL/J/K/Q etc. Many many
  links, including lots of code at <http://nsl.com/k/> and
  <https://a.kx.com/a/k/examples/>  Linked from
  <https://news.ycombinator.com/item?id=16584139> "after K ... the whole
  software engineering world starts to look like a ridiculous house of
  cards.  (K can do) fast and efficient in memory databases in ~20
  lines, or an npm-style package manger[1] in less than ~400 lines"

12 Mar 2018

- <https://news.ycombinator.com/item?id=16562173> - "How to self-learn
  math?"  Many book suggestions.

- <https://news.ycombinator.com/item?id=16562956> - comment in parent
  <https://news.ycombinator.com/item?id=16562694> "Were we more
  productive ... years ago?" "No, absolutely not. ... in web dev
  ... rails was the big revolution. ... wasn’t so much techical as
  social: ... an extremely well-curated set of best practices
  ... under the guise of a framework. ... you could join any team and
  know your way around the codebase on the second day."

- <https://news.ycombinator.com/item?id=16563507> - comment in parent
  <https://news.ycombinator.com/item?id=16562694> "Were we more
  productive ... years ago?" "I definitely have to put up with more
  distraction ... but I also know and learn more. It's hard to tame
  internet to not be invasive ... given most actors are actively
  trying to be invasive. ...  given the utility of internet, one has
  to learn to put up with it, and that's not all that easy. ...  I do
  not enable notifications from anything ... I decide when I want to
  know about the outer world: check feeds or mail manually, when I
  want.  I use no social media.  ... The biggest distraction with
  computers is internet. And one needs to learn how to use it
  defensively. Maybe we need a "Defensive Internet Users" wiki thing?"

10 Mar 2018

- <https://n-o-d-e.net/ubuntu_laptop_overview.html> and
  <https://n-o-d-e.net/ubuntu_laptop_how.html.> "THE DIY $100 MINI
  UBUNTU LAPTOP ... Nexus 7 tablet and keyboard ... fits in one hand,
  and weighs about 900g ... an official Ubuntu ARM port made by
  Canonical which is specifically for the 2012 Nexus 7 ... low power
  ... can easily charge it through a USB charger."  Interesting page
  design and typography.

 7 Mar 2018

- <https://ask.metafilter.com/319841/Classical-music-desert-island-playlistfor-the-Isle-of-the-Dead>
  "I am on a hunt for little or lesser-known classical music that
  invokes disquiet or suspense in the listener."  Many many responses.
  "These are fabulous suggestions! I have slowly been working my way
  through this list..."

 4 Mar 2018

- <https://ask.metafilter.com/319733/Classical-Music-looking-for-contrasting-performances-of-the-same-piece>
  "recommendations from some classical music heads of two or more
  performances of the same piece, both which differ from each other
  and are good (or great) versions of the composition they're
  representing."  Soon followed by this, "inspired by a Mefi comment":
  <https://ask.metafilter.com/319738/Music-that-gives-you-chills>
  "... music that has a real emotional and physiological effect like
  this, that makes your heart go faster and catches your breath. ...
  music that give you chills down your spine and bring tears to your
  eyes. Music that leaves you breathless."

- <https://www3.nd.edu/~dthain/courses/cse40243/fall2017/intel-intro.html>
  "This is a brief introduction to X86-64 assembly language for novice
  compiler writers using the GNU software tools. ... not exhaustive
  ... but ... enough to ... write most of the backend of a C compiler
  for an undergraduate class."

- <http://xxyxyz.org/line-breaking/> - "Line breaking, also known as
  word wrapping or paragraph formation, is the problem of dividing a
  text into a sequence of lines so that every line spans at most some
  fixed width. ...  (The obvious) greedy algorithm ... may leave too
  much whitespace at the end of a line ... wildly different line
  lengths ... The idea then is to come up with a configuration of line
  breaks which minimizes the total sum of such penalties, a strategy
  know as 'minimum raggedness'. "  Presents several algorithms in
  Python, with explanations and references.  Interesting page design
  and typography.  Links to other pages by same author.
  <https://news.ycombinator.com/item?id=16511900> explains the graphs.

 3 Mar 2018

- <https://sortix.org/> - "a small self-hosting operating-system aiming
  to be a clean and modern POSIX implementation. It is a hobbyist
  operating system written from scratch with its own base system,
  including kernel and standard library. It has been in development
  since February 08 2011 by a single developer ... C with a C++ kernel
  ... The lack of compatibility constraints compared to other
  operating systems makes it possible to make a cleaner
  implementation. ... 1.0 release has 169k lines of source code ..."
  <https://news.ycombinator.com/item?id=16500705> - discussion of Sortix
  with several contributions by the author on motivation, design
  decisions, and comparison to other projects.

 2 Mar 2018

- <http://pubs.opengroup.org/onlinepubs/9699919799/utilities/ed.html> 
  POSIX specification for ed, from IEEE Std 1003.1-2008, 2016 Edition
  "The input files shall be text files. ..."

28 Feb 2018

- <https://github.com/norvig/paip-lisp> - "Lisp code for the textbook
  'Paradigms of Artificial Intelligence Programming (1992)' ... (also)
  A pdf of the book ..."
  <https://news.ycombinator.com/item?id=16469167> - "This book is
  timeless classic that is not getting old. ... learn to program after
  you already know how to program. ..." "Following Norvig’s thought
  process on how to develop computer programs is like pair programming
  with one of the best programmers of all time. ..."

- <https://news.ycombinator.com/item?id=16471019> - thread in HN parent
  above: "(Norvig writes) (Lisp) is a good assembly language because
  it is possible to write Lisp in a style that directly reflects the
  operations available on modern computers." (Followed by several
  posts with examples of "this assembly style of programming in Lisp",
  some inline, some links)

- <https://gist.github.com/razimantv/1b33d4a090a5bc9ed94928012b37c3f0> -
  "Stackify!  Deep recursion will give you stack errors. ... you can
  decorate the function by abusing exceptions and turn the function
  iterative ... (defines function named stackify, demonstrates
  @stackify def ackermann(M,N): ...)"
  <https://news.ycombinator.com/item?id=16478534> - "Abusing python can
  really save your life sometimes." "I love how everything is
  available at runtime. ... super useful in a pinch." "Nothing is more
  permanent than a temporary solution." (Many posts show, or link to,
  unobvious uses/abuses of Python)

25 Feb 2018

- <http://lispm.de/springer-lisp-books> - Lisp/AI books from Springer, free
  for download, including:
  LISP Lore: A Guide to Programming the LISP Machine, Second edition, 1987
  LISP, Lore, and Logic, An Algebraic View of LISP Programming,
   Foundations, and Applications, 1990
  Computer-Aided Reasoning, An Approach, 2000 - About ACL2
  Computer-Aided Reasoning, ACL2 Case Studies, 2000
  many more ...

24 Feb 2018

- <https://news.ycombinator.com/item?id=14076352> - comment in
  <https://news.ycombinator.com/item?id=14075795> "Ask HN: Has anyone
  considered forking TempleOS and making a modern OS out of it?"
  "Part of what makes TempleOS so powerful with so little code is that
  everything fits together, so you can make a lot of
  assumptions. ... Really tightly integrated designs eventually get to
  the point where there's almost nothing to change... because each
  design choice relies on the last. ... you eventually end up with an
  extremely lightweight design that is very strong, but where every
  piece of the whole is extremely important. ... It's not perfect but
  it's pointed at perfection and it aims to get there."

21 Feb 2018

- <https://news.ycombinator.com/item?id=16423643> about Steven Levy's
  book Hackers: Heroes... (responding to parent post
  <https://news.ycombinator.com/item?id=16421674> about Brand's Spacewar
  in Rolling Stone): "Reading the book now and it’s making me a little
  sad. Where can I find today’s Tech Model Railroad Club, Homebrew
  Computer Club, Community Memory, People’s Computer Company? Are
  there still places left where computing is small, local,
  non-commercial and so alive? I love programming, but I’ve never felt
  myself to be part of any tribe like the people in Hackers clearly
  do. It all just feels so commoditized and un-magical these days!"

19 Feb 2018

- <https://www.dailycodingproblem.com/blog/archives/> - "Get
  exceptionally good at coding interviews by solving one problem every
  day."  Classic problems with simple Python solutions and explanations:
  blog/knights-tour/
  blog/an-introduction-to-backtracking/
  blog/how-to-formulaically-solve-tree-interview-questions/
  blog/how-to-find-arbitrage-opportunities-in-python/

12 Feb 2018

- <https://blogs.scientificamerican.com/guest-blog/the-evolution-of-the-physicists-picture-of-nature/> - "We are republishing this article by Paul Dirac from the May 1963 issue of Scientific American ..."

- <https://github.com/shreevatsa/knuth-literate-programs/tree/master/programs>
  linked from <https://news.ycombinator.com/item?id=16363186> - "Who is
  the longest-serving programmer? ... (Knuth) still writes two or
  three programs a week ... here:
  <https://cs.stanford.edu/~knuth/programs.html> — the most recent is
  from December 2017. They are in .w format (CWEB) ... I've typeset
  them here (at the above URL).

 9 Feb 2018

- <http://rosalind.info/problems/list-view/> - "Rosalind is a platform
  for learning bioinformatics and programming through problem
  solving."  <http://rosalind.info/problems/locations/> - " If you don't
  know anything about programming, you can start at the Python
  Village. For a collection of exercises to accompany Bioinformatics
  Algorithms book, go to the Textbook Track. Otherwise you can try to
  storm the Bioinformatics Stronghold right now." Also "Bioinformatics
  Armory: Ready-to-use software tools abound for bioinformatics
  analysis. ..." and "Algorithmic Heights: A collection of exercises in
  introductory algorithms to accompany "Algorithms", the popular
  textbook by Dasgupta, Papadimitriou, and Vazirani."

 7 Feb 2018

- <https://news.ycombinator.com/item?id=16324097> - "LMARV-1: A RISC-V
  processor you can see [video]" - link and discussion on
  <https://www.youtube.com/watch?v=yLs_NRwu1Y4> - "LMARV-1: A RISC-V
  processor you can see. Part 1: 32-bit registers. (41:42) ... The LMARV-1
  (Learn Me A Risc-V, version 1) is a RISC-V processor built out of
  MSI and LSI chips. You can point to pieces of the processor and see
  the data flow. It should be a nice way of demonstrating how RISC-V
  works and how simple it is to implement."

- <https://news.ycombinator.com/item?id=16324458> - comment in parent
  Python’s Weak Performance Matters, on why Python succeeded despite
  poor performance, many reasons, for example: "The language is easy,
  very attractive for non-CS people.  The language is consistent
  (everything is an object, or a pointer to an object rather, you can
  only pass by pointer, scope and namespace that make sense all the
  time, etc...) ..."

- <https://news.ycombinator.com/item?id=16322599> - thread in parent
  Python’s Weak Performance Matters.  "Where are the main blowouts in
  python performance? ... is it compilation, evaluation overhead, or
  memory management?"  Many detailed answers with links, for example:
  "tl;dr: Python's dynamic features add lots of overhead to every
  operation, and CPython's simple implementation means you pay the
  overhead even when you don't use the dynamic features. ... The dot
  operator (e.g. `foo.x`) hides a /very complicated/ resolution
  process that can be /very expensive/. ..." (more explanation and
  several other examples follow)

 4 Feb 2018

- <https://github.com/arogozhnikov/python3_with_pleasure> - "Migrating
  to Python 3 with pleasure, A short guide on features of Python 3 for
  data scientists" "hacky suppressing / redirection of printing output:

      _print = print # store the original print function
     def print(*args, **kargs):
        pass  # do something useful, e.g. store output to some file

  Below. ... a context manager that temporarily overrides behavior of
  print: ... not a recommended approach, but a small dirty hack that
  is now possible."  Also other interesting unobvious stuff, and links
  to other Python3 pages.

 2 Feb 2018

- <https://news.ycombinator.com/item?id=16294594> - "Plan 9 is an
  amazing, inspirational, and futuristic operating system from the
  past" Post in parent <https://news.ycombinator.com/item?id=16292162>
  on "Plan 9 public grid (9gridchan.org)"

- <https://news.ycombinator.com/item?id=16295885> "/proc came from plan9
  and BSDs are moving away from it, why is this the case?"  (Another
  post in thread linked above): "Exposing kernel bits via the
  filesystem makes less sense the more you think about it:
  ... Programs now have to deal with malicious applications capable of
  managing mountpoints giving fake results via the filesystem. I could
  link to /dev/random to /dev/zero ... It's definitely not a simple
  interface for the kernel to implement ...  (also) vulnerability to
  file descriptor exhaustion attacks. ..."

31 Jan 2018

- <https://cmcenroe.me/2018/01/30/fbclock.html> - "Programming the Linux
 Framebuffer ... to put a white pixel in the top-left corner of the
 screen ...  echo -en '\xFF\xFF\xFF\x00' > /dev/fb0 ... In order to
 put pixels wherever we want ... we’ll want to mmap the file instead
 ... int fb = open("/dev/fb0", O_RDWR); ... uint32_t buf = mmap(NULL,
 len, PROT_READ | PROT_WRITE, MAP_SHARED, fb, 0); ... Placing a pixel
 is now as simple as assigning buf[y * info.xres + x] an RGB value ..."

- <https://cmcenroe.me/2017/05/05/linux-console.html> - "Configuring the
  Linux Console ... I recently dug up my HP Chromebook 11 ...I used
  splat to install Arch Linux ARM ... I decided not to install X.Org
  and stick to the console. ... it can actually be configured in many
  of the same ways as graphical terminal emulators! ... (shows how)
  ... these are the applications I use on the console: jfbview, PDF
  viewer; fbv, image viewer; ..." (with links to their Arch packages).

- <https://cmcenroe.me/2015/09/27/ascii.html> - "ASCII to My Heart ...
  Values starting with 10 represent the capital letter at the position
  in the alphabet of the last 5 bits. For example, 1000011 is the
  character “C”. ..." (etc.)

30 Jan 2018

- <https://ask.metafilter.com/318420/Site-to-Read-Real-Code-Like-Python>
  Includes my first Ask Metafilter answer, after 10+ years lurking.

- <https://github.com/norvig/pytudes> - "Python programs to practice or
  demonstrate skills" - many IPython notebooks, cited by me in my
  answer above.

- <http://www.aosabook.org/en/index.html> - "500 Lines or Less" -
  another answer (not mine) to the same AskMe.

- <https://news.ycombinator.com/item?id=16267202> - comments on "Xi: an
  editor for the next 20 years [video] (recurse.com)"

- <https://lsub.org/who/nemo/9.intro.pdf> - "Introduction to Operating
  Systems Abstractions Using Plan 9 from Bell Labs by Francisco J
  Ballesteros - Draft 9/28/2007" 416 page book.

- <https://news.ycombinator.com/item?id=16254250> - comment on above -
  "... There's this emphasis on simple, sane ways of fulfilling tasks
  on plan9 that permeates the whole system. It's beautiful."

- <https://marc.info/?l=9fans>&m=111558822710356&w=2 - "From: Russ Cox
  Date: 2001-10-25 ... Why plan 9?"
  <https://news.ycombinator.com/item?id=11882797>


20 Jan 2018

- <http://mad4j.github.io/book-mdpc/> - Minimalist movie posters
  generated using Processing programming language

- <http://aiju.de/code/tiny> - The Tiny Unix Tools: the shortest
  implementations of common Unix tools.  For example, "ed:
  main(a){for(;;){read(0,&a,1);write(1,"?\n",2);}}" Oh, it's a joke.


18 Jan 2018

- <https://www.rand.org/pubs/classics.html> - Classic RAND papers including
  Paul Baran's Distributed Communications series

- <https://jsandler18.github.io/> - "Building an Operating System for
  the Raspberry Pi" and <https://news.ycombinator.com/item?id=16180975>
  with "I used this tooling: <https://github.com/ali1234/rpi-ramdisk> to
  build a tiny fine-tuned Raspbian for "embedded" Python 3 (a project
  I dub PiratePython). It uses multistrap/qemu ..."
  <https://github.com/pimoroni/PiratePython> "...aims to bring the
  simplicity of MicroPython to the Pi, but all the power of the
  full-blown Python..." (links to other minimal distros for RPi in
  these comments)

15 Jan 2018

- <http://tenex.opost.com/hbook.html> - "Origins and Development of
  TOPS-20 by Dan Murphy" especially sections on "User-oriented Design
  Philosophy" "Escape Recognition, Noise Words, Help" "The COMND
  Service".  Also pertinent:
  <http://www.math.utah.edu/~beebe/publications/1987/t20unix.pdf> "Unix
  for TOPS-20 Users", especially section 3 "Command Processors"
  compares Unix shells to TOPS-20 EXEC: "(in Unix) No in-line help is
  available from the shell, like it is with the Tops-20 EXEC. This is
  a serious flaw of essentially every other operating system but
  Tops-20, and forces a user who has partially typed a command line
  and then forgotten the name of a switch to reach for a printed
  manual, or abort the typein and go search for on-line
  documentation."  Recall Hank Levy (former DEC engr, UW CSE faculty)
  said (in 198x) that TOPS-20 had the best command line UI of any OS.

14 Jan 2018

- <https://news.ycombinator.com/item?id=13205419> - "What sort of things
  could/can VMS do that Unix couldn't?"

12 Jan 2018

- <https://retrocomputing.stackexchange.com/questions/5341/how-did-people-use-ed>
  Many memoirs of programming in the 1970s and earlier, with printing
  terminals and punched cards.

10 Jan 2018

- <https://news.ycombinator.com/item?id=16118155> links to
  <http://www.oreilly.com/openbook/utp/UnixTextProcessing.pdf> and says,
  "Whenever I read this book again, I am reminded of how much UNIX
  know-how is probably being lost to new generations that are steered
  away from learning the foundations that still make up their
  operating systems. ...  Be warned, if one demonstrates the effective
  use of such old programs to others who have committed themselves to
  todays large, complex software, the reactions may not be
  positive. They might be dismissive or insulting, they might accuse
  one of being a "luddite", or perhaps a "neckbeard" practicing some
  unexplained type of "elitism".  The uninitiated person who sees the
  results of UNIX text processing as nothing short of "magic" is rare
  indeed. It is that person who might enjoy this book."  This was in
  comments on <https://virtuallyfun.com/2018/01/10/life-in-unix-v7-an-attempt-at-a-simple-task/> 
  "(using) vi, staring at a blob of text with no syntax highlighting
  and with limited space, you start appreciating troff/nroff much
  more. ... LaTeX tends to have fairly verbose commands. ...
  ‘‘parsing’’ troff/nroff syntax is much easier ... on your tiny 80×24
  screen ... As for the (V7/x86) system as a whole, I was positively
  surprised how usable it was by today’s standards."

- <https://ask.metafilter.com/317751/A-few-questions-about-the-blockchain>
  Several clear explanations with links to more.

- <https://github.com/tonybaloney/mocker> - "A crappy imitation of
  Docker, written in 100% Python ... I'm giving a talk ... and fancied
  a simple implementation to show how container isolation works. ... I
  wrote this in 2 days, don't take it seriously" Comment at
  <https://news.ycombinator.com/item?id=16114724>: "This is great, and
  the code is particularly easy to follow and quite Pythonic. Nice!"

 8 Jan 2018

- <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4522609/> "Fifty
  psychological and psychiatric terms to avoid: a list of inaccurate,
  misleading, misused, ambiguous, and logically confused words and
  phrases" "a provisional list of 50 commonly used terms in
  psychology, psychiatry, and allied fields that should be avoided, or
  at most used sparingly and with explicit caveats. We provide
  corrective information for students, instructors, and researchers"

- <https://github.com/hchasestevens/hchasestevens.github.io/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb> 
  Comments <https://news.ycombinator.com/item?id=16084238>
  "This notebook should be named "how to abuse decorators"..." But worth
  looking at anyway.

 7 Jan 2018

- <http://xon.sh/> "the xonsh shell ...  Xonsh is a Python-powered,
  cross-platform, Unix-gazing shell language and command prompt. The
  language is a superset of Python 3.4+ with additional shell
  primitives that you are used to from Bash and IPython. ..."

- <http://www.dougengelbart.org/firsts/1968-demo-interactive.html> -
  Doug Englebart's famous "'Mother of all demos', a chapterized version"

- <https://www.raspberrypi.org/blog/why-raspberry-pi-isnt-vulnerable-to-spectre-or-meltdown/>
  Comment at <https://news.ycombinator.com/item?id=16080002> "This is a
  good overview of modern, superscalar, out-of-order, speculative CPUs
  that literally any programmer could easily understand. Recommended
  reading for every single engineer in the whole world" "Finally I
  understand how the leakage works: no actual reading of kernel memory
  is taking place. Instead, the read-ahead/speculative logic causes
  one of two addresses in user space to be read, and thus placed in
  the cache. So, by reading both of them, and checking the time it
  took, the exploit can indirectly determine one bit (0 or 1) of
  kernel memory. Scary!"

 6 Jan 2018

- <https://zwischenzugs.com/2018/01/06/ten-things-i-wish-id-known-about-bash/>
  comments <https://news.ycombinator.com/item?id=16084763> - "Bash
  has a huge number of little shortcuts that are difficult to learn."
  HN comment links to <http://mywiki.wooledge.org/BashFAQ>, 116 "How do I..?"
  questions.

- <http://yeokhengmeng.com/2018/01/make-the-486-great-again/> "Modern
  Linux in an ancient PC - What is the oldest x86 processor that is
  still supported by a modern Linux kernel in present time?" It's 486,
  "support for the 386 was dropped in Dec 2012."  They get Gentoo
  running on a 1993 IBM PS/1.  "AMD 5X86 486-clone running at 133mhz
  ... 64MB SDRAM" "It takes 11 minutes to boot up to the login prompt
  and 5.5 mins to shutdown."  "low-level detailed instructions" at
  <https://github.com/yeokm1/gentoo-on-486/>  Comments at
  <https://news.ycombinator.com/item?id=16085068> "Wow it's a lot slower
  now than it is with 1992 Linux."

 4 Jan 2018

- <https://github.com/jlevy/the-art-of-command-line> - "Master the
  command line, in one page" - but it's a very long page!  Much is
  potentially useful, not well known (by me).

- <https://medium.com/@amathstudent/learning-math-on-your-own-39fe90c3536b>
  "Learning math on your own. A guide, heartfelt and opinionated"
  Includes some unusual suggestions.

 3 Jan 2018

- <http://www.hellophia.com/> web page of comic/graphic artist Sophia
  Foster-Dimino - unusually good use of color and subtle animation, for
  example <http://www.hellophia.com/#/animation-personal/> Much more in
  comic strip format at <http://sophiafosterdimino.tumblr.com/> via
  comment in MeFi post below.

- <https://www.metafilter.com/171507/2017-was-full-of-great-comics-and-heres-where-to-find-them>,
  links to
  <https://www.theverge.com/2017/12/22/16807260/best-comics-of-2017> and
  several other best-of-2017 lists.

- <https://rcoh.me/posts/notes-on-cpython-list-internals/> - with links
  to CPython source and docs

25 Dec 2017

- <http://www.nyx.net/~ewilli/edtut.pdf> - A Tutorial Introduction to
  the UNIX Text Editor by Brian W. Kernighan - "Almost all text input
  on the UNIX operating system is done with the text-editor ed."

24 Dec 2017

- <https://bitbucket.org/infpi/inferno-rpi> - Inferno OS for Raspberry
  Pi - via <https://news.ycombinator.com/item?id=15993639>: "... many
  aren't aware of Inferno OS and always think Plan 9 was the end of
  the line, when that status actually belongs to Inferno OS.  Which
  implemented the original vision for Plan 9, regarding what Pike
  wanted to do with Alef."

23 Dec 2017

- <https://notamonadtutorial.com/harvey-an-operating-system-with-plan-9-s-shadow-3081414e5f0b>
  "Plan 9 implements true resource sharing as opposed to remote
  access. M. A. Padlipsky succintly defines the difference in his
  classic RFC 871 — A PERSPECTIVE ON THE ARPANET REFERENCE MODEL,
  which is a great read.  Most Unix ­derived systems today implement
  remote access, via tools like ssh, not resource sharing."  Also
  briefly comments on 9front, node9, 9base, Glendix and plan9port.
  via <https://news.ycombinator.com/item?id=15989697> which discusses
  <https://harvey-os.org/> HN comment
  <https://news.ycombinator.com/item?id=15990803> says "it's a Plan9
  fork refreshed for modern build chains plus golang support."

22 Dec 2017

- <https://www.metafilter.com/171362/All-I-want-for-Christmas-is-a-crapton-of-jazz>
  links to jazz Christmas music

20 Dec 2017

- <http://screenl.es/> - The Screenless Office is a system for working
  with media and networks without using a pixel-based display. It is
  an artistic operating system. ...  Currently, it exists as a working
  prototype with software "bureaus" which allow a user to read and
  navigate news, web sites and social media entirely with the use of
  various printers for output and a barcode scanner for input. ..."
  Comments vary from baffled to admiring:
  <https://news.ycombinator.com/item?id=15960056>

- <https://www.metafilter.com/171286/Well-you-neednt-listen-But-you-should>
  Links about Thelonious Monk, links to his music by himself and others.

- <https://www.metafilter.com/142742/Nica> - Links about Kathleen Annie
  Pannonica Rothschild, patroness of jazz, especially Monk.  Also
  links to Monk's music.

18 Dec 2017

- <https://news.ycombinator.com/item?id=15951288> - A plan to rescue the
  Web from the Internet - much discussion of problems and alternatives -
  didn't look at original article

17 Dec 2017

- http://www.inbflat.net/ <http://www.inbflat.net/faq.html>
  In Bb, a collaborative music and spoken word project,
  partly inspired by Terry Riley's In C.
  <https://news.ycombinator.com/item?id=15941838>

12 Dec 2017

- <http://warsus.github.io/lions-/> - A Commentary on the Sixth Edition
  Unix Operating System, by J. Lions. Classic book, in a nice HTML
  rendering.

 9 Dec 2017

- <https://soupi.github.io/rfc/reading_simple_haskell/>

 8 Dec 2017

- <https://news.ycombinator.com/item?id=15877908>, comments on The
  GNUnet System.  "Is anyone knowledgeable that can tell me the
  difference between IPFS, GNUnet, Zeronet, freenet or even something
  like i2p, tor and urbit .. as well as probably others."  Many answers.

 5 Dec 2017

- <https://staff.science.uva.nl/c.dominik/hpcalc/emacs/>
  Emacs for HP49G and hp49g+

 4 Dec 2017

- <https://dave.cheney.net/2017/12/04/what-have-we-learned-from-the-pdp-11>
  blog post reviews Gordon Bell's paper from 1976.

 3 Dec 2017

- <http://seveninchesofyourtime.com/cinemas-greatest-scene-casablanca-and-la-marseillaise/>
  with embedded video and animated GIFs from the film.

 2 Dec 2017

- <http://python.apichecklist.com/> - Checklist for Python library APIs
  also <https://news.ycombinator.com/item?id=15827945>

 1 Dec 2017

- <http://publications.computer.org/annals/2017/11/14/history-of-ibm-branch-offices-1920-1980/> - annals of the history of computing (just an example)
  <http://publications.computer.org/annals/2017/11/14/> - toc for that day
  <http://publications.computer.org/annals/> - home page 
  Blog about the contents of the journal, with summary articles that
  link to the journal articles.

- <http://mattwarren.org/2017/11/28/Exploring-the-BBC-microbit-Software-Stack/>
   MicroPython runtime (among others) on ARM mbed OS.  Links to:

- <https://github.com/carlosperate/awesome-microbit#programming>


15 Nov 2017

- <http://lcamtuf.coredump.cx/electronics/> - Concise electronics for geeks -
  20,000 words, comprehensive rather than concise.

- <https://loomcom.com/contraltojs/> - ContrAltoJS Xerox Alto Emulator
  "This is a port of the Living Computer Museum's ContrAlto project to
  JavaScript."

13 Nov 2017

- <http://nibrahim.net.in/2017/11/04/pycon_india_2017_keynote.html>
  Creating a presentation by hand using calligraphy

- <https://vimeo.com/89837165> - John Coltrane 'A Love Supreme' only
   live performance July 26, 1965 - only 14 minutes.  via
   <http://www.metafilter.com/170480/July-26-1965-A-Love-Supreme-Live>

- <https://github.com/everythingwillbetakenaway/DX7-Supercollider>
  Yamaha DX-7 clone. Programmed in Supercollider.  Comments in
  <https://news.ycombinator.com/item?id=15686350>, including link to
  <https://asb2m10.github.io/dexed/> "Dexed is a multi platform, multi
  format plugin synth that is closely modeled on the Yamaha DX7. Dexed
  is also a midi cartridge librarian/manager for the DX7.  Dexed
  requires a AU/VST host (like Savihost or Reaper) in order to run the
  plugin."

- <https://github.com/jeffmer/micropython-upyphone> - gsm phone using
  pyboard and sim800l. Comments in
  <https://news.ycombinator.com/item?id=15686316> "I thought it would be
  an actual GSM stack written in Micropython (like OsmocomBB etc.),
  but alas, it's only the UI" "only works with a 2G network
  ... T-Mobile is the only operator of such a thing in the US, and
  they're trying to phase it out"

 9 Nov 2017

- <https://www.atlasobscura.com/articles/how-a-retrofuturist-spends-three-days-in-los-angeles>
  That's just another good recent example of Atlas Obscura, which should
  really be in there.  See also 7 Mar above.

 7 Nov 2017

- <https://github.com/pmaupin/pdfrw> - pdfrw is a pure Python library
  that reads and writes PDFs - quite an opus, notable README on that page

 3 Nov 2017

- <http://sfpc.io/spring2018/> - School for Poetic Computation.  Also add
  links to recurse center and criticalengineering.org/courses (above, 21 Jul)


2 Nov 2017

- <https://www.theguardian.com/books/gallery/2017/nov/01/ernst-haeckel-the-art-of-evolution-in-pictures>
  Amazing 19th century biological illustrations.  via <http://www.metafilter.com/170327/Stop-Haeckel-time>, may have better links than Guardian

- <https://blog.lizzie.io/linux-containers-in-500-loc.html> - Literate program 
  with lots of explanation - also HN comments at item?id=15608435.

- <https://github.com/kragniz/omochabako> - Toy container runtime in Python
  (via HN comments above)


30 Oct 2017

- <https://archive.org/stream/9780262610261#page/n0/mode/2up> - A
  FORTRAN Coloring Book - other links to download pdf or ebook formats
  incl. kindle don't work

- <https://mathoverflow.net/questions/43690/whats-a-mathematician-to-do/44213#44213> - Bill Thurston's essay in response to "What's a mathematician to
  do?". He writes, "It's not mathematics that you need to contribute
  to. It's deeper than that: how might you contribute to humanity, and
  even deeper, to the well-being of the world, by pursuing
  mathematics?" ...  "The product of mathematics is clarity and
  understanding ... The world does not suffer from an oversupply of
  clarity and understanding ..."  Other answers in the MO post are
  also very pertinent.


28 Oct 2017

- <https://news.ycombinator.com/item?id=15565872> - about lively.next -
  "... program similarly to Smalltalk and Self, i.e. instead of a
  edit-compile-run cycle you have an ever running "program" and change
  various parts of it directly ... "
  (Later, 30 Oct) another response in this thread on Smalltalk
  "inner platform" - most ST systems create a whole OS including
   graphics, window manager, scheduler ...  difficult to
   separate out an application - 'what if you had to run every
   Java application inside Eclipse' (paraphrase).


24 Oct 2017

- <https://wiki.debian.org/DontBreakDebian> ...

23 Oct 2017

- <https://technicshistory.wordpress.com/2017/23/the-electronic-computers-part3-eniac>
  and other pages in this series - very nicely designed, nice photos.
  This page cites the book ENIAC in Action, which has its own page
  eniacinaction.com

21 Oct 2017

- <http://xeroxalto.computerhistory.org/xerox_alto_file_system_archive.html> - 
  best page on Alto, links to all the reports papers and code including
  microcode.

19 Oct 2017

- therealmntmn.tumbler.com/.../interim-os... - via /archive
   Photos of interim-os - also confirm we have current link to
   interim-os.com.  He has bare bones OS running on RPi 2.
   Source code might be interesting.  On interim-os.com
   he writes "Un(der)documented VideoCore IV "QPU" has boot control ...
   ARM CPU is a peripheral device"

- <https://wiki.debian.org/RaspberryPi> - compares Debian to Raspbian,
   explains disadvantages of RPi "the board design is closed and
   the main processor is not available for purchase by the public"

 7 Oct 2017

- <https://simonwillison.net/2017/Oct/5/django-postgresql-faceted-search/>
   Simon Willison's blog is back!  Looks like it's been there all along -
   how did we lose it several years ago?

   9 Oct - I looked through it = not as good as before - in recent
   years through 2016, and all posts are in the form of a single
   (often banal) question with a (short) answer.  It appears that
   these are mostly Stackoverflow or Quora questions.  Also, more
   about Javascript now than Python.

   10 Oct - Simon Willison's better old-style posts that I remenber
   end June 2010, with "getting married".  After that only Q&A posts.
   Oct 2010 has 65 questions!

 3 Oct 2017

- <https://www.newyorker.com/magazine/2013/01/14/structure> - Structure,
  by John McPhee, on his use of the KEdit editor.

 2 Oct 2017

- metamodular.com/lispos.pdf - LispOs ... by Robert Strandh dated 2013.
  new (working) URL for paper linked in precursors.md.  Any new content?
  Oh, we do have LispOs in precursors.md now.

- <https://news.ycombinator.com/item?id=15379418> - "Ask HN: Where do I
  go to get started on ASIC, FPGA, RTL, Verilog et. al?" - lots of
  informed responses

30 Sep 2017

- <http://www.inwap.com/pdp10/hbaker/hakmem/hakmem.html> - more recent but
  similar URL to the ones we have.

- <http://hakmem.org/> - nicely formatted single page version

27 Sep 2017

- <http://thin.npr.org/> - Text-only NPR.  HN thread shows lots of variations
  using minimal CSS etc.  Put that in typography section.

25 Sep 2017

-  <https://technicshistory.wordpress.com/2017/09/20/the-electronic-computers-part-2-colossus/> - 
  Informative, nice page design.  via
  <https://news.ycombinator.com/item?id=15297861> - John Nagle (Animat)
  comments on Colossus, also reviews 1930s 40s 50s special-purpose or
  non-stored-program calculating/computing machines.

19 Sep 2017

- <http://jsomers.net/blog/docwriter> - "DocWriter: the typewriter that
  sends its keystrokes in real time to a Google Doc" - it's a
  hacked-up Brother portable with an RPi inside!

- <https://github.com/k0kubun/llrb> - "LLVM-based JIT Compiler for Ruby"

- <https://breakerofthings.tech/2017/09/17/how-to-show-text-on-the-screen.html>
  Renders *Hindi* text on the screen!

- <http://zipcpu.com/> - Blog on FPGAs

- <https://gmplib.org/~tege/qemu.html> - "System emulation using QEMU"
  How-to for emulating lots of different architectures on several host OS

- <https://ux.stackexchange.com/questions/101990/why-are-terminal-consoles-still-used>
  Lots of replies on advantages of text/terminals/command line over GUI


16 Sep 2017

- <https://news.ycombinator.com/item?id=15265462> - HN comments on Alan
  Kay thread explaining his vision of a computer system where
  everything can be programmed by the user - a real guitar (Kay's
  Dynabook) vs Guitar Hero (iPad).


15 Sep 2017

- <https://ux.stackexchange.com/questions/101990/why-are-terminal-consoles-still-used>
  see 19 Sep below


14 Sep 2017

- <https://textonly.website/index.html> - "A text-only list of text-only
  websites".  BUT they are in "beautiful, unadorned HTML" not ASCII.
  But, no "fonts, images, stylesheets, images & javascript".
  This is not the large old text only website with lots of retro stuff
  we've seen before.

- <https://spin.atomicobject.com/2017/09/14/.....>  on mid-century
  industrial designer Raymond Loewy.  Links to www.theverge.com
   "the man who designed everything" and www.raymondleowy.com

13 Sep 2017

- <https://softwarefoundations.cis.upenn.edu/current/lf-current/Basics.html>
  etc.  - Coq theorem prover applied to programming language theory,
  with lots of basic tutorial for Coq.  See also GeoCoq (below) for
  geometry proofs, and Freek Wiedijk's Provers of the World (below).

12 Sep 2017

- aschmann.net/AmEng/#SmallMap - awesomely detailed map of US and
   Canadian dialects with tons of explanation and zillions of links to
   youtube with speech samples.

- <https://www.cl.cam.ac.uk/~lp15/MLbook/pub-details.html> - ML for the
  Working Programmer, 2nd Edition - free download!
  (each chapter is a separate .pdf file, links at the bottom of this page)


11 Sep 2017

- <https://www.nostarch.com/xboxfree> - Free download of Bunnie Huang's
  Hacking the Xbox in memory of Aaron Swartz.

- <https://www.edukera.com> - "Teach mathematics with a proof assistant"
  uses Coq in three areas: calculus, logic, sets.


10 Sep 2017

- <https://news.ycombinator.com/item?id=15206540> - HN comments on New Scientist 
  story on incomprehesible proof of ABC conjecture.  Lots of informed comment
  and links on automated theorem proving, proof checking.

- <http://www.cs.ru.nl/~freek/comparison/comparison.pdf> - The Seventeen Provers
  of the World - 169 p pdf linked from above HN thread.

- <https://github.com/yogthos/cheatsheets/blob/master/mastodon.social.md>
  How to set up Mastodon, linked from this advocate's post:
  <https://news.ycombinator.com/item?id=15212373.>   Also
  <https://joinmastodon.org/> is recommended in same HN thread,
  <https://news.ycombinator.com/item?id=15211074>

- <http://www.sunrise-ev.com/6502.htm> - The 6502 40th Anniversary Computer Badge -
  minimal 6502 6-chip SBC + LED character display (to show your name or ...)
  the size of a badge/name tag.

- <http://imgur.com/a/8plOW> - Restoring a Soviet-era analog music
 synthesizer - lots of photos - linked from
 <https://news.ycombinator.com/item?id=15207478> - more links about the
 synthesizer, some of its music.

 6 Sep 2017

- <https://web.stanford.edu/class/e145/2007_fall/materials/noyce.html> -
  'The Tinkerings of Robert Noyce' by Tom Wolfe in Esquire magazine,
  Dec 1983

 5 Sep 2017

- <https://danluu.com/risc-definition/> - What's the definition of RISC? - John Mashey's Usenet posts.  Also at
  <http://userpages.umbc.edu/~vijay/mashey.on.risc.html> but danluu
  version has nicer formatting (HTML not ascii) and more material,
  additional posts on CDC6600 and VLIW.

31 Aug 2017

- <https://news.ycombinator.com/item?id=15120984> comments on Optimizing
  latency of an Arduino MIDI controller - links to other embedded
  musical instrument pages, especially Bela <http://bela.io>
  <https://github.com/BelaPlatform/Bela>
  Bela is from <http://instrumentslab.org/publications/>

- <https://github.com/rswier/swieros> - A tiny hand crafted CPU
  emulator, C compiler, and Operating System ... Unix-ish kernel (based
  on xv6) ... for fun, education, and research.


30 Aug 2017

- <https://github.com/python> - Repositories related to the Python
  Programming language

- <https://github.com/python/cpython> - cpython and standard library

- <https://github.com/python/cpython/tree/master/Lib> - standard library
  for example <https://github.com/python/cpython/blob/master/Lib/datetime.py>
  (one module) or .../Lib/asyncio (package with many modules)

- <https://github.com/python/peps/blob/master/pep-0008.txt> pep-0257.txt etc.

- <https://devguide.python.org/> - Python Developer's Guide

- <https://github.com/python/peps>

- <https://www.python.org/dev/peps/pep-0008/> - PEP 8 -- Style Guide for Python Code

- <https://www.python.org/dev/peps/pep-0257/> - PEP 257 -- Docstring Conventions


26 Aug 2017

- 1988 paper Design Philosophy of the DARPA Internet Protocols

25 Aug 2017

- <http://thinkingeek.com/arm-assembler-raspberry-pi/> - 

- <http://zipcpu.com/blog/2017/08/21/rules-for-newbies.html> - Rules for
  new FPGA designers - comments in <https://news.ycombinator.com/item?id=15089678>

- <http://www.jstor.org/stable/10.4169/mathhorizons.23.4.18> - Network
   of Thrones Andrew Beveridge and Jie Shan in Math Horizons

- <http://n-gate.com/> - unfunny but voluminous, very repetitous snark
   about HN and FOSDEM.

24 Aug 2017

- <https://news.ycombinator.com/item?id=15089476> - Ask HN: What is your
  all time favorite CS paper? - many suggestions to classics and
  others, with links

14 Aug 2017

- www.mathcounterexamples.net - a collection of mathematical curiosities.

11 Aug 2017

- <https://www.youtube.com/watch?v=qqM3McG4-LE> Saul Bass: Famous title
   sequences from Preminger to Scorsese, 23 movies > 1 hour, via
   <http://www.metafilter.com/168771/I-want-to-make-beautiful-things-even-if-nobody-cares>

7 Aug 2017

- <https://github.com/jamesob/tinychain> - A pocket-sized implementation
  of Bitcoin - README explains bitcoin - < 1200 lines of Python

- https:geocoq.github.io/GeoCoq/ also <https://github.com/GeoCoq/GeoCoq> - A
  formalization of the foundations of geometry in Coq based on
  Tarski's axiom system.  First link has links to several related papers,
  explains relation of Tarksi to Hilbert and also Beeson.


4 Aug 2017

- <https://github.come/chrisdone/wish> - trivial web browser written in
  Haskell, one file, < 600 lines. "straight-forward ... given the
  libraries available today" including "sdl2 for creating a window,
  rendering context, and mouse events, sdl2-cairo and cairo for rendering
  text onto the SDL surface."

- <http://hrothen.github.io/posts/lets-build-a-browser-engine-in-haskell.html>
  (coincidentally with above, but a different project)

2 Aug 2017

- <http://herpolhode.com/rob/ugly.pdf> - slides from Rob Pike's 2001
  talk, especially slide 6 'What makes Unix *Unix*' that lists nine
  features including  hierarchical file system, separable shell, pipes,
  regular expressions,...  was surprised to see regexp in that list - but
  what makes the list different from, say, Windows?

  Also this: "What makes the system good at what it’s good at is also
  what makes it bad at what it’s bad at. Its strengths are also its
  weaknesses. A simple example: flat text files. Amazing expressive
  power, huge convenience, but serious problems in pushing past a
  prototype level of performance or packaging. ..."

 1 Aug 2017

- <https://eater.net/8bit/> - Build an 8-bit computer from scratch -
   74LS logic w/28C16 EEPROM on several solderless breadboards - also
   <https://news.ycombinator.com/item?id=14450945> links to similar
   projects

- <https://joinmastodon.org/> - "Mastodon is the world’s largest free,
  open-source, decentralized microblogging network."

- <http://charlesleifer.com/blog/using-sqlite-full-text-search-with-python/>


30 Jul 2017

- <http://www.softwarepreservation.org/projects/LISP/MIT/AIM-001.pdf>
An Algebraic Language for the Manipulation of Symbolic Expressions (1958)
 by John McCarthy, very early report on Lisp.

- <https://github.com/publicus/emacs-org-mode-for-the-laity> - "causes
  Emacs to behave more like a "normal" text editor (with familiar
  keybindings ... such as C-c for copy, C-v for
  paste, C-z for undo ..."


29 Jul 2017

- <https://kelu124.gitbooks.io/echomods/content/RPI.html> - Building a
  Raspberry Pi based ultrasound imaging development platform - lots
  of details and links, including one to a journal article.

- <https://cstheory.stackexchange.com/questions/1168/what-papers-should-everyone-read> - Good selection, with links.

- <https://github.com/banga/prefactor> - prefactor - This is a tool that
  for writing AST-based refactorings for large Python codebases. It
  uses lib2to3 to convert source code to an AST, run a visitor over it
  that modifies the tree, and convert the tree back into source code.
  This comes with a Flask app that makes it really easy to write
  visitors. To use it, just start the app and open it in a browser:
  (cool figure).  Why lib2to3 - The AST returned by Python's ast module
  is lossy — it strips out information necessary for recreating the
  source code with the correct whitespace and comments. The AST
  returned by lib2to3 is more low-level, so it retains all of the
  information required to regenerate the source code faithfully.

- <https://en.wikipedia.org/wiki/Timeline_of_computing_1950%E2%80%9379>
   Actually a table, lots of interesting items from the
   mainframe-mini-micro era, but many omissions -- no Xerox Alto !?


26 Jul 2017

- <https://musikcube.com/> Musikcube, a terminal-based music player,
  library, and streaming server.  <https://news.ycombinator.com/item?id=14853212>
  mentions alternatives.

24 Jul 2017

- <http://www.howardism.org/> lots of emacs stuff including
  <http://www.howardism.org/Technical/Emacs/new-window-manager.html> - See
  also
  <https://www.informatimago.com/linux/emacs-on-user-mode-linux.html>

23 Jul 2017

- <http://www.verizoninternet.com/bookmark/how-wifi-works/>
  note bibliography with links near bottom

21 Jul 2017

- <https://criticalengineering.org/courses/othernet/> also /cli/ /networkshop/
  (links.html Jul 21 2017)

- www.dunneandraby.co.uk/content/bydandr/13/0  Dunne & Raby Critical Design FAQ
  also /content/projects

19 Jul 2017

- <http://www.wilfred.me.uk/blog/2017/04/30/remacs-talk-transcript/>
  "Emacs is really just a lisp interpreter called temacs. The Emacs
  functionality that we know and love is really the standard library
  that ships with temacs. ... Being Emacsy is about providing an
  incredible mutable programming environment ..."

- <http://ask.metafilter.com/311380/Other-jazz-standards-like-these-jazz-standards>
  many heartfelt recommendations for an aspiring pianist, with links
  to youtube for many many standards
  (links.html 21 Jul 2017)

18 Jul 2017

- www.aroundh.org/journey/ - Around Digital Humanities in 80 days - links
  to 80 DH sites hosted/about around the world.

- math.stanford.edu/~ebwarner/SplashTalk.pdf - The Foundational Crisis
  of Mathematics - 18p. paper

- <http://www.ps.uni-saarland.de/~hornung/bachelor.php> - 
  Constructing Number Systems in Coq - follows development in Landau's
  Grundlagen der Analysis - links to 68 p. thesis, talks, and Coq code.
  (in math, in theorem provers, in links.html 21 Jul 2017)

17 Jul 2017

- www.informatica.co.cr/unix-source-code/research/1991/0101.html - Porting
  Unix to the 386 - classic paper on 386BSD design, 1991 - via Trivium blog

11 Jul 2017

- <https://brendanzagaeski.appspot.com/0004.html> - Minimal PDF,
   explains PDF file contents: " PDF is a binary format, but it
   contains mostly plain text ...  PDF is a human-readable document
   description language.
   <https://brendanzagaeski.appspot.com/0005.html> - hand coded PDF tutorial
    this appears to be more basic than 0004.html
   <https://news.ycombinator.com/item?id=14727662> - HN discussion has
   more links to 'hand-made PDFs' etc.

- <http://cppdepend.com/blog/?p=214> "exploring the SQLite codebase"
   <https://news.ycombinator.com/item?id=14729239>

- <https://tylercipriani.com/blog/2017/07/09/the-rsync-algorithm-in-python/>

- <https://github.com/DutchGraa/crackcoin> - Very basic blockchain-free
  cryptocurrency PoC in Python, github README also has explanation -
  <https://eprint.iacr.org/2016/871.pdf> academic paper explaining it:
  "A Framework for Truly Decentralised Fast Transactions"
  <https://news.ycombinator.com/item?id=14730354> - more explanation,
  refs: "basically a blockchain, but with transactions instead of blocks..."


 5 Jul 2017

- <http://www.springer.com/gp/marketing/turing-award-50-years?utm_campaign=CON32079_4>&utm_medium=newsletter&utm_source=email&wt_mc=email.newsletter.8.CON32079.internal_4  
  Papers by Turing award winners to download (not their Turing award speeches/papers, though)

- www.saminiir.com - "Let's code a TCP/IP stack" series, also
  <https://github.com/saminiir/level-ip> "A hacker's userspace TCP/IP
  stack" uses Linux TUN/TAP device to intercept low-level network
  traffic from the Linux kernel.  Blog pages and github README include
  links to references.


 4 Jul 2017

- IEEE chip hall of fame pages for example
  <http://spectrum.ieee.org/semiconductors/devices/chip-hall-of-fame-fairchild-semiconductor-a741-opam>, chip-hall-of-fame-atmel-atmega8 etc.
  Update 6 Jul - toc page is at spectrum.ieee.org/static/chip-hall-of-fame

- A very simple Lisp interpreter in 250 lines of literate
  Python.  <http://khamidou.com/compilers/lisp.py/>
  Interesting text and code side-by-side page design.
  Oh, but it contains what looks like novice Python code:
   for i in range(len(a)):...a[i]...   etc.

- <http://cpsc.yale.edu/sites/default/files/files/tr87.pdf>
  APL idioms by Perlis and Rugaber, 1977, 50 pages!


29 Jun 2017

-  <https://www.maths.cam.ac.uk/sites/www.maths.cam.ac.uk/files/pre2014/undergrad/admissions/readinglist.pdf>
  Recommended readings for high-school students about to start college math.
  The ones I recognize are good, maybe some others are worth a look too.

28 Jun 2017

- ecee.colorado.edu/ecen4553/fall09/notes.pdf - 'compilation: from
  Python to x86 assembly' 80 pages - see also course notes at .../fall09/

- homepage.sns.it/lolli/articoli/Lolli.pdf 'Why mathemeticians do not love
  logic'

- <https://www.loc.gov/collections/webcomics-web-archive/about-this-collection/>
  for example <http://www.octopuspie.com/2007-05-14/001-pea-wiggle/> via
  <http://www.metafilter.com/167893/Its-all-been-eaten-you-cant-have-any-more>
  Web comics (links.html 21 Jul 2017)

- <https://web.stanford.edu/class/e145/2007_fall/materials/noyce.html> -
  Tom Wolfe's 1983 Esquire article about Rob Noyce and Silicon Valley
  Put next to Stuart Brand and Jaron Lanier's memoirs

- <https://www.yourworldoftext.com/home/> - "an infinite grid of text
  editable by any visitor. " see also /Help/ and sample screenshot


27 Jun 2017

- benhoyt.com/writings/pyast64/ - "Compiling Python syntax to x86-64
  assembly...".  Very small Python subset, just function calls, for loops,
  artithmetic expressions.  Uses Python's built-in AST module to do
  much of the work.  Achieves speed 30x Python, similar to C compiled
  with gcc with no optimizations.  Also the HN comments link to
  several other compile-from-python systems.

- <https://github.com/shaunlebron/history-of-lisp-editing> on early 
  structure editors - link in editors section.

- www.lighterra.com/papers/modernmicroprocessors/ 'a 90-minute guide' to
  modern unobvious microprocessor implementation - pipelines, caches,
  threading, out-of-order execution etc.

17 Jun 2017

- <http://www.dear-data.com/theproject/> — Dear Data - saw
  the book at SPL ballard

14 Jun 2017

- HN post today on 16 linux commands that show you about hardware -
   in great faiths/linux - there also add jvns post about bash.

- CS Canon paper posted on HN, HN discussion with links to many of
  the cited books/papers


13 Jun 2017

- <https://pdos.csail.mit.edu/6.828/2012/schedule.html> - course that
  goes with xv6 OS - 2012 has terse lecture notes in .txt files!  The
  ones on virtualization and exokernels are really good.  also 2014
  and 2016 but their notes are in .md files that don't just display in
  browser, boo hiss!  Also, .txt notes on Multics, Plan 9, and
  exokernels etc. from Stanford OS course
  <http://www.scs.stanford.edu/05au-cs240c/notes/>

12 Jun 2017

- <http://www.recommendmeabook.com/> - shows first page from randomly
   selected book, without revealing title/author.  Alternatively,
   select a particular book by clicking on its cover.  Lots of
   classics included. (in classics in literature in links.html, 21 Jul
   2017)

 9 Jun 2017

- plan 9 class notes from cat-v.  Also a few comments from latest HN
  Plan 9 thread.

 8 Jun 2017

- Computer History Museum (CHM) timeline with links to other pages?
   For some reason I didn't like this as much as I hoped to.

 6 Jun 2017

- <https://himmele.blogspot.com/2017/06/fred-brooks-software-design.html>
  highlights from Brooks' Design of Design book.

 5 Jun 2017

- <http://pinksquirrellabs.com/blog/2017/05/30/asi64/> - 6502 assembler
  embedded in Racket, and another in Haskell:
  <http://wall.org/~lewis/2013/10/15/asm-monad.html>

- <https://people.cs.clemson.edu/~mark/uprog.html> - A brief history of
  microprogramming - also a good explanation.

 3 Jun 2017

- https://musicbrainz.org/ and <https://news.ycombinator.com/item?id=14478515>

- <http://cs.brown.edu/~sk/Publications/Papers/Published/pmmwplck-python-full-monty/>
  Python semantics expressed in Racket, makes an interpreter that
  passes some CPython tests.

26 May 2017

- <https://labs.rs/en/> - research on privacy, Facebook, security also
   notable graphic design <http://www.bbc.com/news/business-39947942> -
   BBC news story about this research

- <https://smashingboxes.com/blog/building-programmable-synth-20/>
  a few components on a solderless breadboard.  Uses $11 Nucleo-L432KC
  computer chip, a volume pot, and a transistor to drive a little speaker.

25 May 2017

- <https://mathwithbaddrawings.com/2017/05/17/the-joy-of-slightly-fishy-proofs/>
  and maybe others in this series.


24 May 2017

- maybe add Mesa/Pilot/Tajo/XDE on Xerox D-Machines to prescursors.md.
   Oberon-like but much bigger and more complicated.

- <https://news.ycombinator.com/item?id=14403036> - Helping a Million
  Developers Exit Vim - "I met my wife because she was stuck in
  vi. ..."


23 May 2017

- <https://news.ycombinator.com/item?id=14388127> - "you could build a
   Facebook, Instagram, or Twitter clone on top of email pretty
   easily. All it would take is a slightly reimagined client. Just
   whitelist addresses of people you "follow" and display their emails
   in a separate, more visually rich feed"

- <https://news.ycombinator.com/item?id=14401057> - Good examples of
  interactive command-line user experience - many many links


21 May 2017

- <https://news.ycombinator.com/item?id=14382752> - on old W3C Amaya web
  browser "from a time when the grand vision of the Web was to be much
  more participatory and collaborative".

- <http://callingbullshit.org/syllabus.html> - about the UW course


15 May 2017

- spinroot.com/gerard - history section Gerard Holzmanm's notes on
   history of Bell Labs: link to map of 5th floor with Thompson
   Ritchie et al offices, link to subsequent career paths of Bell Lab
   alumns.  In Unix history.

- <https://technicshistory.wordpress.com> - history of tech blog, 
  especially recent pages on telephone switching 2017/04/09/only-connect
  and relay computers 2017/05/10/lost-generation-the-relay-computers

14 May 2017

- <https://thepointmag.com/> for example
  <https://thepointmag.com/2014/criticism/norman-rush>
  <https://thepointmag.com/2015/examined-life/complications-of-philosophy>

11 May 2017

- <http://eli.thegreenplace.net/2017/adventures-in-jit-compilation-part-4-in-python/> , uses PeachPy (below) also mentions llvmlite

- <https://github.com/Maratyszcza/PeachPy> - "x86-64 assembler embedded
  in Python" - linked conference paper is not very helpful

- <https://github.com/asrp/pymetaterp> - "A python parser that builds
  python ASTs in 502 lines of python without using modules ... Its
  (also) just another parsing expression grammar (PEG) based parser
  ..." (looking at README this looks very preliminary/half-baked)

- <https://codewords.recurse.com/issues/seven/dragon-taming-with-tailbiter-a-bytecode-compiler>
  and <https://github.com/darius/tailbiter> - "just enough Python to
  Python in Python ... A compiler from a subset of Python 3.4
  (starting with abstract syntax trees in Python's ast form) to
  CPython 3.4 bytecode. The compiler is coded in that same Python
  subset; it can compile itself. ... This is a continuation of
  <https://github.com/darius/500lines/tree/master/bytecode-compiler>"
 (also noted Apr 27 below)

- <http://www.metafilter.com/166863/Piano-violin-and-cello> - many links
   to YouTube, also a YouTube playlist.

 8 May 2017

- <https://github.com/iogf/vy> - "A vim-like in python made from
  scratch." - tightly coupled to Tk.  also comments in
  <https://news.ycombinator.com/item?id=14283942> link to
  <https://github.com/RealHacker/python-vi> - uses curses.

- <http://www.openculture.com/2015/10/william-faulkner-draws-mythological-maps-of-yoknapatawpha.htmln> - Faulkner's maps of Yok. county.


4 May 2017

- <https://github.com/MichielDerhaeg/build-linux>
  <https://news.ycombinator.com/item?id=14264189>, comments have any
  comparisons to <http://linuxfromscratch.org/> and
  <http://landley.net/aboriginal/about.html> - "LFS
  teaches you about the whole GNU Userland, getting a kernel up and
  running with busybox is much easier. This project does just that -
  teaching you the bare minimum."

- <http://www.johngustafson.net/pubs/pub57/ABCPaper.htm>, Reconstruction
  of the Atanasoff-Berry Computer


27 Apr 2017

- <http://benhoyt.com/writings/pygit/> - "pygit: Just enough git to
  create a repo, commit, and push itself to GitHub ... Notice the
  theme of using Python’s standard library for everything we can (os
  and hashlib)."

- <https://github.com/darius/tailbiter> - " just enough Python to Python
  in Python ... A compiler from a subset of Python 3.4 to CPython 3.4
  bytecode. The compiler is coded in that same Python subset; it can
  compile itself.  It can optionally run on top of a port of byterun
  to Python 3.4."

20 Apr 2017

- <https://www.huyng.com/posts/python-performance-analysis>

- <https://pypi.python.org/pypi/pudb> - example of windowed text ui

- <http://www.labri.fr/perso/nrougier/from-python-to-numpy/> - online book!

- <https://news.ycombinator.com/item?id=14158269> - comment thread started
   by python beginner with bad impression of numpy etc.

- Calulus Made Easy by Sylvanus Thompson (1914)
  <http://djm.cc/library/Calculus_Made_Easy_Thompson.pdf> - scanned old book pages
  <http://www.gutenberg.org/files/33283/33283-pdf.pdf> - recreated in LaTeX
  <https://github.com/nadvornix/calculus-made-easy/blob/master/33283-pdf.pdf>
    same thing at github
 <https://news.ycombinator.com/item?id=14161876> - testimonials

- <http://www.amightygirl.com/blog?p=14570> - women in science posters -
  other posters (not these) are scattered in unusual media subsection
  in graphics in links.html.

- <http://www.signsforscience.com/sign/carol-gunn-gunn-graphics> -
  science march posters

- <http://www.harkavagrant.com/archivecat.php> - comics is
   now a separate subsection in arts in links.html

18 Apr 2017

- <https://news.ycombinator.com/item?id=13645963> HN comment thread on how
   stability, transparency, convenience in sw products has eroded.

16 Apr 2017

- <https://www.nytimes.com/2017/04/14/technology/robert-taylor-innovator-who-shaped-modern-computing-dies-at-85.html?_r=0> 
  Robert Taylor obit, also links to Alan Kay comment at HN etc.
  (in fallen heroes, links.html, 14 Apr 2017)
  See also "what made xerox parc special"

- <https://github.com/psenough/teach_yourself_demoscene_in_14_days>

- <https://github.com/jed/140bytes/wiki/Byte-saving-techniques>

- Linus Akeson's 256 byte video+music demo for C64/6502
  (linked in both HN and MeFi)

13 Apr 2017

- JC Google+ digital humanities page

11 Apr 2017

- <https://blog.acolyer.org/2017/03/page/3/> - Mar 2017 archive to "The Morning
  Paper" about a CS paper every weekday.  Links to archives for other months.

- SO post what-part-of-milner-hindley-do-you-not-understand

10 Apr 2017

- <https://bookillustrations.quora.com/> via Mefi post, for example
   <https://bookillustrations.quora.com/Boris-Artzybasheffs-Illustrations-for-Creatures>

 8 Apr 2017

- <http://ask.metafilter.com/307705/Tutorials-Algorithms-Software-for-Federated-Services#4452469>
  Explanation of NNTP on AskMe, in response to question about Mastodon
 'federated' (distributed) Twitter-like social network.  See also
  <https://robek.world/featured/what-is-gnu-social-and-is-mastodon-social-a-twitter-clone/>
  <https://motherboard.vice.com/en_us/article/mastodon-is-like-twitter-without-nazis-so-why-are-we-not-using-it>
  <https://github.com/tootsuite/mastodon>
  <https://github.com/tootsuite/mastodon/blob/master/docs/>
  <https://instances.mastodon.xyz/>
  <https://news.ycombinator.com/item?id=14050718> (comment on GNU Social/Mastodon
   in another thread)

 6 Apr 2017

- <https://news.ycombinator.com/item?id=11803165> - Alan Kay and many contributors
   on books, reading etc. etc.

- Oscilloscope pong linked in HN from www.eevblog.com.  Amazing all
  discrete circuit, with zillions of transistors free hanging in air
  above a ground plane, hand-drawn circuit diagrams.

- Alan Kay's answer to What made Xerox PARC so special? on quora.com,
  linked to HN.

 3 Apr 2017

- bit-player.org/publications-by-brian-hayes - links to Brian Hayes'
   stories in American Scientist, both HTML and pdf.  Treasure trove!

- <https://archive.org/details/jot_0.53_ted_nelson>,
  <http://xanadu.com/jotinstructions.txt> - Ted Nelson's Jot editor (1970-1, 1986)

- <http://viewsourcecode.org/snaptoken/kilo/> - build your own text
   editor tutorial, uses antirez' kilo (github) see also openemacs (github).
  <https://news.ycombinator.com/item?id=14046446> - big HN comment thread
   159 comments with lots more links to homemade editors, way too many to
   link individually, many emacs-like.

 2 Apr 2017

- <https://news.ycombinator.com/item?id=14012973> - Python testimonials

 1 Apr 2017

- <https://www.reddit.com/r/Python/comments/62q2sm/python_helped_me_write_again/>
   programmer with MS used Python to program voice recognition + pen plotter
    to write in his own handwriting!  Amazing! (in python/examples and typography, links.html, 18 Apr 2017)

31 Mar 2017

- <https://i.redd.it/uaab4tb56soy.png>
  3x3 alphanumeric font, surprisingly legible. (in typography, links.html, 23 Mar 2017)

- HN comment ...id=13965793 about a test suite for
  <https://hackage.haskell.org/package/acid-state>: "turn arbitrary,
  serializable Haskell data structures into a sort of in-memory
  database that is persisted to disk by writing a log of the transactions
  applied to it."  "Use regular Haskell data structures as your database
  and get stronger ACID guarantees than most RDBMS offer."
  Maybe add to other.md?

- jvns.ca/blog/2017/03/26/bash-quirks - nice brief summary of the
  basics.  Just text, no cartoons this time.
  (links.html, 21 Jul 2017)

- github.com/jgrassler/papercut  - NNTP server in pure Python

- brendaningram.com how-to-create-distraction-free-writing-environment-on-linux
 Actually, how to make a bootable linux on a USB stick.
 He doesn't explain how to boot directly into vim session.
 Right, you start vim from bash.  He also has a quickie vim tutorial
 in another article.

- <https://glitch.com> - via Metafilter - site for live-coding/deploying your own 
  Javascript/node.js web site right in the browser.  "Hypercard for the web"
  see also .../about .../~html-starter
  <https://medium.com/glitch/welcome-to-glitch-fe161d0fc39b>

- <https://www.behance.net/gallery/50164479/WHOS-AFRAID-OF-RED-YELLOW-AND-BLUE>
  Striking photos of big buildings etc in The Hague decked out like
  Mondrian paintings for the 100th anniversary of the De Stijl
  movement.  In unusual media.
  18 Apr 2107

26 Mar 2017

- <https://github.com/riolet/pol> - Python one-liners: Awk-like
  one-liners for python - pol stores stdin in the variable _
  (underscore) in the form of a list of lists.  You can see what's
  inside _ with: $ ls -lah | pol "map(print,_)"
  ['total', '156K']
  ['drwxr-xr-x', '11', 'root', 'root', '4.0K', 'Aug', '2', '2016', '.']
   ... etc. for other directory lines ...  Neat idea - but the
  implementation is in C - using Python.h and Py_ fcns.  Oh, I see, in
  effect builds a whole Python that just reads and executes single
  line of Python code from command line, also pre-processes its stdin
  to list-of-lists.

- <http://www.codersnotes.com/notes/a-constructive-look-at-templeos/>
   Also add to TempleOS entry in precursors.md
   <https://usesthis.com/interviews/terry.davis/> - The Setup interview 

25 Mar 2017

- <http://cs.gmu.edu/~sean/lisp/LispTutorial.html> - interesting side-by-side
  format, discusses debugger etc. HN at <https://news.ycombinator.com/item?id=13948966>

- <http://www.codersnotes.com/notes/a-constructive-look-at-templeos/>

- <http://www.poster.pl/polish_poster_artists.html>

23 Mar 2017

- editor performance comparison at github, linked from HN yesterday

- Nils Nillson's AI history pdf from Stanford

- Peter Smith's Teach Yourself Logic 2017 self-study guide pdf (also put on kindle)
  via www.logicmatters.net/tyl


20 Mar 2017

- HN comments on "How to pick a microcontroller" - difference between
   microcontroller (Arduino) and microcomputer (RPi).  "If you've never
   bought a microcontroller, buy an Arduino" "(beware GPIO) It's so much
   easier to accidentally fry a RasPi than an Arduino" "Bitbanging pwm
   from a raspberry pi is horribly inaccurate"

- HN comments on "Show HN: How to write a recursive descent parser"
  "nearly every *actually used* programming language parser is hand-rolled"
  Link to Lepl 5.1 Pythonic recursive descent parser - now discontinued
  and unsupported, at www.acooke.org/lepl/, also at code.google.com/archive/p/lepl
  Lepl is only one of many at Ned Batchelder's Python parsing page, which
  was succeeded by github.com/webmaven/python-parsing-tools.  This last
  might go in language.md.


18 Mar 2017

- <https://news.ycombinator.com/item?id=13900153> - recommendations for AI/ML books

- <http://ai.stanford.edu/~nilsson/QAI/qai.pdf>  Nils Nilsson's history of AI, 700 pages

- <http://karlrosaen.com/ml/> recommended course of ML study, book and course recs

- ... RSNA article on AI/ML in medical imaging

- <https://news.ycombinator.com/item?id=13898968> - "Virtual machine
  escape fetches $100k at Pwn2Own hacking contest" - refs to books
  courses etc. on security.  Comment: "As far as this hack goes,
  broken down into three separate pieces, the exploits should be
  understandable as being sandbox escapes, but for three different
  sandboxes (Browser, OS, VM)."

- <http://www.sureshjoshi.com/embedded/how-to-pick-a-microcontroller/>
   How to pick a microcontroller - for beginners

- <https://news.ycombinator.com/item?id=13901752> - Hackintosh, recent

- <https://github.com/tedunderwood/LIS590DSH/blob/master/syllabusv2.pdf>
   syllabus for Data Science in the Humanities - the links in
    syllabusv2.pdf don't work from when viewed on github, but they do work
    in the downloaded pdf file.


13 Mar 2017

- <http://gist.github.com/leegao/1073233> that's leegao/Rationale.md
  50-line Python micro-JIT demo for X86 - apparently generates
  and runs x86 machine code - !?

- <https://gist.github.com/simonw/8aa492e59265c1a021f5c5618f9e6b12>
   also <https://news.ycombinator.com/item?id=13847465>
   summarized in <https://news.ycombinator.com/item?id=13855749>
  How to recover lost Python source code if it's still resident in-memory
  Uses gdb, pyrasite

- <https://github.com/lmacken/pyrasite-gui> - Pyrasite GUI, impressive
   like Mac process monitor but for the Python process including threads.


 8 Mar 2017

- <http://selfie.cs.uni-salzburg.at/> also
  <https://github.com/cksystemsteaching/selfie> - Pedagogical VM +
  Compiler + ...


 7 Mar 2017

- "What do compilers do with CPython interpreter main loop?"
   Blog post linked on HN

- Atlas Obscura recent article on Japanese internment art

- <https://github.com/benjamincrom/scrabble> 
  Python Scrabble library recovers all game moves from just final
   board and scores Suprisingly small (<< 1000 lines in all)
   looks like good style, nicely named and formatted with *no* comments.


5 Mar 2017

- <https://news.ycombinator.com/item?id=13794879> - thread on new C#
  hobby OS, compilers, GPUs, links to other C# OS.

- <https://news.ycombinator.com/item?id=13797797> - thread on APL,
  compilers, GPUs.  Or maybe not - very esoteric and insiderish

- <http://www.projectoberon.com/> new home page for recent Project Oberon -
   no HN thread, though.


3 Mar 2017

- HN post today on The Unix Hater's Handbook, including long,
  link-filled threads on alternative OS and alternative graphics (to X
  windows).


 1 Mar 2017

- eniacinaction.com, especially links in /the-book/supporting-technical-materials

- www.computerhistory.org/collections/oralhistories

- CLPython - active 2006, inactive since 2013 (meh - its abandoned)

- mathematical urban legends on math overflow (meh - a few are amusing)

- <http://dev.stephendiehl.com/numpile/>
  <https://github.com/sdiehl/numpile> - LLVM specializer for scientific
  Python code - very nice writeup nice contrast to tailbiter (below),
  which also starts with Python AST


27 Feb 2017

- <https://github.com/larsbrinkhoff/emacs-history>

- <https://codewords.recurse.com/issues/seven/dragon-taming-with-tailbiter-a-bytecode-compiler> - can combine with Alison Kapur's Byterun for a 
  self-hosting Python (subset) - in - Python

- tauthon, renamed unofficial "python2.8", python2.7 with python 3
  features backported

- Links to CPython and its standard library at Github.

25 Feb 2017

- <http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html>
   nice collection of convenient idioms
 HN comments <https://news.ycombinator.com/item?id=7365410>

21 Feb 2017

- <http://ablagoev.github.io/linux/adventures/commands/2017/02/19/adventures-in-usr-bin.html>
   lesser-known but useful unix/linux commands and utilities
   HN comments <https://news.ycombinator.com/item?id=13682925>
   HN comments specifically about editors, piping selected text through commands
    <https://news.ycombinator.com/item?id=13684339>

17 Feb 2017

- seen on HN, Mike Pall (of LuaJIT) on Reddit, recommended reading
  order for Lua C source. (links.html, 24 Feb 2017)

- www.collectorsweekly.com (in graphics/unusual media, links.html, 23 Feb 2017)

16 Feb 2017

- seen on HN, github repo with *transcript* of Rich Hickey's Simple Made Easy talk.
   same repo has other transcripts (links.html, 24 Feb 2017)

15 Feb 2017

- <http://blog.presentandcorrect.com/category/books> - 
   look for categories menu widget at the bottom of the page
   (in graphics/unusual media, links.html, 23 Feb 2017)

- That computing version of Brian Eno's oblique strategies, for programming/heuristics

- <https://news.ycombinator.com/item?id=13590305> 
  HN comment on Unix simplicity, just processes and file descriptors, along
   with riposte on how it's become so complicated (links.html, 24 Feb 2017)

- <https://www.reddit.com/r/AskHistorians/>

 9 Feb 2017

- <http://code-poetry.com/> (in typography, links.html, 24 Feb 2017)

- <https://github.com/ariestiyansyah/python-blogs> - curated list of Python programming blogs


6 Feb 2017

- <http://www.technoblogy.com/show?1KTO>  Tiny Lisp Computer 2 PCP, Eagle files on github
  <https://github.com/technoblogy/tiny-lisp-computer>

- <https://www.youtube.com/watch?v=vzPHdoOU8DQ> - TTY I/O for Mark-8 microcomputer monitor,
   via <http://www.rubyletter.com/newsletter/2017/02/03/terminal.html>
   <https://www.youtube.com/watch?v=qv5b1Xowxdk> - Altair 8800 - Video #7.1 - Loading 4K BASIC with a Teletype and paper tape.


4 Feb 2017

- http://2x-1.net/ob/gray1/ also <http://2x-1.net/ob/reginae-ex-machina/> 
  <https://news.ycombinator.com/item?id=13559615> - CPU made entirely of ROM + RAM
   uses ROM as LUT and FlipFlops (with feedback).

3 Feb 2017

- <https://news.ycombinator.com/item?id=13514057-> old terminal/text
   user interfaces (TUI) often better than newer web and GUI.

- <https://www.thegearpage.net/board/index.php?threads/the-amp-guts-appreciation-thread-part-2.918374/> photos of tube amp insides - showing construction techniques.


2 Feb 2017

- <https://pdos.csail.mit.edu/6.828/2016/xv6/book-rev9.pdf>
  (programming/design examples/unix, links.html, 24 Feb 2017)

31 Jan 2017

- <https://news.ycombinator.com/item?id=13518170> Comments on "The Craft of Text Editing"
  with many links to more recent refs on editor implementation.

- <https://news.ycombinator.com/item?id=13518800>  Comments on "how to build a castle"
  including links to ongoing projects: <http://burgbau.at/burgbaufrie/?page_id=428> (Austria)
   <http://www.guedelon.fr/en/>  (France)

- <https://news.ycombinator.com/item?id=13513367>  Comments on "what is the oldest computer
   program still in use?"

- <https://news.ycombinator.com/item?id=13507122> Comments on
  <https://github.com/monostable/awesome-electronics>, with many more links.

- <https://news.ycombinator.com/item?id=13530657> Comments on "Bring back the dumb phone",
   advice on configuring/using smart phones to minimize distraction.

- <https://github.com/vkazanov/elfuse> - FUSE system in emacs lisp
  <https://news.ycombinator.com/item?id=13529238> - comments on above, commenter
   recalls AmigaOS FrexxEd editor "that makes all open buffers accessible as a file system"
   Sounds similar to Plan 9 Acme.


30 Jan 2017

- <https://news.ycombinator.com/item?id=13520891> Ask HN on programmers' blogs
  Maybe add after my own list in programming/buzz, also copy obscure programmers'
  blogs HN posts from geek culture.


29 Jan 2017

- <http://www.dourish.com/goodies/jargon.html> - HTML version of old pre-ESR Jargon file

- <https://news.ycombinator.com/item?id=13514918> - HN comments on ITS git repo

- <http://jonatron.me/> - RPi PDP11 simulator including front panel


27 Jan 2017

- <https://news.ycombinator.com/item?id=13498365> thread on RS232 and ASCII,
  response to <http://www.catb.org/esr/faqs/things-every-hacker-once-knew/>
  more comments at <https://lobste.rs/s/qph9hd/things_every_hacker_once_knew>
  other extended responses at
    <https://utcc.utoronto.ca/~cks/space/blog/unix/CarriageReturnWhatFor>
    <https://utcc.utoronto.ca/~cks/space/blog/unix/HowUnixBackspaces>
 more, with explanation and diagram of how it's handled in Linux:
  <https://unix.stackexchange.com/questions/117981/what-are-the-responsibilities-of-each-pseudo-terminal-pty-component-software/120071#120071>
 more on ascii (1-Feb-2017):
 <https://garbagecollected.org/2017/01/31/four-column-ascii/>
 <https://news.ycombinator.com/item?id=13539552> HN comments on above, lots of links

24 Jan 2017

- <http://ask.metafilter.com/305199/I-need-a-python-script-that-will-run-a-script>
  First answer has several links on using Flask on RPi as a REST endpoint
  answerer recommends sending HTTP request to 2nd RPi that returns JSON response.
  Another answer recommends ssh on first RPi to run command on second RPi,
  possibly using paramiko.  Another answer recommends scp text file and use
  inotifywait - which waits for changes on a file. (links.html, 26 Jan 2016)

23 Jan 2017

- <https://github.com/PDP-10/its> - Incompatible Timesharing System, code and docs (links.html or maybe precursors.md, 26 Jan 2017)

22 Jan 2017

- <http://oldblog.antirez.com/post/redis-persistence-demystified.html>
  Very long post about persistence in various dbs, Unix file caching
  and writing, append only files (AOF) and how they relate do database
  snapshots .rdb files in Redis.

- <http://everything2.com/title/Fast+6502+multiplication>

- <http://azer.bike/happy-hacking-linux/> - Arch-based distribution with
  tiling window manager (which one? - looks like xmonad).  This page
  includes window manager cheatsheet that summarizes basic key
  operations.  Nice simple web page design

21 Jan 2017

- <http://gnuradio.org/blog/buffers/>  GNU Radio Buffer architecture
  <https://news.ycombinator.com/item?id=13406932> - more links and references

- <https://github.com/lonetwin/pythonrc/> - "a python script intended to
  improve on the default Python interactive shell
  experience. ... Unlike ipython, bpython ...this is not ... used as a separate
  interactive environment. ...  a single file ... use it as any other
  rcfile."

- <https://dlo.me/archives/2014/09/08/pythonrc/>
  another pythonrc

- <https://pypi.python.org/pypi/blessings/> "a pythonic answer to
  curses" "A thin, practical wrapper around terminal coloring,
  styling, and positioning" (pypi page includes instructions)
  <https://news.ycombinator.com/item?id=4399060>
  <http://pythonhosted.org/blessings/> (api doc)

- <https://news.ycombinator.com/item?id=3965396> - unix-like-shells, pipes in Python

20 Jan 2017

- <https://omgfacts.com/we-used-to-have-6-more-letters-in-our-alphabet-a7e1a165853d#.pd56w4he6>
  <https://news.ycombinator.com/item?id=13408797>
  The lost letters of the English alphabet, 195 HN comments many correcting errors

- <http://p.migdal.pl/2016/08/15/quantum-mechanics-for-high-school-students.html>
  Links to course outlines (in Polish!) links to textbooks, online materials, osoftware

17 Jan 2017

- <https://hackaday.io/project/19035-zerophone-a-raspberry-pi-smartphone/log/51839-project-description-and-frequently-asked-questions>
  <https://news.ycombinator.com/item?id=13398705>

14 Jan 2017

- <https://github.com/ChrisPenner/rasa>  Rasa editor in Haskell
  detailed guide to the code: <https://news.ycombinator.com/item?id=13395941>
  (links.html, 17 Jan 2017)

13 Jan 2017

- <http://crna.cc/b/11> Blobless Linux on Raspberry Pi 
  Blog about <https://github.com/christinaa/rpi-open-firmware>
  HN comments at <https://news.ycombinator.com/item?id=13396625>
   including lots of complaints about RPi engineering besides blobs and openness (links.html, 16 Jan 2017)

10 Jan 2017

-  A multiple tab terminal emulator implemented in python
   <https://github.com/stonewell/pymterm>
   <https://news.ycombinator.com/item?id=13370486>
   many dependencies, including paramiko (ssh) pygame kivy (ui)
   in fact it might be useful as guide for how to use the dependencies
   (utilities.md (?), 18 Jan 2017)

 9 Jan 2017

- Containers from Scratch (in great faiths/linux/containers, links.html, 17 Jan 2017)

- Ukelele tuner in Python, uses numpy, pyaudio (links.html, 26 Jan 2017)

- From Python to Numpy

 7 Jan 2017

- 2017.sucks simple website JS demo with nice graphic desing
  via HN <https://2017.sucks/#/>
  <https://github.com/alexbowers/2017.sucks>

- A Minimal TTL Processor for Architecture Exploration
  <http://www.bradrodriguez.com/papers/piscedu2.htm> only
  "designed to achieve a maximum of functionality with a
  minimum of logic."  "Requiring only 22 standard TTL chips (excluding
  memory), it is well within the ability of a student to construct and
  understand." "fully static, it can be run at slow clock speeds or manually single-stepped"
     includes schematic but apparently never built?
also there is <http://repository.cmu.edu/cgi/viewcontent.cgi?article=1595>&context=compsci
     4-bit TTL processor for the classroom - with photo on solderless breadboard
     parts list but no schematic.


 6 Jan 2017

- jehanne.io JehanneOS Plan-9 distro in Plan-9

- marc.info/...9fans...   9fans mailing list archive in Plan-9

- MA single-window minimal acme clone in Tcl/Tk
  <http://www.call-with-current-continuation.org/ma.tar.gz>
  (in editors/acme, links.html, 17 Jan 2017)

- christinaa/LLVM-VideoCore4 + HN comments
   via HN comments on Tourist Guide to LLVM from Reger's blog.
   (in RPi hacking, links.html, 16 Jan 2017)

- 9Fans post on Facebook done right, in Plan 9 style.
   (links.html, 16 Jan 2017)

- HiFive1 RISC-V Arduino-compatible dev kit - in HN and Hackaday.


 4 Jan 2017

- Leslie Lamport's annotated bibliography at
  <http://research.microsoft.com/en-us/um/people/lamport/pubs/pubs.html>

- Portacle IDE for CL with SBCL, QuickLisp, Emacs with Slime, Magit
  (git inside emacs), and Company (text completions) all on a memory
  stick!

3 Jan 2017

- Eno-inspired Oblique Strategies for programing, linked from HN, also HN comments

- PLT MrEd as an OS paper in precursors.md

2 Jan 2017

- Rob Pike on C programming <https://www.lysator.liu.se/c/pikestyle.html>
  (is this the canonical link?)

- Summary of RISC-V assembly programming <https://www.imperialviolet.org/2016/12/31/riscv.html>

- RISC-V programming card <http://www.cl.cam.ac.uk/teaching/1617/ECAD+Arch/files/docs/RISCVGreenCardv8-20151013.pdf>

- vi-style editor in picolisp <http://picolisp.com/wiki/?vip> (links.html, 17 Jan 2017)

- advice on tech writing <https://news.ycombinator.com/item?id=13301511>

29 Dec 2016

- <http://davidad.github.io/blog/2014/03/12/the-operating-system-is-out-of-date/>  "I find that all the significant concepts in software systems were invented/discovered in  the 15 years between 1955 and 1970." add links to HN discussion:
   at <https://news.ycombinator.com/item?id=13271220> 
       <https://news.ycombinator.com/item?id=7402571> (history, links.html, 31 Dec 2016)


27 Dec 2016

- <http://www.maloryproject.com/about.php> typography,
  <http://dodecaglotta.com/> (in typography, links.html, 2 Jan 2017)

- Bringup history of Mac OS X (via HN) at www.pagetable.com (in great
  faiths/mac, links.html, 2 Jan 2017)

- <https://github.com/haskus/haskus-system> www.haskus.org www.vipervm.org
  "provide a full Haskell user-space environment on top of the Linux kernel"

- <http://littleosbook.github.io/> and maybe HN discussion


26 Dec 2016

- <https://zenhack.net/2016/12/25/why-python-is-not-my-favorite-language.html>
  Why Python is not my favorite programming language (in Python
  assessment, links.html 2 Jan 2017)

- HN post on OLPC compared to RPi  <https://news.ycombinator.com/item?id=13258261>
  esp. View Source for any application and ad-hoc networking with wireless neighbors. (precursors.md, 31 Dec 2016)

- PicoLisp tutorial <http://software-lab.de/doc/tut.html> including built-in vi-like editor,
  ok tutorial <https://github.com/JohnEarnest/ok> with useful REPL commands
  (both in other.md 31 Dec 2016)

- netshade/apostasy.md <https://gist.github.com/netshade/fda492cb780bae1190063c1ad41b334a>
  on Macbook -> MS Surface + Linux in a VM  in Great Faiths/Windows


23 Dec 2016

- Apple ][ emulation on AVR microcontroller, seen on HN (links.html, 1 Jan 2017)

22 Dec 2016

- for Piety/doc/... : Googler, command line Google in Python, at github.

21 Dec 2016

- Recent HN Fortran links in language arcana

20 Dec 2016

- Aboriginal Linux "builds the smallest/simplest linux system capable
  of rebuilding itself from source code"
  landley.net/aboriginal/about.html and /history.html
  also landley/toybox, make Android self-hosting.
  He presented on podcast at linuxluddites.com - "Not all change is progress"
  Also github site, <https://github.com/landley/aboriginal> (links.html, 1 Jan 2017)

19 Dec 2016

- BrainF* for Dummies in what, computer architecure?
  <http://blog.klipse.tech/brainfuck/2016/12/17/brainfuck.html>

- ok (APL-like) <https://github.com/JohnEarnest/ok> (other.md, 31 Dec)

- Z acme-inspired editor in scala <https://github.com/sandgorgon/z> (links.html, 31 Dec)

- Berkeley eecs cs152/sp13 page with links to many pdf notes.

- chip8 simulator in CL, literate program. Oh, never mind, I had confused it with
  BBC micro:bit but-- "CHIP-8 is
  an interpreted minimalist programming language that was designed by
  Joseph Weisbecker in the 1970s for use on the RCA COSMAC VIP
  computer. ..."  Still, it's a nice coding study.  Maybe in computer architecture?

- <https://github.com/doorbell88/Aquarium> - runs in mac terminal - maybe
  have a section in links.html or a Piety/doc/display.md for
  terminal display hacks/demos to use/adapt as sample Piety applications
  Don't we already have Life Snakes Rogue-like ... also
  candidates in other languages: sed Flappy bird clone, sed Tetris clone.

- youtube video, Monty Python for Pythonistas

- software heritage

- theorem prover museum

15 Dec 2016

- HN comment "Python has gotten hard to learn" (in Python assessment, links.html 2 Jan 2017)

- HN comment comparing GoboLinux and Nix in great faiths/linux/filesystems


14 Dec 2016

- Andrew Wiles interview in education, call out quotes on problem scale (vs 3rd grade) and getting stuck

- HN comments praising Lotus Notes (in Nostalgia, links.html 2 Jan 2017)

- code-poetry.com (links.html 23 Feb 2017)

- NLP in Python example, Pride and Prejudice, (in Python examples, links.html 2 Jan 2017)

- Scott Aaronson comic strip, "The Talk" satirizing woo about QM in physics/popular culture/humor


13 Dec 2016

- Ancient languages in 10 lessons at
  www.openculture.com/2014/01/learn-latin....  Latin Greek Old English
  etc.


12 Dec 2016

- <https://github.com/jmcgeheeiv/pyfakefs> via HN 
  intended as mock for testing, but might actually serve as
  Piety in-memory file system.
  (utilities.md 18 Jan 2017)

9 Dec 2016

- www.rle.mit.edu/rgallager/documents/BooleShannon.pdf - Claude
  Shannon's methods and accomplishments, lecture by Robert Gallager
  "Shannon's genius lay in finding the "right way", the "simple way"
  to look at everyday technical problems" "Searching for simplicity is
  really searching for intuitive understanding of a simplified version
  of the problem that doesn't ignore the underlying original issues"
  "Graduate students often mistake simplicity for triviality .. The
  misconception is that it takes the best students to solve the most
  complex problems.  Actually, it takes the best students to *find*
  the simplest open problems."

- For Piety precursors.md: Xerox Alto simulators, SALTO and Contralto


8 Dec 2016

- Python 3 module of the week <https://pymotw.com/3/>


7 Dec 2016

- Andrew Wiles interview w/HN comments, also video documentary on FLT

- web page on Butterfield Pi theorem (dimensional analysis)


6 Dec 2016

- ed clone in Haskell via HN Actually Using ed post

- original ed-in-C from V6 Unix at tuhs.org via HN Actually Using ed post
  Oh, we already have this, but maybe revise explanation in following parens.

- Eli Benderski's blog, eli.thegreenplace.net/archives/all via HN post
  on readline.  Add a separate link on same line just for his Python category.
  (and maybe another for Programming, which does not overlap).

- CRSR blog, <https://manignosis.crsr.net/archive.html> via ed clone in Haskell.
  (He recommends The Programming Historian, mentioned above)


3 Dec 2016

- Terry Tao's career advice (links.html)


2 Dec 2016

- for presursors.md, Cosmos C# project - new links including YT in HN today.

- for links.html math/provers, The Incredible Proof Machine with links to other
   pedagogical provers.


1 Dec 2016

- For languages.md, Python PEP 523 on JIT for CPython etc, refs Pyjin
  (?) project.


29 Nov 2016

- Understanding Academic Medical Centers: Simone's Maxims from
  Clinical Cancer Research 1999, via HN, in science/milieu or maybe
  education/something.  Oh, on reading this is clearly about academic politics
  but not so great we should link to it..

- High-quality ramen recommendations from HN post in geek culture/food
  'Eating Ramen by Yourself'

- Butler Lampsons' 1993 "SE: what worked" article maybe with Dan Luu's
  20year followup, in design principles next to Lampson's hints for design.


16 Nov 2016

- For Piety precusors.md:
  notanos, Javascript desktop mentioned in this HN comment:
  <https://news.ycombinator.com/item?id=12956841>
  screenshot:  <http://i.imgur.com/sPh0c6s.png>
  older version: <https://github.com/Lerc/notanos>
