# netwix ♨️

Netwix is a python client for Netflix. With netwix by simply entering the Netflix ID the user can access data related to movies and tv shows available on <a href="https://www.netflix.com">Netflix</a>.


## Installation 📥

Install netwix using pip

```bash
pip install netwix
```
## Authors ✍️

- [@new92](https://www.github.com/new92)


## Contributing 🤝

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`. For more info please check the `CODE_OF_CONDUCT.md` file


## Feedback 💭

If you have any feedback, please reach out to us at <a href="mailto:new92github@gmail.com">this email address</a>.

**Feel free to contact us anytime ! You'll get a reply within a day. Please avoid using abusive or offensive language.
If you are reporting a bug or making a suggestion please make sure your report/suggestion is as much detailed as possible.**


## License 📜

[![License](https://img.shields.io/github/license/new92/netwix?style=for-the-badge)](https://github.com/new92/netwix/blob/main/LICENSE.md)


## Documentation 📄

### Example Movie ID

- **Movie:** Red Notice
- **URL:** `https://www.netflix.com/watch/81161626`
- **Movie ID:** `81161626`

#### Example Movies

```python
from netwix.types import Movies

movie = Movies("81161626")
print(movie.name) # Output: Red Notice
```

#### Example Movies

```python
from netwix.types import Movies

movie = Movies("81161626")
print(movie.allData) # Output: A dictionary with all the data of the specific movie
```

#### Movies Attributes

- `type`
- `name`
- `description`
- `url`
- `contentRating`
- `genre`
- `imgUrl`
- `awards`
- `startDate`
- `creationDate`
- `actors`
- `creators`
- `directors`
- `trailer`

### Example Series ID

- **Serie:** The Office
- **URL:** `https://www.netflix.com/watch/70126228`
- **Series ID:** `70126228`

#### Example Series

```python
from netwix.types import Series

serie = Series("70126228")
print(serie.name) # Output: The Office
```

#### Series Attributes

- `type`
- `name`
- `description`
- `url`
- `contentRating`
- `genre`
- `imgUrl`
- `startDate`
- `creationDate`
- `awards`
- `seasons`
- `actors`
- `creators`
- `directors`
