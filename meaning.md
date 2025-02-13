---
layout: default
title: "The Meaning of Life"
---
[#]: ((((((

```
Memex:

In general: Tie to what others have written.  Make reader-friendly! Tone should be Shelly Kagan
Make dependency the minimal amount that will allow reader to understand story.
Add relevant hyperlinks

We want to give the rabbits *heuristics* that generally cause their genes to be around.
  The heuristics include adaptability to the environment, which includes learning
    Learning might also be necessary computationally, in that we have 4GB of DNA but 100 trillion synapses.  Evolution doesn't have time to encode Tetris

The meaning of life: Why am I here?  What should I do?
  Why am I here?  Biology: Those who had these heuristics were the ones who should be around.
  What should I do?  This is a question for computational optimization!

Death: Cloning, reset.  It's not that there's pressure to die, but having grown old etc., dying isn't as evolutionarily problematic as it might be viewed.

4 scenarios:
  1. Lazaruss Long: a person gets periodic "rejuvinations" including neural tissue
  2. A person clones themselves, then does "network distillation"
  3. A person clones themselves, then does "network distillation" via lessons, etc.
  4. 2 people (with compatible or complementary conceptual structures) make two genetic mixes of themselves.
```

```
Rabbits.  What behaviors will be around?
  Behavior is interaction of genes and environment
  Caveat: evolution isn't "optimal" (Now that we have a "fitness function", evolution is greedy and doesn't have infinite search bandwidth)
Rabbits.  Limited computational budget.

core idea: want to program minds of successful rabbits subject to biological and computational constraints
```

```
x Setup: Happiness of Rabbits
  Designing a brain:
    Consideration
x     Walking = Falling + Catching
      Squiggly Lines
      Enter Complexity: The Peacock's Tail
      Will: Interaction of Cognitive System and Reward System
      Taste
        Specifying Reward: The Bulldog Hugging Robot
        Hill Climbing on the Cingulate Cortex
        Some Strategies for Maximizing Reward
    Bugs
      Artificial Sweetener, Drugs, and Virtual Reality
        Habits and Pain
        Hedonism
  Forays:
    Economics and Ethics
    Atomic Waves and Platonic Forms
      # Point is that creating concepts (beyond atoms) serves a *cognitive* purpose, and can be decided by information theory
    Designing your Successor
    Entropy: A Petri Dish Falling into a Volcano
      Nihilism
  Consciousness and Death (How a person never dies)
  Free Will
  Conclusions
    Also, implications for robots maliciously taking over (unaided by people) (but also Bostrom paper clip bot)

x Geld
***
x Happiness of Rabbits
x Walking = Falling + Catching
  Squiggly Lines
  Specifying Reward: The Bulldog Hugging Robot
  Interaction of Cognitive System and Reward System
  The Peacock's Tail
  Hill Climbing on the Cingulate Cortex
  Some Strategies for Maximizing Reward
  Artificial Sweetener, Drugs, and Virtual Reality
  Habits and Pain
  Hedonism
  Economics and Ethics
  Atomic Waves and Platonic Forms
  Designing your Successor
  A Petri Dish Falling into a Volcano
  Nihilism
  How a Person Never Dies
  Free Will
  Conclusions
    Also, implications for robots maliciously taking over (unaided by people) (but also Bostrom paper clip bot)

```
[Boundless Will](boundless)<br>
[Religion](religion)<br>
[Immortal](2017/04/06/immortal)<br>
[Closet Space](closet)<br>

[#]: )))))(((((

TL;DR: [FIXME]

```
Biological meaning of life is reproduction.
Creatures evolved cognitive systems.
Cognitive capacity is limited.
"Meaning of Life" is convenient term for what we "want" which ultimately drives our cognitive
  systems to take actions that spread genes
A satisfied creature doesn't take actions, so doesn't spread genes.  Therefore happiness isn't a state but a process
Meaning of Life and "Taste" are both heuristics
Taste has holes, which can be exploited
Morality emerges with multiple cognitive willful agents
```

# Introduction
[#]: ))))((((

This essay is a collection of insights gained from my work in Developmental Robotics, Artificial Intelligence, and Reinforcement Learning, as
they pertain to the age-old question "What is the meaning of life?".  I don't claim to have all the answers, though I hope that this essay will
help us get a little closer to answering the question.

With that in mind...  *The biological meaning of life is reproduction.*

If it were that simple, this series would be much shorter, but there's some truth to the statement: Barring any organisms created in a lab, the
only organisms that are alive today are those whose ancestors reproduced, and it's likely that today's organisms have inherited their ancestors'
tendency to reproduce.  But you'd be right to be skeptical that a single word, "reproduction", can answer such a often-pondered question as
"What is the meaning of life?".  The complexity of the meaning of life lies in describing the intricacies that are entailed by the term
"reproduction".

# Happiness of Rabbits: A Thought Experiment about Evolution
[#]: ))))((((

(See Happiness of Rabbits in xblog.md)

# Walking = Falling + Catching
[#]: ))))((((

(See Walking = Falling + Catching in xblog.md)

# Will: Interaction of Cognitive System and Reward System
[#]: ))))((((

TL;DR: We have two systems in our head, which might result in two different meanings of life.

***

> Alas, two souls dwell in my breast, <br>
> --Johann Wolfgang von Goethe (from Faust, 1808)

> No conscious tabulation of the disadvantages and horrors of junk gives you the emotional
> drive to kick [a heroin habit]. <br>
> --William S. Burroughs (from Junky, 1953)

> Man is not truly one, but truly two. <br>
> --Robert Louis Stevenson (from The Strange Case of Dr. Jekyll and Mr. Hyde, 1886)

***

Although our rabbits are really just processes, interactions of molecules, it's useful to create abstractions to describe these processes.
Otherwise, it'd take years of describing things on the atomic level that might be expressed as "That rabbit is hungry.".  In particular, it's
sometimes useful (both from a physiological and psychological point of view) to describe the rabbits as each having a "mind" that consists of
submodules including the "cognitive" and "limbic" systems.

***

Each of us has a world-model in their heads, or a conceptual structure that I'll call a *worldview* (or sometimes called a *Weltanschauung* in
Psychology, which is German for Worldview).  At the most basic level, a worldview is how we categorize The World.  We throw "dogs" into the
"animate beings" category, "icebergs" into the "huge objects" and "floating things" categories, but there's more to a worldview than that.  A
worldview also contains ideas about how hang-gliders behave, associations, generalized abstractions, and "gists" of concepts.  Much of a
person's worldview is tacit knowledge, meaning that it's hard to put some views or concepts into words.  For example, given a photo of an
adult's face, we can easily tell the if the picture's of a man or a woman, but it's incredibly difficult to write a set of rules so precise that
a computer could follow them and make the distinction.  (Computer systems, such as neural networks, can be trained to make the distinction, but
this is virtually always by being trained on examples rather than explicit instructions.)  Tacit knowledge also includes concepts that are so
deep or ever-present that the person doesn't even realize that they're there.  For example, you might not be immediately aware that gravity is
pulling down on you or that you're breathing and blinking.

***

The subfield of Artificial Intelligence called [Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning) would describe a
rabbit as an *agent* that interacts with its *environment* or local surroundings.  The agent takes *actions*, where the actions may be very
low-level, such as twitching an individual muscle.  For example, the "action" of hopping is really a composite of a large number of lower-level
actions involving dozens of muscles.  The agent receives *observations* from its *sensors*, where the observations may also be very low-level:
the reports of individual "pixels" on the rabbit's retina, for example.  As described in the section on Squiggly Lines, a rabbit doesn't
actually see objects such as grass or dingos, but rather a set of sensor values that can be *interpreted* as being caused by grass or dingos.
The rabbit also receives a *reward* signal, and it's the rabbit's goal to maximize the amount of reward it gets over its life.

Standard Reinforcement Learning assumes that the reward signal is a single numerical value.  I think this is oversimplifying matters.  Our
actual "reward" is probably a hodgepodge of often contradictory tricks that evolution hacked together.  But, the Reinforcement Learning model
might be a useful initial approximation.  At any rate, our rabbit will have some criteria for deciding that some possible actions are better
than others.  For example, when confronting a dingo, hiding is usually a "better" strategy placing one's self in a dingo's mouth.  Note that I
just introduced the term "better" when before we had only atoms.  Did we just derive [Ought from
Is](https://en.wikipedia.org/wiki/Is%E2%80%93ought_problem)?  Maybe.  For me, "better" just means that rabbits that tended to evaluate that
strategy A is "better than" strategy B were the ones whose genes got passed on.  From this, we can use terms like "desire" or "wanting" or
"will".

The rabbit would also have a *worldview* or model of The World, and a *cognitive system*.  The rabbit's cognitive system does two things: it
*builds* the worldview by learning from its experience, and it *uses* the worldview to do things like make predictions, draw inferences, and
create plans to get reward.  Here, I'm using the term "prediction" loosely.  For example, if a rabbit sees a dingo's head, it will probably
"predict" that it will soon see the dingo's body.  The predictions aren't necessarily temporal either.  For example, we can "predict" that the
Nile River has a source.

Note that our rabbit's cognitive system can be somewhat independent of its reward system.  For example, if (for some strange reason) we
structure our rabbit's reward system such that it gets reward for doing somersaults, then the cognitive system will figure ways for the rabbit
to do lots of somersaults (and it will cause the rabbit take actions to do this).

***

One of the better known example of classical conditioning is the story of Pavlov's dogs: Every time Dr. Pavlov fed his dogs, he rang a bell just
before serving them.  After several days of this, the dogs began to salivate every time they heard the bell.  This sounds simple enough, but how
did the dogs know it was *the bell* that signaled that food was coming?  Any time the bell rang, there were hundreds of other stimuli going on.
During one particular ring, a bird might have been heard outside the window, one of the dogs may have been sitting in a particular position,
Dr. Pavlov may have been whistling a particular tune.  Why didn't the dogs associate any of these other stimuli with food?

The answer is that they probably did.  At least a little bit at first.  When the dogs are served food, this fact is signaled primarily through
taste and smell to the cingulate cortex, which sends a signal to a pleasure center in the hypothalamus, which "squirts" dopamine all over the
neocortex.  Dopamine causes the areas that were recently active to have a slightly higher "reward value" attached to them.  So, if a dog noticed
the bell, the bird, and that his friend Laika was wagging his tail in an awkward manner, the food will all be slightly more associated with all
these things than it was before.  At the next feeding, the association between the bell and food will be strengthened a little more.  But the
bird probably won't be chirping the same, and Laika's tail probably won't be wagging in the same awkward manner, so the food-assocation with
these stimuli won't be strengthened.

An interesting thing happens *after* the association between the bell and the food has been established.  If we were to measure the dopamine
levels in the dogs' brains, we'd find that, before conditioning, the dogs get a spike of dopamine when they get the food, but not when they hear
the bell.  This suggests that the dogs *feel* pleasure when they actually get the food.  However, after conditioning, the dogs show a dopamine
spike when *the bell is rung*, but not when they get the food.  So the dogs will begin to try to predict *the bell* and figure out how to get
*the bell* to ring, as opposed to trying to figure out how to get the food directly.  If Dr. Pavlov plays a mean trick and decides not to give
his conditioned dogs their food after ringing the bell, the dogs will have a dopamine spike when hearing the bell, but they'll have a marked
*decrease* in dopamine when the food doesn't arrive at the expected time.  The dogs' dopamine levels will momentarily drop well below their
baseline level, indicating the dogs feel "pain" or discomfort when they don't get the food.  In this case, pain works the same way as pleasure,
but in reverse.  Instead of associating recently active brain areas with "good", these areas are associated with "bad".  If Pavlov continues his
rude joke several times, the dogs will eventually extinguish the original "pleasure" association they had with the bell.

Likewise, if someone begins to smoke cigarettes for the first time, initially the reward that nicotine produces will be associated with other
salient features: certain people in the room, a particular flavor of soft drink being sipped, etc..  Only after several instances will our
limbic systems "figure out" that it's the cigarette causing the sensation.

***

Because of the incremental process of evolution, people's brains are somewhat layered.  Our neocortex, which is heavily involved in our higher
cognitive processes, lies atop the "reptilian brain" and the "limbic system".  The reptilian brain, which is the brain stem and cerebellum,
controls low-level instincts and autonomic functions (such as breathing).  The limbic system includes structures such as the amygdala and the
hypothalamus, and is heavily involved in emotional processing and classical conditioning, where a stimulus (such as bell ringing) occurs right
before a reward (such as food) is given, and the stimulus eventually becomes associated with the reward itself.

Neuroscientists will debate how clean the separation is among these layers, but I suspect that higher level thought *can* largely be detached
from emotion or reward[^2].  For example, the neurologist Antonio Damasio describes a patient, called S, whose amygdalae were effectively
knocked out.  Because of this, S didn't experience fear or anger.  When she was put into a situation that would normally induce fear in people,
she understood on an intellectual level why there was cause to be concerned, but she simply didn't experience the emotion of fear.

(A note on my terminology: the terms "limbic system" and "neocortex" refer to the actual structures in our brains.  The terms "reward system"
and "cognitive system" refer to idealized versions of these structures.)

[^2]{Jeff Hawkins gives a computational account of the neocortex which has the goal of making predictions.  Hawkins's model has no reward or
motivational system, which he claims belongs to subcortical structures.}

<!-- *** -->

<!-- <\!-- FIXME cite A not B -\-> -->

<!-- I always thought our family dog, Rex, was something of a dog genius.  That is, until I found -->
<!-- out about the "A-not-B" task used in Developmental Psychology.  In this experiment, a baby is -->
<!-- shown a toy being placed in one of two bowls.  The bowls are within the baby's reach, but are -->
<!-- angled such that the baby can't see inside them.  If the baby is immediately allowed to reach -->
<!-- for the toy, he or she will grab the toy from the correct bowl.  However, in A-not-B, the -->
<!-- experimenter will distract the baby for a moment just before the baby is allowed to reach for -->
<!-- it.  Babies under the age of 10 months won't always reach for the right bowl.  It seems as if -->
<!-- they completely forgot which bowl the toy was in.  I was surprised to learn that even adult -->
<!-- monkeys don't do so well at this task.  I figured that Rex, being the dog-genius he was, could -->
<!-- ace the A-not-B test, so I tried it (replacing the toy with a doggy treat).  Rex failed.  He -->
<!-- always went to the correct bowl when he wasn't distracted, but it was a craps shoot which bowl -->
<!-- he went to if I distracted him for even an instant. -->

<!-- Thus, life as a dog must be quite different from life as a person.  A dog has a somewhat -->
<!-- less-devoloped neocortex than a human, so they must rely more heavily on their limbic system -->
<!-- for making decisions.  A dog, then, lives more in the moment, using instincts and short-term -->
<!-- rewards.  If you can't do the A-not-B task, you don't have much of a medium-term memory.  So -->
<!-- life as a dog might be like life for humans with hippocampal damage, who are unable to form new -->
<!-- memories (such as the main character in the film "Memento").  The chief way that people who -->
<!-- lack a functional hippocampus learn is through classical conditioning, like Pavlov's dogs. -->

<!-- <\!-- find list of animals that can and can't pass this task -\-> -->
<!-- <\!-- dolphins, african grey parrots, chimpanzees, monkeys -\-> -->

***

> Reason is, and ought only to be the slave of the passions, and can never pretend to any other office than to serve and obey them.
>
> --David Hume, 1740

Consider an ideal optic lens.  The "purpose" of an ideal lens isn't reproduction, but rather to focus light as a parabola.  It might not be too
much of a stretch to say that a lens's "purpose" or "goal" is to focus light, and this goal can be described mathematically, so we can say what
makes a good and bad lens.  In our rabbits, their eyes' lenses are "tools".  That is, the proximate purpose of the lenses is to focus light, but
the ultimate purpose is to help the rabbit reproduce.  It's possible that there are lenses that focus light less well, but somehow better help
the rabbit reproduce.  These lenses would be preferred by us (the creators of the rabbits).

Likewise, I'd argue that the "goal" of the cognitive system is to characterize the environment it experiences through its sensors, and that the
cognitive system is also used by to help in reproduction.  It gets more complicated here because the design of a cognitive system has more
flexibility than the design of a lens, so that I can imagine a cognitive system that is worse at prediction but better helps our rabbits to
reproduce.

A reward signal can be helpful for a cognitive system.  The reward signal can provide "hints" as to which parts of The World to pay attention
to.  If an ideal cognitive system has no reward, it has no bias for which parts of the world to characterize: it will devote just as many
cognitive resources to understanding the "politics" of the seagulls on the boardwalk as it will to understanding the politics of the people in
Washington D.C..

So are there two dueling meanings of life?  That is, there's the meaning of life from a biological point of view (which is what our reptilian
brain wants), then there's the meaning of life from the point of view of an ideal cognitive system, which is to characterize the world.

It's interesting to consider which system "we" truly are.  Or it's possible that what we consider to be our inner selves is actually the
combination of both these systems.

# Squiggly Lines
[#]: ))))((((

(See Squiggly Lines in xblog.md)

# Heuristics
[#]: ))))((((

(See Heuristics in xblog.md)

## Specifying Reward: The Bulldog Hugging Robot
[#]: )))(((

TL;DR: The Bulldog Hugging Robot expands on the Squiggly Lines idea and that specifying innate goals is tricky and hacked.

***


A problem with innate rewards for people or rabbits is that we have to be born with them.  There are people (and presumably rabbits) that are
born blind or deaf, yet are still attracted to members of the opposite sex.  This means that our fundamental rewards probably aren't tied to a
specific sensory modality.

***

The Gedankenexperiment of the "Bulldog Hugging Robot" is that you want to build a robot whose goal is to hug bulldogs.  The robot would have
little interest in dalmatians, and no interest at all in hugging people.  In this Gedankenexperiment, we're not allowed to know what the robot's
sensor suite is (we're back at the squiggly lines problem).  So, how do we tell the robot about bulldogs (since we can't ground the concept)?

My idea for a solution is that you can provide an *ungrounded* concept of what a bulldog is.  This representation will be *invariant* with
respect to any specific sensory modality.  The representation will be some relational conceptual structure, and the A.R.R. will develop higher
and higher concepts from its sensors until it eventually develops a concept that has a very similar structure to the abstract one ("Essence of
Bulldog") we provided to it.  At which point, the robot will have grounded this concept.

***

To get an idea of how much is in our innate worldview, consider testosterone.  Since testosterone innately makes a person aggressive, we must
have an innate model of aggression.  I think it's interesting that testosterone serves a similar function in bull sharks and hyenas as it does
in people, since this hormone is only a symbol.  (Unlike glucose (where the molecule actually has energy), there's nothing fundamental to most
hormones that make them behave that way.  My guess is that we could swap dopamine receptors and serotonin receptors, and the respective
neurotransmitters, then serotonin would act like dopamine (meaning lots of serotonin would have the same psychological effect as lots of
dopamine would have) and vice versa.)

I'm guessing people have an innate world-model that's complicated enough to specify the difference between male and female on at least an
abstract level.  From a squiggly lines perspective, it would also be tricky, at least, to have an innate model that's sophisticated enough to
encode innate rewards for things that would be useful for our rabbits such as a desire for social power, maternal behaviour, or jealousy.

***

Consider a "pure bred" bulldog.  Its mom was a bulldog and its dad was a bulldog, and they had sex.  I still haven't been able to put myself in
those bulldogs' shoes: you see a bulldog and get aroused.  (I can't imagine it, even though it makes sense.)  (There's the converse too: I can't
imagine a good-looking human female coming on to me and not feeling affected.)

Along the same lines, there was a point where I couldn't imagine liking Vegemite, the Australian condiment made from yeast extract.  But I've
gradually conditioned myself to like it by mixing it with fatty food.

***

Designing a reward function --what our rabbits *want* deep down-- can be tricky.  Dark tales are told of genies who obey their master's wish to
the letter, but end up doing something the master obviously didn't intend.  Giving exactly the same system 2 different reward functions can
result in 2 radically different behaviours.  For example, Leslie Kaelbling, a researcher in Artificial Intelligence at MIT, describes her
experience with motivating a wheeled robot to navigate a room.  Initially, she "punished" the robot for running into walls FOOTNOTE{She did this
by giving the robot a negative reward when its wall-bump sensors were activated, then programming the robot to maximize its reward, or,
equivalently, to minimize its punishment.}.  The robot quickly learned that the policy that maximized its reward (or minimized its punishment)
was to not move at all.  So Leslie changed the reward function to also include a positive reward for moving.  After this, the robot learned to
simply spin in circles.

## Hill Climbing on the Cingulate Cortex
[#]: )))(((

TL;DR: This is one of the most important sections to understanding happiness is, and further expands on the Bulldog Hugging Robot idea to show
  that finding what makes us happy is essentially a "hillclimbing" search.

***

I have a pet theory that it's the cingulate cortex that encodes our innate invariant reward.  The theory is that the cingulate cortex is
hard-wired, and acts like a hash that is activated only under certain conditions FOOTNOTE{The cingulate can be thought of as one of the boxes in
Jeff Hawkins's model of the neocortex.}.  For example, a region of the cingulate might encode a representation of femininity that's invariant to
any particular sight or sound of a woman.  Furthermore, this probably works with the lower level (plastic) cortical areas in a complex way.  So,
some of what attracts us to a woman is innate, but much of it is learned, probably through classical conditioning.  When a particular area of
the cingulate is activated, it sends a signal to a corresponding area of hypothalamus, which does things like shoot out dopamine (leading to
repeat actions and classical conditioning) or triggers a shot of adrenaline.

If this theory is correct, then much of what we do in life might be described as "hill climbing on the cingulate".  For example, suppose no one
ever told you explicitly about sex or even romantic relationships.  I'd guess that people would still reproduce.  If you're a boy, around age
13, for some reason, you'd find yourself very interested in girls.  You might even find yourself sexually aroused, but you're not sure what to
do about it, but you might have an inkling that it has something to do with girls.  Given unlimited access to girls, you might find you get
reward for touching them and having them touch you, especially if they touch your private areas (and you touch theirs).  I'd imagine, you'd
eventually figure out how to have sex with them.

I wouldn't be surprised if the cingulate encoded (in some form) less base motives such as social power.  Our primate social ancestry has been
long enough to allow at least part of something as complex as social power to be encoded innately.  If this is true, then "trying to find
yourself" or "trying to figure out what makes you happy" might be essentially hill climbing on the cingulate.  You're trying to make the reward
part of your cingulate fire, but you're not sure what causes it to do so.  You get reward for some actions, so you take more actions like those.

In a sense, an invariant representation is a Platonic form.  For any cortical area (cingulate or not), there's some stimulus that maximizes the
area's response.  For example, I remember seeing an experiment where scientists measured the firing rate of a particular cortical area of a
particular monkey.  This area fired lightly when the monkey was shown a cartoon drawing of a smiley face, it fired more heavily when the monkey
was shown a photo of a human's face, and even more heavily given a monkey's face.  I wouldn't be too surprised if the area fired even more
heavily when shown a particular monkey's face (say, the monkey's grandmother) in a particular configuration.  Likewise, areas of our cingulate
might fire strongest (producing the highest reward, punishment, or other base emotional response) for some particular stimulus.  It's our goal
to figure out what that stimulus is (for reward) and how to make that stimulus occur as often as possible.

Even if my theory isn't correct, and this isn't what the cingulate does, but there must be some structure that encodes an invartiant reward (and
other emotional primitives).  Judging by its connectivity with the hypothalamus, I'm putting my money on the cingulate.  I doubt the
hypothalamus itself has the necessary structure to encode an innate representation of social power, for example.

## Some Strategies for Maximizing Reward
[#]: )))(((

TL;DR: This further details how the hill climbing search might work.

***

Some sort of reinforcement mechanism is still at play in the human brain.  It might be an obsolete relic from the time before people evolved
their higher cognitive capacity, but this mechanism is so basic, and has been with us so long (since before we were mammals), that it's still
heavily entrenched in our nervous system.  The mechanism I'm referring to is basic reward prediction in what psychologists call "classical
conditioning".  This is where a stimulus (such as bell ringing) occurs right before a reward (such as food) is given.  Psychologists (and dog
trainers) found that animals (and people) eventually associate the stimulus with the reward itself.  It's as if Pavlov's dogs eventually
associated the bell itself to be almost as good as food and would take actions to *hear the bell*.

Researchers working with animals and rewards have learned a few things about how this reward feedback works in animals.  To make this concrete,
let's say (hypothetically) that we have a laboratory with a bunch of monkeys, some crack (and crack-pipes), a cattle-prod, and a huge pile of
dirty dishes.  Suppose we show the monkeys how to use a crackpipe, so that they know what to do with it, and that we want the monkeys to wash as
many of the dishes as possible (we've also shown the monkeys how to wash dishes while smoking a crack pipe, quite a feat if you've never
attempted this FOOTNOTE{It's quite a feat for all 3 parses: Where the monkeys are smoking during the lesson, where the monkeys will be smoking
while they're washing the dishes, and where *you* are smoking during the lesson of teaching the monkeys to wash dishes.}).

There are a few strategies we could try:
1. The most fun-sounding strategy would be to cattle-prod the monkeys any time they take a break from washing dishes (or when they break the
   dishes), so that the monkeys associate not-washing-the-dishes with being zapped.  This is probably the least effective strategy.
2. In addition to prodding for not-washing, one could also give the monkeys crack for washing dishes, but the fact is that negative
   reinforcement (i.e., the cattle-prod) simply leads to the monkeys associating the whole process of dish-washing with zaps, which will cause
   them to try to escape.
3. Another strategy is to give the monkey a tiny crack rock for every dish that they wash.  This will cause stacks of shiny dishes.
4. Finally, there's a strategy that's even more effective: for every dish that a monkey washes, roll a 20 sided die, and if the monkey rolls a
   20, give the monkey a sizable crack rock (say about 10 times the size of the tiny crack rocks used in the previous strategy).  This strategy
   will have the dishes cleaned at top monkey-speed.  The reason this works is that doing any dish could potentially be worth a big crack rock.
   The randomness ensures that the big-crack-rock dish could be the very next dish at any time.

The phenomenon of the last strategy might explain why some people can spend an entire day in front of a slot machine at a casino, why one might
repeatedly check their mailbox while expecting the next Victoria Secret catalog, why one might do the same with email.  This phenomenon might
also explain why surfers will spend entire summers on the beach waiting for "the perfect wave", or why people will play hand after hand of the
card-game Pinochle waiting for the perfect "1,000 Aces" hand, or why sport-fishermen will spend all day with their lines in the water waiting
for "the big one", or any number of analogous activities waiting for a *Holy Moment*, those rare, but immensely rewarding windfalls.

# Shortcutting Heuristics: Artificial Sweetener, Drugs, and Virtual Reality
[#]: ))))((((

TL;DR: [FIXME]

***

[#]: cognitive "hacks"

**Artificial Sweetener** FOOTNOTE{I'm not sure if insects' mechanisms for sensing sweetness are fooled by some of the same tricks that ours are.
I once did an experiment with ants, giving them different types of sugar substitutes and sugar itself.  The ants went for the normal sugar, but
showed little interest in any of the artificial sweeteners.  For us, it seems that the external chemical properties of artificial sweetener (as
far as what the molecules bind to) is similar to that of sugar, but the artificial sweetener just doesn't have the hydrogen bonds (energy) that
sugar has.} by William Christopher Krueger I, 2008
```quote
Once upon a time, there was an ant colony out traipsing for food.
Its nature beckoned it to gather resources to fulfill its purpose.
It befitted the colony that an inexhaustible mound of sweetness lay due north.
In eerie compliance it was deemed of worth to venture there.

The colony arrived at the spot, antennae flitting about frantically.
Scores of ants began to divide the miracle, each fraction either delivered home or devoured.
And thus ants went on living, from colony to colony, off of this pile of pearls.
The ants once engaged however grew thinner with each return trip.

And also once engaged, the ants returned to the Mound with greater and greater urgency.
Amid scurry, deaths flowered.
The Mound, now littered with corpses, gleamed as sweet as ever.
It was made not of sugar but of artificial sweetener, its lack of substance indistinguishable to ants.
```

***

For our rabbits, mounting the wrong end might not seem like that big of a mistake because it feels good.  But, as the programmer, I'm aiming for
some ideal "meaning of life" for the rabbits.  So for me (who wants to win at Hare Wars) the rabbit mounting the wrong end is a "bug" in the
rabbit's design.

--

If happiness were a person's only goal, they might be tempted to enter a virtual reality, in the same style as in the movie The Matrix, and
never leave.  They'd be having no effect on the world, and people who tend to do that (like people who tend to become addicted to alcohol) get
weeded out of the gene pool.  As the designer of the rabbit, I'd want to prevent this from happening.  Has anything like this ever happened in
evolution?  A hungry person can imagine a hamburger, but there's something that prevents us from getting reward from just imagining eating.

--

There are all kinds of other computational "bugs" found in nature: army ants can follow each other in a big circle until they all die of
exhaustion, goats can eat all the vegetation on an island (causing it to be barren) and then starve to death.  There's the example of the Sphex
wasp described in Godel, Escher, Bach, where the wasp is shown to run an obviously simple routine.  I also view monkeys spanking their humans
(and vice versa) to be along these lines.

--

In filial imprinting, goslings follow the 1st big thing that moves.  In evolution, this worked most the time and was a simple solution.
Evolution lacks any form of foresight, so since this solution was easy and it worked, it's the solution that evolution went with.  Evolution
didn't anticipate wily scientists like Douglas Spalding, who discovered imprinting, or Konrad Lorenz, who exploited the geese's nature to make
them think their mother was a toy wagon.

***

Mainly due to technology, the environment that people live in now has a number of significant differences from the environment in which we did
the bulk of our evolution.  In fact, Wrangham and Peterson argue that, until the last 6 million years (or 300,000 generations, which is not a
long time, on an evolutionary time scale), our environment was somewhat similar to the natural environment of modern chimpanzees.  Evolution
didn't anticipate birth control, such an abundance of fatty foods (via agriculture), video games, heroin needles, or internet pornography.

***

If the meaning of life is reproduction, why do so many people not want children?  During evolution (and now), having kids itself was actually a
pretty weak urge because people didn't make the connection between sex and procreation until recently.  The bigger urge is for sex.  That is,
until the invention of birth control, the desire for kids was subsumed by desire for sex.

***

> For Moral Virtue has for its object-matter pleasures and pains, because by reason of pleasure we do what is bad, and by reason of pain decline
> doing what is right (for which cause, as Plato observes, men should have been trained straight from their childhood to receive pleasure and
> pain from proper objects, for this is the right education).
>
> --Aristotle (384-322 BC), The Ethics


Why we don't naturally find pleasure and pain in the right objects?  Is it all just a result of evolving in a different environment from which
we're now surrounded?  For example, why isn't hard work fun?  If hard work were so good for our well being (and presumably evolutionary
fitness), then wouldn't we have evolved to enjoy hard work?  Or maybe that's just the definition of work: something that's useful for us that's
not naturally enjoyable.

Likewise, one might ask why everything that tastes good is bad for you.  Well, it's not bad for you.  It's actually good for you in small doses.
If eating carrots felt as good as eating candy, then people would eat a lot more carrots, and there'd likely be some chronic problems with
eating too many carrots.  For example, candy is actually very healthy and nutritious.  It's just that *too much* candy is unhealthy.  In our
chimpanzee days, it was rare for the environment to give us too much candy (or calorie-dense food), so we didn't need to have an innate check on
how much of it we ate.

***

A question from "The Book Of Questions" goes like this: "If you could spend one year in perfect happiness but afterward remember nothing of the
experience would you do so?".  My answer is that happiness is never a goal in itself.  Rather, like our rabbits, it's evolution's means to get
us to reproduce.  There are scenarios where you get to keep the fruit of your happiness: relationships, knowledge (though this is probably not
kept, according to the question), babies, etc., which I might go for.  But I think the question means the scenario where you keep none of that.
The year's just clipped out of your life (and you're a year older).  If this were the case, and all else were equal, the rabbits that chose to
be (re)productive during the year instead of "living in perfect happiness" would be the rabbits that would tend to be around.  So we'd hope that
our rabbits' designs would cause them to choose not to take the amnestic year of happiness.

***

The need to always be falling forward is strong, so there are a lot of Artificial Sweetener versions of it.

For example, it's easy for me to spend countless hours playing the computer game called Civilization II.  In this game, you govern a
civilization, and you can expand your empire, develop new technologies.  You can also build new cities and create improvements to them, such as
city walls, and you can create World Wonders, which improve the "greatness" of your civilization.  Like many video games, Civilization II had a
good deal of "leveling up", where your character or civilization keeps improving its "level".  Once you've gotten your civilization going, the
game can become quite addictive.

The games designer, Sid Meier, was asked how he made the game so addicting.  His answer was that he tried to make the game so that there was no
good stopping points: he designed it such that you're always on the verge of completing a new city-improvement or a World Wonder, or discovering
some new technology, and by the time you finish that, there's some other improvement that's just about to finish.  These are all *urgent*, but
if we pay too much attention to them, we neglect to do important-but-not-urgent things, like shutting the computer off and working on our
dissertation.  So Civilization II keeps us busy, and we might not have time to consider whether we're the *right kind* of busy.

Likewise, jigsaw puzzles, collecting beany babies, and solitaire make us *feel* like we're making progress on something without really
accomplishing anything real.  But don't we gain something from playing Civilization II or playing solitaire?  They're thinking games, so we gain
some skills, right?  Well, yes, but there's a point of decreasing returns.  I've spent over 100 hours playing Civilization II, while everything
I learned playing this game could have been compressed into just a few hours.  I can't help but think that those 100 hours could have been
better spent.

## Habits and Pain
[#]: )))(((

TL;DR: [FIXME]

***

Pain killers can be a form of artificial sweetener.  Pain has an evolutionary purpose.  Physical pain can be a way of knocking a person out of a
damaging rut or habit.  For example, if you're right handed and break your right index finger, pain will serve as a "reminder" to not use that
finger and you'll fairly quickly learn to substitute your left hand for tasks such as zipping up your jacket.  So, pain prevents you from
touching your finger when it's in the delicate process of healing.  It quickly breaks any habits that use that finger.  Many of these habits are
tacit in that you usually don't realize just how much you use that finger in your day-to-day activities.  But if you use pain killers, that
"reminder" will be thwarted, and your finger probably won't heal as quickly.  (That being said, there are cases where our pain "notification
system" itself malfunctions.  When this happens, the message doesn't fit the damage, and painkillers would be useful.)

***

Evolutionarily, pain doesn't seem to make sense if there's nothing you can do about it.  The purpose of pain is to cause a change of action (to
lessen the pain).  For example, male emperor penguins stand for a few months during the Antarctic winter incubating their female partner's egg.
During this period the male doesn't eat anything, as there's no food available as far as the males are away from the sea.  I doubt that these
penguins feel hunger during this period because this process is an established part of the penguins' life-cycle, and there's nothing the
penguins can do about it.  If the penguins felt hunger, they might be motivated to fruitlessly search for food, wasting energy.  I do think that
it'd make sense for the males' systems to provide a heightened negative reward for physical exertion or being overly exposed to the cold and
wind, since calories are at a premium.

***

Why does a tragedy, such as the death of a loved one, cause a mourning period?  There's the reinforcement aspect of classical conditioning,
where you try to avoid situations that caused the pain.  For example, if you're learning to ride a bike you might find yourself in a situation
where you're tilted far to the right side.  You try turning right, you crash, and you learn not to turn to the right when you're tilted far to
the right.  You try again, you find yourself again tilted far to the right, you try turning left, and you crash again.  Your conclusion is to
avoid being tilted far to the right.  Likewise, with the death of a loved one, you might try to avoid the deaths of other loved ones.  This is
one purpose of pain, but emotional pain might also cause "adjustments" at a more cognitive level.

With physical pain, such as a broken bone, the pain also prevents you from messing with the bone so that it can heal.  But maybe there's
something more to a period of depression.  Perhaps you use the period as a cognitive restructure, or to "reprogram" to adapt to the change and
modify the parts of your worldview that are no longer valid as a result of the tragedy.  For example, suppose a close confidant dies.
Confidants are useful for giving an outside perspective on problems, and now a person has to either find a new confidant or get into the habit
of providing their own counsel.  Similarly, if a person has a powerful friend who dies, they can't rely on that friend's support, and must get
into a habit of acting less boldly.  Similarly, if a man loses an arm, it would be useful for him to quickly extinguish habits and assumptions
that depend on that arm.  Many of these habits are tacit in the sense that we don't even realize that (e.g.) we use our arm when washing our
hair in the shower.  (If this were the case, wouldn't we have a similar period for a windfall, which is also a major change that could use some
adaptation?  Maybe the "adjustment period" is less crucial after a windfall because a windfall only expands what you can do, so old habits
aren't actually harmful.)

In general, it seems that pain is a way to modify behaviour.  More specifically, it seems like pain is a way to break habits, both cognitive and
behavioral.

## Hedonism
[#]: )))(((

TL;DR: [FIXME]

***

> Junkies are not interested in sex and they have no interest in other people except as suppliers of junk.
>
> --William S. Burroughs (1914-1997)

If a Reinforcement Learning agent is simply trying to take actions to maximize its reward signal, then wouldn't this lead to hedonism (the
philosophy that attainment of pleasure is the goal of a person's life)?  It's true that a good number of people view pleasure as the ultimate
goal in life.  Certainly rats do.  If you hook electrodes up to a rat's brain in such a way that if they push a lever it stimulates their
"pleasure center", the rats will keep pressing the lever until they die of starvation or exhaustion.

The word "hedonism" may bring bacchanalian orgies may to mind.  We usually think of this word in the sense of *immediate gratification* of
*sensual pleasures*.  If we view hedonism in this sense, then it's not necessarily true that a Reinforcement Learning agent would be a hedonist.

1st, we would probably want our rabbits to be able to put off immediate gratification for (a larger) long-term reward.  This would make sense
evolutionarily, and it makes even more sense for people (who have better cognitive abilities to make predictions about the future).  By
associating the predictor of a reward with the reward itself, classical conditioning can give our rabbits some of this ability to delay
gratification.  But classical conditioning is a slow learning method.  So, our cognitive system (as described in **Will: Interaction of
Cognitive System and Reward System**), which is good at making predictions, often needs to take over.  A person's cognitive system will often
"disagree" with the limbic system about which actions to take.  A person (for example, a junky) may cognitively know that action A (not shooting
up heroin) will be better in the long run, yet still do action B.  The philosophy of hedonism will cause a person to always choose their limbic
system over their cognitive system.

2nd, it'd make sense if our innate set of rewards included some that wouldn't be described as sensual and thus wouldn't fall under the usual
rubric of hedonism.  For example, curiosity and social acceptance.  Of course, it might be possible to learn these "abstract" rewards since
they're "derivable" as corollaries from the lower level rewards, but this would take a long time in a being's life, and it'd make sense to
"bootstrap" the agent by having some of these rewards be innate.

***

>  Take the best orgasm you ever had, multiply it by a thousand and you're still nowhere near [the feeling of being on heroin].  When you're on
>  junk you have only one worry: scoring [more junk].
>
> --From the movie Train Spotting (1996)

Evolutionarily, beings that found pleasure in ultimately procreative acts are the beings that procreated (and are around today).  So, although I
believe there's some truth to the above quote, I still wouldn't want to do heroin because I know that the outcome (in terms of pleasure) is
actually worse in the long run.  Most heroin or crack addicts aren't in enviable positions.  Even if the pleasure were guaranteed to be maximal
if I took the drugs or VR helmet, my pride gets in the way of letting me do it if I know it's fake.  Drugs and VR certainly weren't anticipated
by evolution.  I don't know where this pride comes from though.

***

A Gedankenexperiment: Suppose you were virtually omnipotent (or you had the genie from the **Walking = Falling + Catching** section).  Wish
almost anything, and your wish is immediately granted.  Design your life however you want to.  The catch is that (like in the movie Click) you
don't get to *experience* any of it.  You just zoom right to your deathbed where you get to reflect on your life.  Suppose you had the choice to
have this power, would you choose it?  (I don't even know if I would.  It'd feel like I was designing someone else's life.)  Suppose you weren't
given a choice and you had to do it.  Consider now, that (if you're lucky) some day you will be 80 years old and lying on your deathbed
reflecting back on your life.  What would you do then?  I imagine I'd forget about pleasure and just try to maximize my legacy.  Certainly,
rabbits that tried to maximize their legacies would have more legacy than those that didn't.

# Economics and Ethics
[#]: ))))((((

TL;DR: [FIXME]

***

As I mentioned at the beginning of **Enter Complexity: The Peacock's Tail**, the mantra "Eat.  Survive.  Reproduce." sounds too trivial to be
the answer of the meaning of life.  But hidden in this mantra is a good deal of what economists call Game Theory.  This is where multiple
"agents" (e.g., people) partake in a "game" and are trying to maximize their utility or reward.  Evolution has structured our "reward" such that
maximizing it tends to maximize reproduction (see the sections in the chapter "Taste" about how this reward is specified).

A classic example from Game Theory is called Prisoner's Dilemma.  The situation is that there are 2 captives accused of a minor crime, and
they're put into separate rooms and both are offered this deal: "If neither of you confess to the crime, you'll both get 1 year in prison, but
if you confess and your partner doesn't, you'll get off free, and he'll go to jail for 5 years (and vice versa if he confesses and you don't).
If you both confess, you both get 3 years in jail."  Assuming the partners don't care about each other, no matter what the other guy does, each
partner will be better off if he confesses.  But the "tragedy" here is that both partners will confess and both serve 3 years, when they
could've gotten just 1 year each.

Prisoner's Dilemma can get more complex.  Suppose that instead of years in prison, the captives have to pay a fine of a mere dollar for each
year they were to serve.  The catch is that they have to play their game 100 times in a row, knowing what the other has done in the past.
Furthermore, suppose each captive will play this new game, Iterated Prisoner's Dilemma, against each of a large group of other captives.  On the
face of it, it seems like each captive should always "confess", but it turns out that a strategy called "tit-for-tat" will yield a prisoner a
smaller fine than always confessing.  Tit-for-tat is simply starting out by "cooperating" with the person with whom you're playing (i.e., by not
confessing), then doing whatever he did the last time.  If he screwed you over on the last round, you screw him over this round.  The
tit-for-tat strategy will never gain the most against any single opponent in a single round, but it tends to yield high-scoring games.  So if A,
B, and C are playing each other and A and B are tit-for-tat, but C always confesses, and 100 rounds are played amongst each of the 3 pairings,
the final score will be that A and B are both fined only $402, while C owes a fine of $594 FOOTNOTE{When A plays B, both will cooperate every
time and each will get a fine of $100.  When C plays A (or B), C will confess in the 1st round, giving A a $5 fine, but both will confess for
the remaining 99 rounds giving C a fine of $297 and A a fine of $302.}.

These types of games can get arbitrarily complex, and they can quickly push the limits of human intelligence.  There are volumes of books
written on Game Theory, but I'll just touch on a few of the relevant ideas in this memex.

***

Game Theory assumes we have a utility function.  Real life isn't as straightforward as this.  Because of their limited computation power, this
isn't always clear cut for our rabbits.  In fact, our rabbits probably won't have a single utility function.  A utility *vector* might be more
accurate.

At least one concept from Game Theory is useful here: a *Pareto Optimality*.  Suppose you have no way of comparing apples and oranges, but you
know that more apples is better than fewer apples and more oranges is better than fewer oranges.  Suppose you have the following situations:
* **A** 3 apples and 3 oranges
* **B** 3 apples and 4 oranges
* **C** 6 apples and 8 oranges
* **D** 9 apples and 7 oranges

Clearly, situation B is better than situation A because we have an extra orange.  We say that situation B *dominates* situation A.  Both of
situations C and D dominate (are better than) situation B.  But what about situation C vs. situation D?  Situation C has 1 more orange, but
situation D has 3 more apples.  Are the 3 apples worth the loss of the orange?  We can't compare them.  Of these 4 situations, there's no
situation that dominates either C or D, so we call C and D our "Pareto Optimal set", the set of situation that aren't dominated.

--

We could say that utility is ultimately reproduction, and those actions that will cause you to be around (i.e., reproduce) are desirable, but
some situations are like rock, paper scissors: what causes you to be around depends on what everyone else is doing.  For example, if everyone
tries to exploit the same niche, then it won't be useful to try to exploit the niche.

***

One can derive much of ethics by applying Game Theory when there are multiple players.  For example:

>   RISK is interesting because when you have more than 2 players, "governments" emerge.  The fundamental philosophy in RISK is "Macht macht
>   Recht." or "Might makes right.".  Ultimately, someone *will* end up conquering the world.  Andy can make verbal treaties with Gabe, but it's
>   not in the rules that they need to abide by those agreements.  However, a "government" emerges when Andy becomes more powerful than me or
>   Gabe, but not more powerful than both of us together.  At this point, Gabe and I will realize that we're both doomed unless we might
>   cooperate by forming a pact to pound on Andy at least until he's not so powerful.  There's nothing in the rules of the game to prevent
>   either player breaking the pact though.
>
> --From Europe Debris, **Day 10**


***

Since people are social creatures in a cognitive niche, developing relationships consumes a good deal of our time and cognition FOOTNOTE{The
fact that we're both social creatures and that we're in a cognitive niche isn't coincidental.  Many of the smartest creatures: dolphins,
primates, and African grey parrots (arguably the smartest of the birds) are social.  There's a book called The Red Queen which argues that a
good deal of human (and other social species) intelligence is driven by an escalating cognitive arms race.  Basically, people were trying to
outsmart other people.  Then, the bigger brained people reproduced more than the dumber people and the intelligence level for the whole group
rose, meaning that the successful people of the next generation had to be even smarter.  (It's like the Red Queen's race in Alice in Wonderland
where the earth moves backwards as fast as the sprinters move forward so that the net gain is 0.)}.  Our (largely tacit) ethical drives are from
a mix of culture and genes.  I don't know how much of our "social desires" are encoded in our genes as innate Will.  Certainly, much of our
ethical drives are learnable, being derivable as corollaries from our more fundamental Will, but I wouldn't be too surprised if people had an
innate Will for power, for example, though it could be tricky to encode this in terms of squiggly lines.

***

Question 99 from The Book of Questions posits the hypothetical scenario: "You are driving late at night in a safe but deserted neighborhood when
a dog suddenly darts in front of your car.  Though you slam on the breaks, you hit the animal.  Would you stop to see how injured the animal
was?  If you did so and found that the dog was dead but had a name tag, would you contact the owner?".  Even if there was no consequence (i.e.,
you're sure no one will know that it was *you* who hit the dog), there's motivation to stop to see how the dog was, and to contact the owner.
What good does it do you to do so?  It could be that if you simply have habits of character to do good (i.e., what's good for other people),
then you'll establish a reputation for this, which is good for you.

# Atomic Waves and Platonic Forms
[#]: ))))((((

TL;DR: [FIXME]

***

[#]: A couple notes:

1. Ship of Theseus: Many philosophical quandries can be resolved by "mu", that they presume e.g.  binary attributes ("it's either the same ship
   or not").
2. The way we carve up the world is at least in part affected by information theory.


[#]: Even for materialists, not everything is matter.

[#]: People, minds, and the meaning of life "exist" in a Platonic realm
[#]: The Meaning of Life is really just an abstraction
[#]: The concept of self is fuzzy

To say that we're all just collections of atoms is oversimplifying things.  An average human body has about 6.7 octillion atoms: Hydrogen,
Oxygen, Carbon, Nitrogen, Calcium, Phosphorus, Sulfur, and less than .1% each of various other elements.  One fact that this oversimplification
is missing is that not just any lump of the proper amounts of these elements will make a person.  In fact, you need very specific compounds in
the right order to make anything that we could call a person.  A 2nd fact that the oversimplification overlooks is that you can replace the
atoms in a person 1 by 1 and still wind up with the same person.  In fact, the cells in our bodies are constantly being replaced.  A person is a
*wave*, a self-reproducing form.  It's the same as if you wag the end of a chain and watch the ripple flow down along the chain.  The wave in
the chain isn't the individual links, but the motion that you created with your wag.  Likewise, a person isn't really the individual atoms that
make him up, but rather the *pattern* that the atoms make up.  The point of all this is that at the atomic level, a person doesn't exist.  What
we call "a person" is just shorthand for a particular "wave" of atoms.

Since a person doesn't exist at the fundamental level of the universe, the meaning of life for a person doesn't exist at that level either.
Atoms simply obey the laws of physics.

But people *do* exist in 2 senses.  The 1st is that the concept of a person is a useful abstraction for describing a particular wave of atoms.
The 2nd sense is deeper.  Consider the concept of a circle.  There is a mathematically precise formulation of this concept (a set of points on a
plane that are all a certain distance (the radius) from another point (the circle's center)).  However, approximations to circles are frequent
in nature: the iris of our own eye, the disk of the moon, the cross-section of a tree, the orbital path of a satellite over Earth.  Although
perfect circles are rare or non-existent in nature, an elegant ideal "exists" in the realm of ideas.  The equation for a circle and the
computation for the related value of $\pi$ are the same on Earth as they would be for intelligent beings billions of light years away.

Elegant ideals "exist" for more complicated concepts: ellipses, parabolas (which the lenses of our eyes approximate), gases, and perhaps
machines and chemical compounds.  Certainly some algorithms, such as the computation of an average, exist in the realm of ideas.  In the same
vein, I believe cognition (which is really just an algorithm) must "exist" in an ideal form (this idea is explored more fully by Hoimar von
Ditfurth).  I see no reason why this shouldn't be the same for people and for the meaning of life.

Maybe the concepts of mind and happiness are "out there" in the same sense that the number $\pi$ exists independently of people.  They don't
really exist in pure form, but something is trying to approximate them.  Or maybe these pure concepts are the minimum distance from all the
approximations (i.e. the actual examples).

Another thing to keep in mind is that ideal forms can be independent of a substrate.  For example, a lens can be made out of glass, fiber cells,
or even diamond.  Likewise, the substrate of computation can be silicone, mechanical parts, or even neurons.

[#]: We describe computation independently of its implementation: it could
[#]: be electrons in silicon, neurons, or even tinker toys.

***

In a sense, a genetic line (such as humanity) is a wave too.  If a person is simply a wave of atoms, then is there a difference in the type of
existence for a person and the type of existence for a genetic line?

Culture, in the sense of information passed down through generations of people, is also a wave.  In fact, there are cultural memes (such as an
evangelical religion) that are "infectious" and self-reproducing as viruses.  So, on some level, isn't a *culture* existing as an entity as much
as a person exists as an entity?  For that matter, I don't know that a physical object, such as a pen, *isn't* a wave.  Electrons and other
subatomic particles can be viewed as waves, so why not objects made out of them?

***

Here's a seeming contradiction in basic philosophies that I haven't resolved yet:

A chihuahua seems to be a living contradiction.  People have bred chihuahuas to be something that probably wouldn't exist in nature otherwise.
The dogs are so small that they constantly shiver unless they're in a very warm room.  (I remember someone saying that her chihuahua was "too
small for its body".)  I escape from this "contradiction" by saying that the chihuahua doesn't actually exist.  It's just a collection of
molecules in a particular formation, and there's nothing about that formation that's against the laws of physics.  You can resolve all sorts of
"contradictions" and escape a bunch of philosophical arguments (such as ones concerning abstract ideas such as "freedom") by taking this stance.

So the 1st idea is that "The universe is just a computation.".  (It could be Stephen Wolfram's Rule 110 CITE{wolfram:2002}, a program running on
a Turing Machine, or a bunch of atoms (or quarks or strings or whatever the primitives are) interacting.)  Any objects beyond that are human
constructs or abstractions.  I wouldn't doubt that there's some principled way of making that abstraction, but, under this framework, chihuahuas
don't really exist.  (I might call this "raw materialism".)

On the other hand, there's the 2nd philosophy: that the concept $\pi$ exists independently of matter, and that soap bubbles "try" to approximate
an ideal sphere.  So ideas and Platonic forms exist outside of matter, which seems to fly in the face of raw materialism.  Also on this side of
the debate is the idea of waves.  A traffic jam "exists" independently of any of the cars in it.  You could even say that a chihuahua is a
"wave" since its cells are constantly being replaced.  We can say a chihuahua is like Granddad's axe, which has had 5 different handles and 3
different heads, but it's still Granddad's axe.  The same wave can exist on different mediums.  For example, I could take some computational
process running on a computer, suspend it, write the relevant memory to disk, then restart the process on a different computer, or on some weird
computer that uses millions of trained crack-monkeys to do its basic logic-gate operations.

I don't know enough about physics to say, but it seems that there's the physical universe and the rules by which the physical universe abides.
The latter might be called an idea-system, and the former might be an *instantiation* of the idea-system.  It's possible that the rules of how
an electron behaves are somehow inherent in the electron itself, but for now I'll assume they're separate.  It's also possible that there's only
a single possible starting configuration of matter in the universe, but for now I'll assume otherwise as well.  Thus, at some level, ideas (such
as the idea of a circle) exist independently of matter.  There's still the question of how an idea-system gets instantiated.  If I ran a
simulation of a miniature universe on a supercomputer, I have little doubt that the "beings" that evolved in it would feel as real as I feel
because everything it interacted with would be as "real" as it was.  "Infinitesimal objects have real significance when viewed through
infinitesimal eyes."

# Designing your Successor
[#]: ))))((((

TL;DR: [FIXME]

***

> What, then, when an agent can best bear The Will be steering the creation of a new agent?  The Will is to reach ultimate existence.
>
> --HElmut neeman (aka Marc Pickett I), The Will (1998)

In our rabbit Gedankenexperiment, Hare Wars, we assume we know what one of our rabbits is, but a rabbit is simply a collection of atoms (an
atomic wave).  It's not always clear whether an animal is one of our rabbits.

For example, suppose our rabbits figured out how to genetically modify their offspring so that they could metabolize sunlight (while giving up
none of their current abilities).  This might sound like a good thing to do (in our eyes) because a rabbit that can metabolize sunlight surely
has a higher survival and reproductive potential than one that can't.  But suppose that in modifying their genes, they end up having the same
sequence as the rabbits of our competing player of Hare Wars.  Would we want our rabbits to do this then?  Would they still be *our* rabbits.

Another way to look at it is to consider if you could genetically modify your offspring.  What if "the best" doesn't resemble you at all?
Should we have a directive that our offspring be like us, or would the directive to produce "the best" offspring win out?  If the meaning of
life is to reproduce, *to make things like you*, what about genetic engineering?  For example, if through genetic engineering, I could make my
child smarter, I might do this (and presumably, the child would have a better chance of survival).  However, this means that I'd be making a
child less similar to me than I would without the genetic engineering.  This seems to be a paradox, "The best way to reproduce is to make
offspring that are dislike yourself.", and we need to delve into a deeper level of complexity to resolve it.  Maybe, I'd have to define "me" as
something more general than my gene sequence.  Maybe part of me is the cultural idea of making greater beings (and this would be passed on)...

Finally, what if we can build robots that are bigger, stronger, faster, and smarter than us.  Would it make sense for these to become our
descendents?  What about if we could upload our consciousness to a machine?  For example, we could replace our neurons one at a time with
functionally equivalent silicone circuits.

***

What constitutes a "self"?  E.g., would you rather be like a bacterium and have 1000s of tiny offspring, or like a whale and have a few huge
offspring?  Since a whale is billions of cells, does a single whale count as millions of bacteria?

In Hare Wars, suppose my opponent made rabbits so tiny that a single carrot could feed thousands of them.  Would he win since he has more
rabbits, or should the measure we use be the total mass of all our rabbits?

***

If our goal is to spread our genes (as in The Selfish Gene CITE{dawkins:1976}), what about replicating our "junk" DNA?  Well, this isn't useful
because if the junk DNA is truly junk (i.e., it has no phenotype), then it hasn't caused its own replication.

***

Initially, all life was unicellular creatures.  We are really just waves of a group of cells, and a culture is a wave where *we* are the medium.
A culture is, in a sense, an organism that can reproduce.  What level do we look at when we say we want to reproduce?  If a cell reproduces too
quickly in our bodies, *it* is successful, but this process, cancer, is never good for us.  Likewise, cultural memes can compete with individual
reproduction.  For example, a culture that causes people to adopt African babies would spread itself because the adopted babies would learn much
of their foster parents' culture, including whatever habits of thought led them to their decision to adopt the African babies, but this culture
would be detrimental to the individuals' genetic reproduction because they won't have as many resources for their own biological children.

--

A "cultural organism" should be mostly unconcerned with what its medium is made out of, just as a biological creature should be mostly
unconcerned about the cells that make it up.  A cultural organism should only be concerned with these as far as its survival is dependent on
having hosts and how different hosts have different effects.

# Entropy: A Petri Dish Falling into a Volcano
[#]: ))))((((

TL;DR: [FIXME]

***

A rabbit's success is not measured by how many children it has, but better by how many grandchildren it has, even better yet by how many
great-great-great-...grandchildren.  This is another complicating matter for the mantra "Eat.  Survive. Reproduce.".  It's not about simply
having as many babies as possible, because you need to provide for these babies so that they can have babies as well.  However, if entropy is
unstoppable, then this number (at infinity) is 0 *no matter what the rabbit does*.  This would mean that the success rate of *all* rabbits is
the same.

This is related to a question I've been thinking about for at least 12 years, and to which I haven't found a satisfactory answer.  "What would
you do if the Earth would end in 1 year?"  In a sense, it doesn't matter what you do because the same outcome happens.  But the answer can't be
that life has no meaning.  You *must do something*, and there has to be *some* criteria on which to base your decisions.

Suppose you have a petri dish full of bacteria that's falling from a high altitude towards a volcano, such that when the dish hits the lava, it
and the bacteria will all be destroyed.  The bacteria don't have any means of escaping.  What should the bacteria do?  What will the bacteria
do?  Well, they'll probably keep doing their thing exactly as if they weren't falling toward a volcano, eating, surviving, and reproducing.  The
bacteria that have the *tendency* to dominate the petri dish when it hits the lava will be those most likely to be those that are around when
the dish actually hits the lava.

--

There's a card game called Falling Down.  In this game, each player is falling from the top of a tall building, and the goal in the card game is
to hit the ground last.  The game's tag line is "It's not much of a goal, but it's all you could think of on the way down.".  This is
essentially the same situation as the bacteria in the petri dish.

The game Falling Down has another parallel with life in that, in life, you don't have "pre-game" time to think about what to do with life.
You're thrown into life already taking actions.  You can think, and you can act, but you can't "pause" the game to think about what you're going
to do.  Thinking is acting.

***

If I knew everyone would die in a nuclear war in 1 week, in a sense, it wouldn't matter what I did, because the rubble and ashes that would be
left wouldn't be that different no matter what my actions were.  Furthermore, no one would be around to care about any differences.

My abstraction of the meaning of life ("Eat. Survive. Reproduce.")  doesn't handle this case.  Therefore, I have to step back a level (or reason
using a higher level of complexity and jump back to the "sequence of events" level).  One could say that my life would be ultimately
meaningless.  My response to this is summarized by the following quote:

> Infinitesimal objects have real significance when viewed through infinitesimal eyes.
>
> --HElmut neeman, The Will (1998)

What I mean by this is that we always have to do *something* (even if that means sitting around doing nothing).  It's impossible to not make a
decision, because even sitting around thinking is doing something.  Therefore, there must be some criteria for deciding what to do.  These
criteria amount to what I call The Meaning of Life.

So, if it doesn't matter one way or another, then you "step down" to the next level of decisions.  You fall back to your heuristics.  Our Will
is actually a heuristic.  From a cognitive point of view, people probably aren't born with a full world model.  Even with my current world model
and an explicit goal of reproducing, I don't know what would cause the most offspring (or great-grand offspring).

People have much better reasoning capabilities than rabbits, but we still have our heuristics.  When "the ground" is gone (i.e., when your
actions can't affect the ultimate outcome, as in the nuclear war scenario), all you have is the heuristic.  This heuristic is what causes
artificial sweetener to taste good.  Artificial sweetener isn't actually nutritious, but it tricks our taste buds into "telling" us that it is.
This heuristic also tells us that protected sex or masturbation feels good, even though it doesn't increase our reproductive fitness.  (This is
also related to the "tricks" of the Bumblebee orchid described in the section on "Squiggly Lines".)  This heuristic is also what causes people
to be fat, since eating all available high-calorie foods *was* desirable 100,000 years ago because of those foods' limited quantity.

I never view pleasure as an end in itself, but as a manifestation of this heuristic.  This extends to reading.  Although I enjoy reading, I view
its actual purpose as acquiring knowledge, which is generally useful.  However, the day before Hermann G\"oring was to be executed, he read a
book in his cell.  He'd obviously never be able to put that knowledge to use, but what else could he do?

So, in the case of nuclear war in 1 week, I'd basically be left with just my heuristic and the knowledge that nothing would be left in a week.
The idea behind delayed gratification is that your heuristic is overridden by rational thought.  But with only 1 week to live, the short term
heuristic takes over.  So, I'd predict that there'd be lots of sex, drugs, and goodbyes.  It'd be the wildest party ever.  There's also the
quote that "If you lived every day like it was your last, then you'd never do your laundry.".  So, I doubt anyone would do their laundry.  I'd
personally probably engage in lots of sex, but not drugs or alcohol, as I'd want to have a clear mind.  I'd also talk to strangers, and take
risks I wouldn't normally.  In a sense, there would be no strangers, we'd all be the human family facing a common doom.

If we knew that the nuclear war would be in 20 years, instead of 1 week, the heuristics in this case would be longer term, to "maximize my
utility" over 20 years.  This'd mean that I wouldn't work on the AI problem, I wouldn't worry about having kids, I might plan on developing a
drug habit (and doing all the other debauched things) in the last year.

***

At this point (and in Isaac Asimov's short story "The Last Question"), we still don't know whether entropy is reversible.  If this is the case,
then a default answer to "What is the meaning of life?" is to figure out how to reverse entropy (and thereby allowing us to survive and
reproduce indefinitely). If entropy is not reversible, then we're the bacteria in the lava-bound petri dish.

## Nihilism
[#]: )))(((

TL;DR: [FIXME]

***

In one sense, the universe is dead.  That is, the universe is a collection of matter that is simply following the laws of physics, coldly
carrying out calculations.  For example, my brain, *the machinery for my soul*, is simply a collection of atoms, each of which is obeying the
laws of Chemistry.

A problem of Philosophy is whether it is possible to get "should" from "is".  That is, given a *description* of a situation, is it possible to
say how the situation should go?  Is there an objective measure for this?  In the universe, when you look very closely, there is only "is".
That is, an outside observer only sees a description of things.  We're all just a collection of atoms.  "Should" is an abstraction of things
that *are* (see "Atomic Waves and Platonic Forms").  "Should" is contained entirely within the universe.  "Should" is a property of our brains
which are contained within the universe, so we *can* get "should" from "is" simply by abstracting.  On the one hand, I can describe a cockroach
as a physical system, but on the other hand, it might be expedient for me to use the *abstraction* of Will and talk about what the cockroach
*wants*.

***

As in \meme{53}, if I ran a simulation of a miniature universe on a supercomputer, I would be able to describe the simulation as bits on the
computer, simply states of information, particular configurations in the computer's memory.  On the other hand, beings *within* the simulation
would find the "objects" in it very real (as real as they themselves were).  Even the idea of a "physical object" in this simulation is just an
abstraction for a particular information states.  There are certainly no objects in the computer's physical memory.  Nor are there colors,
though it might be useful to talk about the "red" chair in the simulation.  But "red" is really just a numeric value.  In the simulation, we
could probably call change the name of the idea that we had been calling "red" to "blue" or "forgnorp" even, and the simulation would still be
the same.  It's still all just states of electrons.

Likewise, biological life has arisen from *within* the dead universe.  The human mind and notably our Will are products of the universe, and
Will is entirely within our minds.  Thus, Will is *created*.

***

For any person (or robot) who is forced to take actions, Nihilism, the belief that life is meaningless (or that the meaning is arbitrary), is
impossible.  Every action must be based on some set of criteria, and *that* set of criteria is the meaning for that person.

A person can say I've *decided* that *my* meaning of life will be to paint everything green, but that decision was based on some criteria as
well.  Ultimately, these criteria ground out in a design created over millions of years of evolution, with the ultimate goal of reproduction (as
in \meme{1588}).

[#]: (Why is my meaning of life superior to painting everything green?)

[#]: Also, impossibility of taking action without dopamine.  Look up
[#]: Parkinson's and cases in Awakenings (are they unconscious when they're
[#]: not taking any actions?).

--

Finally, even if you're not convinced that there is a meaning of life, it would be hard to prove that there isn't.  Meanwhile, we can create AI,
which will help us determine whether there is a meaning of life, and if there is, it will help us fulfill it.

# Consciousness and Death (How a person never dies)
[#]: ))))((((

[#]: See also "Immortal" and Meme 1962

TL;DR: [FIXME]

***

Any discussion on the meaning of life would be incomplete without a mention of death.  Death is the cessation of consciousness or sentience.
Consciousness, sentience, and self awareness are related, but different.  We can say that a patient is conscious if they respond to their
environment.  A person is self aware if they are able to discuss themselves and reflect on their own thoughts.  Sentience is the most difficult
to define.  A person is sentient if they feel or are aware in the same sense that we are.  Sentience is possibly the most slippery concept I can
imagine.  This is because at once our own sentience is the fact that we're most sure of (Cogito, ergo sum.), and even if we accept our senses,
other people's sentience must be taken on faith.  It's nearly impossible to prove that *someone else* is sentient.  Even if we've proven that
another person's intelligent, they could be some automaton or zombie "acting" like they're sentient.

For this reason, I'm loathe to put a lot of thought into sentience.  My belief is that cognition will be easier to figure out because, though it
might be difficult to understand, cognition is at least tangible.  We can test whether a person or robot has some degree of cognition.  The
process of understanding cognition *may* lend some insight into our understanding of sentience.

***

> Every single person is a World, which is born and dies with him.  Under every gravestone lies a
> World's history.
>
> --Heinrich Heine (1797-1856)

What a tragedy when someone dies.  All that knowledge acquired over a lifetime, the entire tacit worldview, all gone to rot.  A million secrets
taken to the grave, synapses destroyed.

--

If sentience has an ideal or Platonic form (and I think it does), then I'm sure that this form isn't meant to have a finite life.  For example,
I can imagine a design for a cognitive system that's supposed to keep learning and predicting indefinitely.  If its World is complex enough, it
doesn't seem like this system would ever reach a natural stopping point.  80 years (or even 120) seems like much too short a time for a
cognitive system as complex as a human brain FOOTNOTE{It might be interesting to consider how much information a human brain can hold, and thus
what its "steady state" would be.  If people lived thousands of years (but had the same cognitive capacity they have now), there'd be some point
where forming new memories would mean losing old memories.  Except for significant events, a person's "working memory" might be just a few
decades.  It's hard for us to not remember where we were when we heard about the news of September 11th, 2001, but if we lived forever,
eventually this information would be drowned out by even more significant memories.}.

***


> The syllogism he had learnt from Kiesewetter's Logic: "Caius is a man, men are mortal, therefore Caius is mortal," had always seemed to him
> correct as applied to Caius, but certainly not as applied to himself.  That Caius -- man in the abstract -- was mortal, was perfectly correct,
> but he was not Caius, not an abstract man, but a creature quite, quite separate from all others. He had been little Vanya, with a mamma and a
> papa, with Mitya and Volodya, with the toys, a coachman and a nurse, afterwards with Katenka and with all the joys, griefs, and delights of
> childhood, boyhood, and youth. What did Caius know of the smell of that striped leather ball Vanya had been so fond of? Had Caius kissed his
> mother's hand like that, and did the silk of her dress rustle so for Caius? Had he rioted like that at school when the pastry was bad? Had
> Caius been in love like that? Could Caius preside at a session as he did?  "Caius really was mortal, and it was right for him to die; but for
> me, little Vanya, Ivan Ilych, with all my thoughts and emotions, it's altogether a different matter. It cannot be that I ought to die. That
> would be too terrible."
>
> --From "The Death of Ivan Ilych" (1886) by Leo Nikolayevich Tolstoy


> It is not I who will die but the world that will end.
>
> --Ayn Rand (1905-1982), when asked about death

I think of understanding one's own death as being similar to understanding consciousness.  Actually, understanding one's own death is
understanding the end of one's own consciousness (the only consciousness one is sure of).

We're all immortal.  This sounds farfetched, but consider this: We can never fully perceive our own death because our brain stops.  It's a
little like being unconscious, our experience goes from conscious period to conscious period.  For example, if we undergo general anesthesia
during an operation, we'll be aware of laying on the operating table, then the next thing we'll know is that we're coming to after the
operation.  We have no idea of how much time has passed.  When I was 11, I played the red-face game and passed out (kids, don't be as stupid as
I was).  I was out for only a few seconds, but it could've been years.  It was virtually the same as when I was put under for a minor operation
and came to almost an hour later.

We've all already "experienced" a period similar to death: the time before our conception, when we simply don't exist.

Suppose that my computer, Lappy, somehow became sentient (say by an implementation of my cognitive architecture called "The Marchitecture").  If
I suspended the Marchitecture process (I'm using "process" in the Operating Systems sense), then Lappy would cease to be conscious.  If I slowed
the process down, Lappy would just see the world going by faster.  I could even theoretically suspend the process for several millennia, and
Lappy wouldn't know the difference until I continued the process.  If I killed the process altogether, Lappy would be completely unaware of it.

When someone *else* dies, that person stops, but when *you* yourself die, the entire world stops, in a sense.  So our own death is quite
different from the death of other people.  Just as I don't know of a way to *prove* that anyone else is sentient, but I *know* that I'm
sentient.

So, fully believing and understanding that *I* will die is equivalent to fully understanding that *existence* will cease, which is pert near
impossible.  More to the point: a person is immortal himself because if *other* people die, the world goes on, but when oneself dies, the world
ceases.  So, there's no such thing as the world existing with oneself dead.

***

Suppose instead of creating our rabbits, we simulated them on a computer (ignoring the fact that this would require an enormous amount of
computation).  We could slow down or speed up this simulation, or stop it altogether, and the simulated rabbits would be none the wiser.  Value
(e.g., the meaning of life) only exists *inside* our simulation.  For us on the outside, these are just states of the computer's circuits.
Value is created in the system, and to the rabbits in the system, it is quite real.

If I *pause* the simulation then continue running it, the rabbits will be completely unaware that I paused it, even if I pause the simulation
for 100 years or a trillion years.  For our rabbits, the time lag is imperceptible because they have nothing to perceive it with.  It's also
imperceptible to the rabbits if I *never* continue the simulation, if I simply throw my computer off a cliff.  Likewise, when a person's
unconscious, their brain has effectively been "paused".  The difference between death and unconsciousness is that in unconsciousness, the
"program" is resumed, whereas in death, the program never starts again.

***

For a cow, its muscle serves a function: it's a "tool" for pulling its bones together.  For someone eating a hamburger, the muscle is a
collection of proteins.

Our brains can be viewed as a collection of physical neurons.  At a higher level, intelligence and sentience are emergent properties of
interactions of these cells.  This is difficult for me to grasp.  A neuron is a physical object that I could actually touch, but sentience seems
intangible.  When a brain is alive, it's a sentient being.  When it's dead, it's a lump of inert matter.

***


> Death is nothing to us, when we exist, death is not yet present, and when death is present, then we do not exist.  All sensation and
> consciousness ends with death and therefore in death there is neither pleasure nor pain. The fear of death arises from the false belief that
> in death there is awareness.
>
> --Epicurus (341-270 BC)


Dying is the *event* of going to existing to not.  Any creature with a nervous system sophisticated enough to support the notion, will have a
strong aversion to death.  In fact, animals as simple as mosquitos will take measures to avoid death FOOTNOTE{The males of some insects and
spiders will take actions to be eaten by a female after they've mated.  In this case, the Will to reproduce (which is the ultimate goal)
outweighs the avoidance of death.}.  So, it's natural that people (or our rabbits) will have a strong aversion to death as well.

Robots probably won't be sentient at all like people.  Movies, such as AI, Terminator, The Matrix, Star Wars, Star Trek, and Short Circuit, all
overly anthropomorphize.  The Will that evolution has installed in people is so deep and ever-present, people don't realize that it's even there
(or when they're wrongfully applying it).  (Until 400 years ago, people did the same thing with gravity.)  It might be completely contradictory
to our intuitions to imagine a robot that "enjoys" abuse, or that doesn't mind things we consider very unpleasant, but consider the bulldog: A
bulldog *likes* to mate with other bulldogs.  I certainly think that'd be unpleasant, but the bulldogs seem to enjoy it.

In **Will: Interaction of Cognitive System and Reward System** I argue that it may be possible to have an intelligent system with no Will.  If
you had such a system, I'd be willing to say it's as self-aware as I am, but its sentience is something different.  Since it'd have no Will
aside from its cognitive "Will" to make predictions (i.e., it'd have no external reward signal), it wouldn't care about anything.


> The mind of an intelligent robot would probably have some major differences from that of a person.  People came about because of evolution,
> and this process installed in people an innate Will for self preservation, for example.  A robot I designed wouldn't necessarily have such a
> Will (unless I programmed it in).  Without this Will, I could tear off the robot's gripper and throw the robot off a cliff, and the robot
> would *feel* none of the terror that a person would feel.  If it were smart enough, it would come to the conclusion that it wouldn't survive
> the fall, but the robot would look at the situation with as objective nonchalance as if it were observing a cloud being whisked apart by the
> wind.  I could give the robot goals, and maybe even a reward signal, but I'm not sure that the robot would *feel* pleasure when I set its
> reward signal to {\tt high}.
>
> --From Europe Debris, **Day 06**


A cognitive system (such as a robot) finding itself in existence doesn't have to be "life" in the reproducing biological sense.  It wouldn't be
a product of evolution.  Reproduction is the *biological* meaning of life.  Therefore, a robot's goals don't have to be those of my rabbits.
So, a robot wouldn't want rights or anything else, unless it was programmed in such a way as to have this happen.  It would be folly to program
the robots in such a way though, and this would most likely have to be explicit because the odds of this happening by accident are slim.
Likewise, it'd be a mistake to make self-reproducing robots.  That'd be shooting yourself in the foot.  Robots' Will should always be
subservient to the Will of people.

--

Why are pleasure and pain different from other sensory signals?  Maybe the answers are in **Will: Interaction of Cognitive System and Reward
System**.  If we gave our (purely cognitive) robot a human body with a full sensor suite, and we held its finger to a hot surface, it'd receive
a signal that would say something like "nerve % 10228 is reading a value of 0.98, nerve % 37128 is reading a value of 0.95, etc.".  A human
brain would "know" that these particular nerve readings mean that a certain area of the skin on our finger is being damaged, and the
person-brain would probably issue commands to jerk our hand away.  To the robot, this is just another signal.

***

Both my parents dated other people before they met.  It seemed like a narrow margin that they ended up with each other.  It's easy for me to
think that if my dad had stayed with his previous girlfriend, then I would've had a different mother, and it's not too hard to think that if my
mom would've stayed with her previous boyfriend, then I would've had a different dad, but I can't hold both views simultaneously.

Likewise, a woman has 1,000s of eggs, and a man has billions of sperm.  By sheer luck, I was a particular egg and a particular sperm.  Had
either been different, I wouldn't be me, I would be a sibling that doesn't exist, and *I* wouldn't exist at all.

--

"Why am I me at this time in history (and not somebody else at some other time)?", "If I'm just a collection of molecules, how can I have
feelings?".  I couldn't conceive of the void that comes after death (and before birth) or how this lucky arrangement of molecules resulted in my
being.  Everything I've ever perceived or thought has been the result of about 3 pounds of matter in my skull.

***

> Death is the release from all pain and complete cessation, beyond which our suffering will not extend. It will return us to that condition of
> tranquility, which we had enjoyed before we were born. Should anyone mourn the deceased, then he must also mourn the unborn. Death is neither
> good nor evil, for good or evil can only be something that actually exists. However, whatever is of itself nothing and which transforms
> everything else into nothing will not all be able to put us at the mercy of Fate.
>
> --Lucius Annaeus Seneca (4 BC - 65 AD)

Marc being not-alive is the natural state of the universe.  For its approximately 12,000,000,000 year existence, Marc has been alive for less
than 32, and will certainly be alive for less than 150 years compared to the total past and future existence of more than 30,000,000,000 years.
Despite that, the entirety of my experience with the universe has been and will be during the time that Marc's alive.  (The same is true for
places: most parties don't have Marc, yet I've only been to parties where Marc was there.)

***

What is it that makes a person?  I can say that I'm not really my liver, for example, because I can have a liver transplant without really
altering what I consider my fundamental self.  If it were technologically feasible, I doubt I would say the same thing about a *brain*
transplant.  In fact, if I swapped brains with another person, I would find "myself" in the other person's body.  This operation might be better
thought of as a *body* transplant FOOTNOTE{Adjusting to your new body will likely be nontrivial. At the least, you be probably be really clumsy
for a while.  Consider what your voice might sound like.  If the transplant were with Arnold Scwarzenegger, you might accidentally hit yourself
(when you meant to scratch your nose) a lot to begin with.}.

So we might say that what we are is really our brains, but this idea can be challenged too.  To begin, the skin cells of our body are gradually
replaced.  This goes for most other organs too.  So, our livers might be a "wave" like Granddad's axe (which has had 5 different handles and 3
different heads, but it's still Granddad's axe).  It was once believed that, after a certain age, we no longer produce new brain cells.  That,
unlike most other cells in our body, brain cells are there for life.  More recently, this idea has been challenged.  Regadless of what actually
happens biologically, in principle it's possible to replace our brain cells one at a time and end up with a "new" brain that behaves identically
to the "old" brain.  If the replacement is seamless, we wouldn't be able to notice that our brain cells were being switched out.

Now, suppose instead of replacing brain cells with other brain cells, we replaced them with functionally equivalent *mechanical* brain cells.
Again, if the replacement is seamless, we wouldn't be able to notice the difference.  But this time, instead of ending with another brain, we
have a *machine* that we call ourself.  Now, suppose that instead of housing this machine in our skull, we connect the brain stem to remotely
controlled interface that sends inputs to and receives outputs from the machine wirelessly.  Assuming the interface is seamless, the machine
would still be *us*.

Finally, suppose that instead of "running" the actual brain-machine, we *simulate* it on a supercomputer, and interact with our body via the
wireless interface.  This would still be *us*, but now what we call *us* is just a *process* on a supercomputer.

So, a person's consciousness, their being, is a collection of ideas and a set of processes on those ideas.  These processes are basically
organizing the ideas and using the ideas to find a way to accomplish their Will.  Their Will is basically to spread their genes.  We are our
genes and our experiences, nothing more.

So, what we call "ourself" is bigger than our bodies.  Given this, there are 2 more ways that what we call "ourself" might live on after our
bodies die: we can spread our ideas to other people through conversations and writings, and our genes can also live on after our deaths, not
only through our children, but through other relatives, such as our siblings' children.

***

[Aside about Robot consciousness and will to self-preservation]

Thus, robots would be conscious in an entirely different way that people are unless this signal is carefully crafted to have *specific* things
like self-preservation.

# Free Will
[#]: )))(((

TL;DR: [FIXME]

***

Discussions on consciousness usually include some mention of free will, which is why I'm including this here.

The opposite of free will is where we have no choices.  It's possible to be completely deterministic, yet feel like you have choices.  You don't
need non-determinism (or even pseudo-randomness) to be unable to fully explain your own thought processes.  This is a more an issue of
meta-cognition and complexity than of non-determinism.

For example, a classic chess playing computer program works by searching the "tree" of moves.  It will look at all its possible moves, then all
its opponent's possible responses to each move, then all its possible responses to each of those moves and so on up until a certain number of
moves.  At the end (or leaf) of each branch, it will use a heuristic to decide how good that branch is.  This heuristic could be something
simple like how many pieces it has left for the leaf board state, or it can be much more sophisticated.  Suppose our chess playing program is
deterministic in that it has a definite method for choosing which branch to search next.  This program will search for the best move because it
"wants" to win.  So, we could say that the program lacks free will because it's deterministic.  On the other hand, the program *chooses* the
move that it judges to be best.

We can imagine giving the program a (deterministic) meta-cognitive process choosing how much search to put into each branch.  So that's another
layer of choice, but the meta-cognitive process is also deterministic.  We can give the program a meta-meta process as well, which decides
factors in the meta-cognitive process, and we can give the computer a meta-meta-meta process and so on, but all these processes can still be
deterministic.  The computer isn't changing what it wants.  It has no way of escaping that it wants to win.

It is true, on the other hand, that the computer wouldn't be able to predict what it's going to do, because as the computer's sophistication
increases with which to understand itself, its complexity increases, so it needs to understand more and more about itself.  It's like a dog
chasing its tail.  In a sense, the computer will *feel* like it has free will because it will feel nondeterministic to itself because it has
parts of its process that it isn't able to understand.

***

It's impossible for me to want something I don't want, or to choose what I want.  This is because any choice must be based on some criterion.
If I decided something "arbitrarily" (e.g., with a coin toss), tossing the coin was a choice.  In this particular instance, my choice to toss
the coin would be caused by the desire to be "free" of any governing rules.  We want "free will" because we want freedom in general because
constraints are usually bad for our wellbeing, and we've generalized this idea to include the "constraints" of the Will that is in our nature.

***

If we're all deterministic, can we be held accountable for our actions?  Yes.  Consider a mosquito.  They're not very smart.  In fact, I view
them as stimulus/response automata (with a few internal "states").  I believe they don't have any choice in their behaviour.  They *need* blood
to reproduce.  But this doesn't prevent me from swatting them when they land on me.

In the case of people it's more complex, but the principle's the same.  If people have no choice (in a deterministic sense) in their actions,
does it make sense to punish a thief, for example?  Yes.  The purpose of punishment is to act as a deterrent.  The fact that you may be punished
for doing something goes into your own process for determining your actions.

# Conclusions
[#]: ))))((((

TL;DR: [FIXME]

***

Although, these memes may have raised more questions than they answered, I hope they've at least given some tools for thinking about the bigger
questions such as "What should I do with my life?"  or "When faced with 2 possibilities, what criteria should I use for choosing between them?".

Now that we understand a bit more about where our motivations come from and how they work, we have some insight as to how to fulfill them.  It's
not truly the case that *our* goals should ultimately be reproduction any more than the goals of our rabbits (from their perspective) will be
reproduction.  Our rabbits lack the computational power to figure out what behaviours will cause their genes to be around.  Even the designers
(be it us or evolution) lack the computational power for all situations.  But understanding how and why our Will is set up as it is may be
useful for understanding why we're here and what we should do.  In Reinforcement Learning terms, the Meaning of Life is to make our reward
signal fire for the long term.  This is different from Hedonism for reasons explained in the section on that subject.

***

> Equations are more important to me than politics because politics are for the present, but an equation is something for eternity.
>
> --Albert Einstein (1879-1955)

In **Walking = Falling + Catching**, I wrote that a person always needs goals.  This begs the question of what these goals should be.  What is
progress?  Reproduction is so broad.  When we unpack what this means, it unfolds into a complex array of what it entails.

Achievements that have lasting power seem to be more satisfactory than temporary results.  Having and raising children is a "project" that has
staying power.  Creating new knowledge (e.g., inventing, writing, exploring, and discovering) also has staying power.  Being a social creature,
a good deal of a person's wellbeing depends on their relations with other people, so cultivating relations also has a good deal of staying
power.  There's also the creation of goods or setting up social projects.  We should always be falling towards something.

--

On the other hand, if just we're living for our legacy after we're dead, can't we just pretend to have been (e.g.) Thomas Edison?  Aren't we
just as much Thomas Edison as are the bones lying in Edison's grave?  Well, no.  The question is what to do with our life while we're alive.  So
pretending we were Thomas Edison doesn't answer any questions about which actions to take, and we have to do *something*.  Rabbits that took
this approach aren't the rabbits that left legacies, and are less likely to be the rabbits that had a lasting effect on their world.  A *group*
of rabbits that had few inventors would be less likely to survive and reproduce than a group of rabbits that did.

So what about Isaac Newton?  Here was a man who may have been the world's single greatest influence on modern science.  He co-invented calculus,
developed the laws of mechanics and gravitation, and developed a theory of optics.  However, Isaac Newton never married and had no children.
So, if Newton were one of our rabbits, would we consider him a failure?  Maybe, but because of his work, his countrymen gained a technological
advantage that helped spread genes like his.  Ultimately, the knowledge that he helped developed has helped and will help the survival of the
whole human race.

In 1879, in modern day South Africa, some 4,000 Zulus attacked a remote hospital housing 139 British soldiers (and medical personnel, etc.),
many of whom were sick or wounded.  In the end, the British, who suffered only a few dozen casualties (only 19 British died as a result of the
battle), inflicted heavy losses on the Zulus (it's estimated that the Zulus lost 600 men), and the Zulus withdrew CITE{barthorp:1980}.  To me,
this illustrates how ideas, from the invention and production of the firearms used by the British, to the clever strategy devised by Lieutenant
John Chard, the British commanding officer, can manifest themselves in a reality of blood and flesh.  In this battle, ideas, *such as strategy
and inventions*, meant the life and death of several hundred people.  Had Chard been somewhat more dimwitted, the British could have easily been
wiped out by the sheer numbers of the Zulu horde.

***

The question of *what* creates real value vs. what is only Artificial Sweetener still plagues me.  For example, when between the ages of 7 and
11, I collected coins.  I saved up my allowance, and instead of spending it on a bike or a sling shot, I spent it on coins.  This collecting
*felt* like progress, and I had the added satisfaction that I could later sell the collection and gain a profit.  It has gained in value, but
the collection that I spent 4 years of my childhood obtaining is now worth less than a month of my adult's salary.

There are cases where it's clear what my future 80-year-old self will have wanted, but sometimes it's not so clear.  For example, when I was an
undergraduate, I focused on my studies because that's what I thought future-Marc would have wanted me to do.  I never drank, did drugs, or
partied.  My social life wasn't very active.  I graduated at the top of my class and got into a good graduate program, but I've I've since
regretted that I didn't socialize more and sow some wild oats.  I should have been more moderate.

[#]: I should go in to some investigation of what creates value.  That is, use the principles
[#]: outlined in the memex (about the rabbits and
[#]: limited cognitive resources and myopic evolution) to say what is
[#]: actually desirable: power, human relations, family, etc..

[#]: Social acceptance and power.  Money is effectively a contract on human labor.  Isn't this just a formalization of "the favor bank"?

***

>  Let an ultraintelligent machine be defined as a machine that can far surpass all the intellectual activities of any man however clever.
>  Since the design of machines is one of these intellectual activities, an ultraintelligent machine could design even better machines; there
>  would then unquestionably be an "intelligence explosion", and the intelligence of man would be left far behind.  Thus the first
>  ultraintelligent machine is the last invention that man need ever make, provided that the machine is docile enough to tell us how to keep it
>  under control.  It is more probable than not that, within the twentieth century, an ultraintelligent machine will be built and that it will
>  be the last invention that man need make.
>
> --I. J. Good  CITE{good:1965}


>The Übermensch is the meaning of the earth.
>
>--Friedrich Wilhelm Nietzsche, from Also Sprach Zarathustra CITE{nietzsche:1885}

I've found I can accomplish the most by doing research in Artificial Intelligence.  Even if not achieved during my lifetime, this has the
potential to give me an academic legacy.  But, if achieved during my lifetime, AI has the potential to think all those thoughts that I'll have
died without thinking otherwise.  It has the potential to figure out a way to preserve me.  It would create a superbrain that could help answer
the question of whether entropy is reversible (if the universe is a closed system).
