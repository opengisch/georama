# Contributing to Georama

<div align="center">
  <br>
  <img width="150" height="136" alt="georama_logo" src="https://github.com/user-attachments/assets/abcf1b27-c221-454b-a526-ed086d9a38b8" />
  <br>
</div>

First off, thank you for being here! 🎉

Georama is an open-source project by [OPENGIS.ch](https://opengis.ch), and we genuinely value every contribution, whether it's a bug report, a documentation fix, a feature idea, or a pull request. 

Open-source thrives on community, and we're glad you're part of ours!

---

## Before you dive in

We want to be upfront with you: **at the moment, we have limited time and resources to review and merge external contributions**. This doesn't mean we don't want your help, quite the opposite! It just means that, to avoid frustration on both sides, we strongly encourage you to **get in touch with us before investing significant time in a PR or a new feature**.

The best ways to do this are:

- [**Open an issue**](https://github.com/opengisch/georama/issues/new) if you've found a bug or have a concrete feature request
- **Start a discussion** in our [GitHub Discussions space](https://github.com/opengisch/georama/discussions) if you have an idea you'd like to explore or get feedback on

Early dialogue helps everyone: it ensures we're not stepping on each other's feet, gives the community a chance to weigh in, and often leads to better solutions. Your idea might cover one specific use case, but a quick conversation could help shape it into something that benefits many more users.

---

## What we're focused on right now

Georama's mission is to be a **strong, robust core platform for geospatial data publication workflows**, simple enough for anyone, powerful enough for complex enterprise needs.

We have a longer-term vision of supporting additional features and functionalities through **plugins and extensions**, but we're not there yet architecturally. For now, we are laser-focused on doing one thing really well: geospatial data publication. This means we will prioritize contributions that strengthen the core, including bug fixes, stability improvements, and features that are central to the publication workflow.

If you have an idea that feels more like an add-on or a niche use case, don't be discouraged. Start a discussion! It may well be the perfect candidate for a future plugin.

---

## Ways to contribute

### 🐛 Report a bug

Found something that doesn't behave as expected? Please [open an issue](https://github.com/opengisch/georama/issues/new) and include:

- Your browser and version
- Steps to reproduce the problem (even rough ones help!)
- What you expected to happen, and what actually happened
- Any relevant details about your local setup
- A picture is worth 1000 words! Please add screenshots / screencasts if possible

### 💡 Suggest a feature or improvement

Have an idea? We'd love to hear it. Head over to [Discussions](https://github.com/opengisch/georama/discussions) and share your thoughts. The more context you can give, such as why you need it, what problem it solves, and who else might benefit, the better.

### 📝 Improve documentation

Good documentation is as valuable as good code. If you spot something unclear, outdated, or missing, feel free to open an issue for doc fixes.

### 🔧 Submit a fix or feature

Ready to write some code? Wonderful! Please make sure you've discussed it with us first (see [Before you dive in](#before-you-dive-in)), then follow the technical setup below.

---

## Technical setup

### 1. Fork and clone

Fork the repository on GitHub, then clone your fork locally:

```bash
git clone git@github.com:opengisch/georama.git
```

### 2. Set up your local environment

Assuming you have virtualenv installed, this is how you set up your fork for local development:

```bash
cd georama
virtualenv env --python=python3
source env/bin/activate
pip install -e .
```

### 3. Create a branch for local development

```bash
git checkout -b name-of-your-bugfix-or-feature
```

### 4. Make your changes

Go ahead! If you're adding functionality, please write tests as you go. It makes review much smoother.

### 5. Run the tests

```bash
pip install tox
tox
```

This runs the test suite against multiple Python versions. Make sure everything passes before submitting.

### 6. Check test coverage

Coverage is important to us. After running tox, check the report in the `htmlcov` directory. Please don't include this directory in your commits.

### 7. Commit and push

```bash
git add -p
git commit -m "A clear and descriptive commit message"
git push origin name-of-your-bugfix-or-feature
```

### 8. Open a pull request

Submit your PR through GitHub. Please keep PRs focused: one feature or fix per PR makes review much easier.

### Testing with tox
 
Tox uses pytest under the hood and supports the same syntax for selecting tests. For more details, see the [pytest usage docs](http://pytest.org/en/latest/example/index.html).
 
To run the full test suite across all configured Python versions:
 
```bash
tox
```
 
To run all tests using a specific Python version, e.g. Python 3.8:
 
```bash
tox -e py38
```
 
To run only tests matching a specific name, e.g. `smoke_test`, using Python 3.8:
 
```bash
tox -e py38 -- -k 'smoke_test'
```
 
To produce built `.tar.gz` and wheel distributions:
 
```bash
tox -e check && tox -e build
```


---

## Pull request checklist

Before submitting, please check:

- [ ] My changes are covered by tests
- [ ] All tests pass locally
- [ ] I've updated the documentation where relevant
- [ ] My PR is focused and doesn't bundle multiple unrelated changes
- [ ] I've discussed this change with the team (via issue or discussion)

---

## Coding standards

We value:

- **Single responsibility:** each unit of code does one thing
- **Modularity:** keep things loosely coupled
- **Composition over inheritance**

---

## For core committers

### Reviewing pull requests

- Think carefully about long-term implications. Will this affect existing users? Is it something we want to maintain indefinitely?
- Be thorough. PRs almost always need at least one round of feedback before they're ready. Quality over speed.
- When merging, close or update any related issues with a note on how they were addressed.

### Prioritizing pull requests

From most to least urgent:

1. Fixes for broken tests (on any supported platform or Python version)
2. Tests for uncovered corner cases
3. Minor documentation edits
4. Bug fixes
5. Major documentation updates
6. New features

---

*Georama is a volunteer-driven project. We appreciate your patience, your ideas, and your contributions, big or small. Welcome aboard!* 🌍
