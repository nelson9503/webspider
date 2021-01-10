# webspider - Methods

**func |** `get_web_html` `(` `url`: *str* `)` `->` `html`: *str*

**func |** `get_web_text` `(` `url`: *str*, `splitToLines`: *bool* `)` `->` `text`: *str*/*list*

**func |** `get_web_json` `(` `url`: *str* `)` `->` `json`: *dict*

**func |** `get_web_photo` `(` `url`: *str*, `savepath`: *str* `)`

**func |** `removeAbnormalSpaces` `(` `x`: *str* `)` `->` `text`: *str*

**func |** `selectTextBetween` `(` `text`: *str*, `left`: *str*, `right`: *str* `)` `->` `textlist`: *list*

**func |** `checkStartChars` `(` `text`: *str*, `chars`: *str* `)` `->` `check`: *bool*

**class |** `GoogleChrome` `(` `headless`: *bool*, `windowSize`: *list* `)`

* **func |** `connect` `(` `)`

* **func |** `close` `(` `)`

* **func |** `browse` `(` `url`: *str* `)`

* **func |** `getHTML` `(` `)` `->` `html`: *str*

* **func |** `getText` `(` `splitToLines`: *bool* `)` `->` `text`: *str*/*list*

* **func |** `getJSON` `(` `)` `->` `json`: *dict*

