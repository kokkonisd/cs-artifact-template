# Using the artifact

As established in the previous sections, a big advantage of setting up your artifact in this way is
that you can both use the artifact to _produce_ the results of your paper and give it to artifact
evaluators to _reproduce_ the results.

## Producing the results for a paper

### Storing the results and producing data for the paper

When producing results for a paper, it is a good idea to be able to **store the raw results**
instead of storing **metrics _about_ the results**. For example, you can store the true/false
positive/negative rates of an experiment and throw away everything else to save space; however, if
you later want to retrieve some other metric from the same data, it will be impossible.

In some cases, the raw results are simply too large (even in compressed form). In such cases, you
might be able to filter some of it out, keeping only a _core_ of "most useful" data, to reduce the
size down to an acceptable amount. Barring exceptionally incompressible data, however, you should
probably simply compress the results and keep everything.

It is a good practice to have the raw results be as _read-only_ as possible. One such way is to
immediately compress them after the experiment (e.g., in a `.tar.xz` tarball), and then create
scripts to interpret the results from the tarball itself.

For better performance, you can set a fixed directory within the tarball where the results get
stored. Then, a script would only have to extract these result files (e.g., CSV files), parse them,
perform any necessary calculations on them and output the results (e.g., in TikZ form, or even
simply as text on `stdout`).

While there is some slowness associated with this approach (as you have to de-compress the raw
results), it is arguably not really noticeable, as the results often only need to be extracted once
(and then stored somewhere if further inspection is necessary). At the same time, the raw results
can now be easily packaged with the artifact on an archival repository (e.g., on Zenodo) to provide
even better means to other researchers of reproducing your results.

### Running experiments in Docker containers

When using Docker containers, it is a good idea to auto-remove them when done by running them with
the `--rm` option. However, a crash might cause all data in the container to be lost (in some cases,
it can be multiple hours or even days worth of data). For that reason, it is a good practice to
_bind mount a volume_ to the container, essentially mapping a directory on the host machine to a
directory in the container. This can be achieved through the `--volume` option, like so:

```console
$ docker run -ti --rm --volume /path/to/host-dir:/path/to/container-dir
```

For instance, we can map `$HOME/experiment_target_YYYY-MM-DD` on the host to `/root/output` in the
container, and direct _all_ output of the experiment in the container in `/root/output`. That way,
even in the event of a crash, we will be able to save whatever data has been produced up until the
crash.

Another benefit of this use of containers is that they are less likely to run out of space. As their
"default" space is commonly placed on a shared volume on the host machines, on machines that see
heavy Docker container usage across multiple users, you run the risk of running out of space on the
shared volume (which might ruin an experiment). By using a bind mount as described before, you
ensure that the directory containing the largest and most important data from your experiment will
not also be used by other running containers.

## Providing a reproduction environment for other researchers

The same artifact can be used by other researchers (e.g., in the context of artifact evaluation) to
reproduce the results of the paper easily and in some cases even accurately down to the bit level.
Since the very same environment was used to produce the results in the first place, we can be very
confident of its robustness and its ability to reproduce the same results.
