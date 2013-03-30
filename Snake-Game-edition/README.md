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

### Brief description of our flavor of the Snake game

The game happens on a 16x16 board.  
At the start of the game, the board looks like this:

```
         · ○ ○ ○ ○ ○ ○ ○ ○ ○ ○       
                             ○       
                             ○       
                             ○       
               #             ○       
                             ○       
                             ○       
                             ○       
                             ○       
                             ○       
                             ○       
                     ¤ ○ ○ ○ ○       
```

When pursuing the pellet, the snake always follows the shortest path, even at the risk of intersecting with itself (there is no AI involved).  
The snake scores an additional point for every pellet it swallows.  
Whenever the snake swallows a pellet, a new - randomly generated - pellet shows up on the board.  
The game ends when the snake intersects with itself.

Here's what the board looks like mid-game:

```
                       ·             
                       ○             
                       ○             
                       ○             
                       ○             
                       ○             
                       ○             
                       ○             
     ○ ○ ○ ○ ○ ○ ○ ○ ○ ○             
     ○                               
     ○                               
     ○ ○ ○ ○ ○ ¤         #           
```

### The problem statement

Test-drive a program that computes the snake's behavior and keeps score throughout the entire game.

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

