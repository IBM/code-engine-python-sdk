# Questions

If you are having problems using this SDK or have a question about IBM Cloud services,
please ask a question on [Stack Overflow](http://stackoverflow.com/questions/ask) or
[dW Answers](https://developer.ibm.com/answers/questions/ask).

# Issues

If you encounter an issue with the project, you are welcome to submit a [bug report](<github-repo-url>/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

# Pull Requests

If you want to contribute to the repository, here's a quick guide:
  1. Fork the repository
  2. Develop and test your code changes:
      * Install you dependencies using `pip3 install requirements.txt`
      * To run the tests: `pytest`
      * Please add one or more tests to validate your changes.
  3. Check and fix code style: `./pylint.sh`
  4. Make sure everything builds/tests cleanly
  5. Commit your changes
  6. Push to your fork and submit a pull request to the **master** branch
  
# Coding Style

This SDK follows a coding style based on the [PEP8 Style Guide for Python](https://www.python.org/dev/peps/pep-0008/),
with the following modifications:
- four spaces instead of tabs for indentation

All non-trivial methods should have docstrings. Docstrings should follow the [PEP257 guidelines](https://www.python.org/dev/peps/pep-0257/). For more examples, see the [Google style guide](https://google.github.io/styleguide/pyguide.html#381-docstrings) regarding docstrings.

Use [PyLint](https://www.pylint.org/) to adhere to these guidelines.

# Running the Tests

Out of the box, `pytest` runs unit tests and integration tests (which require credentials).

To run the integration tests, you need to provide credentials to the integration test framework.
The integration test framework will skip integration tests for any service that does not have credentials,

To provide credentials for the integration tests, export your credentials as environment variables.

You can run a specific test by adding the name of the test file, e.g.:

```
pytest -q test35.py
```

# Code Coverage

This repo uses [coverage](https://pypi.org/project/coverage/) to measure code coverage. To obtain a code coverage report, run `coverage run`from the root of the project, and then view the coverage report from the `coverage report` command.


## Additional Resources
+ [General GitHub documentation](https://help.github.com/)
+ [GitHub pull request documentation](https://help.github.com/send-pull-requests/)

# Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
   have the right to submit it under the open source license
   indicated in the file; or

(b) The contribution is based upon previous work that, to the best
   of my knowledge, is covered under an appropriate open source
   license and I have the right under that license to submit that
   work with modifications, whether created in whole or in part
   by me, under the same open source license (unless I am
   permitted to submit under a different license), as indicated
   in the file; or

(c) The contribution was provided directly to me by some other
   person who certified (a), (b) or (c) and I have not modified
   it.

(d) I understand and agree that this project and the contribution
   are public and that a record of the contribution (including all
   personal information I submit with it, including my sign-off) is
   maintained indefinitely and may be redistributed consistent with
   this project or the open source license(s) involved.
