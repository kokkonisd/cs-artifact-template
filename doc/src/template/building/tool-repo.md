# The tool repository
In the Git repository of the _tool_, copy all files from the `template/tool-repo/` directory of the
template. If you are not starting from a fresh repository, make sure to not overwrite any existing
versions of these files. For example, you can run:
```console
$ rsync -a -v --ignore-existing \
    /path-to-template/template/tool-repo/* /path-to-tool-repo/
```

Once that is done, you can now go through each file and edit it as described below.

## `AUTHORS`
You should delete the contents of this file and replace them with the names (and emails, if they so
wish) of the authors. A good format to follow is `Firstname Lastname <email_address>`, with one
author per line. For example, `Jane Doe <jane.doe@example.com>`.

## `build.sh`
You should replace `TODO` with the name of your tool.

## `CITATION.cff`
You should delete the contents of this file and replace them with valid metadata. You can find more
about the format of this file on <https://citation-file-format.github.io/>, and you can use a tool
such as <https://citation-file-format.github.io/cff-initializer-javascript/> to generate a valid
`CITATION.cff` file.

**This file is not a priority.** In fact, you will most likely obtain all of the necessary
information some time after the acceptance of the associated paper, so you can come back to it at a
later time.

## `CONTRIBUTING.md`
You should replace `TODO` with the name of your tool in the heading. You should also write a
thorough contributing guide, including developer dependencies, a guide on how to set up a
development environment and so on.

**This file is not a priority.** You should take care of this before making the repository public,
but you obviously do not need it during the experimental phase.

## `Dockerfile`
You should delete the contents of this file and replace them with the appropriate code to generate
a usable Docker image for your tool. You can find the full reference at
<https://docs.docker.com/reference/dockerfile/>.

## `.dockerignore`
This file contains some reasonable defaults that you will most likely want to omit from the
generated Docker image. However, you should adapt it to the needs of the tool. For example, if your
tool's build process generates build artifacts in a `build/` directory, that directory should
probably also be added to the `.dockerignore` (as well as the `.gitignore`).

## `IMAGE`
You should delete the contents of this file and replace them with the name of the Docker image of
your tool. This should most likely just be the name of the tool in lowercase.

## `LICENSE`
You should delete the contents of this file and replace them with an actual license, preferably an
[open source](https://opensource.org/licenses) license.

## `README.md`
You should replace the TODOs with appropriate text throughout the file. You can of course edit,
remove or add text as you see fit, and depending on the context of your tool.

**This file is not a priority**, but it is often very useful to add some information such as
dependencies as soon as you have it. If multiple people are working on this repository, it will
also make collaboration easier if it is kept up to date with information about the dependencies or
the build process of the tool.

## `run.sh`
You should replace `TODO` with the name of your tool.

## `VERSION`
This file starts at a reasonable first version, so you do not need to edit it at first. You are,
however, expected to edit it as you keep track of the version of the tool. It is a good idea to
make sure this version number stays aligned with other version-tracking mechanisms (e.g., in
`pyproject.toml` for Python-based tools or in `Cargo.toml` for Rust-based tools).
