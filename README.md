# ChuShogi Random
This is my attempt to create a simple USI chushogi engine meant to play only Random moves. The provided code does not have explicit knowledge of where each piece is or how each piece moves. It only generates random moves without considering the current position or piece movements.

## USI Protocol Implementation
An example of the usi commands execution is shown below. The bestmove is provided in the usi format. To execute usi commands you can eirther compile and run the [`chushogi.py`](chushogi.py) file or run `python3 chushogi.py` in your terminal.
```bash
< usi

> id name ChuShogi Random
> id author Yohaan Seth Nathan
> usiok

< isready

> readyok

< usinewgame
< position lfcsgekgscfl/a1b1txot1b1a/mvrhdqndhrvm/pppppppppppp/3i4i3/12/12/3I4I3/PPPPPPPPPPPP/MVRHDNQDHRVM/A1B1TOXT1B1A/LFCSGKEGSCFL b - 1
< go

> bestmove k7l6
```