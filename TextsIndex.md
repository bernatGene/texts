## Poemes  

```dataview
	TABLE file.cday, file.mday
from "textsstuff/texts"
sort file.cday DESC
```

```dataview
	TABLE file.mday, length(rows) as Number
from "textsstuff/texts"
group by type
```
