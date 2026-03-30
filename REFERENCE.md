# References

A quick reference guide for how the database is set up


### Dictionary
|word|meaning|
|---|---|
|note|(can also refer to as `ingr` or ingredient) refers to a perfume note, an adjective specific to world of perfume|
|base|refers to a perfume base, refers to a chemical perfume base with a unique [CAS number](https://cdxapps.epa.gov/oms-substance-registry-services/swagger-ui/)|

### `index.json`
> A list of notes

|field|description|
|--|--|
|`idx`|UUID of note|
|`name`|name of note|
|`link`|links to possible ingredients, description of note, more information of the note, etc.|

### `/ingredients/ .json`
> Folder contains json files of the ingredients that is associated with the note in question.
> 
> Example: `/ingredients/1.json` correlates to `index.json` where `idx=1`

|field|description|
|--|--|
|file name|`idx` field of `index.json`, indicates what note it's related to|
|`idx`|UUID of base|
|`ingr_name`|name of base that is associated with note|
|`ingr_link`|link to base that is associated with the note|

### `base.json`
> File which contains the index to navigate the folder
|field|description|
|--|--|
|`idx`|base index number|
|`cas`|CAS number of base|
|`notes`|notes associated with the base|
|`adjs`|adjectives associated with the base|

# Visualizating the data
![""](/images/basic.png)
`index.json` contains notes, `/ingredients` contain list of ingredients for that note (file names are idx of `index.json`), and the `profiles` page contains information about the ingredient.
