---
icon: lucide/languages
---

# Internationalisation

Georama's user interface is available in several languages. This page explains how the
translation system works, how to keep the translations up to date and how to add a new
language.

## How It Works

Georama uses the [translation system of Django](https://docs.djangoproject.com/en/6.0/topics/i18n/translation/),
which is based on [GNU gettext](https://www.gnu.org/software/gettext/).

### Settings

The relevant settings are in `src/georama/settings.py`:

| Setting         | Value                                                                       |
|-----------------|-----------------------------------------------------------------------------|
| `USE_I18N`      | `True`, enables the translation system                                      |
| `LANGUAGE_CODE` | `"en"`, the default language, also used when a string is not translated     |
| `LANGUAGES`     | The languages offered to users: English, French, Italian and German         |
| `LOCALE_PATHS`  | `src/georama/locale`, a single catalog shared by all Georama apps           |

### Language Selection

`django.middleware.locale.LocaleMiddleware` activates a language for each request. It
uses, in this order:

1. the language cookie, set when the user picks a language in the selector of the
   navigation bar (`core/base.html`), which posts to Django's `set_language` view
   (`/i18n/setlang/`),
2. the `Accept-Language` header sent by the browser,
3. `LANGUAGE_CODE` as fallback.

### Translatable Strings

The source strings are written in English and marked for translation:

- in Python code, with `gettext_lazy` imported as `_` (e.g. `verbose_name`, `help_text`
  of model fields, `verbose_name` and `description` of the app configs),
- in templates, with `{% load i18n %}` and the `{% translate %}` /
  `{% blocktranslate %}` tags.

!!! note "Migrations"
    `verbose_name` and `help_text` are part of the model state: marking or changing them
    creates a Django migration, which has to be generated with `makemigrations` and
    committed like any other model change.

### Catalogs

Each language has a catalog in `src/georama/locale/<language>/LC_MESSAGES/`:

- `django.po` is the text file holding the source strings and their translations, it is
  committed;
- `django.mo` is the compiled version Django reads at runtime. It is built from the
  `.po` file with `msgfmt` and is **not** committed (it is ignored by git).

The `.mo` files are compiled automatically:

- in the production image, by the `Dockerfile`; the build fails if a catalog is invalid,
- in the development container, by `docker/dev.debug.entrypoint.sh` each time the
  container starts.

## Update the Translations

Run these steps whenever translatable strings are added, changed or removed.

1. Mark the new strings in the code or templates as described above.

2. Extract the strings and merge them into the existing catalogs:

    ```shell
    docker compose run --rm --entrypoint bash georama -c \
      "cd src && uv run manage makemessages --all --add-location file"
    ```

    The command has to run from `src/`, so that the references in the catalogs are
    relative paths like `georama/core/apps.py`. `--add-location file` omits the line
    numbers, which keeps the diffs of the catalogs small.

3. Translate the strings in each `django.po`: fill in the empty `msgstr` entries and
   review the entries marked `#, fuzzy`. `makemessages` marks an entry as fuzzy when it
   guesses its translation from a similar string; Django ignores fuzzy entries, so check
   the translation and remove the `#, fuzzy` line. Strings removed from the code are
   kept at the end of the file as obsolete entries (prefixed with `#~`), they can be
   deleted.

4. Restart the development container to compile the catalogs and load them:

    ```shell
    docker compose restart georama
    ```

    The development server only reloads on Python changes, a restart is needed to pick up
    new translations.

5. Commit the updated `django.po` files.

!!! tip "Untranslated strings"
    A string without translation is displayed in English, so a catalog can be completed
    progressively.

## Add a New Language

The example below adds Spanish (`es`).

1. Add the language to `LANGUAGES` in `src/georama/settings.py`, with its name marked for
   translation:

    ```python
    LANGUAGES = [
        ("en", _("English")),
        ("fr", _("French")),
        ("it", _("Italian")),
        ("de", _("German")),
        ("es", _("Spanish")),
    ]
    ```

    The language selector lists the languages of this setting, each one under its own
    name (e.g. "español").

2. Create the catalog of the new language:

    ```shell
    docker compose run --rm --entrypoint bash georama -c \
      "cd src && uv run manage makemessages -l es --add-location file"
    ```

    `--all` only processes the languages which already have a catalog, which is why the
    new language is given with `-l`. Then update the other catalogs with the command of
    [Update the Translations](#update-the-translations), so that they get the new
    language name to translate.

3. Complete the header of the new `src/georama/locale/es/LC_MESSAGES/django.po`, which
   is created from a template:

    - remove the `#, fuzzy` line above the header, otherwise the header is ignored,
    - set `Language` to the language code (`"Language: es\n"`),
    - check `Plural-Forms`: the template always uses the English rule
      (`nplurals=2; plural=(n != 1);`), which is wrong for some languages (e.g. French
      uses `plural=(n > 1)`); the [gettext documentation](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html)
      lists the rule of each language,
    - set `Project-Id-Version` to `Georama`, like the other catalogs.

4. Translate the strings, then restart the container and commit, as described in
   [Update the Translations](#update-the-translations).

Nothing has to be changed in the `Dockerfile` or the entrypoint script: they compile the
catalogs of every language found in `src/georama/locale/`.
