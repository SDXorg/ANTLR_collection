# ANTLR-collection
Collects ANTLR code for various SD model translation tasks.

# ANTLR-collection
Collects ANTLR code for various SD model translation tasks.

A goal is for this repo to serve as a submodule in other projects (such as [PySD](https://github.com/JamesPHoughton/pysd)), and for the grammars to be useable in any of the ANTLR targets (Java, JavaScript, Python).

In this case, it probably makes sense for the repo to host the grammars, and the boilerplate code ANTLR generates from the various grammars, but for whatever project extends this repo (essentially provides the backend on a translation or compilation piece) to include the extended visitors/walkers in other places.

Test models are hosted externally in the test-models repo.
