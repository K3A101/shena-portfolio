# Editing the HTML pages directly

This guide explains how to change the website by editing its pages (the `.html` files) yourself. You don't need coding experience, but read **"Before you start"** first.

There are two ways to change this site:

| | **Way A: the content file** ([README.md](README.md)) | **Way B: the HTML pages** (this guide) |
|---|---|---|
| What you edit | Only the top of `build.py` | The `.html` files themselves |
| A change to a project… | …updates every page it appears on automatically | …must be made by hand on **every** page it appears on |
| Good for | Adding projects, changing text and pictures | Quick small fixes, or changes the content file can't make |

---

## ⚠️ Before you start: choose one way

**Running `python3 build.py` rewrites all HTML pages from `build.py`.** Any change you made by hand in an `.html` file is then **lost**.

So once you've edited an HTML file, do one of these:

- **Stop using `build.py`** from then on, and only edit the HTML files. This is the simplest choice if you prefer editing pages directly.
- **Or make the same change in `build.py` as well**, so it survives the next build.

If you use Git or GitHub Desktop, it's easy to check: GitHub Desktop shows which files changed. Commit your hand edits before you ever run `build.py`, so you can always get them back.

---

## What you need

- **VS Code** ([download](https://code.visualstudio.com/)). Don't use Word, Pages or TextEdit, because they can damage the file.
- **A browser** to check your changes. Open a page by double-clicking it in Finder. After saving a change, refresh the page in your browser with `Cmd + R`.

Open the project in VS Code with **File → Open Folder…** and select the `shena-portfolio` folder.

---

## HTML in five minutes

An HTML page is text wrapped in **tags**. A tag has an opening part and a closing part with a `/`:

```html
<p>This is a paragraph.</p>
<h2>This is a heading</h2>
```

**You only change the text between the tags.** Leave the tags themselves alone.

Some tags carry extra information called **attributes**, written as `name="value"`:

```html
<a href="projects/houten-paviljoen.html">Houten paviljoen</a>
<img src="images/paviljoen.jpg" alt="Het houten paviljoen op de campus">
```

- `href` is where a link goes.
- `src` is which picture is shown.
- `alt` is a description of the picture, for people who can't see it.

These are the tags you'll meet most often:

| Tag | Meaning |
|---|---|
| `<h1>`, `<h2>`, `<h3>` | Headings (`h1` is the biggest; there is only one per page) |
| `<p>` | A paragraph of text |
| `<a href="…">` | A link |
| `<img src="…" alt="…">` | A picture (it has no closing tag) |
| `<ul>` / `<ol>` with `<li>` | A list, with one `<li>` per item |
| `<figcaption>` | The caption under a picture |

### Rules that keep the page working

| Rule | Good ✅ | Wrong ❌ |
|---|---|---|
| Every opening tag has its closing tag | `<p>Tekst</p>` | `<p>Tekst` |
| Write `&` as `&amp;` | `Ontwerper &amp; maker` | `Ontwerper & maker` |
| Don't use `<` or `>` in your text; write them as `&lt;` and `&gt;` | `minder dan 5 (&lt; 5)` | `minder dan 5 (< 5)` |
| Don't use `"` inside an attribute value | `alt="Het 'paviljoen'"` | `alt="Het "paviljoen""` |
| Don't change `class="…"`, `id="…"` or `aria-…="…"` | | |

**Leave alone:** everything between `<head>` and `</head>`, the `<script>` lines, and all `class`, `id` and `aria-` attributes. They control the layout, the menu and accessibility.

You'll see codes such as `&rarr;` (→), `&larr;` (←) and `&copy;` (©). These are special characters. Leave them as they are.

**Lines between `<!--` and `-->` are notes.** They don't appear on the website.

---

## Where everything is

| File | What it contains |
|---|---|
| `index.html` | Home page: introduction and photo, the four competentie cards, the timeline, contact details |
| `reflectie.html` | The STAR-reflectie |
| `competenties/digitale-expert.html` (and the other 3) | One competentie: its leerdoelen and cards for its projects |
| `projects/houten-paviljoen.html` (and the others) | One project page |
| `css/` and `js/` | Styling and behaviour. **Don't edit these**, unless you know CSS. |

**Tip:** to find something, open the file and press `Cmd + F`. To search **all** files at once, press `Cmd + Shift + F`.

---

## Common changes

### Change text anywhere

1. Find the text with `Cmd + F` (or `Cmd + Shift + F` for all files).
2. Change only the words between the tags.
3. Save with `Cmd + S`, then refresh the browser.

> A project's title and short description appear in **several places**: on the project page, on the card on each competentie page it belongs to, and on the home-page timeline. Use `Cmd + Shift + F` to find every place and change them all.

### Write a project's story

Open the project's page in `projects/`. The story is in three sections:

```html
<h2 id="opgave-title">De opgave</h2>
<p>Beschrijf de ontwerp- of onderzoeksvraag. ...</p>
```

Replace the text inside the `<p>…</p>` under **De opgave**, **Het proces** and **Het resultaat**. For an extra paragraph, copy a whole `<p>…</p>` line and paste it right below.

The bullet list under *Het proces* works the same way: one `<li>…</li>` per bullet. Copy a line to add a bullet, and delete a line to remove one.

At the top of the page you'll also find the **lead** (`project-detail__lead`), and the **Rol**, **Periode** and **Software & tools** values, each between `<dd>` and `</dd>`.

### Change a picture

1. Put the picture in the **`images`** folder (create the folder next to `index.html` if needed). Use `.jpg` for photos, simple file names without spaces, and about 1600 pixels wide.
2. Find the `<img …>` tag and replace what's inside `src="…"`.

**The path depends on where the page is:**

| Page | Write the picture as |
|---|---|
| `index.html`, `reflectie.html` | `src="images/paviljoen.jpg"` |
| Pages in `projects/` or `competenties/` | `src="../images/paviljoen.jpg"` (`../` means "one folder up") |

Example: a project page

```html
<img src="../images/paviljoen.jpg" alt="Het houten paviljoen op de campus" width="1200" height="675">
```

- On **project pages and the home-page photo**, write a real description in `alt="…"`.
- On **cards** (competentie pages and the timeline), keep `alt=""` empty. The card title already describes the project.

The project picture appears in three places: the project page, the cards on its competentie pages, and the timeline in `index.html`. Search for the old picture name (e.g. `shena-houten-paviljoen`) with `Cmd + Shift + F` to find them all.

### Change contact details

In `index.html`, search for `contact__list`. Each item looks like this:

```html
<a class="contact__value" href="mailto:hello@example.com">hello@example.com</a>
```

Change the address **in both places**: inside `href="…"` (where the link goes) and between the tags (what people see). For the phone number, the `href` has no spaces: `href="tel:+31612345678"`. To remove an item completely, delete everything from its `<li class="contact__item reveal">` down to and including its `</li>`.

### Write the STAR-reflectie

Open `reflectie.html`. Each part looks like this:

```html
<h2 class="star-step__title" id="reflectie-1-title"><span class="star-step__letter" aria-hidden="true">S</span> Situatie</h2>
<p>Beschrijf de context: ...</p>
```

Replace the text in the `<p>…</p>` under each letter. Copy a `<p>…</p>` line for more paragraphs.

### Add the competentie 4 diagram

Open `competenties/professioneel-handelen.html` and search for `project-detail__image-placeholder`. Replace that whole `<div …></div>` line with:

```html
<img src="../images/professioneel-handelen-hbo.png" alt="Diagram professioneel handelen HBO">
```

---

## Adding a new project by hand

This takes several steps, because a project appears in several places. (With the content file in [README.md](README.md), this is done automatically.)

1. **The project page.** In `projects/`, copy an existing project file, e.g. right-click → *Copy*, then *Paste*. Rename the copy with lowercase letters and hyphens, e.g. `daglicht-onderzoek.html`. In the new file, change:
   - the `<title>` near the top, and the `content="…"` of `<meta name="description" …>`
   - the last breadcrumb item, the `<h1>`, the lead, the details (`<dd>`), the picture, and the story
   - the **Aangetoonde leerdoelen** list. Copy or delete whole `<li class="leerdoel">…</li>` blocks, and copy the leerdoel text from the competentie page.
   - the buttons at the bottom: "Terug naar competentie …" and "Volgende: …"
2. **The competentie pages.** For each competentie the project belongs to, open its page in `competenties/`. Copy a whole project card, from `<li class="reveal">` to its matching `</li>`, and paste it where it should appear. In the copy, change the link (`href="../projects/daglicht-onderzoek.html"`), title, tags, description, leerdoel numbers and picture.
3. **The home page.**
   - Update the counts on the competentie cards, e.g. `4 leerdoelen · 5 projecten`.
   - For the timeline: copy a whole `<li class="timeline__item">…</li>` block and paste it in date order. Change the date, picture, link, title and tags. Also update the "**… van 11 leerdoelen aangetoond**" text, the bar width `style="width: 45%"` (the same number as a percentage: 5 of 11 is 45%) and the "Nieuw: …" line. Check the projects that come **after** it on the timeline, because their numbers may change too.
4. **The "Volgende" link** on the project before it, so visitors can click through to the new project.

**To remove a project:** delete its file in `projects/`, then remove its cards from the competentie pages and the timeline, and fix the counts and "Volgende" links that pointed to it.

---

## Changing something on every page

The menu, footer and header are copied on **every** page (12 files). To change them all at once:

1. Press `Cmd + Shift + F` and search for the exact text, e.g. `Alle rechten voorbehouden`.
2. Click the small arrow on the left of the search box to show the **Replace** field.
3. Type the new text and click **Replace All** (the button next to the Replace field).

Be careful with links: pages in `projects/` and `competenties/` use `../` in front of their links, but `index.html` and `reflectie.html` don't.

---

## Checking your work

After each change, save (`Cmd + S`) and refresh the page in your browser (`Cmd + R`).

| Problem | Likely cause |
|---|---|
| Part of the page has disappeared, or the layout is broken | A missing closing tag, e.g. `<p>` without `</p>`, or a deleted `<` or `>` |
| A picture doesn't show | The file name in `src` doesn't match the file exactly (capital letters count!), or `../` is missing on a page in `projects/` or `competenties/` |
| A link gives "Cannot GET" or "File not found" | A typo in `href`, or a missing `../` |
| Strange characters, like `&` showing up wrong | Write `&` as `&amp;` |

**Undo:** `Cmd + Z` undoes your last changes in VS Code. With GitHub Desktop, right-click a changed file and choose **Discard Changes…** to return to the last saved version.

To save your work to GitHub and put the site online, see **"Saving your work to GitHub"** in [README.md](README.md).
