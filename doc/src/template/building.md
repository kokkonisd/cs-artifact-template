# Building the artifact

Following what was established in the [_Architecture_](../architecture.md) section, the artifact
should be built _before_ the main paper experiments begin, but _after_ the prototyping phase. A good
rule of thumb is to start working on the artifact when the list of experiments needed for the final
paper has more or less been established.

## Creating the Git repositories

The tool itself should be in its own Git repository. If you already have a Git repository, either
because you had one from the prototyping phase you'd like to keep or because you're forking an
existing tool, you are done with this step. Otherwise, you should create one now with `git init`.
This repository should remain _private_ for now, as making it public may hurt the double-blind
review process; consult your target conference's guidelines first.

Similarly, you should create a new, separate Git repository for the _artifact_. This repository will
transparently pull in the tool (defined in the previous repository), but it will also contain other
data relevant to the experiments _specifically_, that have no place in the tool's "primary"
repository.

## Versioning

This template encourages the use of [Semantic Versioning](https://semver.org/) in tandem with
[Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) to aid in reproducibility and
debugging.

In simple terms, once you are happy with the state of the artifact, you should:

- Edit `VERSION` (as well as any other version-tracking files depending on the programming
  language(s) used) in the _tool_ repository, commit and tag;
- Edit `VERSION` in the _artifact_ repository, commit and tag.
