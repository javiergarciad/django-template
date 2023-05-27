<div align="center" id="top">
  <img src="./.github/app.gif" alt="Django Template" />
  &#xa0;


</div>

<h1 align="center">Django Template</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/javiergarciad/django-template?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/javiergarciad/django-template?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/javiergarciad/django-template?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/javiergarciad/django-template?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/javiergarciad/django-template?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/javiergarciad/django-template?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/javiergarciad/django-template?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center">
	🚧  Django Template 🚀 Under construction...  🚧
</h4>

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#lock-security">Security</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#notebook-readings-that-help-me ">Readings</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/javiergarciad" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Basic Django template.

## :lock: Security ##

After cloning the repo add the 'envs/' directory to .gitgnore.

## :sparkles: Features ##

:heavy_check_mark: Apps structure;\
:heavy_check_mark: Differente .envs for local dev or production;\

## :rocket: Technologies ##

The following tools were used in this project:

- [Django](https://www.djangoproject.com/)

## :notebook: Readings that help me ##

- [Mastering Django](https://masteringdjango.com/django-tutorials/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python3](https://python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/javiergarciad/django-template

# Access
$ cd django-template

# Create virtualenv
$ virtualenv .venv

# Activate virtualenv
$ source .venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Select the enviroment
on '/core/setting.py' find the line 'env = dotenv_values(Path(BASE_DIR, "envs", ".env.local"))' and modify the las component to point to your enviromental file.

# Run the project
$ python manage.py runserver

# The server will initialize in the <http://localhost:8000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/javiergarciad" target="_blank">Javier Garcia</a>

&#xa0;

<a href="#top">Back to top</a>
