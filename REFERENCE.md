# References

A quick reference guide for how the database is set up

In general, `idx` stands for the UUID

---

# How does it look like?
![""](/images/basic.png)
`index.json` contains notes, `/ingredients` contain list of ingredients for that note (file names are idx of `index.json`), and the `profiles` page contains information about the ingredient.

### `index.json`
Contains perfume notes.
|field|description|
|--|--|
|name|perfume note|
|link|links to possible ingredients, description of note, more information etc.|

---

### `ingredients.json`
file name = perfume note
|field|description|
|--|--|
|name|name of ingredient|
|link|links to ingredients|