# A note on stacking Docker images

This template encourages the use of the _tool_ Docker image as a base for the _artifact_ Docker
image. This avoids duplication of code and dependency information, and offers a more stable and
reproducible setup.

However, in some cases, multiple Docker images may be used. This can occur when the tool makes use
of external dependencies which must be used through their own Docker image. It can also occur if the
work's contributions contain both a tool and a new benchmark/dataset, in which case both must be
published, potentially in different Docker images.

In any case, if you have to "stack" Docker images, you might be tempted to do the following in the
_artifact_ `Dockerfile`:

```dockerfile
# Contains dependency at `/root/tool`.
FROM external-dependency/tool:0.1.0 AS dependency
# Contains our tool at `/root/tool`.
FROM my-tool:0.1.0 

COPY --from=dependency /root/tool /root/dependency

# Now, we should have both `/root/tool` and `/root/dependency`.
# Setup code for the rest of the artifact...
```

While this might result in all of the _important files_ of `external-dependency/tool:0.1.0` being
put in the right place in the final image (provided there are no conflicts between
`external-dependency/tool:0.1.0` and `my-tool:0.1.0`), the dependency might not work as expected.
For example, if it needs to install system packages, they will not be installed in the final image,
as the last `FROM` command will essentially overwrite the installation with its own installation of
system packages.

One way to get around that is to copy _everything_ from the previous image(s) like so:

```dockerfile
FROM external-dependency/tool:0.1.0 AS dependency
FROM my-tool:0.1.0

COPY --from=dependency / /

# Setup code for the rest of the artifact...
```

This might seem inelegant, but it will work. `COPY` will not overwrite the entirety of `/`, but
rather copy the missing files (i.e., whatever was installed via the system package manager).

However, at least for images ultimately based on `ubuntu:22.04` and `ubuntu:24.04`, this will result
in a broken `apt`, meaning that other packages needed by the artifact will not be able to be easily
installed after that `COPY` command.

A known fix to this is the following:

```dockerfile
# See https://askubuntu.com/a/1272402.
RUN rm /var/lib/dpkg/statoverride && \
    rm /var/lib/dpkg/lock && \
    dpkg --configure -a && \
    apt-get --fix-broken install
```
