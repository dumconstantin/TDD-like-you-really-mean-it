## TDD like you really mean it - Pacman edition

**"TDD like you really mean it"** is a rather extreme coding technique that reveals the true nature of TDD.

Knowledge of the traditional TDD technique is assumed. For a quick refresher, please refer to the appendix at the bottom of this page.

**In "TDD like you really mean it", your workflow is going to be:**
- to only add brand-new code to test methods in a test class.
- to only add just enough production code in order to make a failing test pass (production code goes into the same test method where the test code is).
- to only create new non-test methods by way of a "refactoring-extraction" (when you notice duplication of production code).
- to only create new domain-specific classes as destinations for a "refactoring-move".

**Be very strict about this. Refactoring only happens:**
- by extracting code from test methods into non-test methods in the same test class, when duplication of production code has been noticed.
- by moving non-test methods into domain-specific classes, when the solution design eventually starts to emerge.

Inevitably, there is going to be an initial mental block due to the fact that there is no solution code to test - you obviously can't have tests that talk about a solution that doesn't exist yet.  
So how do you overcome that initial mental block?  
How do you jumpstart the process?  
Is there anything you can write tests about?  
**Yes.**  
You can write tests about inputs and outputs without there being a piece of formally structured code that takes those inputs and produces those outputs.  
You can write tests about domain-specific computations as they intrinsically exist outside of any solution design.  
In other words, you can write tests about the problem domain, because that's all there is for you to write tests about.  
You are going to notice how the next step in your solution design emerges from the code you wrote to make those tests about the problem domain pass.  
That's the way in.  
The process is **not** going to feel natural, and it's going to make your brain hurt, but remember - if your brain doesn't hurt once in a while, you're not really learning anything new.  

### The invariants of our flavor of the Pacman game

At the start of the game, the board looks like this:

```
       (a1) (a2) (a3) (a4) (a5 Pacman)
       (b1)                (b5)
       (c1)                (c5)
       (d1)                (d5)
       (e1) (e2) (e3) (e4) (e5)
       (f1)                (f5)
       (g1)                (g5)
       (h1)                (h5)
 (Ghost i1) (i2) (i3) (i4) (i5)
```

As you can see, the board is shaped like the digit "8".

<table>
<tr>
<td valign="top">Pacman moves back and forth along an "S"-shaped path, reversing direction at each end, at a speed of one board position per second.</td>
<td valign="top">Ghost moves continuously along a big-"O"-shaped path, in a counterclockwise fashion, at a speed of one board position per second.</td>
</tr>
<tr>
<td valign="top">At the start of the game, Pacman is at board position "a5" and moves to the left.</td>
<td valign="top">At the start of the game, Ghost is at board position "i1" and moves to the right.</td>
</tr>
<tr>
<td valign="top">If Pacman is either in the same position as Ghost or in his immediate vicinity when Ghost turns red (toxic), Pacman dies and the game is over.<br>
(Yes, Pacman and Ghost can be in the same board position at the same time.)</td>
<td valign="top">Ghost is blue (harmless) most of the time, but turns red (toxic) for a duration of exactly one second every x number of seconds (x is an integer obtained from user input at the start of the game).</td>
</tr>
<tr>
<td valign="top">Pacman collects points by eating pellets.</td>
<td valign="top">Ghost generates a pellet and leaves it behind every time he turns red (toxic). If a pellet already exists at that position, Ghost does not generate a new one.</td>
</tr>
</table>

Pacman moves back and forth along this path:

```
P P P P P
P       •
P       •
P       •
P P P P P
•       P
•       P
•       P
P P P P P
```

Ghost moves continuously along this path:

```
G G G G G
G       G
G       G
G       G
G • • • G
G       G
G       G
G       G
G G G G G
```

### The problem statement

Test-drive a program that takes an integer x (the length of time in seconds between when Ghost turns red/toxic) and produces the number of points collected / pellets eaten by Pacman throughout the entire game.

### Appendix: The traditional TDD technique

**Add a test**
- the simplest one you can think of

**See it fail**
- nobody ever learned anything from a passing test
- not compiling counts as failing
- in dynamic languages, exceptions such as NameError, AttributeError and NoMethodError count as failing

**Make all tests pass**
- by implementing the absolute minimum amount of production code, even if the code is trivial

**(Optionally) Refactor production code**

**(Optionally) Refactor test code**

**Repeat until done**

Design thinking **only** happens during the refactoring steps.

