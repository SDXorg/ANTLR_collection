# ANTLR-collection
Collects ANTLR code for various SD model translation tasks.

A goal is for this repo to serve as a submodule in other projects (such as [PySD](https://github.com/JamesPHoughton/pysd)), and for the grammars to be useable in any of the ANTLR targets (Java, JavaScript, Python).

In this case, it probably makes sense for the repo to host the grammars, and the boilerplate code ANTLR generates from the various grammars, but for whatever project extends this repo to include the extended visitors/walkers in other places, as there is no need for extension-specific backend code to be universally shared.

Test models are hosted externally in the [test-models](https://github.com/SDXorg/test-models) repo.
