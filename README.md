# PyAlphaClock: Library for interacting with the Alpha Clock Five

Simple Pythonic library for manipulating the screen of the [Alpha Clock Five](http://wiki.evilmadscientist.com/Alpha_Clock_Five) desk clock by [Evil Mad Scientist](http://www.evilmadscientist.com/).

### Installation

```
pip install pyalphaclock
```

### Usage

```python
> from pyalphaclock import AlphaClock
> clock = AlphaClock()
> clock.clear_screen()
> clock.display_scrolling_text("Hello everybody")
> from datetime import datetime
> now = datetime.now()
> clock.display_time(now)
> clock.display_date(now)
```

### License

MIT
