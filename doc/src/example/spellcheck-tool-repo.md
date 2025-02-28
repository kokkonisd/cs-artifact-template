# The `spellcheck` tool repository

The repository for the `spellcheck` tool can be found under `example/spellcheck-repo`.

The _Spellcheck_ approach is implemented here in the form of a Python script, `spellcheck.py`. It
has an external dependency on another tool, called `similar-word-finder` (found under the directory
with the same name). Such a dependency can be materialized in many ways; for example, if
`similar-word-finder` has its own public repository, it can be "linked" to this repository via a
[Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules), conveniently pinning its
version down to the exact commit ID.

## General "must-have"s

The following essential files are present in the repository:

- `README.md`. It gives a short explanation of the approach and tool, listing the dependencies
  needed in order to install and use it. It also links to the contributing guide (see
  `CONTRIBUTING.md` below) and provides a citation for other papers to use (see `CITATION.cff`
  below).
- `AUTHORS`. It contains a simple list of authors and their emails. In this case, there is a single
  author: Jane Doe.
- `LICENSE`. It contains the license of the tool. In this case, it is the
  [LGPL-2.1](https://opensource.org/license/lgpl-2-1).
- `CITATION.cff`. It contains metadata that can help cite this repository. See
  <https://citation-file-format.github.io/>.
- `CONTRIBUTING.md`. It contains a guide to help others (researchers or industry practitioners) to
  contribute new features or bug fixes to the tool.

## Docker image

In order to facilitate the use of the tool on different machines, as well as to make the
construction of the artifact easier, this repository is also set up to generate a
[Docker image](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/) of
the tool, which can then be used to run a
[Docker container](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
containing the tool. Portability aside, this may also be convenient in some cases where the tool
must run in an isolated environment (e.g., in the cases of malware detection or fuzzing).

The image can be built locally with the `build.sh` utility script, provided that Docker (either
[Desktop](https://docs.docker.com/desktop/) or [Engine](https://docs.docker.com/engine/)) is
installed on the machine. A container using the previously built image can then be started via the
`run.sh` script.

These two scripts make use of the `IMAGE` and `VERSION` files. The `IMAGE` file defines the name of
the generated image (in this case, `spellcheck`), while `VERSION` defines its version number. See
[_Versioning_](#versioning) below for more details.

Finally, the `Dockerfile` and `.dockerignore` determine how the image gets built. See
<https://docs.docker.com/reference/dockerfile/> for a detailed description of these files.

## Documentation

Most tools need thorough documentation, which should not only explain how to use them in their
intended context, but also how to extend them and use them in new contexts (something that is very
common in research). In this case, since the example is very simple, there is a single file in the
`doc` directory, but in a real use case the documentation would be much more detailed.

## Versioning

[Semantic Versioning](https://semver.org/) is used (in tandem with Git) for the versioning of
Spellcheck. Concretely, Spellcheck versions will materialize through
[Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) and updates to the `VERSION` file.
This makes reproducing results using specific versions of Spellcheck (such as the one used in the
fictional paper) easier, and citations to the repository/tool can specify the version to avoid
ambiguities, as Spellcheck evolves.
