# Shena's portfolio: how to fill in the content

This guide explains how to change the text, projects and pictures of this portfolio website. You don't need to know how to code. You only need to edit some text in one file and run one command.

> Prefer to edit the pages themselves? See [EDITING-HTML.md](EDITING-HTML.md). Don't mix the two ways without reading its warning first.

---

## How it works

The website is made of HTML pages, such as `index.html` and the pages in the `projects/` and `competenties/` folders. **You don't edit those pages yourself.** A small program, `build.py`, writes them for you.

All the content lives in one place: **the top part of `build.py`**. The steps are always the same:

1. **Edit** the text at the top of `build.py`.
2. **Save** the file.
3. **Run** `python3 build.py`. This rebuilds all pages.
4. **Look** at the result in your browser.

> ⚠️ Never edit the `.html` files directly. The next time `build.py` runs, your changes there are overwritten and lost.

---

## What you need (one-time setup)

1. **A text editor.** [Visual Studio Code](https://code.visualstudio.com/) is free and works well. Don't use Word or Pages, because they change quotation marks and break the file.
2. **Python 3.** It is already installed on most Macs. To check:
   - Open the **Terminal** app (press `Cmd + Space`, type *Terminal*, press Enter).
   - Type `python3 --version` and press Enter.
   - If you see something like `Python 3.9.6`, you're ready. If not, install Python from [python.org](https://www.python.org/downloads/).
3. **The project folder** on your computer, e.g. `shena-portfolio`.

### Opening the project

In VS Code, choose **File → Open Folder…** and select the `shena-portfolio` folder. The files are listed on the left.

### Running the build command

In VS Code, open the built-in terminal with **Terminal → New Terminal**. It opens in the project folder already. Type:

```
python3 build.py
```

and press Enter. You'll see a list of lines like `wrote index.html`, which means it worked.

### Viewing the site

Double-click `index.html` in Finder to open it in your browser. After rebuilding, refresh the page in your browser (`Cmd + R`).

---

## The rules of the content file

The top of `build.py` looks like a list of labels and values. For example:

```python
"title": "Houten paviljoen",
"role": "Ontwerper & maker",
```

Some rules keep it working:

| Rule | Good ✅ | Wrong ❌ |
|---|---|---|
| Text goes between **straight double quotes** | `"Mijn tekst"` | `Mijn tekst` or `“Mijn tekst”` |
| Every line in a block ends with a **comma** | `"role": "Ontwerper",` | `"role": "Ontwerper"` |
| Don't use `"` **inside** your text. Use `'` or curly quotes `“ ”` instead | `"Het 'paviljoen' project"` | `"Het "paviljoen" project"` |
| Keep the **brackets** `{ }` and `[ ]` paired | `["1.2", "2.1"]` | `["1.2", "2.1"` |
| Only change what's **to the right** of the colon | `"title": "Nieuwe titel",` | `"titel": "Nieuwe titel",` |

Lines starting with `#` are notes for you. The website ignores them.

**Tip:** make **one change at a time**, then run `python3 build.py`. If something breaks, you know exactly what caused it.

---

## What can I change, and where?

Everything below is in `build.py`. Use **Edit → Find** (`Cmd + F`) to jump to the word in **bold**.

### 1. Your introduction, photo and contact details: **`SITE =`**

```python
SITE = {
    "hero_greeting": "Hoi, ik ben Shena",
    "hero_title": "Bouwkundige die ontwerp, data en *techniek* verbindt.",
    "hero_text": "Ik studeer bouwkunde en ...",
    "hero_image": None,
    "hero_image_alt": "Voorbeeldfoto (placeholder)",
    "email": "hello@example.com",
    "phone": "+31 6 00 00 00 00",
    "linkedin": "https://www.linkedin.com/in/shena",
    "github": "https://github.com/shena",
}
```

- In `hero_title`, the word between `*asterisks*` is shown in the pink accent colour.
- For your own photo, see **Adding pictures** below. Then replace `None` with the file name in quotes, e.g. `"hero_image": "shena.jpg",`. Also change `hero_image_alt` to describe the photo, e.g. `"Portret van Shena"`.
- Don't want to show something, such as your phone number? Make it empty: `"phone": "",`

### 2. Projects: **`PROJECTS =`**

Each project is a block between `{` and `},`. This is a complete example, with every option filled in:

```python
    {
        "slug": "houten-paviljoen",
        "title": "Houten paviljoen",
        "leerdoelen": ["1.3", "1.4", "2.1"],
        "tags": ["parametrisch", "fabricage"],
        "lead": "Een paviljoen van gefreesde houten platen, parametrisch ontworpen en digitaal geproduceerd.",
        "role": "Ontwerper & maker",
        "date": "2026-09",
        "tools": "Rhino, Grasshopper, CNC-frees",
        "image": "paviljoen.jpg",
        "image_alt": "Het houten paviljoen op de campus, gezien vanaf de ingang",
        "caption": "Het paviljoen tijdens de opbouw.",
        "challenge": "Wat was de opdracht? ...",
        "process": "Hoe heb je het aangepakt? ...",
        "steps": ["Analyse", "Ontwerp in Grasshopper", "Frezen en bouwen"],
        "result": "Wat was het resultaat en wat heb je geleerd? ...",
    },
```

What each label means:

| Label | What to fill in | Required? |
|---|---|---|
| `slug` | The page's web address, e.g. `houten-paviljoen` becomes `projects/houten-paviljoen.html`. Use lowercase letters and hyphens only, with no spaces. | Yes |
| `title` | The project name. | Yes |
| `leerdoelen` | Which leerdoelen this project shows, e.g. `["1.2", "2.2"]`. **The first one decides the main competentie** of the project. See section 3. | Yes |
| `tags` | Labels such as `["arcgis", "python"]`. Choose from: `parametrisch`, `arcgis`, `fabricage`, `python`. | Yes |
| `lead` | One or two sentences summarising the project. Shown on the cards and at the top of the project page. | Yes |
| `role` | Your role, e.g. `Ontwerper`. | Yes |
| `date` | Year and month, written as `"YYYY-MM"`, e.g. `"2026-10"` for October 2026. | Yes |
| `tools` | Software and tools you used. | Yes |
| `image` | The file name of the project picture. See **Adding pictures**. | No |
| `image_alt` | A short description of the picture, for people who can't see it. Required if you add an `image`. | No |
| `caption` | The text under the picture. | No |
| `challenge` | Text for **De opgave**. | No |
| `process` | Text for **Het proces**. | No |
| `steps` | A bullet list under *Het proces*. Write `[]` for no list. | No |
| `result` | Text for **Het resultaat**. | No |

Labels you leave out get example text, so the page never looks empty. Remember to fill them in before you publish.

**To add a new project:** copy an existing project block, from its `{` down to and including its `},`. Paste it right below, then change the values. Give it a new, unique `slug`.

**The order of the projects** in this list is the order they appear on the competentie pages.

**To remove a project:** delete its whole block. Then also delete its old page from the `projects/` folder. The build reminds you with a `warning:` line.

### 3. Competenties and leerdoelen: **`COMPETENTIES =`**

The four competenties and their leerdoelen are already filled in. The leerdoelen are numbered automatically by their position: the first leerdoel of competentie 1 is `1.1`, the second is `1.2`, and so on.

> ⚠️ If you change the **order** of leerdoelen, or add one in the middle, their numbers change. Check that your projects still point to the right leerdoelen.

**The diagram for competentie 4:** place the image in the `images/` folder. Then, under competentie 4, change `"image": None,` into the file name, e.g. `"image": "professioneel-handelen-hbo.png",`.

### 4. The timeline on the home page: **`TIMELINE =`**

```python
TIMELINE = {"start": "2026-09", "end": "2027-01"}
```

The timeline shows every project with a `date` between `start` and `end`, oldest first. For each project it shows how many leerdoelen you had demonstrated up to that point. Projects outside this period still appear on the competentie pages, just not on the timeline.

### 5. Your STAR-reflectie: **`REFLECTIE =`**

The reflectie page has four parts: **S**ituatie, **T**aak, **A**ctie and **R**esultaat. Replace the example questions in `paragraphs` with your own text. For more than one paragraph, add more lines, each in quotes and ending with a comma:

```python
            "paragraphs": [
                "Mijn eerste alinea.",
                "Mijn tweede alinea.",
            ],
```

### 6. Tags: **`TAGS =`**

To add a new tag, e.g. Revit, add a line like `"revit": "Revit",`. You can then use `"revit"` in a project's `tags`.

---

## Adding pictures

1. Create a folder called **`images`** in the project folder, next to `index.html`, if it doesn't exist yet.
2. Put your picture in it. Good to know:
   - Use **`.jpg`** for photos and **`.png`** for diagrams.
   - Use simple file names without spaces, e.g. `paviljoen-gevel.jpg`.
   - Make it about **1600 pixels wide**. Larger images make the site slow. On a Mac, use the Preview app: *Tools → Adjust Size*.
   - **Landscape** pictures work best for projects; the site crops them to a wide format. A **portrait** photo works best for the home page.
3. Put the file name in `build.py`, e.g. `"image": "paviljoen-gevel.jpg",`, and run `python3 build.py`.

Until you add your own picture, the site shows a random stand-in photo. **Replace all of these before you publish.**

---

## When something goes wrong

After `python3 build.py`, look at the last lines in the terminal.

| You see | What it means | Fix |
|---|---|---|
| `SyntaxError` (plus a line number) | Something is wrong in how the text is written: often a missing comma, a missing quote, or a `"` inside your text. | Go to that line number, or the line just above it. Look for the problems in the rules table above. |
| `error: project '…' refers to unknown leerdoel 5.1` | The leerdoel number doesn't exist. | Use an existing number, such as `1.1` to `4.1`. |
| `error: project '…' refers to unknown tag '…'` | That tag isn't in `TAGS`. | Check the spelling, or add the tag to `TAGS`. |
| `error: … has date '…'` | The date is written wrong. | Write it as `"2026-10"`: year, hyphen, two-digit month. |
| `warning: projects/… is not in build.py anymore` | You renamed or removed a project, and its old page is still there. | Delete that file from the `projects/` folder. |
| `command not found: python3` | Python isn't installed. | Install it from [python.org](https://www.python.org/downloads/). |

**Still stuck?** In VS Code, use `Cmd + Z` to undo your last changes until the build works again.

---

## Saving your work to GitHub

The project is a git repository, so you can save versions and put the site on GitHub.

**The easiest way: GitHub Desktop.**
1. Install [GitHub Desktop](https://desktop.github.com/) and log in.
2. Choose **File → Add Local Repository…** and select the `shena-portfolio` folder.
3. After making changes and running `python3 build.py`, GitHub Desktop lists the changed files.
4. Type a short description at the bottom left, e.g. *Tekst hittestress-project toegevoegd*. Click **Commit to main**.
5. Click **Push origin** to upload to GitHub. The first time, it asks you to **Publish repository**.

**Putting the site online with GitHub Pages:** on github.com, open your repository and go to **Settings → Pages**. Under *Branch*, choose `main` and click **Save**. After a minute or two, the site is live at `https://<your-username>.github.io/shena-portfolio/`.

---

## Checklist before you publish

- [ ] All six example projects replaced with your real projects
- [ ] Each project linked to the right leerdoelen
- [ ] A real picture, with an `image_alt` description, for every project
- [ ] Your own photo on the home page (`hero_image`)
- [ ] The diagram for competentie 4 added
- [ ] Your STAR-reflectie written
- [ ] Your real e-mail, phone, LinkedIn and GitHub in `SITE`
- [ ] Ran `python3 build.py` one last time, and checked every page in the browser
