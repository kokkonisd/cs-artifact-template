# Architecture

The goals of this artifact template are to produce an artifact which can:

1. Be used to both _produce_ (by yourself) and _reproduce_ (by others) experimental results for/from
   the associated paper;
2. Be used by others just like any piece of software (if applicable), in various contexts (such as
   research—e.g., other papers, or industry).

As such, this template proposes to split the work into two repositories:

- The **tool** repository, containing the software itself, to be independently maintained and
  distributed as needed;
- The **artifact** repository, building on the _tool_ repository, but also adding any additional
  material needed to (re)produce experimental results for/from the associated paper.

This split allows for nominal maintenance of both parts of the work. On the one hand, the _tool_
repository should be both **published in a live repository** (e.g., on GitHub), to allow authors to
continue to maintain and distribute the tool, allow others to fork and contribute to it, and
**archived**, to allow for long-term preservation and enable reproduction in the future. On the
other hand, the _artifact_ repository should also be **archived** (for the same reasons), but it
should probably not be published in a live repository, as it is not destined to be distributed or
accept contributions from others; after all, its only purpose is reproducing the results of the
associated paper.

This way, the two repositories can stay clean, containing only relevant content, and avoiding
confusion regarding the two main "target groups": developers or researchers modifying the tool are
probably only interested in the _tool_ repository, while artifact evaluators are probably only
interested in the _artifact_ repository.
