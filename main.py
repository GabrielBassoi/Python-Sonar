"""sonar.py, by Gabriel Bassoi, 2022-11-23
This program is a sonar screen made with matplotlib to show
the data comming from an arduino.
"""
import sonar


def main(s):
    s.connect()
    s.sonar()


if __name__ == "__main__":
    s = sonar.Sonar()
    main(s)
